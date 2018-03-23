###############################
#
# FLOOD DEFINITIONS GO IN HERE
#
###############################

define oph = Character("Ophelia", callback=speaker("oph"))
define oli = Character("Oliver", callback=speaker("oli"))
define dai = Character("Daisy", callback=speaker("dai"))
define hop = Character("Hope", callback=speaker("hop"))

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
image oph defensive close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth normal1")

image oph irritated = OphPose1("oph eyes irritated1", "oph mouth normal1")
image oph irritated close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth normal1")

image oph scared = OphPose1("oph eyes scared1", "oph mouth scared1")
image oph scared close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth scared1")

image oph smile = OphPose1("oph eyes normal1", "oph mouth smile1")
image oph smile close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth smile1")

image oph surprised = OphPose1("oph eyes scared1", "oph mouth normal1")
image oph surprised close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth normal1")

image oph tiredsmile = OphPose1("oph eyes tired1", "oph mouth smile1")
image oph tiredsmile close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth smile1")

image oph weirdedout = OphPose1("oph eyes weirded1", "oph mouth weirded1")
image oph weirdedout close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth weirded1")


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
image oli smile noflower close = OliPose2("game_flood/sprites/Oliver/Pose 2/eyes normal open.png", "oli mouth normal2") #No eye close art

image oli serious noflower = OliPose2("oli eyes serious2", "oli mouth serious2")
image oli serious noflower close = OliPose2("game_flood/sprites/Oliver/Pose 2/eyes normal open.png", "oli mouth serious2") #No eye close art

###############################
#
# OLI POSE 2 (FLOWER) SPRITES
#
###############################

init python:
    OliPose2F = BaseCSprite("oli", "game_flood/sprites/Oliver/Pose 2/baseflower.png", (696, 1080))

image oli smile = OliPose2F("oli eyes normal2", "oli mouth normal2")
image oli smile close = OliPose2F("game_flood/sprites/Oliver/Pose 2/eyes normal open.png", "oli mouth normal2") #No eye close art

image oli serious = OliPose2F("oli eyes serious2", "oli mouth serious2")
image oli serious close = OliPose2F("game_flood/sprites/Oliver/Pose 2/eyes normal open.png", "oli mouth serious2") #No eye close art

###############################
#
# DAI POSE 1 SPRITES
#
###############################

init python:
    DaiPose1 = BaseCSprite("dai", "game_flood/sprites/Daisy/Pose 1/base.png", (450, 1080))

image dai neutral = DaiPose1("dai eyes normal1", "dai mouth normal1")
image dai neutral close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth normal1")

image dai smile = DaiPose1("dai eyes normal1", "dai mouth smile1")
image dai smile close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth smile1")

image dai confident = DaiPose1("dai eyes normal1", "dai mouth confident1")
image dai confident close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth confident1")

image dai hopeful = DaiPose1("dai eyes hopeful1", "dai mouth smile1")
image dai hopeful close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth smile1")

image dai disappointed = DaiPose1("dai eyes disappointed1", "dai mouth sad1")
image dai disappointed close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth sad1")

image dai disappointedside = DaiPose1("dai eyes disappointedside1", "dai mouth sad1")
image dai disappointedside close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth sad1")

###############################
#
# DAI POSE 2 SPRITES
#
###############################

init python:
    DaiPose2 = BaseCSprite("dai", "game_flood/sprites/Daisy/Pose 2/base.png", (450, 1080))

image dai distant neutral = DaiPose2("dai eyes normal2", "dai mouth normal2")
image dai distant neutral close = DaiPose2("game_flood/sprites/Daisy/Pose 2/eyes normal open.png", "dai mouth normal2") #No eye close art

image dai distant frown = DaiPose2("dai eyes sad1", "dai mouth sad2")
image dai distant frown close = DaiPose2("game_flood/sprites/Daisy/Pose 2/eyes frown open.png", "dai mouth sad2") #No eye close art

