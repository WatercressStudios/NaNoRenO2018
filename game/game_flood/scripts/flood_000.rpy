###############################
#
# CHEAT SHEET
#
###############################

### show [character] ###
#formatting below
#show [character] [emotion] with dissolve
#Example: show oph neutral with dissolve

#For list of emotions, see draz's list (or list them out here manually)


### scene background or CGs ###
#formatting below
#scene flood [name here] with dissolve
#Example: scene flood cafe with dissolve

#For list of BG and CGs, see folder (or list them out here manually)


### play music ###

# play music "game_flood/music/[introname].ogg" noloop fadeout 1.0
# queue music "game_flood/music/[loopname].ogg" loop

# play music "game_flood/music/[noloopname].ogg" fadeout 1.0


### play ambience ###

# play ambience "game_flood/ambience/[ambiencename].ogg" fadeout 2.0 fadein 2.0


### play sound ###

# play sound "game_flood/sfx/[sfxname].ogg"


###############################
#
# FLOOD DEFINITIONS GO IN HERE
#
###############################


define oph = Character("oph_name", callback=speaker("oph"), color="#d68385", dynamic=True)
define oli = Character("oli_name", callback=speaker("oli"), color="#aab421", dynamic=True)
define dai = Character("dai_name", callback=speaker("dai"), color="#55b2ad", dynamic=True)
define hop = Character("hop_name", callback=speaker("hop"), color="#ca483d", dynamic=True)
define wai = Character("Waitress", color="#ddd")
define grl = Character("Little Girl", color="#ddd") #Hope
define vce = Character("Voice", color="#ddd") #Hope's Dad
define dad = Character("Dad", color="#ddd")
define mom = Character("Mom", color="#ddd")
define sis = Character("Sister", color="#ddd")
define ogl = Character("Other Girl", color="#ddd")
define per = Character("Performer", color="#ddd") #Daisy
define dsy = Character("Daisy", color="#ddd") #idk why there are two daisy tags
define old = Character("Old Man", color="#ddd") #Oliver
define mgr = Character("Manager", color="#ddd")

image white = "#fff"

init python:
    define_images("game_flood/bgs", 2, False, ["flood"])
    define_images("game_flood/cgs", 2, False, ["flood"])

###############################
#
# FLAGS
#
###############################

default hope = False
default daisy = False
default oliver = False

init:
    $ oph_name = "Ophelia"
    $ oli_name = "Old Man"
    $ dai_name = "Performer"
    $ hop_name = "Little Girl"


###############################
#
# OPH POSE 1 SPRITES
#
###############################

init python:
    OphPose1 = BaseCSprite("oph", "game_flood/sprites/Ophelia/Pose 1/base.png", (414, 1080))

image oph neutral = OphPose1("oph eyes normal1", "oph mouth normal1")
image oph neutral close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth normal1")

image oph defensive = OphPose1("oph eyes defensive1", "oph mouth normal1")
image oph defensive close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes defensive close.png", "oph mouth normal1")

image oph irritated = OphPose1("oph eyes irritated1", "oph mouth normal1")
image oph irritated close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes defensive close.png", "oph mouth normal1")

image oph scared = OphPose1("oph eyes scared1", "oph mouth scared1")
image oph scared close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes scared close.png", "oph mouth scared1")

image oph smile = OphPose1("oph eyes normal1", "oph mouth smile1")
image oph smile close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth smile1")

image oph surprised = OphPose1("oph eyes scared1", "oph mouth normal1")
image oph surprised close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes scared close.png", "oph mouth normal1")

image oph tiredsmile = OphPose1("oph eyes tired1", "oph mouth smile1")
image oph tiredsmile close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes tired close.png", "oph mouth smile1")

image oph weirdedout = OphPose1("oph eyes weirded1", "oph mouth weirded1")
image oph weirdedout close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes weirded close.png", "oph mouth weirded1")


###############################
#
# OLI POSE 1 SPRITES
#
###############################

init python:
    OliPose1 = BaseCSprite("oli", "game_flood/sprites/Oliver/Pose 1/base.png", (696, 1080))

image oli cheerful smile = OliPose1("oli eyes normal1", "oli mouth normal1")
image oli cheerful smile close = OliPose1("game_flood/sprites/Oliver/Pose 1/eyes normal close.png", "oli mouth normal1")

image oli cheerful grin = OliPose1("oli eyes normal1", "oli mouth smile1")
image oli cheerful grin close = OliPose1("game_flood/sprites/Oliver/Pose 1/eyes normal close.png", "oli mouth normal1")

