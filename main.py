import asyncio
import discord as d
from discord.utils import get
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot, component, interaction
import math
import os









lvltab = [0,46,99,159,229,309,401,507,628,768,928,1112,1324,1567,1847,2168,2537,2961,3448,4008,4651,5389,6237,7212,
8332,9618,11095,12792,14742,16982,19555,22510,25905,29805,34285,39431,45342,52132,59932,68892,79184,91006,104586,
120186,138106,158690,182335,209496,240696,276536,317705,364996,419319,481720,553400,635738,730320,838966,963768,
1107128,1271805,1460969,1678262,1927866,2214586,2543940,2922269,3356855,3856063,4429503,5088212,5844870,6714042,
7712459,8859339,10176758,11690075,13428420,15425254,17719014,20353852,23380486,26857176,30850844,35438364,40708040,
46761308,53714688,61702024,70877064,81416417,93522954,107429714,123404386,141754466,162833172,187046247,214859767,
246809111,283509271,325666684,374092835,429719875,493618564,567018884,651333710,748186012,859440093,987237472,
1134038112,1302667765,1496372370,1718880532,1974475291,2268076571,2605335878,2992745089,3437761413,3948950932,
4536153492,5210672106]
lvldef = [46, 53, 60, 70, 80, 92, 106, 121, 140, 160, 184, 212, 243, 280, 321, 369, 424, 487, 560, 643, 738, 
848, 975, 1120, 1286, 1477, 1697, 1950, 2240, 2573, 2955, 3395, 3900, 4480, 5146, 5911, 6790, 7800, 8960, 
10292, 11822, 13580, 15600, 17920, 20584, 23645, 27161, 31200, 35840, 41169, 47291, 54323, 62401, 71680, 82338,
94582, 108646, 124802, 143360, 164677, 189164, 217293, 249604, 286720, 329354, 378329, 434586, 499208, 573440,
658709, 756658, 869172, 998417, 1146880, 1317419, 1513317, 1738345, 1996834, 2293760, 2634838, 3026634, 3476690,
3993668, 4587520, 5269676, 6053268, 6953380, 7987336, 9175040, 10539353, 12106537, 13906760, 15974672, 18350080,
21078706, 24213075, 27813520, 31949344, 36700160, 42157413, 48426151, 55627040, 63898689, 73400320, 84314826,
96852302, 111254081, 127797379, 146800640, 168629653, 193704605, 222508162, 255594759, 293601280, 337259307,
387409211, 445016324, 511189519, 587202560]






combat={"bat" : 8 ,"slime" : 16 ,"fishing_spider" : 38,"mashroom" : 46,"forest_spider" : 55 ,"forest_bat": 60 ,"snow_bat" : 125 ,
"ice_slime": 165 ,"snowman" : 210 ,"ice_spider" : 250 ,"skeletal_snake" : 300  ,"cave_spider" : 350 ,"skeletal_bat" : 385 ,
"sapphire_scarab" : 400,"cave_bat" : 560 ,"scorpion" : 700 ,"ice_fiend" : 850 ,"raptor" : 900 ,"ruby_scarab" : 1000 ,
"forest_fiend" : 1080 ,"desert_raptor" : 1850 ,"rock_fiend" : 2000 ,"giant_hornet" : 2100 ,"luminant_slime" : 2200 ,
"ancient_bat" : 2400 ,"ice_raptor" : 2750 ,"arosite_scarab" : 2850 ,"spectral_flame" : 2700 ,"cactus_soldier" : 2800 ,
"phantom_flame" : 2900 ,"spectral_fiend" : 3100 ,"phantom_fiend" : 3600 ,"ancient_cyclops" : 4000 ,"anubis" : 4000 ,
"magnetite_scarab" : 4250 ,"golemite_bat" : 4400 ,"golemite_fiend" : 5270 ,"poltergeist" : 250 ,"anubis_elite" : 7500 ,
"baby_dragon" : 5750 ,"gold_snake" : 1000 ,"brown_snake" : 1000 ,"purple_snake" : 1000 ,"sandstone_golem" : 11500 ,
"cursed_totem" : 1 ,"war_bat" : 1200 ,"rock_demon" : 10000 , "spinus" : 8500 ,"ancient_war_bat" : 12000 ,
"ice_Demon" : 16500 ,"reanimated_soul" : 1000 ,"golem" : 22500 ,"umbra" : 24000 ,"mummy" : 20000 }





skills = ['Mining','Smithing','Woodcutting','crafting','Fishing','Cooking']

