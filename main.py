import discord as d
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot, ButtonStyle
import math
import os
import time
import psycopg2
from psycopg2 import Error
from db_helper import update ,retrieve ,insert


invite_url = 'https://discord.com/api/oauth2/authorize?client_id=891750013774991370&permissions=139586783296&scope=bot%20applications.commands'

combat={
    "Bat" : 8 ,"Slime" : 16 ,"Fishing Spider" : 38,"Mashroom" : 46,"Forest Spider" : 55 ,"Forest Bat": 60 ,"Skeletal Snake" : 300  ,"Cave Spider" : 350 ,"Skeletal Bat" : 385 ,"Cave Bat" : 560 ,
    "Forest Fiend" : 1080 ,"Rock Fiend" : 2000 ,"Giant Hornet" : 2100 ," Shadow Flame": 2800,"Shadow fiend": 1500 ,

    "Snow Bat" : 125 ,"Ice Slime": 165 ,"Snowman" : 210 ,"Ice Spider" : 250 ,"Ice Fiend" : 850 ,"Ancient Bat" : 2400 ,"Ice Raptor" : 2750 ,"Spectral Flame" : 2700 ,"Phantom Flame" : 2900 ,
    "Spectral Fiend" : 3100 ,"Phantom Fiend" : 3600 ,"Ancient Cyclops" : 4000 ,

    "Sapphire Scarab" : 400,"Scorpion" : 700 ,"Raptor" : 900 ,"Ruby Scarab" : 1000 ,"Desert Raptor" : 1850 ,"Gold Snake" : 1000 ,"Brown Snake" : 1000 ,"Purple Snake" : 1000 ,"Sandstone Golem" : 11500 ,
    "Anubis" : 4000 ,"Cactus Soldier" : 2800 ,"Arosite Scarab" : 2850 ,"Magnetite Scarab" : 4250 ,"Anubis Elite" : 7500 ,

    "Luminant Slime" : 2200 ,"Golemite Bat" : 4400 ,"Golemite Fiend" : 5270 ,"Baby Dragon" : 5750 ,

    "War Bat" : 1200 ,"Rock Demon" : 10000 ,"Ice Demon" : 16500 ,"Shadow Demon": 	20000,"Ancient War Bat" : 12000 ,"Spinus" : 8500 ,"Reanimated Soul" : 1000 ,"Mummy" : 20000 ,"Golem" : 22500 ,"Umbra" : 24000 ,
    }

bright_leaf = [
    ['Bat', 922919347423416381], ['Slime', 922919366025171056], ['Fishing Spider', 922919348492992552], ['Mashroom', 922919357812727818], ['Forest Spider', 922919349013073950],
    ['Forest Bat', 922919348597846046], ['Skeletal Snake', 922919364016091176], ['Cave Spider', 922919347914174508], ['Skeletal Bat', 922919363957387394], ['Cave Bat', 922919347977064508],
    ['Forest Fiend', 922919348455239711], ['Rock Fiend', 922919361776332861], ['Giant Hornet', 922923881294090310], ['Shadow Flame', 922919363944804372], ['Shadow Fiend', 922924878875754496]
    ]
wintermist = [
    ['Snow Bat', 922919366125834261], ['Ice Slime', 922919354348236841], ['Snowman', 922919365777711125], ['Ice Spider', 922919355812036668], ['Ice Fiend', 922919354088185906],
    ['Ancient Bat', 922919346806865930], ['Ice Raptor', 922919354205630565], ['Spectral Flame', 922919365274398750],['Phantom Flame', 922919358353793034], ['Spectral Fiend', 922919365148553216],
    ['Phantom Fiend', 922919357846269995], ['Ancient Cyclops', 922919347175952414]
    ]
desert = [
    ['Sapphire Scarab', 922919363714105384], ['Scorpion', 922925746685632533], ['Raptor', 922919363386957864], ['Ruby Scarab', 922919362032181299], ['Desert Raptor', 922919348371329085],
    ['Gold Snake', 922919349247955025], ['Brown Snake', 922919347868028948], ['Purple Snake', 922919363311456327], ['Sandstone Golem', 922919363198193675], ['Anubis', 922919347436019772],
    ['Cactus Soldier', 922926198240182352], ['Arosite Scarab', 922919347494740048], ['Magnetite Scarab', 922919362166407190], ['Anubis Elite', 922919347951906868]
    ]
