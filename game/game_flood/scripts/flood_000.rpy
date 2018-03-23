###############################
#
# FLOOD DEFINITIONS GO IN HERE
#
###############################

define oph = Character("Ophelia")
define oli = Character("Oliver")
define dai = Character("Daisy")
define hop = Character("Hope")

###############################
#
# OPH POSE 1 SPRITES
#
###############################

init python:
    OphPose1 = BaseCSprite("oph", "game_flood/sprites/Ophelia/Pose 1/base.png", (000, 0000))

image oph normal1 = OphPose1("oph eyes normal1", "oph mouth normal1")
image oph normal1 close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth normal1")

image oph defensive1 = OphPose1("oph eyes defensive1", "oph mouth normal1")
image oph defensive1 close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth normal1")

image oph irritated1 = OphPose1("oph eyes irritated1", "oph mouth normal1")
image oph irritated1 close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth normal1")

image oph scared1 = OphPose1("oph eyes scared1", "oph mouth scared1")
image oph scared1 close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth scared1")

image oph happy1 = OphPose1("oph eyes normal1", "oph mouth smile1")
image oph happy1 close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth smile1")

image oph surprised1 = OphPose1("oph eyes scared1", "oph mouth normal1")
image oph surprised1 close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth normal1")

image oph tired1 = OphPose1("oph eyes tired1", "oph mouth smile1")
image oph tired1 close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth smile1")

image oph weirdedout1 = OphPose1("oph eyes weirded1", "oph mouth weirded1")
image oph weirdedout1 close = OphPose1("game_flood/sprites/Ophelia/Pose 1/eyes normal close.png", "oph mouth weirded1")


###############################
#
# OLI POSE 1 SPRITES
#
###############################

init python:
    OliPose1 = BaseCSprite("oli", "game_flood/sprites/Oliver/Pose 1/base.png", (000, 0000))

image oli normal1 = OliPose1("oli eyes normal1", "oli mouth normal1")
image oli normal1 close = OliPose1("game_flood/sprites/Oliver/Pose 1/eyes normal close.png", "oli mouth normal1")

image oli happy1 = OliPose1("oli eyes normal1", "oli mouth smile1")
image oli happy1 close = OliPose1("game_flood/sprites/Oliver/Pose 1/eyes normal close.png", "oli mouth normal1")

###############################
#
# OLI POSE 2 (NO FLOWER) SPRITES
#
###############################

init python:
    OliPose2 = BaseCSprite("oli", "game_flood/sprites/Oliver/Pose 2/basenoflower.png", (000, 0000))

image oli normal2 = OliPose2("oli eyes normal2", "oli mouth normal2")
image oli normal2 close = OliPose2("game_flood/sprites/Oliver/Pose 2/eyes normal open.png", "oli mouth normal2") #No eye close art

image oli serious1 = OliPose2("oli eyes serious1", "oli mouth serious1")
image oli serious1 close = OliPose2("game_flood/sprites/Oliver/Pose 2/eyes normal open.png", "oli mouth serious1") #No eye close art

###############################
#
# OLI POSE 2 (FLOWER) SPRITES
#
###############################

init python:
    OliPose2F = BaseCSprite("oli", "game_flood/sprites/Oliver/Pose 2/baseflower.png", (000, 0000))

image oli normal2F = OliPose2F("oli eyes normal2", "oli mouth normal2")
image oli normal2F close = OliPose2F("game_flood/sprites/Oliver/Pose 2/eyes normal open.png", "oli mouth normal2") #No eye close art

image oli serious1F = OliPose2F("oli eyes serious1", "oli mouth serious1")
image oli serious1F close = OliPose2F("game_flood/sprites/Oliver/Pose 2/eyes normal open.png", "oli mouth serious1") #No eye close art

###############################
#
# DAI POSE 1 SPRITES
#
###############################

init python:
    DaiPose1 = BaseCSprite("dai", "game_flood/sprites/Daisy/Pose 1/base.png", (000, 0000))

image dai normal1 = DaiPose1("dai eyes normal1", "dai mouth normal1")
image dai normal1 close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth normal1")

image dai happy1 = DaiPose1("dai eyes normal1", "dai mouth smile1")
image dai happy1 close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth smile1")

image dai confident1 = DaiPose1("dai eyes normal1", "dai mouth confident1")
image dai confident1 close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth confident1")

image dai confident2 = DaiPose1("dai eyes normal1", "dai mouth confident2")
image dai confident2 close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth confident2")

image dai hopeful1 = DaiPose1("dai eyes hopeful1", "dai mouth smile1")
image dai hopeful1 close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth smile1")

