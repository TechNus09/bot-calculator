import asyncio
import discord as d
from discord.utils import get
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot, component, interaction, ButtonStyle
import math
import os
import time

invite_url = 'https://discord.com/api/oauth2/authorize?client_id=891750013774991370&permissions=2147814464&scope=bot'
combat={"Bat" : 8 ,"Slime" : 16 ,"Fishing Spider" : 38,"Mashroom" : 46,"Forest Spider" : 55 ,"Forest Bat": 60 ,"Skeletal Snake" : 300  ,"Cave Spider" : 350 ,"Skeletal Bat" : 385 ,"Cave Bat" : 560 ,
"Forest Fiend" : 1080 ,"Rock Fiend" : 2000 ,"Giant Hornet" : 2100 ," Shadow Flame": 2800,"Shadow fiend": 1500 ,

"Snow Bat" : 125 ,"Ice Slime": 165 ,"Snowman" : 210 ,"Ice Spider" : 250 ,"Ice Fiend" : 850 ,"Ancient Bat" : 2400 ,"Ice Raptor" : 2750 ,"Spectral Flame" : 2700 ,"Phantom Flame" : 2900 ,
"Spectral Fiend" : 3100 ,"Phantom Fiend" : 3600 ,"Ancient Cyclops" : 4000 ,

"Sapphire Scarab" : 400,"Scorpion" : 700 ,"Raptor" : 900 ,"Ruby Scarab" : 1000 ,"Desert Raptor" : 1850 ,"Gold Snake" : 1000 ,"Brown Snake" : 1000 ,"Purple Snake" : 1000 ,"Sandstone Golem" : 11500 ,
"Anubis" : 4000 ,"Cactus Soldier" : 2800 ,"Arosite Scarab" : 2850 ,"Magnetite Scarab" : 4250 ,"Anubis Elite" : 7500 ,

"Luminant Slime" : 2200 ,"Golemite Bat" : 4400 ,"Golemite Fiend" : 5270 ,"Baby Dragon" : 5750 ,

"War Bat" : 1200 ,"Rock Demon" : 10000 ,"Ice Demon" : 16500 ,"Shadow Demon": 	20000,"Ancient War Bat" : 12000 ,"Spinus" : 8500 ,"Reanimated Soul" : 1000 ,"Mummy" : 20000 ,"Golem" : 22500 ,"Umbra" : 24000 ,
}


bright_leaf = ["Bat" ,"Slime" ,"Fishing Spider" ,"Mashroom" ,"Forest Spider" ,"Forest Bat" ,"Skeletal Snake" ,"Cave Spider" ,"Skeletal Bat" ,"Cave Bat" ,
"Forest Fiend" ,"Rock Fiend" ,"Giant Hornet" ," Shadow Flame" ,"Shadow fiend" ]
wintermist =["Snow Bat" ,"Ice Slime" ,"Snowman" ,"Ice Spider" ,"Ice Fiend" ,"Ancient Bat" ,"Ice Raptor" ,"Spectral Flame" ,"Phantom Flame"  
"Spectral Fiend" ,"Phantom Fiend" ,"Ancient Cyclops" ]
desert = ["Sapphire Scarab" ,"Scorpion" ,"Raptor" ,"Ruby Scarab" ,"Desert Raptor" ,"Gold Snake" ,"Brown Snake" ,"Purple Snake" ,"Sandstone Golem" ,
"Anubis" ,"Cactus Soldier" ,"Arosite Scarab" ,"Magnetite Scarab" ,"Anubis Elite" ]
varaxite = ["Luminant Slime" ,"Golemite Bat" ,"Golemite Fiend" ,"Baby Dragon" ]
bosses = ["War Bat" ,"Rock Demon" ,"Ice Demon" ,"Shadow Demon" ,"Ancient War Bat" ,"Spinus" ,"Reanimated Soul" ,"Mummy" ,"Golem" ,"Umbra" ]
locations = ["Bright Leaf","Wintermist","Desert","Varaxite","Bosses"]