varaxite = [
    ['Luminant Slime', 922919355946266624], ['Golemite Bat', 922919351357698079], ['Golemite Fiend', 922919353207382079], ['Baby Dragon', 922919347494744105]
    ]
bosses = [
    ['War Bat', 922919365995810836], ['Rock Demon', 922919363508600862], ['Ice Demon', 922919354151096370], ['Shadow Demon', 922926354171826247], ['Ancient War Bat', 922919347335335986],
    ['Spinus', 922919365303750736], ['Reanimated Soul', 922927550857105448], ['Mummy', 922919357976293376], ['Golem', 922919350711779388], ['Umbra', 922919365840617502]
    ]

locations = ["Bright Leaf","Wintermist","Desert","Varaxite","Bosses"]

skills = ['Combat','Mining','Smithing','Woodcutting','crafting','Fishing','Cooking','Tailoring']

combatRsc=[bright_leaf,wintermist,desert,varaxite,bosses]
miningRsc = [
    ['Tin Ore', 922854986357043280], ['Copper Ore', 922855022180577290], ['Iron Ore', 922855050156585020], ['Salt', 922855080099729429], ['Coal', 922855065990099004],
    ['Silver Ore', 922855652198592586], ['Crimsteel Ore', 922855136513126460], ['Gold Ore', 922855152073981952], ['Pink Salt', 922855174563831829], ['Mythan Ore', 922855187343884341],
    ['Sandstone', 922855639816994836], ['Cobalt Ore', 922855201956823080], ['Varaxium', 922855217937133568], ['Black Salt', 922855247943204865]
    ]
smithingRsc = [
    ['Bronze Bar', 922855760193531904], ['Iron Bar', 922855781030842409], ['Steel Bar', 922855918633377802], ['Crimsteel Bar', 922855814669156442], ['Silver Bar', 922855844989784074],
    ['Gold Nugget', 922865224091070555], ['Gold Bar', 922855856901586994], ['Mythan Bar', 922855882117775360], ['Cobalt Bar', 922855936161349653], ['Varaxite Bar', 922855948719108126]
    ]
woodcuttingRsc = [
    ['Pine Log', 922856057909420072], ['Dead Log', 922856079233269780], ['Birch Log', 922856103849623702], ['Applewood', 922856116017299466], ['Willow Log', 922856157587058688],
    ['Oak Log', 922856175345754163], ['Chestnut Log', 922856194002001960], ['Maple Log', 922856235978588161], ['Olive Log', 922856248985145374], ['Palm Wood', 922856261052149761],
    ['Magic Log', 937002915716005929]
    ]
craftingRsc = [
    ['Accuracy Relic', 922857047014395904], ['Guarding Relic', 922857046926327899], ['Healing Relic', 922871203033649222], ['Wealth Relic', 922871202773618768],
    ['Power Relic', 922871202907828254], ['Nature Relic', 922871202979135531], ['Fire Relic', 922857046913716286], ['Damage Relic', 922857046762721281],
    ['Leeching Relic', 922871203079794698], ['Experience Relic', 922871203130134528], ['Cursed Relic', 922857046934708235],["Ice Relic",936964378517975040]
    ]
fishingRsc = [
    ['Anchovies', 922873492137992222], ['Goldfish', 922873492536442940], ['Mackerel', 922873492821672027], ['Squid', 922873493312376862], ['Sardine', 922873493060743189],
    ['Eel', 922873492272189451], ['Anglerfish', 922873492293177405], ['Trout', 922873493345959996], ['Trout+Jellyfish', 922876044111937548], ['Bass', 922873492058284094],
    ['Bass+Herringbone', 922876044036407326], ['Tuna', 922873493475950672], ['Lobster', 922873492813271051], ['Lobster+SeaTurtle', 922876043780575233], ['Manta Ray', 922873492691644447],
    ['Shark', 922873493115248721], ['Shark+Orca', 922876044158070825], ['Shark+Orca+GiantSquid', 922876044342624376]
    ]