image dai disappointed1 = DaiPose1("dai eyes disappointed1", "dai mouth sad1")
image dai disappointed1 close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth sad1")

image dai disappointed2 = DaiPose1("dai eyes disappointed2", "dai mouth sad1")
image dai disappointed2 close = DaiPose1("game_flood/sprites/Daisy/Pose 1/eyes normal close.png", "dai mouth sad1")

###############################
#
# DAI POSE 2 SPRITES
#
###############################

init python:
    DaiPose2 = BaseCSprite("dai", "game_flood/sprites/Daisy/Pose 2/base.png", (000, 0000))

image dai normal2 = DaiPose2("dai eyes normal2", "dai mouth normal2")
image dai normal2 close = DaiPose2("game_flood/sprites/Daisy/Pose 2/eyes normal open.png", "dai mouth normal2") #No eye close art

image dai sad1 = DaiPose2("dai eyes sad1", "dai mouth sad2")
image dai sad1 close = DaiPose2("game_flood/sprites/Daisy/Pose 2/eyes frown open.png", "dai mouth sad2") #No eye close art

###############################
#
# HOP POSE 1 SPRITES
#
###############################

init python:
    HopPose1 = BaseCSprite("hop", "game_flood/sprites/Hope/Pose 1/base.png", (000, 0000))

image hop normal1 = HopPose1("hop eyes normal1", "hop mouth normal1")
image hop normal1 close = HopPose1("game_flood/sprites/Hope/Pose 1/eyes normal open.png", "hop mouth normal1") #No eye close art

image hop happy1 = HopPose1("hop eyes happy1", "hop mouth smile1")
image hop happy1 = HopPose1("game_flood/sprites/Hope/Pose 1/eyes smile open.png", "hop mouth smile1") #No eye close art

image hop angry1 = HopPose1("hop eyes angry1", "hop mouth angry1")
image hop angry1 close = HopPose1("game_flood/sprites/Hope/Pose 1/eyes angry open.png", "hop mouth angry1") #No eye close art

image hop angry2 = HopPose1("hop eyes angry1", "hop mouth angry2")
image hop angry2 close = HopPose1("game_flood/sprites/Hope/Pose 1/eyes angry open.png", "hop mouth angry2") #No eye close art

###############################
#
# HOP POSE 2 SPRITES
#
###############################

init python:
    HopPose2 = BaseCSprite("hop", "game_flood/sprites/Hope/Pose 2/base.png", (000, 0000))

image hop normal2 = HopPose2("hop eyes normal2", "hop mouth normal2")
image hop normal2 close = HopPose2("game_flood/sprites/Hope/Pose 2/eyes normal open.png", "hop mouth normal2") #No eye close art

image hop embarrassed1 = HopPose2("hope eyes embarrassed1", "hop mouth normal2")
image hop embarrassed1 close = HopPose2("game_flood/sprites/Hope/Pose 2/eyes embarrassed open.png", "hop mouth normal2") #No eye close art

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

image oph mouth normal1 = FlapMouth("oph", "game_flood/sprites/Ophelia/Pose 1/mouth normal open.png", "game_flood/sprites/Ophelia/Pose 1/mouth normal close.png")

image oph mouth scared1 = FlapMouth("oph", "game_flood/sprites/Ophelia/Pose 1/mouth scared open.png", "game_flood/sprites/Ophelia/Pose 1/mouth normal close.png")

image oph mouth weirded1 = FlapMouth("oph", "game_flood/sprites/Ophelia/Pose 1/mouth weirded open.png", "game_flood/sprites/Ophelia/Pose 1/mouth weirded close.png")

image oph mouth smile1 = FlapMouth("oph", "game_flood/sprites/Ophelia/Pose 1/mouth smile open.png", "game_flood/sprites/Ophelia/Pose 1/mouth smile close.png")

###############################
#
# OLI POSE 1 COMPOSITE PARTS
#
###############################

image oli eyes normal1 = blinkeyes("game_flood/sprites/Oliver/Pose 1/eyes normal open.png", "game_flood/sprites/Oliver/Pose 1/eyes normal close.png")

image oli mouth normal1 = FlapMouth("oli", "game_flood/sprites/Oliver/Pose 1/mouth normal open.png", "game_flood/sprites/Oliver/Pose 1/mouth normal close.png")

image oli mouth smile1 = FlapMouth("oli", "game_flood/sprites/Oliver/Pose 1/mouth normal open.png", "game_flood/sprites/Oliver/Pose 1/mouth grin close.png")

###############################
#
# OLI POSE 2 COMPOSITE PARTS
#
###############################