skills = ['Combat','Mining','Smithing','Woodcutting','crafting','Fishing','Cooking']

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
"Trout", "Trout+Jellyfish", "Bass", "Bass+Herringbone", "Tuna", "Lobster", "Lobster+SeaTurtle", "Manta Ray", 
"Shark", "Shark+Orca", "Shark+Orca+GiantSquid"]
cookingRsc=["Cooked Anchovies", "Cooked Mackerel", "Cooked Squid", "Cooked Sardine", "Cooked Eel", 
"Cooked Anglerfish", "Cooked Trout", "Cooked Bass", "Cooked Tuna", "Cooked Lobster", 
"Cooked Sea Turtle", "Cooked Manta Ray", "Cooked Shark", "Cooked Orca", "Cooked Giant Squid"]
combatRsc=[bright_leaf,wintermist,desert,varaxite,bosses]
baits = {"Anchovies":" Earthworm", "Goldfish":" Earthworm", "Mackerel":"Iceworm", "Squid":"Iceworm", "Sardine":"Corpseworm", "Eel":"ToxicWorm", "Anglerfish":"Sandworm", 
"Trout":"Beetle", "Trout+Jellyfish":"Beetle", "Bass":"Grasshopper", "Bass+Herringbone":"Grasshopper", "Tuna":"Wasp", "Lobster":"Scallop", "Lobster+SeaTurtle":"Scallop", "Manta Ray":"Crab", 
"Shark":"Bass", "Shark+Orca":"Bass", "Shark+Orca+GiantSquid":"Bass"}


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
"Trout":750,"Jellyfish":900,"Trout+Jellyfish":825,"Bass":1350,"Herringbone":1700,"Bass+Herringbone":1525,"Tuna":2000,"Lobster":3500,"Sea Turtle":6500,"Lobster+SeaTurtle":5000,
"Manta Ray":9500,"Shark":14500,"Orca":29500,"Giant Squid":55000,"Shark+Orca":22000,"Shark+Orca+GiantSquid":33000,
"Cooked Anchovies":10,"Cooked Mackerel":50,"Cooked Squid":115,"Cooked Sardine":375,"Cooked Eel":500,"Cooked Anglerfish":30,
"Cooked Trout":750,"Cooked Bass":1350,"Cooked Tuna":2000,"Cooked Lobster":3500,"Cooked Sea Turtle":6500,
"Cooked Manta Ray":9500,"Cooked Shark":13500,"Cooked Orca":22500,"Cooked Giant Squid":41500}

Combat_boosts = ["NoBoost","XpRelics","XpPotion","XpRelics+XpPotion","WorldBoost","XpRelics+WorldBoost","XpPotion+WorldBoost","XpRelics+XpPotion+WorldBoost"]
Mining_boosts = ["NoBoost","ProsNeck","WorldBoost","ProsNeck+WorldBoost"]
Smithing_boosts = ["NoBoost","InfHammer","InfRing","InfHammer+InfRing","WorldBoost","hammer+WorldBoost","Ring+WorldBoost","Hammer+Ring+WorldBoost"]
Woodcutting_boosts = ["NoBoost","WorldBoost"]
Crafting_boosts = ["NoBoost","WorldBoost"]
Fishing_boosts = ["NoBoost","WorldBoost"]
Cooking_boosts = ["NoBoost","WorldBoost"]
boostsValues = {"NoBoost":1.0,"InfHammer":1.04,"InfRing":1.04,"XpRelics":1.05,"XpPotion":1.05,"ProsNeck":1.05,"InfHammer+InfRing":1.0816,"XpRelics+XpPotion":1.1025,"WorldBoost":1.5,"hammer+WorldBoost":1.56,
"Ring+WorldBoost":1.56,"XpRelics+WorldBoost":1.575,"XpPotion+WorldBoost":1.575,"ProsNeck+WorldBoost":1.575,"Hammer+Ring+WorldBoost":1.6224,"XpRelics+XpPotion+WorldBoost":1.65375}

boosts = [Combat_boosts,Mining_boosts,Smithing_boosts,Woodcutting_boosts,Crafting_boosts,Fishing_boosts,Cooking_boosts]