cookingRsc = [
    ['Cooked Anchovies', 922873530536824843], ['Cooked Mackerel', 922873531073716235], ['Cooked Squid', 922873531165982801], ['Cooked Sardine', 922873531337957427],
    ['Cooked Eel', 922873530943668235], ['Cooked Anglerfish', 922873530897559602], ['Cooked Trout', 922873531698647101], ['Cooked Bass', 922873530725568592],
    ['Cooked Tuna', 922873531803533382], ['Cooked Lobster', 922873530973036574], ['Cooked Sea Turtle', 922873531547664384], ['Cooked Manta Ray', 922873531195355176],
    ['Cooked Shark', 922873531501510686], ['Cooked Orca', 922873530994003989], ['Cooked Giant Squid', 922873530943680532]
    ]

tailoringRsc = [['Wand',936964379080024135],
    ['Paper',936964378773831721],['Book',936964379092594718],['Ember Tome',936964378283114506],
    ['Leech Tome',936964378891264001],['Haunt Tome',936964378002071573],['Fire Staff',936964377867862048],['Ice Staff',936964378606075934],
    ['Nature Staff',936964379067437096],['Cursed Staff',936964377964322857],['Icicle Tome',936964378689957958],['Ignite Tome',936964378748674090],
    ['Drain Tome',936964378077564988],['Curse Tome',936964377867874305],['Freeze Tome',936964378337615912],['Inferno Tome',936964378568318977],
    ['Consume Tome',936964377565876286],['Torture Tome',936964379147124786],['Blizzard Tome',936964377712676906]
    ]



tlr = {'Wand':936964379080024135,
    'Paper':936964378773831721,'Book':936964379092594718,'Ember Tome':936964378283114506,
    'Leech Tome':936964378891264001,'Haunt Tome':936964378002071573,'Fire Staff':936964377867862048,'Ice Staff':936964378606075934,
    'Nature Staff':936964379067437096,'Cursed Staff':936964377964322857,'Icicle Tome':936964378689957958,'Ignite Tome':936964378748674090,
    'Drain Tome':936964378077564988,'Curse Tome':936964377867874305,'Freeze Tome':936964378337615912,'Inferno Tome':936964378568318977,
    'Consume Tome':936964377565876286,'Torture Tome':936964379147124786,'Blizzard Tome':936964377712676906
    }


baits = {
    "Anchovies":" Earthworm", "Goldfish":" Earthworm", "Mackerel":"Iceworm", "Squid":"Iceworm", "Sardine":"Corpseworm", "Eel":"ToxicWorm", "Anglerfish":"Sandworm", 
    "Trout":"Beetle", "Trout+Jellyfish":"Beetle", "Bass":"Grasshopper", "Bass+Herringbone":"Grasshopper", "Tuna":"Wasp", "Lobster":"Scallop", "Lobster+SeaTurtle":"Scallop", 
    "Manta Ray":"Crab", "Shark":"Bass", "Shark+Orca":"Bass", "Shark+Orca+GiantSquid":"Bass"
    }

baits_id = {
    'Anchovies': 922887338357567499, 'Goldfish': 922887338357567499, 'Mackerel': 922887338655354962, 'Squid': 922887338655354962, 'Sardine': 922887338269499414,
    'Eel': 922887339037044756, 'Anglerfish': 922887338848296970, 'Trout': 922887338412097656, 'Trout+Jellyfish': 922887338412097656, 'Bass': 922887338810548265,
    'Bass+Herringbone': 922887338810548265, 'Tuna': 922887339070619708, 'Lobster': 922887338756030515, 'Lobster+SeaTurtle': 922887338756030515, 'Manta Ray': 922887338567286784,
    'Shark': 922873492058284094, 'Shark+Orca': 922873492058284094, 'Shark+Orca+GiantSquid': 922873492058284094
    }

skills_id = {
    'Combat':880221520121700362,
    'Mining':880221690049732638,
    'Smithing':880221615374360648,
    'Woodcutting':880221633913163796,
    'Crafting':880221589050916914,
    'Fishing':880221548399697923,
    'Cooking':880221572751847444,
    'Sailing':937013045404786758,
    'Tailoring':937013045488648252
    }