image oli eyes normal2 = blinkeyes("game_flood/sprites/Oliver/Pose 2/eyes normal open.png", "game_flood/sprites/Oliver/Pose 2/eyes normal open.png")

image oli eyes serious1 = blinkeyes("game_flood/sprites/Oliver/Pose 2/eyes serious open.png", "game_flood/sprites/Oliver/Pose 2/eyes serious open.png")

image oli mouth normal2 = FlapMouth("oli", "game_flood/sprites/Oliver/Pose 2/mouth normal open.png", "game_flood/sprites/Oliver/Pose 2/mouth normal close.png")

image oli mouth serious1 = FlapMouth("oli", "game_flood/sprites/Oliver/Pose 2/mouth serious open.png", "game_flood/sprites/Oliver/Pose 2/mouth serious close.png")

###############################
#
# DAI POSE 1 COMPOSITE PARTS
#
###############################

image dai eyes normal1 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes normal open.png", "game_flood/sprites/Daisy/Pose 1/eyes normal close.png")

image dai eyes hopeful1 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes hopeful open.png", "game_flood/sprites/Daisy/Pose 1/eyes normal close.png")

image dai eyes disappointed1 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes dissapointed open.png", "game_flood/sprites/Daisy/Pose 1/eyes normal close.png")

image dai eyes disappointed2 = blinkeyes("game_flood/sprites/Daisy/Pose 1/eyes dissapointedside open.png", "game_flood/sprites/Daisy/Pose 1/eyes normal close.png")

image dai mouth normal1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth normal open.png", "game_flood/sprites/Daisy/Pose 1/mouth normal close.png")

image dai mouth confident1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth normal open.png", "game_flood/sprites/Daisy/Pose 1/mouth confident close.png")

image dai mouth confident2 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth smile open.png", "game_flood/sprites/Daisy/Pose 1/mouth confident close.png")

image dai mouth sad1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth sad open.png", "game_flood/sprites/Daisy/Pose 1/mouth sad close.png")

image dai mouth smile1 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 1/mouth smile open.png", "game_flood/sprites/Daisy/Pose 1/mouth smile close.png")

###############################
#
# DAI POSE 2 COMPOSITE PARTS
#
###############################

image dai eyes normal2 = blinkeyes("game_flood/sprites/Daisy/Pose 2/eyes normal open.png", "game_flood/sprites/Daisy/Pose 2/eyes normal open.png")

image dai eyes sad1 = blinkeyes("game_flood/sprites/Daisy/Pose 2/eyes frown open.png", "game_flood/sprites/Daisy/Pose 2/eyes frown open.png")

image dai mouth normal2 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 2/mouth normal open.png", "game_flood/sprites/Daisy/Pose 2/mouth normal close.png")

image dai mouth sad2 = FlapMouth("dai", "game_flood/sprites/Daisy/Pose 2/mouth normal open.png", "game_flood/sprites/Daisy/Pose 2/mouth frown close.png")

###############################
#
# HOP POSE 1 COMPOSITE PARTS
#
###############################

image hop eyes normal1 = blinkeyes("game_flood/sprites/Hope/Pose 1/eyes normal open.png", "game_flood/sprites/Hope/Pose 1/eyes normal open.png")

image hop eyes angry1 = blinkeyes("game_flood/sprites/Hope/Pose 1/eyes angry open.png", "game_flood/sprites/Hope/Pose 1/eyes angry open.png")

image hop eyes happy1 = blinkeyes("game_flood/sprites/Hope/Pose 1/eyes smile open.png", "game_flood/sprites/Hope/Pose 1/eyes smile open.png")

image hop mouth normal1 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth normal open.png", "game_flood/sprites/Hope/Pose 1/mouth normal close.png")

image hop mouth smile1 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth normal open.png", "game_flood/sprites/Hope/Pose 1/mouth close smile.png")

image hop mouth angry1 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth angry open.png", "game_flood/sprites/Hope/Pose 1/mouth angry close.png")

image hop mouth angry2 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 1/mouth angry open.png", "game_flood/sprites/Hope/Pose 1/mouth angry clench.png")

###############################
#
# HOP POSE 2 COMPOSITE PARTS
#
###############################

image hop eyes normal2 = blinkeyes("game_flood/sprites/Hope/Pose 2/eyes normal open.png", "game_flood/sprites/Hope/Pose 2/eyes normal open.png")

image hop eyes embarrassed1 = blinkeyes("game_flood/sprites/Hope/Pose 2/eyes embarrassed open.png", "game_flood/sprites/Hope/Pose 2/eyes embarrassed open.png")