###############################
#
# HOP POSE 1 SPRITES
#
###############################

init python:
    HopPose1 = BaseCSprite("hop", "game_flood/sprites/Hope/Pose 1/base.png", (425, 1080))

image hop neutral = HopPose1("hop eyes normal1", "hop mouth normal1")
image hop neutral close = HopPose1("game_flood/sprites/Hope/Pose 1/eyes normal open.png", "hop mouth normal1") #No eye close art

image hop happy = HopPose1("hop eyes happy1", "hop mouth smile1")
image hop happy = HopPose1("game_flood/sprites/Hope/Pose 1/eyes smile open.png", "hop mouth smile1") #No eye close art

image hop angry = HopPose1("hop eyes angry1", "hop mouth angry1")
image hop angry close = HopPose1("game_flood/sprites/Hope/Pose 1/eyes angry open.png", "hop mouth angry1") #No eye close art

image hop angry clench = HopPose1("hop eyes angry1", "hop mouth angryclench1")
image hop angry clench close = HopPose1("game_flood/sprites/Hope/Pose 1/eyes angry open.png", "hop mouth angryclench1") #No eye close art

###############################
#
# HOP POSE 2 SPRITES
#
###############################

init python:
    HopPose2 = BaseCSprite("hop", "game_flood/sprites/Hope/Pose 2/base.png", (425, 1080))

image hop hurt downtrodden = HopPose2("hop eyes normal2", "hop mouth normal2")
image hop hurt downtrodden close = HopPose2("game_flood/sprites/Hope/Pose 2/eyes normal open.png", "hop mouth normal2") #No eye close art

image hop hurt embarrassed = HopPose2("hop eyes embarrassed2", "hop mouth normal2")
image hop hurt embarrassed close = HopPose2("game_flood/sprites/Hope/Pose 2/eyes embarrassed open.png", "hop mouth normal2") #No eye close art



###############################
#
# OPH POSE 1 COMPOSITE PARTS
#
###############################

image oph eyes normal1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes normal open.png", "game_flood/sprites/Ophelia/Pose 1/eyes normal close.png")

image oph eyes tired1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes tired open.png", "game_flood/sprites/Ophelia/Pose 1/eyes normal close.png")

image oph eyes scared1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes scared open.png", "game_flood/sprites/Ophelia/Pose 1/eyes normal close.png")

image oph eyes weirded1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes weirded open.png", "game_flood/sprites/Ophelia/Pose 1/eyes normal close.png")

image oph eyes irritated1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes irritated open.png", "game_flood/sprites/Ophelia/Pose 1/eyes normal close.png")

image oph eyes defensive1 = blinkeyes("game_flood/sprites/Ophelia/Pose 1/eyes defensive open.png", "game_flood/sprites/Ophelia/Pose 1/eyes normal close.png")

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

image oli eyes normal2 = blinkeyes("game_flood/sprites/Oliver/Pose 2/eyes normal open.png", "game_flood/sprites/Oliver/Pose 2/eyes normal open.png")

image oli eyes serious2 = blinkeyes("game_flood/sprites/Oliver/Pose 2/eyes serious open.png", "game_flood/sprites/Oliver/Pose 2/eyes serious open.png")

image oli mouth normal2 = FlapMouth("oli", "game_flood/sprites/Oliver/Pose 2/mouth normal close.png", "game_flood/sprites/Oliver/Pose 2/mouth normal open.png")

image oli mouth serious2 = FlapMouth("oli", "game_flood/sprites/Oliver/Pose 2/mouth serious close.png", "game_flood/sprites/Oliver/Pose 2/mouth serious open.png")

###############################
#
# DAI POSE 1 COMPOSITE PARTS
#
###############################

image dai eyes normal1 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes normal open.png", "game_flood/sprites/Daisy/Pose 1/eyes normal close.png")

image dai eyes hopeful1 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes hopeful open.png", "game_flood/sprites/Daisy/Pose 1/eyes normal close.png")