###############################
#
# OLI POSE 2 (NO FLOWER) SPRITES
#
###############################

init python:
    OliPose2 = BaseCSprite("oli", "game_flood/sprites/Oliver/Pose 2/basenoflower.png", (696, 1080))

image oli smile noflower = OliPose2("oli eyes normal2", "oli mouth normal2")
image oli smile noflower close = OliPose2("game_flood/sprites/Oliver/Pose 2/eyes normal close.png", "oli mouth normal2") #No eye close art

image oli serious noflower = OliPose2("oli eyes serious2", "oli mouth serious2")
image oli serious noflower close = OliPose2("game_flood/sprites/Oliver/Pose 2/eyes serious close.png", "oli mouth serious2") #No eye close art

###############################
#
# OLI POSE 2 (FLOWER) SPRITES
#
###############################

init python:
    OliPose2F = BaseCSprite("oli", "game_flood/sprites/Oliver/Pose 2/baseflower.png", (696, 1080))

image oli smile = OliPose2F("oli eyes normal2", "oli mouth normal2")
image oli smile close = OliPose2F("game_flood/sprites/Oliver/Pose 2/eyes normal close.png", "oli mouth normal2") #No eye close art

image oli serious = OliPose2F("oli eyes serious2", "oli mouth serious2")
image oli serious close = OliPose2F("game_flood/sprites/Oliver/Pose 2/eyes serious close.png", "oli mouth serious2") #No eye close art

###############################
#
# DAI POSE 1 SPRITES
#
###############################

init python:
    DaiPose1 = BaseCSprite("dai", "game_flood/sprites/Daisy/Pose 1/base.png", (450, 1080))

image dai neutral = DaiPose1("dai eyes normal1", "dai mouth normal1")
image dai neutral close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes neutral close.png", "dai mouth normal1")

image dai smile = DaiPose1("dai eyes normal1", "dai mouth smile1")
image dai smile close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth smile1")

image dai confident = DaiPose1("dai eyes normal1", "dai mouth confident1")
image dai confident close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth confident1")

image dai hopeful = DaiPose1("dai eyes hopeful1", "dai mouth smile1")
image dai hopeful close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth smile1")

image dai disappointed = DaiPose1("dai eyes disappointed1", "dai mouth sad1")
image dai disappointed close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes disappointed close.png", "dai mouth sad1")

image dai disappointedside = DaiPose1("dai eyes disappointedside1", "dai mouth sad1")
image dai disappointedside close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes disappointed close.png", "dai mouth sad1")

###############################
#
# DAI POSE 2 SPRITES
#
###############################

init python:
    DaiPose2 = BaseCSprite("dai", "game_flood/sprites/Daisy/Pose 2/base.png", (450, 1080))

image dai distant neutral = DaiPose2("dai eyes normal2", "dai mouth normal2")
image dai distant neutral close = DaiPose2("game_flood/sprites/Daisy/Pose 2/eyes normal close.png", "dai mouth normal2") #No eye close art

image dai distant frown = DaiPose2("dai eyes sad1", "dai mouth sad2")
image dai distant frown close = DaiPose2("game_flood/sprites/Daisy/Pose 2/eyes frown close.png", "dai mouth sad2") #No eye close art

###############################
#
# HOP POSE 1 SPRITES
#
###############################

init python:
    HopPose1 = BaseCSprite("hop", "game_flood/sprites/Hope/Pose 1/base.png", (425, 1080))

image hop neutral = HopPose1("hop eyes normal1", "hop mouth normal1")
image hop neutral close = HopPose1("game_flood/sprites/Hope/Pose 1/eyes normal close.png", "hop mouth normal1") #No eye close art

image hop happy = HopPose1("hop eyes happy1", "hop mouth smile1")
image hop happy close = HopPose1("game_flood/sprites/Hope/Pose 1/eyes smile close.png", "hop mouth smile1") #No eye close art

image hop angry = HopPose1("hop eyes angry1", "hop mouth angry1")
image hop angry close = HopPose1("game_flood/sprites/Hope/Pose 1/eyes angry close.png", "hop mouth angry1") #No eye close art

image hop angry clench = HopPose1("hop eyes angry1", "hop mouth angryclench1")
image hop angry clench close = HopPose1("game_flood/sprites/Hope/Pose 1/eyes angry close.png", "hop mouth angryclench1") #No eye close art

###############################
#
# HOP POSE 2 SPRITES
#
###############################