resources = {
    "Tin Ore": 10, "Copper Ore": 10, "Iron Ore" : 50,"Salt": 80, "Coal": 115, "Silver Ore": 135, "Crimsteel Ore": 350,
    "Gold Ore": 400, "Pink Salt" : 500, "Mythan Ore": 650, "Sandstone": 1100, "Cobalt Ore": 1200, "Varaxium": 1800, "Black Salt": 2500,
    "Bronze Bar" : 5, "Iron Bar" : 14,"Steel Bar" : 20 , "Crimsteel Bar" : 130,
    "Silver Bar" : 1000,"Gold Bar" : 20000,"Gold Nugget" : 60,"Mythan Bar" : 5000,"Cobalt Bar" : 15000,"Varaxite Bar" : 20000,
    "Pine Log": 10,"Dead Log": 20,"Birch Log": 50,"Applewood": 115,"Willow Log": 350,"Oak Log": 475,
    "Chestnut Log": 650,"Maple Log": 1200,"Olive Log": 1800,"Palm Wood": 2600,"Magic Log":4000,
    "Accuracy Relic":3 ,"Guarding Relic":8 ,"Healing Relic":18 ,"Wealth Relic":40 ,"Power Relic":105 ,"Nature Relic":200 ,
    "Fire Relic":425 ,"Damage Relic":900 ,"Leeching Relic":1400 ,"Experience Relic":1850 ,"Cursed Relic":2750 ,"Ice relic":4120,
    "Anchovies":10,"Goldfish":20,"Mackerel":50,"Squid":115,"Sardine":375,"Eel":500,"Anglerfish":625,
    "Trout":750,"Jellyfish":900,"Trout+Jellyfish":825,"Bass":1350,"Herringbone":1700,"Bass+Herringbone":1525,"Tuna":2000,"Lobster":3500,"Sea Turtle":6500,"Lobster+SeaTurtle":5000,
    "Manta Ray":9500,"Shark":14500,"Orca":29500,"Giant Squid":55000,"Shark+Orca":22000,"Shark+Orca+GiantSquid":33000,
    "Cooked Anchovies":10,"Cooked Mackerel":50,"Cooked Squid":115,"Cooked Sardine":375,"Cooked Eel":500,"Cooked Anglerfish":30,
    "Cooked Trout":750,"Cooked Bass":1350,"Cooked Tuna":2000,"Cooked Lobster":3500,"Cooked Sea Turtle":6500,
    "Cooked Manta Ray":9500,"Cooked Shark":13500,"Cooked Orca":22500,"Cooked Giant Squid":41500,
    "Wand":12,"Paper":1,"Book":5,"Fire Staff":500,"Nature Staff":500,"Ice Staff":500,"Cursed Staff":500,"Icicle Tome":40,"Freeze Tome":900,"Blizzard Tome":4300,"Leech Tome":20,
    "Drain Tome":115,"Consume Tome":2110,"Haunt Tome":28,"Curse Tome":200,"Torture Tome":2750,"Ember Tome":12,"Ignite Tome":100,"Inferno Tome":1380
    }

Combat_boosts = ["NoBoost","XpRelics","XpPotion","XpRelics+XpPotion","WorldBoost","XpRelics+WorldBoost","XpPotion+WorldBoost","XpRelics+XpPotion+WorldBoost"]
Mining_boosts = ["NoBoost","ProsNeck","WorldBoost","ProsNeck+WorldBoost"]
Smithing_boosts = ["NoBoost","InfHammer","InfRing","InfHammer+InfRing","WorldBoost","hammer+WorldBoost","Ring+WorldBoost","Hammer+Ring+WorldBoost"]
Woodcutting_boosts = ["NoBoost","WorldBoost"]
Crafting_boosts = ["NoBoost","WorldBoost"]
Fishing_boosts = ["NoBoost","WorldBoost"]
Cooking_boosts = ["NoBoost","WorldBoost"]
Tailoring_boosts = ["NoBoost","WorldBoost"]
boostsValues = {
    "NoBoost":1.0,"InfHammer":1.04,"InfRing":1.04,"XpRelics":1.05,"XpPotion":1.05,"ProsNeck":1.05,"InfHammer+InfRing":1.0816,"XpRelics+XpPotion":1.1025,"WorldBoost":1.5,"hammer+WorldBoost":1.56,
    "Ring+WorldBoost":1.56,"XpRelics+WorldBoost":1.575,"XpPotion+WorldBoost":1.575,"ProsNeck+WorldBoost":1.575,"Hammer+Ring+WorldBoost":1.6224,"XpRelics+XpPotion+WorldBoost":1.65375
    }