image dai eyes disappointed1 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes disappointed open.png", "game_flood/sprites/Daisy/Pose 1/eyes normal close.png")

image dai eyes disappointedside1 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes disappointedside open.png", "game_flood/sprites/Daisy/Pose 1/eyes normal close.png")

image dai mouth normal1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth normal close.png", "game_flood/sprites/Daisy/Pose 1/mouth normal open.png")

image dai mouth confident1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth confident close.png", "game_flood/sprites/Daisy/Pose 1/mouth smile open.png")

image dai mouth sad1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth sad close.png", "game_flood/sprites/Daisy/Pose 1/mouth sad open.png")

image dai mouth smile1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth smile close.png", "game_flood/sprites/Daisy/Pose 1/mouth smile open.png")

###############################
#
# DAI POSE 2 COMPOSITE PARTS
#
###############################

image dai eyes normal2 = blinkeyes("game_flood/sprites/Daisy/Pose 2/eyes normal open.png", "game_flood/sprites/Daisy/Pose 2/eyes normal open.png")

image dai eyes sad1 = blinkeyes("game_flood/sprites/Daisy/Pose 2/eyes frown open.png", "game_flood/sprites/Daisy/Pose 2/eyes frown open.png")

image dai mouth normal2 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 2/mouth normal close.png", "game_flood/sprites/Daisy/Pose 2/mouth normal open.png")

image dai mouth sad2 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 2/mouth frown close.png", "game_flood/sprites/Daisy/Pose 2/mouth normal open.png")

###############################
#
# HOP POSE 1 COMPOSITE PARTS
#
###############################

image hop eyes normal1 = blinkeyes("game_flood/sprites/Hope/Pose 1/eyes normal open.png", "game_flood/sprites/Hope/Pose 1/eyes normal open.png")

image hop eyes angry1 = blinkeyes("game_flood/sprites/Hope/Pose 1/eyes angry open.png", "game_flood/sprites/Hope/Pose 1/eyes angry open.png")

image hop eyes happy1 = blinkeyes("game_flood/sprites/Hope/Pose 1/eyes smile open.png", "game_flood/sprites/Hope/Pose 1/eyes smile open.png")

image hop mouth normal1 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth normal close.png", "game_flood/sprites/Hope/Pose 1/mouth normal open.png")

image hop mouth smile1 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth close smile.png", "game_flood/sprites/Hope/Pose 1/mouth normal open.png")

image hop mouth angry1 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth angry close.png", "game_flood/sprites/Hope/Pose 1/mouth angry open.png")

image hop mouth angryclench1 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth angry clench.png", "game_flood/sprites/Hope/Pose 1/mouth angry open.png")

###############################
#
# HOP POSE 2 COMPOSITE PARTS
#
###############################

image hop eyes normal2 = blinkeyes("game_flood/sprites/Hope/Pose 2/eyes normal open.png", "game_flood/sprites/Hope/Pose 2/eyes normal open.png")

image hop eyes embarrassed2 = blinkeyes("game_flood/sprites/Hope/Pose 2/eyes embarrassed open.png", "game_flood/sprites/Hope/Pose 2/eyes embarrassed open.png")

image hop mouth normal2 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 2/mouth normal close.png", "game_flood/sprites/Hope/Pose 2/mouth normal open.png")



###############################
#
# FLOOD STORY START
#
###############################

label flood_000:
    $ persistent.last_story = "flood"
    #jump flood_101

    menu:
        "Show everyone's expressions":
            jump flood_expressions