miningRsc=["Tin Ore","Copper Ore","Iron Ore","Salt","Coal","Silver Ore","Crimsteel Ore",
"Gold Ore","PinkSalt","Mythan Ore","Sandstone","Cobalt Ore","Varaxium","BlackSalt"]
smithingRsc =["Bronze Bar","Iron Bar","Steel Bar","Crimsteel Bar","Silver Bar","Gold Nugget",
"Gold Bar","Mythan Bar","Cobalt Bar","Varaxite Bar"]
woodcuttingRsc=["Pine Log","Dead Log","Birch Log","Applewood","Willow Log","Oak Log","Chestnut Log",
"Maple Log","Olive Log","Palm Wood"]
craftingRsc=["Accuracy Relic","Guarding Relic","Healing Relic","Wealth Relic",
"Power Relic","Nature Relic","Fire Relic","Damage Relic","Leeching Relic","Experience Relic",
"Cursed Relic"]
fishingRsc=["Anchovies", "Goldfish", "Mackerel", "Squid", "Sardine", "Eel", "Anglerfish", 
"Trout", "Jellyfish", "Bass", "Herringbone", "Tuna", "Lobster", "Sea Turtle", "Manta Ray", 
"Shark", "Orca", "Giant Squid"]
cookingRsc=["Cooked Anchovies", "Cooked Mackerel", "Cooked Squid", "Cooked Sardine", "Cooked Eel", 
"Cooked Anglerfish", "Cooked Trout", "Cooked Bass", "Cooked Tuna", "Cooked Lobster", 
"Cooked Sea Turtle", "Cooked Manta Ray", "Cooked Shark", "Cooked Orca", "Cooked Giant Squid"]
    
resources = {
"Tin Ore": 10, "Copper Ore": 10, "Iron Ore" : 50,"Salt": 80, "Coal": 115, "Silver Ore": 135, "Crimsteel Ore": 350,
"Gold Ore": 400, "PinkSalt" : 500, "Mythan Ore": 650, "Sandstone": 1100, "Cobalt Ore": 1200, "Varaxium": 1800, "BlackSalt": 2500,
"Bronze Bar" : 5, "Iron Bar" : 14,"Steel Bar" : 20 , "Crimsteel Bar" : 130,
"Silver Bar" : 1000,"Gold Bar" : 20000,"Mythan Bar" : 5000,"Cobalt Bar" : 15000,"Varaxite Bar" : 20000,
"Pine Log": 10,"Dead Log": 20,"Birch Log": 50,"Applewood": 115,"Willow Log": 350,"Oak Log": 475,
"Chestnut Log": 650,"Maple Log": 1200,"Olive Log": 1800,"Palm Wood": 2600,
"Accuracy Relic":3 ,"Guarding Relic":8 ,"Healing Relic":18 ,"Wealth Relic":40 ,"Power Relic":105 ,"Nature Relic":200 ,
"Fire Relic":425 ,"Damage Relic":900 ,"leeching Relic":1400 ,"Experience Relic":1850 ,"Cursed Relic":2750,
"Anchovies":10,"Goldfish":20,"Mackerel":50,"Squid":115,"Sardine":375,"Eel":500,"Anglerfish":625,
"Trout":750,"Jellyfish":900,"Bass":1350,"Herringbone":1700,"Tuna":2000,"Lobster":3500,"Sea Turtle":6500,
"Manta Ray":9500,"Shark":14500,"Orca":29500,"Giant Squid":55000,
"Cooked Anchovies":10,"Cooked Mackerel":50,"Cooked Squid":115,"Cooked Sardine":375,"Cooked Eel":500,"Cooked Anglerfish":30,
"Cooked Trout":750,"Cooked Bass":1350,"Cooked Tuna":2000,"Cooked Lobster":3500,"Cooked Sea Turtle":6500,
"Cooked Manta Ray":9500,"Cooked Shark":13500,"Cooked Orca":22500,"Cooked Giant Squid":41500}