boosts = [Combat_boosts,Mining_boosts,Smithing_boosts,Woodcutting_boosts,Crafting_boosts,Fishing_boosts,Cooking_boosts,Tailoring_boosts]

skill_rsc = [combatRsc,miningRsc, smithingRsc, woodcuttingRsc, craftingRsc, fishingRsc,cookingRsc,tailoringRsc]

lvltab = [
    0,46,99,159,229,309,401,507,628,768,928,1112,1324,1567,1847,2168,2537,2961,3448,4008,4651,5389,6237,7212,8332,9618,11095,12792,14742,16982,19555,22510,25905,29805,34285,
    39431,45342,52132,59932,68892,79184,91006,104586,120186,138106,158690,182335,209496,240696,276536,317705,364996,419319,481720,553400,635738,730320,838966,963768,1107128,1271805,
    1460969,1678262,1927866,2214586,2543940,2922269,3356855,3856063,4429503,5088212,5844870,6714042,7712459,8859339,10176758,11690075,13428420,15425254,17719014,20353852,23380486,
    26857176,30850844,35438364,40708040,46761308,53714688,61702024,70877064,81416417,93522954,107429714,123404386,141754466,162833172,187046247,214859767,246809111,283509271,325666684,
    374092835,429719875,493618564,567018884,651333710,748186012,859440093,987237472,1134038112,1302667765,1496372370,1718880532,1974475291,2268076571,2605335878,2992745089,3437761413,
    3948950932,4536153492,5210672106
    ]
lvldef = [
    46, 53, 60, 70, 80, 92, 106, 121, 140, 160, 184, 212, 243, 280, 321, 369, 424, 487, 560, 643, 738, 848, 975, 1120, 1286, 1477, 1697, 1950, 2240, 2573, 2955, 3395, 3900, 
    4480, 5146, 5911, 6790, 7800, 8960, 10292, 11822, 13580, 15600, 17920, 20584, 23645, 27161, 31200, 35840, 41169, 47291, 54323, 62401, 71680, 82338, 94582, 108646, 124802, 143360, 
    164677, 189164, 217293, 249604, 286720, 329354, 378329, 434586, 499208, 573440, 658709, 756658, 869172, 998417, 1146880, 1317419, 1513317, 1738345, 1996834, 2293760, 2634838, 3026634, 
    3476690, 3993668, 4587520, 5269676, 6053268, 6953380, 7987336, 9175040, 10539353, 12106537, 13906760, 15974672, 18350080, 21078706, 24213075, 27813520, 31949344, 36700160, 42157413, 
    48426151, 55627040, 63898689, 73400320, 84314826, 96852302, 111254081, 127797379, 146800640, 168629653, 193704605, 222508162, 255594759, 293601280, 337259307, 387409211, 445016324, 
    511189519, 587202560
    ]

bot = ComponentsBot('*')
bot.remove_command('help')

def tabfill(xp):    
    lvl=0
    a=0
    for l in range(120):
        if (xp > lvltab[l]):
            lvl = l+1
            a = round((((xp- lvltab[l]) / lvldef[l])*100),2)
    return lvl, a

def getxp( lv, nlv, per, nper):
    minxp= lvltab[lv-1] + (lvldef[lv-1]*(per/100))
    if nlv == 120:
        bigxp= lvltab[119]
    else:
        bigxp= lvltab[nlv-1] + (lvldef[nlv-1]*(nper/100))
    XPneeded = round(bigxp - minxp)
    return XPneeded
    







