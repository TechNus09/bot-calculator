import asyncio
import discord as d
from discord.ext import commands
from discord.utils import get
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


skis = ['','-mining', '-smithing', '-woodcutting', '-crafting', '-fishing', '-cooking']
skils = ['combat','mining', 'smithing', 'woodcutting', 'crafting', 'fishing', 'cooking']



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
mining={"tinO": 10, "copperO": 10, "IronO" : 50,"saltO": 80, "coalO": 115, "silverO": 135, "crimsteelO": 350,
"goldO": 400, "pinksaltO" : 500, "mythanO": 650, "sandstoneO": 1100, "cobaltO": 1200, "varaxiumO": 1800, "blacksaltO": 2500}
smelting ={ "BronzeB" : 24, "ironB" : 8,	"steelB" : 14 , "crimsteelB" : 25,
"silverB" : 50,"goldN" : 60,"goldB" : 60,"mythanB" : 100,"cobaltB" : 200,"varaxiteB" : 350}
smithing ={ "BronzeB" : 5, "ironB" : 14,"steelB" : 20 , "crimsteelB" : 130,
"silverB" : 1000,"goldB" : 20000,"mythanB" : 5000,"cobaltB" : 15000,"varaxiteB" : 20000}
woodcutting={"pine": 10,"deadlog": 20,"birch": 50,"applewood": 115,"willow": 350,"oak": 475,
"chestnut": 650,"maple": 1200,"Olive": 1800,"palm": 2600}
crafting={"accuracyRelic":3 ,"guardingRelic":8 ,"healRelic":18 ,"wealthRelic":40 ,"powerRelic":105 ,"natureRelic":200 ,
"fireRelic":425 ,"damageRelic":900 ,"leechRelic":1400 ,"expRelic":1850 ,"cursedRelic":2750}
fishing={"anchovies":10,"goldfish":20,"mackerel":50,"squid":115,"sardine":375,"eel":500,"anglerfish":625,
"trout":750,"jellyfish":900,"bass":1350,"herringbone":1700,"tuna":2000,"lobster":3500,"sea_turtle":6500,
"manta_ray":9500,"shark":14500,"orca":29500,"giant_squid":55000}
cooking={"anchovies":10,"mackerel":50,"squid":115,"sardine":375,"eel":500,"anglerfish":30,
"trout":750,"bass":1350,"tuna":2000,"lobster":3500,"sea_turtle":6500,
"manta_ray":9500,"shark":13500,"orca":22500,"giant_squid":41500}
miningresc=["tinO","copperO","IronO","saltO","coalO","silverO","crimsteelO",
"goldO","pinksaltO","mythanO","sandstoneO","cobaltO","varaxiumO","blacksaltO"]
smithingresc =["BronzeB","ironB","steelB","crimsteelB","silverB","goldN",
"goldB","mythanB","cobaltB","varaxiteB"]
woodcuttingresc=["pine","deadlog","birch","applewood","willow","oak","chestnut",
"maple","Olive","palm"]
craftingresc=["accuracyRelic","guardingRelic","healRelic","wealthRelic",
"powerRelic","natureRelic","fireRelic","damageRelic","leechRelic","expRelic",
"cursedRelic"]
fishingresc=["anchovies","goldfish","mackerel","squid","sardine","eel","anglerfish",
"trout","jellyfish","bass","herringbone","tuna","lobster","sea_turtle","manta_ray",
"shark","orca","giant_squid"]
cookingresc=["anchovies","mackerel","squid","sardine","eel","anglerfish","trout",
"bass","tuna","lobster","sea_turtle","manta_ray","shark","orca","giant_squid"]
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
skills=["combat", "mining", "smithing", "woodcutting", "crafting", "fishing", "cooking"]
skillss={"combat": combatresc, "mining": miningresc, "smithing":smithingresc, "woodcutting":woodcuttingresc, "crafting": craftingresc, "fishing":fishingresc, "cooking":cookingresc}
skillsss={"combat": combat, "mining": mining, "smithing":smithing, "woodcutting":woodcutting, "crafting": crafting, "fishing":fishing, "cooking":cooking}
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
def tabfill(xp):    
    lvl=0
    a=0
    for l in range(120):
        if (xp > lvltab[l]):
            lvl = l+1
            a = round((((xp- lvltab[l]) / lvldef[l])*100),2)
    return lvl, a

def getxp( lv, nlv, per, nper ):
        minxp= lvltab[lv-1] + (lvldef[lv-1]*(per/100))
        bigxp= lvltab[nlv-1] + (lvldef[nlv-1]*(nper/100))
        XPneeded = round(bigxp - minxp)
        return XPneeded

def show(skill):
    string = "| "
    temp_rsc = skillss[skill]
    for i in range(len(temp_rsc)):
        string = string + temp_rsc[i]+ ' | '
    return string

###########################################################################################


bot = commands.Bot(command_prefix='*')
client = d.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=d.Activity(type=d.ActivityType.watching, name="Calculator"))




@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def calc(ctx,skill_name,curr_lvl,curr_perc,tar_lvl,tar_perc,rsc):

    rescneeded=round(getxp( int(curr_lvl), int(tar_lvl), int(curr_perc), int(tar_perc) )/skillsss[skill_name][rsc])
    invneeded=round(rescneeded/36)

    if skill_name == 'combat' :
        msg = f'you need {rescneeded} of {rsc}'
    else:
        msg = f'you need {rescneeded} of {rsc} (approximately {invneeded} inventories)'
    
    await ctx.send(msg)

@bot.command()
async def how(ctx):
    help_msg = f' *calc [skill_name] [current_lvl] [current_%] [target_lvl] [target_%] [rescource_name]'
    await ctx.send(help_msg)

@bot.command()
async def rsc_of(ctx,skill_name):
    resources = show(skill_name)
    await ctx.send(resources)

bot.run(os.environ.get("TOKEN"))