init python:
    HopPose2 = BaseCSprite("hop", "game_flood/sprites/Hope/Pose 2/base.png", (425, 1080))

image hop hurt downtrodden = HopPose2("hop eyes normal2", "hop mouth normal2")
image hop hurt downtrodden close = HopPose2("game_flood/sprites/Hope/Pose 2/eyes normal close.png", "hop mouth normal2") #No eye close art

image hop hurt embarrassed = HopPose2("hop eyes embarrassed2", "hop mouth normal2")
image hop hurt embarrassed close = HopPose2("game_flood/sprites/Hope/Pose 2/eyes embarrassed close.png", "hop mouth normal2") #No eye close art



###############################
#
# OPH POSE 1 COMPOSITE PARTS
#
###############################

image oph eyes normal1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes normal open.png", "game_flood/sprites/Ophelia/Pose 1/eyes normal close.png")

image oph eyes tired1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes tired open.png", "game_flood/sprites/Ophelia/Pose 1/eyes tired close.png")

image oph eyes scared1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes scared open.png", "game_flood/sprites/Ophelia/Pose 1/eyes scared close.png")

image oph eyes weirded1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes weirded open.png", "game_flood/sprites/Ophelia/Pose 1/eyes weirded close.png")

image oph eyes irritated1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes irritated open.png", "game_flood/sprites/Ophelia/Pose 1/eyes defensive close.png")

image oph eyes defensive1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes defensive open.png", "game_flood/sprites/Ophelia/Pose 1/eyes defensive close.png")

image oph mouth normal1 = FlapMouth("oph", "game_flood/sprites/Ophelia/Pose 1/mouth normal close.png", "game_flood/sprites/Ophelia/Pose 1/mouth normal open.png")

image oph mouth scared1 = FlapMouth("oph", "game_flood/sprites/Ophelia/Pose 1/mouth scared open.png", "game_flood/sprites/Ophelia/Pose 1/mouth normal close.png")

image oph mouth weirded1 = FlapMouth("oph", "game_flood/sprites/Ophelia/Pose 1/mouth weirded close.png", "game_flood/sprites/Ophelia/Pose 1/mouth weirded open.png")

image oph mouth smile1 = FlapMouth("oph", "game_flood/sprites/Ophelia/Pose 1/mouth smile close.png", "game_flood/sprites/Ophelia/Pose 1/mouth smile open.png")

###############################
#
# OLI POSE 1 COMPOSITE PARTS
#
###############################

image oli eyes normal1 = blinkeyes("game_flood/sprites/Oliver/Pose 1/eyes normal open.png", "game_flood/sprites/Oliver/Pose 1/eyes normal close.png")

image oli mouth normal1 = FlapMouth("oli", "game_flood/sprites/Oliver/Pose 1/mouth normal close.png", "game_flood/sprites/Oliver/Pose 1/mouth normal open.png")

image oli mouth smile1 = FlapMouth("oli", "game_flood/sprites/Oliver/Pose 1/mouth grin close.png", "game_flood/sprites/Oliver/Pose 1/mouth normal open.png")

###############################
#
# OLI POSE 2 COMPOSITE PARTS
#
###############################

image oli eyes normal2 = blinkeyes("game_flood/sprites/Oliver/Pose 2/eyes normal open.png", "game_flood/sprites/Oliver/Pose 2/eyes normal close.png")

image oli eyes serious2 = blinkeyes("game_flood/sprites/Oliver/Pose 2/eyes serious open.png", "game_flood/sprites/Oliver/Pose 2/eyes serious close.png")

image oli mouth normal2 = FlapMouth("oli", "game_flood/sprites/Oliver/Pose 2/mouth normal close.png", "game_flood/sprites/Oliver/Pose 2/mouth normal open.png")

image oli mouth serious2 = FlapMouth("oli", "game_flood/sprites/Oliver/Pose 2/mouth serious close.png", "game_flood/sprites/Oliver/Pose 2/mouth serious open.png")

###############################
#
# DAI POSE 1 COMPOSITE PARTS
#
###############################

image dai eyes normal1 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes normal open.png", "game_flood/sprites/Daisy/Pose 1/eyes neutral close.png")

image dai eyes hopeful1 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes hopeful open.png", "game_flood/sprites/Daisy/Pose 1/eyes neutral close.png")

image dai eyes disappointed1 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes disappointed open.png", "game_flood/sprites/Daisy/Pose 1/eyes disappointed close.png")