async def selectionTest(ctx,curLv,tarLv,curPerc,tarPerc):
    skill_msg = await ctx.send(content='Skill :',components=[Select(
        placeholder='Select Skill !',
        options=[
            SelectOption(label=f'Combat',value='0', emoji=bot.get_emoji(880221520121700362)),
            SelectOption(label=f'Mining',value='1', emoji=bot.get_emoji(880221690049732638)),
            SelectOption(label=f'Smiting',value='2', emoji=bot.get_emoji(880221615374360648)),
            SelectOption(label=f'woodcutting',value='3', emoji=bot.get_emoji(880221633913163796)),
            SelectOption(label=f'Crafting',value='4', emoji=bot.get_emoji(880221589050916914)),
            SelectOption(label=f'Fishing',value='5', emoji=bot.get_emoji(880221548399697923)),
            SelectOption(label=f'Cooking',value='6', emoji=bot.get_emoji(880221572751847444)),
            SelectOption(label=f'Tailoring',value='7', emoji=bot.get_emoji(937013045488648252)),
            SelectOption(label=f'🚫 Cancel',value='Cancel')
            
            ],custom_id='SelectSkill'
    )])
    interaction = await bot.wait_for('select_option',
    check=lambda inter: inter.custom_id == 'SelectSkill' and inter.user == ctx.author)
    await skill_msg.delete()
    choice = interaction.values[0]
    if choice == 'Cancel' :
        await interaction.send('You have canceled the interaction')
    elif choice == '0':
        location_list = locations
        temp_list = []
        for i in range(len(location_list)):
            temp_list.append(SelectOption(label=location_list[i],value=str(i+1)))#add locations emoji = bot.get_emoji(emoji_id)
        temp_list.append(SelectOption(label="Cancel",value="Cancel"))
        resource_msg = await ctx.send(content='Location :',components=[Select(
        placeholder='Select Location !',
        options=temp_list
        
        ,custom_id='SelectLoc'
        )])
        interaction3 = await bot.wait_for('select_option',
        check=lambda inter: inter.custom_id == 'SelectLoc' and inter.user == ctx.author)
        await resource_msg.delete()
        choice3 = interaction3.values[0]
        if choice3 == 'Cancel' :
            await interaction3.send('You have canceled the interaction')
        else:
            mob_list = combatRsc[int(choice3)-1]
            temp_list = []
            for i in range(len(mob_list)):
                temp_list.append(SelectOption(label=mob_list[i][0],value=str(i+1),emoji=bot.get_emoji(mob_list[i][1])))#add mobs emoji = bot.get_emoji(emoji_id)
            temp_list.append(SelectOption(label="Cancel",value="Cancel"))
            resource_msg = await ctx.send(content='Mob :',components=[Select(
            placeholder='Select Mob !',
            options=temp_list
            
            ,custom_id='SelectMob'
            )])
            interaction4 = await bot.wait_for('select_option',
            check=lambda inter: inter.custom_id == 'SelectMob' and inter.user == ctx.author)
            await resource_msg.delete()
            choice4 = interaction4.values[0]
            if choice4 == 'Cancel' :
                await interaction4.send('You have canceled the interaction')

            else:
                boost_list = Combat_boosts
                temp_list1 = []
                for i in range(len(boost_list)):
                    temp_list1.append(SelectOption(label=boost_list[i],value=str(i+1)))#add boosts emoji = bot.get_emoji(emoji_id)
                temp_list1.append(SelectOption(label="Cancel",value="Cancel"))
                boost_msg = await ctx.send(content='Boost :',components=[Select(
                placeholder='Select Boost !',
                options=temp_list1
                
                ,custom_id='SelectBst'
                )])
                interaction2 = await bot.wait_for('select_option',
                check=lambda inter: inter.custom_id == 'SelectBst' and inter.user == ctx.author)
                await boost_msg.delete()
                choice2 = interaction2.values[0]
                if choice2 == 'Cancel' :
                    await interaction2.send('You have canceled the interaction')

                else:
                    combat_emoji = bot.get_emoji(880221520121700362)
                    mob_emoji = bot.get_emoji(combatRsc[int(choice3)-1][int(choice4)-1][1])
                    mob_used = combatRsc[int(choice3)-1][int(choice4)-1][0]
                    mob_xp = combat[mob_used]
                    bst_name = boost_list[int(choice2)-1]
                    bst_used = boostsValues[bst_name]
                    chosen_skill = skills[int(choice)] 
                    xp_needed = getxp(int(curLv),int(tarLv),float(curPerc),float(tarPerc))
                    rsc_needed = math.ceil(xp_needed / mob_xp) + 1
                    rsc_needed_boosted = math.ceil(rsc_needed / bst_used)
                    result = f'Skill : {combat_emoji} Combat' + '\n Mob : ' + f'{mob_emoji}' + mob_used + '\n Current Lvl : ' + curLv + ' ' + curPerc + '%' + '\n target Lvl : ' + tarLv + ' ' + tarPerc + '%' + '\n Boost : ' + bst_name + '\n Quantity Needed : ' + f'{rsc_needed_boosted:,}'
                    
                    await ctx.send(result)

        
    else:
        rsc_list = skill_rsc[int(choice)]
        temp_list = []
        for i in range(len(rsc_list)):
            temp_list.append(SelectOption(label=rsc_list[i][0],value=str(i+1),emoji=bot.get_emoji(rsc_list[i][1])))#add resources emoji = bot.get_emoji(emoji_id)
        temp_list.append(SelectOption(label="Cancel",value="Cancel"))
        resource_msg = await ctx.send(content='Resource :',components=[Select(
        placeholder='Select Resource !',
        options=temp_list
        
        ,custom_id='SelectRsc'
        )])
        interaction1 = await bot.wait_for('select_option',
        check=lambda inter: inter.custom_id == 'SelectRsc' and inter.user == ctx.author)
        await resource_msg.delete()
        choice1 = interaction1.values[0]
        if choice1 == 'Cancel' :
            await interaction1.send('You have canceled the interaction')

        else:
            boost_list = boosts[int(choice)]
            temp_list1 = []
            for i in range(len(boost_list)):
                temp_list1.append(SelectOption(label=boost_list[i],value=str(i+1)))#add boosts emoji = bot.get_emoji(emoji_id)
            temp_list1.append(SelectOption(label="Cancel",value="Cancel"))
            boost_msg = await ctx.send(content='Boost :',components=[Select(
            placeholder='Select Boost !',
            options=temp_list1
            
            ,custom_id='SelectBst'
            )])
            interaction2 = await bot.wait_for('select_option',
            check=lambda inter: inter.custom_id == 'SelectBst' and inter.user == ctx.author)
            await boost_msg.delete()
            choice2 = interaction2.values[0]
            if choice2 == 'Cancel' :
                await interaction1.send('You have canceled the interaction')

            else:
                rsc_used = skill_rsc[int(choice)][int(choice1)-1][0]
                rsc_xp = resources[rsc_used]
                bst_name = boost_list[int(choice2)-1]
                bst_used = boostsValues[bst_name]
                chosen_skill = skills[int(choice)] 
                skill_id = skills_id[chosen_skill.capitalize()]
                skill_emoji = bot.get_emoji(skill_id)
                resource_emoji = bot.get_emoji(skill_rsc[int(choice)][int(choice1)-1][1])
                xp_needed = getxp(int(curLv),int(tarLv),float(curPerc),float(tarPerc))
                rsc_needed = math.ceil(xp_needed / rsc_xp) + 1
                rsc_needed_boosted = math.ceil(rsc_needed / bst_used)
                if chosen_skill.lower() == "fishing" :
                    bait_id = baits_id[rsc_used]
                    bait_emoji = bot.get_emoji(bait_id)
                    result = f'Skill : {skill_emoji} ' + chosen_skill.capitalize() + f'\n Fish : {resource_emoji} ' + rsc_used + f'\n Bait : {bait_emoji} ' + baits[rsc_used] + '\n Current Lvl : ' + curLv + ' ' + curPerc + '%' + '\n target Lvl : ' + tarLv + ' ' + tarPerc + '%' + '\n Boost : ' + bst_name + '\n Quantity Needed : ' + f'{rsc_needed_boosted:,}'
                else :
                    result = f'Skill : {skill_emoji} ' + chosen_skill.capitalize() + f'\n Resource : {resource_emoji} ' + rsc_used + '\n Current Lvl : ' + curLv + ' ' + curPerc + '%' + '\n target Lvl : ' + tarLv + ' ' + tarPerc + '%' + '\n Boost : ' + bst_name + '\n Quantity Needed : ' + f'{rsc_needed_boosted:,}'
                
                await ctx.send(result)