label flood_expressions:
    show oph neutral
    oph "oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... "

    show oph neutral close
    oph "oph normal1 close... oph normal1 close... oph normal1 close... oph normal1 close... oph normal1 close... oph normal1 close... oph normal1 close... oph normal1 close... "

    show oph defensive
    oph "oph defensive1... oph defensive1... oph defensive1... oph defensive1... oph defensive1... oph defensive1... oph defensive1... oph defensive1... oph defensive1... "

    show oph defensive close
    oph "oph defensive1 close... oph defensive1 close... oph defensive1 close... oph defensive1 close... oph defensive1 close... oph defensive1 close... oph defensive1 close... "

    show oph irritated
    oph "oph irritated1... oph irritated1... oph irritated1... oph irritated1... oph irritated1... oph irritated1... oph irritated1... oph irritated1... oph irritated1... "

    show oph irritated close
    oph "oph irritated1 close... oph irritated1 close... oph irritated1 close... oph irritated1 close... oph irritated1 close... oph irritated1 close... oph irritated1 close... "

    show oph scared
    oph "oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... "

    show oph scared close
    oph "oph scared1 close... oph scared1 close... oph scared1 close... oph scared1 close... oph scared1 close... oph scared1 close... oph scared1 close... oph scared1 close... "

    show oph smile
    oph "oph smile... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... "

    show oph smile close
    oph "oph smile close... oph happy1 close... oph happy1 close... oph happy1 close... oph happy1 close... oph happy1 close... oph happy1 close... oph happy1 close... "

    show oph surprised
    oph "oph surprised... oph surprised1... oph surprised1... oph surprised1... oph surprised1... oph surprised1... oph surprised1... oph surprised1... oph surprised1... "

    show oph surprised close
    oph "oph surprised close... oph surprised1 close... oph surprised1 close... oph surprised1 close... oph surprised1 close... oph surprised1 close... oph surprised1 close... "

    show oph tiredsmile
    oph "oph tiredsmile... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... "

    show oph tiredsmile close
    oph "oph tiredsmile close... oph tired1 close... oph tired1 close... oph tired1 close... oph tired1 close... oph tired1 close... oph tired1 close... oph tired1 close... "

    show oph weirdedout
    oph "oph weirdedout... oph weirdedout1... oph weirdedout1... oph weirdedout1... oph weirdedout1... oph weirdedout1... oph weirdedout1... oph weirdedout1... oph weirdedout1... "

    show oph weirdedout close
    oph "oph weirdedout close... oph weirdedout1 close... oph weirdedout1 close... oph weirdedout1 close... oph weirdedout1 close... oph weirdedout1 close... oph weirdedout1 close... "

    hide oph

    show oli cheerful smile
    oli "oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... "

    show oli cheerful smile close
    oli "oli normal1 close... oli normal1 close... oli normal1 close... oli normal1 close... oli normal1 close... oli normal1 close... oli normal1 close... oli normal1 close... "

    show oli cheerful grin
    oli "oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... "

    show oli cheerful grin close
    oli "oli happy1 close... oli happy1 close... oli happy1 close... oli happy1 close... oli happy1 close... oli happy1 close... oli happy1 close... oli happy1 close... "

    show oli smile noflower
    oli "oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... "

    show oli smile noflower close
    oli "oli normal2 close... oli normal2 close... oli normal2 close... oli normal2 close... oli normal2 close... oli normal2 close... oli normal2 close... oli normal2 close... "

    show oli serious noflower
    oli "oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... "

    show oli serious noflower close
    oli "oli serious1 close... oli serious1 close... oli serious1 close... oli serious1 close... oli serious1 close... oli serious1 close... oli serious1 close... oli serious1 close... "

    show oli smile
    oli "oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... "

    show oli smile close
    oli "oli normal2F close... oli normal2F close... oli normal2F close... oli normal2F close... oli normal2F close... oli normal2F close... oli normal2F close... oli normal2F close... "

    show oli serious
    oli "oli serious1F... oli serious1F... oli serious1F... oli serious1F... oli serious1F... oli serious1F... oli serious1F... oli serious1F... oli serious1F... "

    show oli serious close
    oli "oli serious1F close... oli serious1F close... oli serious1F close... oli serious1F close... oli serious1F close... oli serious1F close... oli serious1F close... "

    hide oli

    show dai neutral
    dai "dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... "

    show dai neutral close
    dai "dai normal1 close... dai normal1 close... dai normal1 close... dai normal1 close... dai normal1 close... dai normal1 close... dai normal1 close... dai normal1 close... "

    show dai smile
    dai "dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... "

    show dai smile close
    dai "dai happy1 close... dai happy1 close... dai happy1 close... dai happy1 close... dai happy1 close... dai happy1 close... dai happy1 close... dai happy1 close... "

    show dai confident
    dai "dai confident1... dai confident1... dai confident1... dai confident1... dai confident1... dai confident1... dai confident1... dai confident1... dai confident1... "

    show dai confident close
    dai "dai confident1 close... dai confident1 close... dai confident1 close... dai confident1 close... dai confident1 close... dai confident1 close... dai confident1 close... "

    show dai hopeful
    dai "dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... "

    show dai hopeful close
    dai "dai hopeful1 close... dai hopeful1 close... dai hopeful1 close... dai hopeful1 close... dai hopeful1 close... dai hopeful1 close... dai hopeful1 close... "

    show dai disappointed
    dai "dai disappointed1... dai disappointed1... dai disappointed1... dai disappointed1... dai disappointed1... dai disappointed1... dai disappointed1... dai disappointed1... "

    show dai disappointed close
    dai "dai disappointed1 close... dai disappointed1 close... dai disappointed1 close... dai disappointed1 close... dai disappointed1 close... dai disappointed1 close... "

    show dai disappointedside
    dai "dai disappointedside1... dai disappointedside1... dai disappointedside1... dai disappointedside1... dai disappointedside1... dai disappointedside1... dai disappointedside1... "

    show dai disappointedside close
    dai "dai disappointedside1 close... dai disappointedside1 close... dai disappointedside1 close... dai disappointedside1 close... dai disappointedside1 close... dai disappointedside1 close... "

    show dai distant neutral
    dai "dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... "

    show dai distant neutral close
    dai "dai normal2 close... dai normal2 close... dai normal2 close... dai normal2 close... dai normal2 close... dai normal2 close... dai normal2 close... dai normal2 close... "

    show dai distant frown
    dai "dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... "

    show dai distant frown close
    dai "dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... "

    hide dai

    show hop neutral
    hop "hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... "

    show hop neutral close
    hop "hop normal1 close... hop normal1 close... hop normal1 close... hop normal1 close... hop normal1 close... hop normal1 close... hop normal1 close... hop normal1 close... "

    show hop happy
    hop "hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... "

    show hop happy close
    hop "hop happy1 close... hop happy1 close... hop happy1 close... hop happy1 close... hop happy1 close... hop happy1 close... hop happy1 close... hop happy1 close... "

    show hop angry
    hop "hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... "

    show hop angry close
    hop "hop angry1 close... hop angry1 close... hop angry1 close... hop angry1 close... hop angry1 close... hop angry1 close... hop angry1 close... hop angry1 close... "

    show hop angry clench
    hop "hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... "

    show hop angry clench close
    hop "hop angry2 close... hop angry2 close... hop angry2 close... hop angry2 close... hop angry2 close... hop angry2 close... hop angry2 close... hop angry2 close... "

    show hop hurt downtrodden
    hop "hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... "

    show hop hurt downtrodden close
    hop "hop normal2 close... hop normal2 close... hop normal2 close... hop normal2 close... hop normal2 close... hop normal2 close... hop normal2 close... hop normal2 close... "

    show hop hurt embarrassed
    hop "hop embarrassed2... hop embarrassed2... hop embarrassed2... hop embarrassed2... hop embarrassed2... hop embarrassed2... hop embarrassed2... hop embarrassed2... "

    show hop hurt embarrassed close
    hop "hop embarrassed2 close... hop embarrassed2 close... hop embarrassed2 close... hop embarrassed2 close... hop embarrassed2 close... hop embarrassed2 close... "

    hide hop
    #jump flood_000

    "FLOOD END (remove once scripts are in)"