image dai eyes disappointedside1 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes disappointedside open.png", "game_flood/sprites/Daisy/Pose 1/eyes disappointed close.png")

image dai mouth normal1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth normal close.png", "game_flood/sprites/Daisy/Pose 1/mouth normal open.png")

image dai mouth confident1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth confident close.png", "game_flood/sprites/Daisy/Pose 1/mouth smile open.png")

image dai mouth sad1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth sad close.png", "game_flood/sprites/Daisy/Pose 1/mouth sad open.png")

image dai mouth smile1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth smile close.png", "game_flood/sprites/Daisy/Pose 1/mouth smile open.png")

###############################
#
# DAI POSE 2 COMPOSITE PARTS
#
###############################

image dai eyes normal2 = blinkeyes("game_flood/sprites/Daisy/Pose 2/eyes normal open.png", "game_flood/sprites/Daisy/Pose 2/eyes normal close.png")

image dai eyes sad1 = blinkeyes("game_flood/sprites/Daisy/Pose 2/eyes frown open.png", "game_flood/sprites/Daisy/Pose 2/eyes frown close.png")

image dai mouth normal2 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 2/mouth normal close.png", "game_flood/sprites/Daisy/Pose 2/mouth normal open.png")

image dai mouth sad2 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 2/mouth frown close.png", "game_flood/sprites/Daisy/Pose 2/mouth normal open.png")

###############################
#
# HOP POSE 1 COMPOSITE PARTS
#
###############################

image hop eyes normal1 = blinkeyes("game_flood/sprites/Hope/Pose 1/eyes normal open.png", "game_flood/sprites/Hope/Pose 1/eyes normal close.png")

image hop eyes angry1 = blinkeyes("game_flood/sprites/Hope/Pose 1/eyes angry open.png", "game_flood/sprites/Hope/Pose 1/eyes angry close.png")

image hop eyes happy1 = blinkeyes("game_flood/sprites/Hope/Pose 1/eyes smile open.png", "game_flood/sprites/Hope/Pose 1/eyes smile close.png")

image hop mouth normal1 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth normal close.png", "game_flood/sprites/Hope/Pose 1/mouth normal open.png")

image hop mouth smile1 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth close smile.png", "game_flood/sprites/Hope/Pose 1/mouth normal open.png")

image hop mouth angry1 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth angry close.png", "game_flood/sprites/Hope/Pose 1/mouth angry open.png")

image hop mouth angryclench1 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth angry clench.png", "game_flood/sprites/Hope/Pose 1/mouth angry open.png")

###############################
#
# HOP POSE 2 COMPOSITE PARTS
#
###############################

image hop eyes normal2 = blinkeyes("game_flood/sprites/Hope/Pose 2/eyes normal open.png", "game_flood/sprites/Hope/Pose 2/eyes normal close.png")

image hop eyes embarrassed2 = blinkeyes("game_flood/sprites/Hope/Pose 2/eyes embarrassed open.png", "game_flood/sprites/Hope/Pose 2/eyes embarrassed close.png")

image hop mouth normal2 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 2/mouth normal close.png", "game_flood/sprites/Hope/Pose 2/mouth normal open.png")

###############################
#
# FLOOD STORY START
#
###############################

label flood_000:
    $ persistent.last_story = "flood"
    $ current_story = "flood"

    menu:
        "Show everyone's expressions":
            jump flood_expressions