Combat_boosts = ["NoBoost","XpRelics","XpPotion","XpRelics+XpPotion","WorldBoost","XpRelics+WorldBoost","XpPotion+WorldBoost","XpRelics+XpPotion+WorldBoost"]
Mining_boosts = ["NoBoost","ProsNeck","WorldBoost","ProsNeck+WorldBoost"]
Smithing_boosts = ["NoBoost","InfHammer","InfRing","InfHammer+InfRing","WorldBoost","hammer+WorldBoost","Ring+WorldBoost","Hammer+Ring+WorldBoost"]
Woodcutting_boosts = ["NoBoost","World Boost"]
Crafting_boosts = ["NoBoost","World Boost"]
Fishing_boosts = ["NoBoost","World Boost"]
Cooking_boosts = ["NoBoost","World Boost"]
boostsValues = {"NoBoost":1.0,"InfHammer":1.04,"InfRing":1.04,"XpRelics":1.05,"XpPotion":1.05,"ProsNeck":1.05,"InfHammer+InfRing":1.0816,"XpRelics+XpPotion":1.1025,"WorldBoost":1.5,"hammer+WorldBoost":1.56,"Ring+WorldBoost":1.56,"XpRelics+WorldBoost":1.575,"XpPotoin+WorldBoost":1.575,"ProsNeck+WorldBoost":1.575,"Hammer+Ring+WorldBoost":1.6224,"XpRelics+XpPotoin+WorldBoost":1.65375}


boosts = [Mining_boosts,Smithing_boosts,Woodcutting_boosts,Crafting_boosts,Fishing_boosts,Cooking_boosts]


skill_rsc = [miningRsc, smithingRsc, woodcuttingRsc, craftingRsc, fishingRsc,cookingRsc]




combatresc=["bat","slime","fishing_spider","mashroom","forest_spider","forest_bat",
"snow_bat","ice_slime","snowman","ice_spider",
"skeletal_snake","cave_spider","skeletal_bat","sapphire_scarab","cave_bat","scorpion",
"ice_fiend","raptor","ruby_scarab",
"forest_fiend","desert_raptor","rock_fiend","giant_hornet","luminant_slime",
"ancient_bat","ice_raptor","arosite_scarab",
"spectral_flame","cactus_soldier","phantom_flame","spectral_fiend","phantom_fiend",
"ancient_cyclops","anubis",
"magnetite_scarab","golemite_bat","golemite_fiend","poltergeist","anubis_elite",
"baby_dragon","gold snake","brown snake",
"purple_snake","sandstone_golem","cursed_totem","war_bat","rock_demon","spinus",
"ancient_war_bat","ice_Demon","reanimated_soul",
"golem","umbra","mummy"]



lvltab = [0,46,99,159,229,309,401,507,628,768,928,1112,1324,1567,1847,2168,2537,2961,3448,4008,4651,5389,6237,7212,8332,9618,11095,12792,14742,16982,19555,22510,25905,29805,34285,
39431,45342,52132,59932,68892,79184,91006,104586,120186,138106,158690,182335,209496,240696,276536,317705,364996,419319,481720,553400,635738,730320,838966,963768,1107128,1271805,
1460969,1678262,1927866,2214586,2543940,2922269,3356855,3856063,4429503,5088212,5844870,6714042,7712459,8859339,10176758,11690075,13428420,15425254,17719014,20353852,23380486,
26857176,30850844,35438364,40708040,46761308,53714688,61702024,70877064,81416417,93522954,107429714,123404386,141754466,162833172,187046247,214859767,246809111,283509271,325666684,
374092835,429719875,493618564,567018884,651333710,748186012,859440093,987237472,1134038112,1302667765,1496372370,1718880532,1974475291,2268076571,2605335878,2992745089,3437761413,
3948950932,4536153492,5210672106]
lvldef = [46, 53, 60, 70, 80, 92, 106, 121, 140, 160, 184, 212, 243, 280, 321, 369, 424, 487, 560, 643, 738, 848, 975, 1120, 1286, 1477, 1697, 1950, 2240, 2573, 2955, 3395, 3900, 
4480, 5146, 5911, 6790, 7800, 8960, 10292, 11822, 13580, 15600, 17920, 20584, 23645, 27161, 31200, 35840, 41169, 47291, 54323, 62401, 71680, 82338, 94582, 108646, 124802, 143360, 
164677, 189164, 217293, 249604, 286720, 329354, 378329, 434586, 499208, 573440, 658709, 756658, 869172, 998417, 1146880, 1317419, 1513317, 1738345, 1996834, 2293760, 2634838, 3026634, 
3476690, 3993668, 4587520, 5269676, 6053268, 6953380, 7987336, 9175040, 10539353, 12106537, 13906760, 15974672, 18350080, 21078706, 24213075, 27813520, 31949344, 36700160, 42157413, 
48426151, 55627040, 63898689, 73400320, 84314826, 96852302, 111254081, 127797379, 146800640, 168629653, 193704605, 222508162, 255594759, 293601280, 337259307, 387409211, 445016324, 
511189519, 587202560]

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