###########################################################################################



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    await bot.change_presence(activity=d.Game(name="Calculator"))

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.command()
async def test(ctx):
    cooking_emoji = bot.get_emoji(880221572751847444)
    await ctx.send(f"{cooking_emoji}")

@bot.command(name="OwO",aliases=["owo","Owo","oWo","OWo","OWO","oWO"])
async def OwO(ctx):
    await ctx.send("Numba Wan")
    
@bot.command(name='calc',aliases=['Calc'])
async def calc(ctx,curLv,tarLv,curPerc=None,tarPerc=None):
    if curPerc is None:
        curPerc='0'
    if tarPerc is None:
        tarPerc='0'
    await selectionTest(ctx,curLv,tarLv,curPerc,tarPerc)
    counter = retrieve()
    counter = counter + 1
    print(counter)
    update(counter)

@bot.command()
async def invite(ctx):
    e = d.Embed(title="Click The Button To Invite Me", color=0x00ff00)
    inv = await ctx.send(embeds=[e],components=[Button(style=ButtonStyle.URL, label="Invite Me !", url=invite_url)])
    time.sleep(5)
    await inv.edit(embeds=[e],components=[Button(style=ButtonStyle.URL, label="Invite Me !", url=invite_url,disabled=True)])

@bot.command()
async def help(ctx):
    ping_msg = f'ping : Show Ping'
    calc_msg = f'calc [currentLvl] [targetLvl] [current%]* [target%]* \n     (current% and target% are optionals)'
    invite_msg = f"invite : Send Bot's Invite Link to DM"
    help_msg = ping_msg + '\n' + calc_msg + '\n' + invite_msg
    await ctx.send(help_msg)