skill_rsc = [combatRsc,miningRsc, smithingRsc, woodcuttingRsc, craftingRsc, fishingRsc,cookingRsc]



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
            SelectOption(label='⚔ Combat',value='0'),
            SelectOption(label='⛏ Mining',value='1'),
            SelectOption(label='⚒ Smiting',value='2'),
            SelectOption(label='🌴 woodcutting',value='3'),
            SelectOption(label='🔨 Crafting',value='4'),
            SelectOption(label='🎣 Fishing',value='5'),
            SelectOption(label='🍳 Cooking',value='6'),
            SelectOption(label='🚫 Cancel',value='Cancel')
            
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
            temp_list.append(SelectOption(label=location_list[i],value=str(i+1)))
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
                temp_list.append(SelectOption(label=mob_list[i],value=str(i+1)))
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
                    temp_list1.append(SelectOption(label=boost_list[i],value=str(i+1)))
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
                    mob_used = combatRsc[int(choice3)-1][int(choice4)-1]
                    mob_xp = combat[mob_used]
                    bst_name = boost_list[int(choice2)-1]
                    bst_used = boostsValues[bst_name]
                    chosen_skill = skills[int(choice)] 
                    xp_needed = getxp(int(curLv),int(tarLv),float(curPerc),float(tarPerc))
                    rsc_needed = math.ceil(xp_needed / mob_xp) + 1
                    rsc_needed_boosted = math.ceil(rsc_needed / bst_used)
                    result = 'Skill : Combat' + '\n Mob : ' + mob_used + '\n Current Lvl : ' + curLv + ' ' + curPerc + '%' + '\n target Lvl : ' + tarLv + ' ' + tarPerc + '%' + '\n Boost : ' + bst_name + '\n Quantity Needed : ' + str(rsc_needed_boosted)
                    
                    await ctx.send(result)

        
    else:
        rsc_list = skill_rsc[int(choice)]
        temp_list = []
        for i in range(len(rsc_list)):
            temp_list.append(SelectOption(label=rsc_list[i],value=str(i+1)))
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
                temp_list1.append(SelectOption(label=boost_list[i],value=str(i+1)))
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
                rsc_used = skill_rsc[int(choice)][int(choice1)-1]
                rsc_xp = resources[rsc_used]
                bst_name = boost_list[int(choice2)-1]
                bst_used = boostsValues[bst_name]
                chosen_skill = skills[int(choice)] 
                xp_needed = getxp(int(curLv),int(tarLv),float(curPerc),float(tarPerc))
                rsc_needed = math.ceil(xp_needed / rsc_xp) + 1
                rsc_needed_boosted = math.ceil(rsc_needed / bst_used)
                if chosen_skill.lower() == "fishing" :
                    result = 'Skill : ' + chosen_skill.capitalize() + '\n Fish : ' + skill_rsc[int(choice)][int(choice1)-1] +'\n Bait : ' + baits[rsc_used] + '\n Current Lvl : ' + curLv + ' ' + curPerc + '%' + '\n target Lvl : ' + tarLv + ' ' + tarPerc + '%' + '\n Boost : ' + bst_name + '\n Quantity Needed : ' + str(rsc_needed_boosted)
                else :
                    result = 'Skill : ' + chosen_skill.capitalize() + '\n Resource : ' + skill_rsc[int(choice)][int(choice1)-1] + '\n Current Lvl : ' + curLv + ' ' + curPerc + '%' + '\n target Lvl : ' + tarLv + ' ' + tarPerc + '%' + '\n Boost : ' + bst_name + '\n Quantity Needed : ' + str(rsc_needed_boosted)
                
                await ctx.send(result)



###########################################################################################



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    await bot.change_presence(activity=d.Game(name="Calculator"))

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

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

@bot.command()
async def invite(ctx):
    e = d.Embed(title="Click The Button To Invite Me", color=0x00ff00)
    inv = await ctx.send(embeds=[e],components=[Button(style=ButtonStyle.URL, label="Invite Me !", url=invite_url)])
    time.sleep(10)
    await inv.edit(embeds=[e],components=[Button(style=ButtonStyle.URL, label="Invite Me !", url=invite_url,disabled=True)])

@bot.command()
async def help(ctx):
    ping_msg = f'ping : Show Ping'
    calc_msg = f'calc [currentLvl] [targetLvl] [current%]* [target%]*'
    invite_msg = f"invite : Send Bot's Invite Link to DM"
    help_msg = ping_msg + '\n' + calc_msg + '\n' + invite_msg
    await ctx.send(help_msg)

@bot.command()
async def servers(ctx):
    tech_id = os.environ.get("TECH_ID")
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