def getxp( lv, nlv, per = 0, nper = 0 ):
        minxp= lvltab[lv-1] + (lvldef[lv-1]*(per/100))
        bigxp= lvltab[nlv-1] + (lvldef[nlv-1]*(nper/100))
        XPneeded = round(bigxp - minxp)
        return XPneeded
    
async def selectionTest(ctx,curLv,tarLv):
    await ctx.send(content='Skill :',components=[Select(
        placeholder='Select Skill !',
        options=[
            SelectOption(label='⛏ Mining',value='0'),
            SelectOption(label='⚒ Smiting',value='1'),
            SelectOption(label='🪓 woodcutting',value='2'),
            SelectOption(label='🔨 Crafting',value='3'),
            SelectOption(label='🎣 Fishing',value='4'),
            SelectOption(label='🍽 Cooking',value='5'),
            SelectOption(label='🚫 Cancel',value='Cancel')
            
            ],custom_id='SelectSkill'
    )])
    interaction = await bot.wait_for('select_option',
    check=lambda inter: inter.custom_id == 'SelectSkill' and inter.user == ctx.author)
    
    choice = interaction.values[0]
    if choice == 'Cancel' :
        await interaction.send('You have canceled the interaction')
    
    else:
        rsc_list = skill_rsc[int(choice)]
        temp_list = []
        for i in range(len(rsc_list)):
            temp_list.append(SelectOption(label=rsc_list[i],value=str(i+1)))
        temp_list.append(SelectOption(label="Cancel",value="Cancel"))
        await ctx.send(content='Resource :',components=[Select(
        placeholder='Select Resource !',
        options=temp_list
        
        ,custom_id='SelectRsc'
        )])
        interaction1 = await bot.wait_for('select_option',
        check=lambda inter: inter.custom_id == 'SelectRsc' and inter.user == ctx.author)
        
        choice1 = interaction1.values[0]
        if choice1 == 'Cancel' :
            await interaction1.send('You have canceled the interaction')

        else:
            boost_list = boosts[int(choice)]
            temp_list1 = []
            for i in range(len(boost_list)):
                temp_list1.append(SelectOption(label=boost_list[i],value=str(i+1)))
            temp_list1.append(SelectOption(label="Cancel",value="Cancel"))
            await ctx.send(content='Boost :',components=[Select(
            placeholder='Select Boost !',
            options=temp_list1
            
            ,custom_id='SelectBst'
            )])
            interaction2 = await bot.wait_for('select_option',
            check=lambda inter: inter.custom_id == 'SelectBst' and inter.user == ctx.author)
            
            choice2 = interaction2.values[0]
            if choice2 == 'Cancel' :
                await interaction1.send('You have canceled the interaction')

            else:
                rsc_used = skill_rsc[int(choice)][int(choice1)-1]
                rsc_xp = resources[rsc_used]
                bst_name = boost_list[int(choice2)-1]
                bst_used = boostsValues[bst_name]
                xp_needed = getxp(int(curLv),int(tarLv))
                rsc_needed = math.ceil(xp_needed / rsc_xp) + 1
                rsc_needed_boosted = math.ceil(rsc_needed * bst_used)
                result = 'Skill : ' + skills[int(choice)] + '\n Resource : ' + skill_rsc[int(choice)][int(choice1)-1] + '\n Current Lvl : ' + curLv + '\n target Lvl : ' + tarLv + '\n Boost : ' + bst_name + '\n Quantity Needed : ' + str(rsc_needed_boosted)
                
                await ctx.send(result)



###########################################################################################



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await bot.change_presence(activity=d.Game(name="Calculator"))




@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")
    
@bot.command()
async def calc(ctx,curLv,tarLv):
    await selectionTest(ctx,curLv,tarLv)

@bot.command()
async def invite(ctx):
    member = ctx.author
    channel = await member.create_dm()
    await channel.send('https://discord.com/api/oauth2/authorize?client_id=891750013774991370&permissions=39936&scope=bot')

@bot.command()
async def help(ctx):
    ping_msg = f'*ping : Show Ping'
    calc_msg = f'*calc [current_lvl] [target_lvl]'
    invite_msg = f"*invite : Send Bot's Invite Link to DM"
    help_msg = ping_msg + '\n' + calc_msg + '\n' + invite_msg
    await ctx.send(help_msg)

@bot.event
async def  on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You can't do that ;-;")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter all the required arguments \n*calc [current_lvl] [target_lvl]")
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send("Member not found, Please mention a valid user!")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have the permissions to do that!")
    else:
        raise error


bot.run(os.environ.get("TOKEN"))