@bot.command()
async def guide(ctx):
    emoji_0 = bot.get_emoji(tlr['Paper'])
    emoji_1 = bot.get_emoji(tlr['Book'])
    emoji_2 = bot.get_emoji(tlr['Ember Tome'])
    emoji_3 = bot.get_emoji(tlr['Leech Tome'])
    emoji_4 = bot.get_emoji(tlr['Haunt Tome'])
    emoji_5 = bot.get_emoji(tlr['Icicle Tome'])
    emoji_6 = bot.get_emoji(tlr['Ignite Tome'])
    emoji_7 = bot.get_emoji(tlr['Drain Tome'])
    emoji_8 = bot.get_emoji(tlr['Curse Tome'])
    emoji_9 = bot.get_emoji(tlr['Freeze Tome'])
    emoji_10 = bot.get_emoji(tlr['Inferno Tome'])
    emoji_11 = bot.get_emoji(tlr['Consume Tome'])
    emoji_12 = bot.get_emoji(tlr['Torture Tome'])

    guide_msg =   f'Lv. 1-3 : 100 {emoji_0} Papers \n
                    Lv. 3-5 : 27 {emoji_1} Book \n
                    Lv. 5-9 : 35 {emoji_2} Ember Tomes \n
                    Lv. 9-15 : 62 {emoji_3} Leech Tomes \n
                    Lv. 15-20 : 79 {emoji_4} Haunt Tomes \n
                    Lv. 20-29 : 270 {emoji_5} Icicle Tomes \n
                    Lv. 29-33 : 113 {emoji_6} Ignite Tomes \n
                    Lv. 33-40 : 375 {emoji_7} Drain Tomes \n
                    Lv. 40-60 : 5193 {emoji_8} Curse Tomes \n
                    Lv. 60-68 : 2501 {emoji_9} Freeze Tomes \n
                    Lv. 68-76 : 4943 {emoji_10} Inferno Tomes \n
                    Lv. 76-80 : 3576 {emoji_11} Consume Tomes \n
                    Lv. 80-92 : 27567 {emoji_12} Torture Tomes'

    embed=d.Embed(title="Tailoring Guide", 
                               description=guide_msg, 
                               color=0x0000FF)
    await ctx.send(embed=embed)


@bot.command()
async def servers(ctx):
    tech_id = 465858376182530059
    if ctx.author.id == int(tech_id) :
        guilds = list(bot.guilds)
        await ctx.send(f"Connected on {str(len(guilds))} servers:")
        await ctx.send('\n'.join(guild.name for guild in guilds))
    else :
        await ctx.send("You don't have permissions to check this")

@bot.event
async def  on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that ;-;")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter all the required arguments \ncalc [currentLvl] [targetLvl] [current%]* [target%]* ")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("Member not found, Please mention a valid user!")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have the permissions to do that!")
    else:
        raise error

bot.run(os.environ.get("TOKEN"))