image hop mouth normal2 = FlapMouth("hop", "game_flood/sprites/Hope/Pose 2/mouth normal open.png", "game_flood/sprites/Hope/Pose 2/mouth normal close.png")

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
    show oph normal1
    oph "oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... oph normal1... "

    show oph normal1 close
    oph "oph normal1 close... oph normal1 close... oph normal1 close... oph normal1 close... oph normal1 close... oph normal1 close... oph normal1 close... oph normal1 close... "

    show oph defensive1
    oph "oph defensive1... oph defensive1... oph defensive1... oph defensive1... oph defensive1... oph defensive1... oph defensive1... oph defensive1... oph defensive1... "

    show oph defensive1 close
    oph "oph defensive1 close... oph defensive1 close... oph defensive1 close... oph defensive1 close... oph defensive1 close... oph defensive1 close... oph defensive1 close... "

    show oph irritated1
    oph "oph irritated1... oph irritated1... oph irritated1... oph irritated1... oph irritated1... oph irritated1... oph irritated1... oph irritated1... oph irritated1... "

    show oph irritated1 close
    oph "oph irritated1 close... oph irritated1 close... oph irritated1 close... oph irritated1 close... oph irritated1 close... oph irritated1 close... oph irritated1 close... "

    show oph scared1
    oph "oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... oph scared1... "

    show oph scared1 close
    oph "oph scared1 close... oph scared1 close... oph scared1 close... oph scared1 close... oph scared1 close... oph scared1 close... oph scared1 close... oph scared1 close... "

    show oph happy1
    oph "oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... oph happy1... "

    show oph happy1 close
    oph "oph happy1 close... oph happy1 close... oph happy1 close... oph happy1 close... oph happy1 close... oph happy1 close... oph happy1 close... oph happy1 close... "

    show oph surprised1
    oph "oph surprised1... oph surprised1... oph surprised1... oph surprised1... oph surprised1... oph surprised1... oph surprised1... oph surprised1... oph surprised1... "

    show oph surprised1 close
    oph "oph surprised1 close... oph surprised1 close... oph surprised1 close... oph surprised1 close... oph surprised1 close... oph surprised1 close... oph surprised1 close... "

    show oph tired1
    oph "oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... oph tired1... "

    show oph tired1 close
    oph "oph tired1 close... oph tired1 close... oph tired1 close... oph tired1 close... oph tired1 close... oph tired1 close... oph tired1 close... oph tired1 close... "

    show oph weirdedout1
    oph "oph weirdedout1... oph weirdedout1... oph weirdedout1... oph weirdedout1... oph weirdedout1... oph weirdedout1... oph weirdedout1... oph weirdedout1... oph weirdedout1... "

    show oph weirdedout1 close
    oph "oph weirdedout1 close... oph weirdedout1 close... oph weirdedout1 close... oph weirdedout1 close... oph weirdedout1 close... oph weirdedout1 close... oph weirdedout1 close... "

    hide oph

    show oli normal1
    oli "oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... oli normal1... "

    show oli normal1 close
    oli "oli normal1 close... oli normal1 close... oli normal1 close... oli normal1 close... oli normal1 close... oli normal1 close... oli normal1 close... oli normal1 close... "

    show oli happy1
    oli "oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... oli happy1... "

    show oli happy1 close
    oli "oli happy1 close... oli happy1 close... oli happy1 close... oli happy1 close... oli happy1 close... oli happy1 close... oli happy1 close... oli happy1 close... "

    show oli normal2
    oli "oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... oli normal2... "

    show oli normal2 close
    oli "oli normal2 close... oli normal2 close... oli normal2 close... oli normal2 close... oli normal2 close... oli normal2 close... oli normal2 close... oli normal2 close... "

    show oli serious1
    oli "oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... oli serious1... "

    show oli serious1 close
    oli "oli serious1 close... oli serious1 close... oli serious1 close... oli serious1 close... oli serious1 close... oli serious1 close... oli serious1 close... oli serious1 close... "

    show oli normal2F
    oli "oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... oli normal2F... "

    show oli normal2F close
    oli "oli normal2F close... oli normal2F close... oli normal2F close... oli normal2F close... oli normal2F close... oli normal2F close... oli normal2F close... oli normal2F close... "

    show oli serious1F
    oli "oli serious1F... oli serious1F... oli serious1F... oli serious1F... oli serious1F... oli serious1F... oli serious1F... oli serious1F... oli serious1F... "

    show oli serious1F close
    oli "oli serious1F close... oli serious1F close... oli serious1F close... oli serious1F close... oli serious1F close... oli serious1F close... oli serious1F close... "

    hide oli

    show dai normal1
    dai "dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... dai normal1... "

    show dai normal1 close
    dai "dai normal1 close... dai normal1 close... dai normal1 close... dai normal1 close... dai normal1 close... dai normal1 close... dai normal1 close... dai normal1 close... "

    show dai happy1
    dai "dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... dai happy1... "

    show dai happy1 close
    dai "dai happy1 close... dai happy1 close... dai happy1 close... dai happy1 close... dai happy1 close... dai happy1 close... dai happy1 close... dai happy1 close... "

    show dai confident1
    dai "dai confident1... dai confident1... dai confident1... dai confident1... dai confident1... dai confident1... dai confident1... dai confident1... dai confident1... "

    show dai confident1 close
    dai "dai confident1 close... dai confident1 close... dai confident1 close... dai confident1 close... dai confident1 close... dai confident1 close... dai confident1 close... "

    show dai confident2
    dai "dai confident2... dai confident2... dai confident2... dai confident2... dai confident2... dai confident2... dai confident2... dai confident2... dai confident2... "

    show dai confident2 close
    dai "dai confident2 close... dai confident2 close... dai confident2 close... dai confident2 close... dai confident2 close... dai confident2 close... dai confident2 close... "

    show dai hopeful1
    dai "dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... dai hopeful1... "

    show dai hopeful1 close
    dai "dai hopeful1 close... dai hopeful1 close... dai hopeful1 close... dai hopeful1 close... dai hopeful1 close... dai hopeful1 close... dai hopeful1 close... "

    show dai disappointed1
    dai "dai disappointed1... dai disappointed1... dai disappointed1... dai disappointed1... dai disappointed1... dai disappointed1... dai disappointed1... dai disappointed1... "

    show dai disappointed1 close
    dai "dai disappointed1 close... dai disappointed1 close... dai disappointed1 close... dai disappointed1 close... dai disappointed1 close... dai disappointed1 close... "

    show dai disappointed2
    dai "dai disappointed2... dai disappointed2... dai disappointed2... dai disappointed2... dai disappointed2... dai disappointed2... dai disappointed2... dai disappointed2... "

    show dai disappointed2 close
    dai "dai disappointed2 close... dai disappointed2... dai disappointed2... dai disappointed2... dai disappointed2... dai disappointed2... dai disappointed2... dai disappointed2... "

    show dai normal2
    dai "dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... dai normal2... "

    show dai normal2 close
    dai "dai normal2 close... dai normal2 close... dai normal2 close... dai normal2 close... dai normal2 close... dai normal2 close... dai normal2 close... dai normal2 close... "

    show dai sad1
    dai "dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... dai sad1... "

    show dai sad1 close
    dai "dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... dai sad1 close... "

    hide dai

    show hop normal1
    hop "hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... hop normal1... "

    show hop normal1 close
    hop "hop normal1 close... hop normal1 close... hop normal1 close... hop normal1 close... hop normal1 close... hop normal1 close... hop normal1 close... hop normal1 close... "

    show hop happy1
    hop "hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... hop happy1... "

    show hop happy1 close
    hop "hop happy1 close... hop happy1 close... hop happy1 close... hop happy1 close... hop happy1 close... hop happy1 close... hop happy1 close... hop happy1 close... "

    show hop angry1
    hop "hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... hop angry1... "

    show hop angry1 close
    hop "hop angry1 close... hop angry1 close... hop angry1 close... hop angry1 close... hop angry1 close... hop angry1 close... hop angry1 close... hop angry1 close... "

    show hop angry2
    hop "hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... hop angry2... "

    show hop angry2 close
    hop "hop angry2 close... hop angry2 close... hop angry2 close... hop angry2 close... hop angry2 close... hop angry2 close... hop angry2 close... hop angry2 close... "

    show hop normal2
    hop "hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... hop normal2... "

    show hop normal2 close
    hop "hop normal2 close... hop normal2 close... hop normal2 close... hop normal2 close... hop normal2 close... hop normal2 close... hop normal2 close... hop normal2 close... "

    show hop embarrassed1
    hop "hop embarrassed1... hop embarrassed1... hop embarrassed1... hop embarrassed1... hop embarrassed1... hop embarrassed1... hop embarrassed1... hop embarrassed1... "

    show hop embarrassed1 close
    hop "hop embarrassed1 close... hop embarrassed1 close... hop embarrassed1 close... hop embarrassed1 close... hop embarrassed1 close... hop embarrassed1 close... "

    hide hop
    #jump flood_000

    "FLOOD END (remove once scripts are in)"