label flood_expressions:
    show oph neutral
    oph "oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... "

    show oph neutral at flip
    oph "oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... oph neutral... "

    show oph neutral close
    oph "oph neutral close... oph neutral close... oph neutral close... oph neutral close... oph neutral close... oph neutral close... oph neutral close... "

    show oph defensive
    oph "oph defensive... oph defensive... oph defensive... oph defensive... oph defensive... oph defensive... oph defensive... oph defensive... oph defensive... "

    show oph defensive close
    oph "oph defensive close... oph defensive close... oph defensive close... oph defensive close... oph defensive close... oph defensive close... oph defensive close... "

    show oph irritated
    oph "oph irritated... oph irritated... oph irritated... oph irritated... oph irritated... oph irritated... oph irritated... oph irritated... oph irritated... "

    show oph irritated close
    oph "oph irritated close... oph irritated close... oph irritated close... oph irritated close... oph irritated close... oph irritated close... oph irritated close... "

    show oph scared
    oph "oph scared... oph scared... oph scared... oph scared... oph scared... oph scared... oph scared... oph scared... oph scared... oph scared... oph scared... "

    show oph scared close
    oph "oph scared close... oph scared close... oph scared close... oph scared close... oph scared close... oph scared close... oph scared close... oph scared close... "

    show oph smile
    oph "oph smile... oph smile... oph smile... oph smile... oph smile... oph smile... oph smile... oph smile... oph smile... oph smile... oph smile... oph smile... oph smile... "

    show oph smile close
    oph "oph smile close... oph smile close... oph smile close... oph smile close... oph smile close... oph smile close... oph smile close... oph smile close... "

    show oph surprised
    oph "oph surprised... oph surprised... oph surprised... oph surprised... oph surprised... oph surprised... oph surprised... oph surprised... oph surprised... "

    show oph surprised close
    oph "oph surprised close... oph surprised close... oph surprised close... oph surprised close... oph surprised close... oph surprised close... oph surprised close... "

    show oph tiredsmile
    oph "oph tiredsmile... oph tiredsmile... oph tiredsmile... oph tiredsmile... oph tiredsmile... oph tiredsmile... oph tiredsmile... oph tiredsmile... oph tiredsmile... "

    show oph tiredsmile close
    oph "oph tiredsmile close... oph tiredsmile close... oph tiredsmile close... oph tiredsmile close... oph tiredsmile close... oph tiredsmile close... "

    show oph weirdedout
    oph "oph weirdedout... oph weirdedout... oph weirdedout... oph weirdedout... oph weirdedout... oph weirdedout... oph weirdedout... oph weirdedout... oph weirdedout... "

    show oph weirdedout close
    oph "oph weirdedout close... oph weirdedout close... oph weirdedout close... oph weirdedout close... oph weirdedout close... oph weirdedout close... "

    hide oph

    show oli cheerful smile
    oli "oli cheerful smile... oli cheerful smile... oli cheerful smile... oli cheerful smile... oli cheerful smile... oli cheerful smile... oli cheerful smile... "

    show oli cheerful smile close
    oli "oli cheerful smile close... oli cheerful smile close... oli cheerful smile close... oli cheerful smile close... oli cheerful smile close... "

    show oli cheerful grin
    oli "oli cheerful grin... oli cheerful grin... oli cheerful grin... oli cheerful grin... oli cheerful grin... oli cheerful grin... oli cheerful grin... "

    show oli cheerful grin close
    oli "oli cheerful grin close... oli cheerful grin close... oli cheerful grin close... oli cheerful grin close... oli cheerful grin close... oli cheerful grin close... "

    show oli smile noflower
    oli "oli smile noflower... oli smile noflower... oli smile noflower... oli smile noflower... oli smile noflower... oli smile noflower... oli smile noflower... "

    show oli smile noflower close
    oli "oli smile noflower close... oli smile noflower close... oli smile noflower close... oli smile noflower close... oli smile noflower close... "

    show oli serious noflower
    oli "oli serious noflower... oli serious noflower... oli serious noflower... oli serious noflower... oli serious noflower... oli serious noflower... "

    show oli serious noflower close
    oli "oli serious noflower close... oli serious noflower close... oli serious noflower close... oli serious noflower close... oli serious noflower close... "

    show oli smile
    oli "oli smile... oli smile... oli smile... oli smile... oli smile... oli smile... oli smile... oli smile... oli smile... oli smile... oli smile... oli smile... oli smile... "

    show oli smile close
    oli "oli smile close... oli smile close... oli smile close... oli smile close... oli smile close... oli smile close... oli smile close... oli smile close... "

    show oli serious
    oli "oli serious... oli serious... oli serious... oli serious... oli serious... oli serious... oli serious... oli serious... oli serious... oli serious... oli serious... "

    show oli serious close
    oli "oli serious close... oli serious close... oli serious close... oli serious close... oli serious close... oli serious close... oli serious close... "

    hide oli

    show dai neutral
    dai "dai neutral... dai neutral... dai neutral... dai neutral... dai neutral... dai neutral... dai neutral... dai neutral... dai neutral... dai neutral... dai neutral... "

    show dai neutral close
    dai "dai neutral close... dai neutral close... dai neutral close... dai neutral close... dai neutral close... dai neutral close... dai neutral close... "

    show dai smile
    dai "dai smile... dai smile... dai smile... dai smile... dai smile... dai smile... dai smile... dai smile... dai smile... dai smile... dai smile... dai smile... dai smile... "

    show dai smile close
    dai "dai smile close... dai smile close... dai smile close... dai smile close... dai smile close... dai smile close... dai smile close... dai smile close... "

    show dai confident
    dai "dai confident... dai confident... dai confident... dai confident... dai confident... dai confident... dai confident... dai confident... dai confident... "

    show dai confident close
    dai "dai confident close... dai confident close... dai confident close... dai confident close... dai confident close... dai confident close... dai confident close... "

    show dai hopeful
    dai "dai hopeful... dai hopeful... dai hopeful... dai hopeful... dai hopeful... dai hopeful... dai hopeful... dai hopeful... dai hopeful... dai hopeful... dai hopeful... "

    show dai hopeful close
    dai "dai hopeful close... dai hopeful close... dai hopeful close... dai hopeful close... dai hopeful close... dai hopeful close... dai hopeful close... "

    show dai disappointed
    dai "dai disappointed... dai disappointed... dai disappointed... dai disappointed... dai disappointed... dai disappointed... dai disappointed... dai disappointed... "

    show dai disappointed close
    dai "dai disappointed close... dai disappointed close... dai disappointed close... dai disappointed close... dai disappointed close... dai disappointed close... "

    show dai disappointedside
    dai "dai disappointedside... dai disappointedside... dai disappointedside... dai disappointedside... dai disappointedside... dai disappointedside... "

    show dai disappointedside close
    dai "dai disappointedside close... dai disappointedside close... dai disappointedside close... dai disappointedside close... dai disappointedside close... "

    show dai distant neutral
    dai "dai distant neutral... dai distant neutral... dai distant neutral... dai distant neutral... dai distant neutral... dai distant neutral... dai distant neutral... "

    show dai distant neutral close
    dai "dai distant neutral close... dai distant neutral close... dai distant neutral close... dai distant neutral close... dai distant neutral close... "

    show dai distant frown
    dai "dai distant frown... dai distant frown... dai distant frown... dai distant frown... dai distant frown... dai distant frown... dai distant frown... "

    show dai distant frown close
    dai "dai distant frown close... dai distant frown close... dai distant frown close... dai distant frown close... dai distant frown close... dai distant frown close... "

    hide dai

    show hop neutral
    hop "hop neutral... hop neutral... hop neutral... hop neutral... hop neutral... hop neutral... hop neutral... hop neutral... hop neutral... hop neutral... hop neutral... "

    show hop neutral close
    hop "hop neutral close... hop neutral close... hop neutral close... hop neutral close... hop neutral close... hop neutral close... hop neutral close... "

    show hop happy
    hop "hop happy... hop happy... hop happy... hop happy... hop happy... hop happy... hop happy... hop happy... hop happy... hop happy... hop happy... hop happy... hop happy... "

    show hop happy close
    hop "hop happy close... hop happy close... hop happy close... hop happy close... hop happy close... hop happy close... hop happy close... hop happy close... "

    show hop angry
    hop "hop angry... hop angry... hop angry... hop angry... hop angry... hop angry... hop angry... hop angry... hop angry... hop angry... hop angry... hop angry... hop angry... "

    show hop angry close
    hop "hop angry close... hop angry close... hop angry close... hop angry close... hop angry close... hop angry close... hop angry close... hop angry close... "

    show hop angry clench
    hop "hop angry clench... hop angry clench... hop angry clench... hop angry clench... hop angry clench... hop angry clench... hop angry clench... hop angry clench... "

    show hop angry clench close
    hop "hop angry clench close... hop angry clench close... hop angry clench close... hop angry clench close... hop angry clench close... hop angry clench close... "

    show hop hurt downtrodden
    hop "hop hurt downtrodden... hop hurt downtrodden... hop hurt downtrodden... hop hurt downtrodden... hop hurt downtrodden... hop hurt downtrodden... hop hurt downtrodden... "

    show hop hurt downtrodden close
    hop "hop hurt downtrodden close... hop hurt downtrodden close... hop hurt downtrodden close... hop hurt downtrodden close... hop hurt downtrodden close... "

    show hop hurt embarrassed
    hop "hop hurt embarrassed... hop hurt embarrassed... hop hurt embarrassed... hop hurt embarrassed... hop hurt embarrassed... hop hurt embarrassed... hop hurt embarrassed... "

    show hop hurt embarrassed close
    hop "hop hurt embarrassed close... hop hurt embarrassed close... hop hurt embarrassed close... hop hurt embarrassed close... hop hurt embarrassed close... "

    hide hop
    jump flood_101

    "FLOOD END (remove once scripts are in)"
