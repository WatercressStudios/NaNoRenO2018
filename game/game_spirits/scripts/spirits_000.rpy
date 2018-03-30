###############################
#
# CHEAT SHEET
#
###############################

### show alx ###

# neutral1
# happy1
# sad1
# angry1
# bitter1
# scared1
# surprised1

## additionally...
# [emotion] close
# [emotion] blush
# [emotion] close blush


### show cae ###

# neutral1
# happy1
# sad1
# angry1
# bitter1
# scared1
# surprised1

## additionally...
# [emotion] close
# [emotion] blush
# [emotion] close blush

### show hmom ###

# neutral1
# happy1
# sad1
# surprised1

## additionally...
# [emotion] close


### show gen ###

# neutral1
# happy1
# sad1
# angry1
# surprised1


### scene background ###
#formatting below
#scene spirits [name here] with dissolve
#Example: scene spirits alex bedroom clean with dissolve

# alex bedroom clean
# alex bedroom empty
# alex bedroom messy
# alex bedroom night clean
# alex bedroom night messy
# autumn
# box closed
# box open
# caelum bedroom
# cellar
# city street
# classroom
# courtyard
# emergency room
# foyer
# loft
# school hallway
# stairs

### play music ###

# play

### play sound ###

# play sound ""

##############################
#
# SPIRITS DEFINITIONS GO IN HERE
#
###############################

init:
    $ Alex = "Alex"
    $ Caelum = "Hallway Boy"
    $ Genevieve = "Ghost"

    $ caelumAlive = True
    $ firstTrueEndFlag = True
    $ hasDiary = True
    $ hasLetter = True
    $ hasAmmo = True
    $ secondTrueEndFlag = False  

define alx = Character("Alex", callback=speaker("alx"), color="#e95540", dynamic=True)
define cae = Character("Caelum", callback=speaker("cae"), color="#f7b857", dynamic=True)
define hmom = Character("Jianmei", callback=speaker("hmom"), color="#8cb180")
define gen = Character("Genevieve", callback=speaker("gen"), color="#b7a295", dynamic=True)
define wra = Character("Wraith", color="#ffffff")
define caex = Character("Hallway Boy", callback=speaker("caex"), color="#f7b857") #Caelum voice
define ama = Character("Mama", color="#ffffff")
define Dad = Character("Papa", color="#ffffff")
define n = Character(None, kind=nvl)
define cxx = Character("Caelum...?", callback=speaker("cxx"), color="#f7b857") #Caelum voice
define gez = Character("Genevieve", callback=speaker("gez"), color="#b7a295") #Mix voiced
define gex = Character("Genevieve", callback=speaker("gex"), color="#b7a295") #Mix voiced
define nurse = Character("Nurse", color="#ffffff")
define gho = Character("Ghost", color="#b7a295")

init python:
    define_images("game_spirits/bgs", 2, False, ["spirits"])
    define_images("game_spirits/cgs", 2, False, ["spirits"])
    define_images("game_spirits/objects", 2, False, ["spirits"])

define bgmspirits_cae = "game_spirits/music/Theme of Caelum.ogg"
define bgmspirits_wra = "game_spirits/music/Theme of Cornelius.ogg"
define bgmspirits_gen = "game_spirits/music/Theme of Genevieve.ogg"
define bgmspirits_relax = "game_spirits/music/Relaxation (School).ogg"
define bgmspirits_sthings = "game_spirits/music/Stranger Things.ogg"
define bgmspirits_main = "game_spirits/music/Artemis Hall.ogg"

###############################
#
# ALX POSE 1 SPRITES
#
###############################

init python:
    AlxPose1 = BaseCSprite("alx", "game_spirits/sprites/Alex/Pose 1/base.png", (608, 1080))

image alx neutral1 = AlxPose1("alx eyes neutral1", "alx mouth neutral1")
image alx neutral1 close = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes neutral close.png", "alx mouth neutral1")
image alx neutral1 blush = AlxPose1("alx eyes neutral1", "alx mouth neutral1", "game_spirits/sprites/Alex/Pose 1/blush.png")
image alx neutral1 close blush = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes neutral close.png", "alx mouth neutral1", "game_spirits/sprites/Alex/Pose 1/blush.png")

image alx happy1 = AlxPose1("alx eyes happy1", "alx mouth happy1")
image alx happy1 close = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes happy close.png", "alx mouth happy1")
image alx happy1 blush = AlxPose1("alx eyes happy1", "alx mouth happy1", "game_spirits/sprites/Alex/Pose 1/blush.png")
image alx happy1 close blush = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes happy close.png", "alx mouth happy1", "game_spirits/sprites/Alex/Pose 1/blush.png")

image alx sad1 = AlxPose1("alx eyes sad1", "alx mouth sad1")
image alx sad1 close = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes sad close.png", "alx mouth sad1")
image alx sad1 blush = AlxPose1("alx eyes sad1", "alx mouth sad1", "game_spirits/sprites/Alex/Pose 1/blush.png")
image alx sad1 close blush = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes sad close.png", "alx mouth sad1", "game_spirits/sprites/Alex/Pose 1/blush.png")

image alx angry1 = AlxPose1("alx eyes angry1", "alx mouth angry1")
image alx angry1 close = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes angry close.png", "alx mouth angry1")
image alx angry1 blush = AlxPose1("alx eyes angry1", "alx mouth angry1", "game_spirits/sprites/Alex/Pose 1/blush.png")
image alx angry1 close blush = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes angry close.png", "alx mouth angry1", "game_spirits/sprites/Alex/Pose 1/blush.png")

image alx bitter1 = AlxPose1("alx eyes angry1", "alx mouth bitter1")
image alx bitter1 close = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes angry close.png", "alx mouth bitter1")
image alx bitter1  blush = AlxPose1("alx eyes angry1", "alx mouth bitter1", "game_spirits/sprites/Alex/Pose 1/blush.png")
image alx bitter1 close blush = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes angry close.png", "alx mouth bitter1", "game_spirits/sprites/Alex/Pose 1/blush.png")

image alx scared1 = AlxPose1("alx eyes scared1", "alx mouth scared1")
image alx scared1 close = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes scared close.png", "alx mouth scared1")
image alx scared1 blush = AlxPose1("alx eyes scared1", "alx mouth scared1", "game_spirits/sprites/Alex/Pose 1/blush.png")
image alx scared1 close blush = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes scared close.png", "alx mouth scared1", "game_spirits/sprites/Alex/Pose 1/blush.png")

image alx surprised1 = AlxPose1("alx eyes neutral1", "alx mouth scared1")
image alx surprised1 close = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes neutral close.png", "alx mouth scared1")
image alx surprised1 blush = AlxPose1("alx eyes neutral1", "alx mouth scared1", "game_spirits/sprites/Alex/Pose 1/blush.png")
image alx surprised1 close blush = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes neutral close.png", "alx mouth scared1", "game_spirits/sprites/Alex/Pose 1/blush.png")

image alx sheepish1 = AlxPose1("alx eyes sad1", "alx mouth happy1")
image alx sheepish1 close = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes sad close.png", "alx mouth happy1")
image alx sheepish1 blush = AlxPose1("alx eyes sad1", "alx mouth happy1", "game_spirits/sprites/Alex/Pose 1/blush.png")
image alx sheepish1 close blush = AlxPose1("game_spirits/sprites/Alex/Pose 1/eyes sad close.png", "alx mouth happy1", "game_spirits/sprites/Alex/Pose 1/blush.png")


###############################
#
# CAE POSE 1 SPRITES
#
###############################

init python:
    CaePose1 = BaseCSprite("cae", "game_spirits/sprites/Caelum/Pose 1/base.png", (608, 1080))

image cae neutral1 = CaePose1("cae eyes neutral1", "cae mouth neutral1")
image cae neutral1 close = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes neutral close.png", "cae mouth neutral1")
image cae neutral1 blush = CaePose1("cae eyes neutral1", "cae mouth neutral1", "game_spirits/sprites/Caelum/Pose 1/blush.png")
image cae neutral1 close blush = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes neutral close.png", "cae mouth neutral1", "game_spirits/sprites/Caelum/Pose 1/blush.png")

image cae happy1 = CaePose1("cae eyes neutral1", "cae mouth happy1")
image cae happy1 close = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes neutral close.png", "cae mouth happy1")
image cae happy1 blush = CaePose1("cae eyes neutral1", "cae mouth happy1", "game_spirits/sprites/Caelum/Pose 1/blush.png")
image cae happy1 close blush = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes neutral close.png", "cae mouth happy1", "game_spirits/sprites/Caelum/Pose 1/blush.png")

image cae sad1 = CaePose1("cae eyes sad1", "cae mouth sad1")
image cae sad1 close = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes neutral close.png", "cae mouth sad1")
image cae sad1 blush = CaePose1("cae eyes sad1", "cae mouth sad1", "game_spirits/sprites/Caelum/Pose 1/blush.png")
image cae sad1 close blush = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes neutral close.png", "cae mouth sad1", "game_spirits/sprites/Caelum/Pose 1/blush.png")

image cae angry1 = CaePose1("cae eyes angry1", "cae mouth neutral1")
image cae angry1 close = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes angry close.png", "cae mouth neutral1")
image cae angry1 blush = CaePose1("cae eyes angry1", "cae mouth neutral1", "game_spirits/sprites/Caelum/Pose 1/blush.png")
image cae angry1 close blush = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes angry close.png", "cae mouth neutral1", "game_spirits/sprites/Caelum/Pose 1/blush.png")

image cae bitter1 = CaePose1("cae eyes sad1", "cae mouth neutral1")
image cae bitter1 close = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes sad close.png", "cae mouth neutral1")
image cae bitter1 blush = CaePose1("cae eyes sad1", "cae mouth neutral1", "game_spirits/sprites/Caelum/Pose 1/blush.png")
image cae bitter1 close blush = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes sad close.png", "cae mouth neutral1", "game_spirits/sprites/Caelum/Pose 1/blush.png")

image cae scared1 = CaePose1("cae eyes scared1", "cae mouth scared1")
image cae scared1 close = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes scared close.png", "cae mouth scared1")
image cae scared1 blush = CaePose1("cae eyes scared1", "cae mouth scared1", "game_spirits/sprites/Caelum/Pose 1/blush.png")
image cae scared1 close blush = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes scared close.png", "cae mouth scared1", "game_spirits/sprites/Caelum/Pose 1/blush.png")

image cae surprised1 = CaePose1("cae eyes surprised1", "cae mouth scared1")
image cae surprised1 close = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes neutral close.png", "cae mouth scared1")
image cae surprised1 blush = CaePose1("cae eyes surprised1", "cae mouth scared1", "game_spirits/sprites/Caelum/Pose 1/blush.png")
image cae surprised1 close blush = CaePose1("game_spirits/sprites/Caelum/Pose 1/eyes neutral close.png", "cae mouth scared1", "game_spirits/sprites/Caelum/Pose 1/blush.png")

###############################
#
# HMOM POSE 1 SPRITES
#
###############################

init python:
    HmomPose1 = BaseCSprite("hmom", "game_spirits/sprites/Fang/Pose 1/base.png", (608, 1080))

image hmom neutral1 = HmomPose1("hmom eyes neutral1", "hmom mouth neutral1")
image hmom neutral1 close = HmomPose1("game_spirits/sprites/Fang/Pose 1/eyes happy close.png", "hmom mouth neutral1")

image hmom happy1 = HmomPose1("hmom eyes happy1", "hmom mouth happy1")
image hmom happy1 close = HmomPose1("game_spirits/sprites/Fang/Pose 1/eyes happy close.png", "hmom mouth happy1")

image hmom sad1 = HmomPose1("hmom eyes sad1", "hmom mouth sad1")
image hmom sad1 close = HmomPose1("game_spirits/sprites/Fang/Pose 1/eyes sad close.png", "hmom mouth sad1")

image hmom surprised1 = HmomPose1("hmom eyes surprised1", "hmom mouth surprised1")
image hmom surprised1 close = HmomPose1("game_spirits/sprites/Fang/Pose 1/eyes sad close.png", "hmom mouth surprised1")

###############################
#
# GEN POSE 1 SPRITES
#
###############################

init python:
    GenPose1 = BaseCSprite("gen", "game_spirits/sprites/Gene/Pose 1/base.png", (608, 1080))

image gen neutral1 = GenPose1("game_spirits/sprites/Gene/Pose 1/eyes neutral.png", "gen mouth neutral1")

image gen happy1 = GenPose1("game_spirits/sprites/Gene/Pose 1/eyes neutral.png", "gen mouth happy1")

image gen sad1 = GenPose1("game_spirits/sprites/Gene/Pose 1/eyes sad.png", "gen mouth sad1")

image gen angry1 = GenPose1("game_spirits/sprites/Gene/Pose 1/eyes angry.png", "gen mouth angry1")

image gen surprised1 = GenPose1("game_spirits/sprites/Gene/Pose 1/eyes surprised.png", "gen mouth surprised1")

###############################
#
# ALX POSE 1 COMPOSITE PARTS
#
###############################

image alx eyes neutral1 = blinkeyes("game_spirits/sprites/Alex/Pose 1/eyes neutral open.png", "game_spirits/sprites/Alex/Pose 1/eyes neutral close.png")

image alx eyes happy1 = blinkeyes("game_spirits/sprites/Alex/Pose 1/eyes happy open.png", "game_spirits/sprites/Alex/Pose 1/eyes happy close.png")

image alx eyes sad1 = blinkeyes("game_spirits/sprites/Alex/Pose 1/eyes sad open.png", "game_spirits/sprites/Alex/Pose 1/eyes sad close.png")

image alx eyes angry1 = blinkeyes("game_spirits/sprites/Alex/Pose 1/eyes angry open.png", "game_spirits/sprites/Alex/Pose 1/eyes angry close.png")

image alx eyes scared1 = blinkeyes("game_spirits/sprites/Alex/Pose 1/eyes scared open.png", "game_spirits/sprites/Alex/Pose 1/eyes scared close.png")

image alx mouth neutral1 = FlapMouth("alx", "game_spirits/sprites/Alex/Pose 1/mouth neutral close.png", "game_spirits/sprites/Alex/Pose 1/mouth neutral open.png")

image alx mouth happy1 = FlapMouth("alx", "game_spirits/sprites/Alex/Pose 1/mouth happy close.png", "game_spirits/sprites/Alex/Pose 1/mouth scared open.png")

image alx mouth sad1 = FlapMouth("alx", "game_spirits/sprites/Alex/Pose 1/mouth sad close.png", "game_spirits/sprites/Alex/Pose 1/mouth neutral open.png")

image alx mouth angry1 = FlapMouth("alx", "game_spirits/sprites/Alex/Pose 1/mouth angry close.png", "game_spirits/sprites/Alex/Pose 1/mouth scared open.png")

image alx mouth bitter1 = FlapMouth("alx", "game_spirits/sprites/Alex/Pose 1/mouth bitter close.png", "game_spirits/sprites/Alex/Pose 1/mouth scared open.png")

image alx mouth scared1 = FlapMouth("alx", "game_spirits/sprites/Alex/Pose 1/mouth scared open.png", "game_spirits/sprites/Alex/Pose 1/mouth neutral open.png")

###############################
#
# CAE POSE 1 COMPOSITE PARTS
#
###############################

image cae eyes neutral1 = blinkeyes("game_spirits/sprites/Caelum/Pose 1/eyes neutral open.png", "game_spirits/sprites/Caelum/Pose 1/eyes neutral close.png")

image cae eyes sad1 = blinkeyes("game_spirits/sprites/Caelum/Pose 1/eyes sad open.png", "game_spirits/sprites/Caelum/Pose 1/eyes sad close.png")

image cae eyes angry1 = blinkeyes("game_spirits/sprites/Caelum/Pose 1/eyes angry open.png", "game_spirits/sprites/Caelum/Pose 1/eyes angry close.png")

image cae eyes scared1 = blinkeyes("game_spirits/sprites/Caelum/Pose 1/eyes scared open.png", "game_spirits/sprites/Caelum/Pose 1/eyes scared close.png")

image cae eyes surprised1 = blinkeyes("game_spirits/sprites/Caelum/Pose 1/eyes surprised open.png", "game_spirits/sprites/Caelum/Pose 1/eyes neutral close.png")

image cae mouth neutral1 = FlapMouth("cae", "game_spirits/sprites/Caelum/Pose 1/mouth neutral close.png", "game_spirits/sprites/Caelum/Pose 1/mouth neutral open.png")

image cae mouth happy1 = FlapMouth("cae", "game_spirits/sprites/Caelum/Pose 1/mouth happy close.png", "game_spirits/sprites/Caelum/Pose 1/mouth neutral open.png")

image cae mouth sad1 = FlapMouth("cae", "game_spirits/sprites/Caelum/Pose 1/mouth sad close.png", "game_spirits/sprites/Caelum/Pose 1/mouth neutral open.png")

image cae mouth scared1 = FlapMouth("cae", "game_spirits/sprites/Caelum/Pose 1/mouth surprised open.png", "game_spirits/sprites/Caelum/Pose 1/mouth neutral close.png")

###############################
#
# HMOM POSE 1 COMPOSITE PARTS
#
###############################

image hmom eyes neutral1 = blinkeyes("game_spirits/sprites/Fang/Pose 1/eyes neutral open.png", "game_spirits/sprites/Fang/Pose 1/eyes happy close.png")

image hmom eyes happy1 = blinkeyes("game_spirits/sprites/Fang/Pose 1/eyes happy open.png", "game_spirits/sprites/Fang/Pose 1/eyes happy close.png")

image hmom eyes sad1 = blinkeyes("game_spirits/sprites/Fang/Pose 1/eyes sad open.png", "game_spirits/sprites/Fang/Pose 1/eyes sad close.png")

image hmom eyes surprised1 = blinkeyes("game_spirits/sprites/Fang/Pose 1/eyes surprised open.png", "game_spirits/sprites/Fang/Pose 1/eyes sad close.png")

image hmom mouth neutral1 = FlapMouth("hmom", "game_spirits/sprites/Fang/Pose 1/mouth neutral close.png", "game_spirits/sprites/Fang/Pose 1/mouth neutral open.png")

image hmom mouth happy1 = FlapMouth("hmom", "game_spirits/sprites/Fang/Pose 1/mouth happy close.png", "game_spirits/sprites/Fang/Pose 1/mouth neutral open.png")

image hmom mouth sad1 = FlapMouth("hmom", "game_spirits/sprites/Fang/Pose 1/mouth sad close.png", "game_spirits/sprites/Fang/Pose 1/mouth neutral open.png")

image hmom mouth surprised1 = FlapMouth("hmom", "game_spirits/sprites/Fang/Pose 1/mouth surprised open.png", "game_spirits/sprites/Fang/Pose 1/mouth neutral close.png")

###############################
#
# GEN POSE 1 COMPOSITE PARTS
#
###############################

image gen mouth neutral1 = FlapMouth("gen", "game_spirits/sprites/Gene/Pose 1/mouth neutral close.png", "game_spirits/sprites/Gene/Pose 1/mouth surprised open.png")

image gen mouth happy1 = FlapMouth("gen", "game_spirits/sprites/Gene/Pose 1/mouth happy close.png", "game_spirits/sprites/Gene/Pose 1/mouth surprised open.png")

image gen mouth sad1 = FlapMouth("gen", "game_spirits/sprites/Gene/Pose 1/mouth sad close.png", "game_spirits/sprites/Gene/Pose 1/mouth angry open.png")

image gen mouth angry1 = FlapMouth("gen", "game_spirits/sprites/Gene/Pose 1/mouth angry open.png", "game_spirits/sprites/Gene/Pose 1/mouth neutral close.png")

image gen mouth surprised1 = FlapMouth("gen", "game_spirits/sprites/Gene/Pose 1/mouth surprised open.png", "game_spirits/sprites/Gene/Pose 1/mouth neutral close.png")

###############################
#
# SPIRITS STORY START
#
###############################

label spirits_000:
    $ persistent.last_story = "spirits"
    $ current_story = "spirits"

    menu:
        "From beginning (Act 1)":
            jump spirits_a1s0
        "Act 1 Scene 7":
            jump spirits_a1s7
        "Act 2 Scene 2 (Caelum Alive)":
            $ caelumAlive = True
            jump spirits_a2s2
        "Act 2 Scene 2 (Caelum Dead)":
            $ caelumAlive = False
            jump spirits_a2s2
        "Diary Scene (for NVL test)":
            jump spirits_a2s3
        "Act 3":
            jump spirits_a3s1
        "Show everyone's expressions":
            jump spirits_expressions

label spirits_expressions:

    show alx neutral1
    alx "alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... "

    show alx neutral1 close
    alx "alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... "

    show alx neutral1 blush
    alx "alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... alx neutral1... "

    show alx neutral1 close blush
    alx "alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... alx neutral1 close... "

    show alx happy1
    alx "alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... "

    show alx happy1 close
    alx "alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... "

    show alx happy1 blush
    alx "alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... alx happy1... "

    show alx happy1 close blush
    alx "alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... alx happy1 close... "

    show alx sad1
    alx "alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... "

    show alx sad1 close
    alx "alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... "

    show alx sad1 blush
    alx "alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... alx sad1... "

    show alx sad1 close blush
    alx "alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... alx sad1 close... "

    show alx angry1
    alx "alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... "

    show alx angry1 close
    alx "alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... "

    show alx angry1 blush
    alx "alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... alx angry1... "

    show alx angry1 close blush
    alx "alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... alx angry1 close... "

    show alx bitter1
    alx "alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... "

    show alx bitter1 close
    alx "alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... "

    show alx bitter1 blush
    alx "alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... alx bitter1... "

    show alx bitter1 close blush
    alx "alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... alx bitter1 close... "

    show alx scared1
    alx "alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... "

    show alx scared1 close
    alx "alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... "

    show alx scared1 blush
    alx "alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... alx scared1... "

    show alx scared1 close blush
    alx "alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... alx scared1 close... "

    show alx surprised1
    alx "alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... "

    show alx surprised1 close
    alx "alx surprised1 close... alx surprised1 close... alx surprised1 close... alx surprised1 close... alx surprised1 close... alx surprised1 close... alx surprised1 close... alx surprised1 close... "

    show alx surprised1 blush
    alx "alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... alx surprised1... "

    show alx surprised1 close blush
    alx "alx surprised1 close... alx surprised1 close... alx surprised1 close... alx surprised1 close... alx surprised1 close... alx surprised1 close... alx surprised1 close... alx surprised1 close... "

    hide alx

    show cae neutral1
    cae "cae neutral1... cae neutral1... cae neutral1... cae neutral1... cae neutral1... cae neutral1... cae neutral1... cae neutral1... cae neutral1... cae neutral1... cae neutral1... "

    show cae neutral1 close
    cae "cae neutral1 close... cae neutral1 close... cae neutral1 close... cae neutral1 close... cae neutral1 close... cae neutral1 close... cae neutral1 close... cae neutral1 close... cae neutral1 close... "

    show cae neutral1 blush
    cae "cae neutral1 blush... cae neutral1 blush... cae neutral1 blush... cae neutral1 blush... cae neutral1 blush... cae neutral1 blush... cae neutral1 blush... cae neutral1 blush... cae neutral1 blush... "

    show cae neutral1 close blush
    cae "cae neutral1 close blush... cae neutral1 close blush... cae neutral1 close blush... cae neutral1 close blush... cae neutral1 close blush... cae neutral1 close blush... cae neutral1 close blush... "

    show cae happy1
    cae "cae happy1... cae happy1... cae happy1... cae happy1... cae happy1... cae happy1... cae happy1... cae happy1... cae happy1... cae happy1... cae happy1... cae happy1... "

    show cae happy1 close
    cae "cae happy1 close... cae happy1 close... cae happy1 close... cae happy1 close... cae happy1 close... cae happy1 close... cae happy1 close... cae happy1 close... cae happy1 close... cae happy1 close... "

    show cae happy1 blush
    cae "cae happy1 blush... cae happy1 blush... cae happy1 blush... cae happy1 blush... cae happy1 blush... cae happy1 blush... cae happy1 blush... cae happy1 blush... cae happy1 blush... "

    show cae happy1 close blush
    cae "cae happy1 close blush... cae happy1 close blush... cae happy1 close blush... cae happy1 close blush... cae happy1 close blush... cae happy1 close blush... cae happy1 close blush... cae happy1 close blush... "

    show cae sad1
    cae "cae sad1... cae sad1... cae sad1... cae sad1... cae sad1... cae sad1... cae sad1... cae sad1... cae sad1... cae sad1... cae sad1... cae sad1... cae sad1... cae sad1... "

    show cae sad1 close
    cae "cae sad1 close... cae sad1 close... cae sad1 close... cae sad1 close... cae sad1 close... cae sad1 close... cae sad1 close... cae sad1 close... cae sad1 close... cae sad1 close... "

    show cae sad1 blush
    cae "cae sad1 blush... cae sad1 blush... cae sad1 blush... cae sad1 blush... cae sad1 blush... cae sad1 blush... cae sad1 blush... cae sad1 blush... cae sad1 blush... cae sad1 blush... "

    show cae sad1 close blush
    cae "cae sad1 close blush... cae sad1 close blush... cae sad1 close blush... cae sad1 close blush... cae sad1 close blush... cae sad1 close blush... cae sad1 close blush... cae sad1 close blush... cae sad1 close blush... "

    show cae angry1
    cae "cae angry1... cae angry1... cae angry1... cae angry1... cae angry1... cae angry1... cae angry1... cae angry1... cae angry1... cae angry1... cae angry1... cae angry1... cae angry1... "

    show cae angry1 close
    cae "cae angry1 close... cae angry1 close... cae angry1 close... cae angry1 close... cae angry1 close... cae angry1 close... cae angry1 close... cae angry1 close... cae angry1 close... "

    show cae angry1 blush
    cae "cae angry1 blush... cae angry1 blush... cae angry1 blush... cae angry1 blush... cae angry1 blush... cae angry1 blush... cae angry1 blush... cae angry1 blush... cae angry1 blush... cae angry1 blush... "

    show cae angry1 close blush
    cae "cae angry1 close blush... cae angry1 close blush... cae angry1 close blush... cae angry1 close blush... cae angry1 close blush... cae angry1 close blush... cae angry1 close blush... cae angry1 close blush... "

    show cae bitter1
    cae "cae bitter1... cae bitter1... cae bitter1... cae bitter1... cae bitter1... cae bitter1... cae bitter1... cae bitter1... cae bitter1... cae bitter1... cae bitter1... cae bitter1... "

    show cae bitter1 close
    cae "cae bitter1 close... cae bitter1 close... cae bitter1 close... cae bitter1 close... cae bitter1 close... cae bitter1 close... cae bitter1 close... cae bitter1 close... cae bitter1 close... "

    show cae bitter1 blush
    cae "cae bitter1 blush... cae bitter1 blush... cae bitter1 blush... cae bitter1 blush... cae bitter1 blush... cae bitter1 blush... cae bitter1 blush... cae bitter1 blush... cae bitter1 blush... cae bitter1 blush... "

    show cae bitter1 close blush
    cae "cae bitter1 close blush... cae bitter1 close blush... cae bitter1 close blush... cae bitter1 close blush... cae bitter1 close blush... cae bitter1 close blush... cae bitter1 close blush... cae bitter1 close blush... "

    show cae scared1
    cae "cae scared1... cae scared1... cae scared1... cae scared1... cae scared1... cae scared1... cae scared1... cae scared1... cae scared1... cae scared1... cae scared1... cae scared1... cae scared1... "

    show cae scared1 close
    cae "cae scared1 close... cae scared1 close... cae scared1 close... cae scared1 close... cae scared1 close... cae scared1 close... cae scared1 close... cae scared1 close... cae scared1 close... "

    show cae scared1 blush
    cae "cae scared1 blush... cae scared1 blush... cae scared1 blush... cae scared1 blush... cae scared1 blush... cae scared1 blush... cae scared1 blush... cae scared1 blush... cae scared1 blush... cae scared1 blush... "

    show cae scared1 close blush
    cae "cae scared1 close blush... cae scared1 close blush... cae scared1 close blush... cae scared1 close blush... cae scared1 close blush... cae scared1 close blush... cae scared1 close blush... cae scared1 close blush... "

    show cae surprised1
    cae "cae surprised1... cae surprised1... cae surprised1... cae surprised1... cae surprised1... cae surprised1... cae surprised1... cae surprised1... cae surprised1... cae surprised1... cae surprised1... cae surprised1... "

    show cae surprised1 close
    cae "cae surprised1 close... cae surprised1 close... cae surprised1 close... cae surprised1 close... cae surprised1 close... cae surprised1 close... cae surprised1 close... cae surprised1 close... cae surprised1 close... "

    show cae surprised1 blush
    cae "cae surprised1 blush... cae surprised1 blush... cae surprised1 blush... cae surprised1 blush... cae surprised1 blush... cae surprised1 blush... cae surprised1 blush... cae surprised1 blush... cae surprised1 blush... "

    show cae surprised1 close blush
    cae "cae surprised1 close blush... cae surprised1 close blush... cae surprised1 close blush... cae surprised1 close blush... cae surprised1 close blush... cae surprised1 close blush... cae surprised1 close blush... "

    hide cae

    show hmom neutral1
    hmom "hmom neutral1... hmom neutral1... hmom neutral1... hmom neutral1... hmom neutral1... hmom neutral1... hmom neutral1... hmom neutral1... hmom neutral1... hmom neutral1... hmom neutral1... "

    show hmom neutral1 close
    hmom "hmom neutral1 close... hmom neutral1 close... hmom neutral1 close... hmom neutral1 close... hmom neutral1 close... hmom neutral1 close... hmom neutral1 close... hmom neutral1 close... hmom neutral1 close... "

    show hmom happy1
    hmom "hmom happy1... hmom happy1... hmom happy1... hmom happy1... hmom happy1... hmom happy1... hmom happy1... hmom happy1... hmom happy1... hmom happy1... hmom happy1... hmom happy1... "

    show hmom happy1 close
    hmom "hmom happy1 close... hmom happy1 close... hmom happy1 close... hmom happy1 close... hmom happy1 close... hmom happy1 close... hmom happy1 close... hmom happy1 close... hmom happy1 close... hmom happy1 close... "

    show hmom sad1
    hmom "hmom sad1... hmom sad1... hmom sad1... hmom sad1... hmom sad1... hmom sad1... hmom sad1... hmom sad1... hmom sad1... hmom sad1... hmom sad1... hmom sad1... hmom sad1... hmom sad1... "

    show hmom sad1 close
    hmom "hmom sad1 close... hmom sad1 close... hmom sad1 close... hmom sad1 close... hmom sad1 close... hmom sad1 close... hmom sad1 close... hmom sad1 close... hmom sad1 close... hmom sad1 close... "

    show hmom surprised1
    hmom "hmom surprised1... hmom surprised1... hmom surprised1... hmom surprised1... hmom surprised1... hmom surprised1... hmom surprised1... hmom surprised1... hmom surprised1... hmom surprised1... "

    show hmom surprised1 close
    hmom "hmom surprised1 close... hmom surprised1 close... hmom surprised1 close... hmom surprised1 close... hmom surprised1 close... hmom surprised1 close... hmom surprised1 close... hmom surprised1 close... "

    hide hmom

    show gen neutral1
    gen "gen neutral1... gen neutral1... gen neutral1... gen neutral1... gen neutral1... gen neutral1... gen neutral1... gen neutral1... gen neutral1... gen neutral1... gen neutral1... gen neutral1... "

    show gen happy1
    gen "gen happy1... gen happy1... gen happy1... gen happy1... gen happy1... gen happy1... gen happy1... gen happy1... gen happy1... gen happy1... gen happy1... gen happy1... gen happy1... "

    show gen sad1
    gen "gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... gen sad1... "

    show gen angry1
    gen "gen angry1... gen angry1... gen angry1... gen angry1... gen angry1... gen angry1... gen angry1... gen angry1... gen angry1... gen angry1... gen angry1... gen angry1... gen angry1... gen angry1... "

    show gen surprised1
    gen "gen surprised1... gen surprised1... gen surprised1... gen surprised1... gen surprised1... gen surprised1... gen surprised1... gen surprised1... gen surprised1... gen surprised1... gen surprised1... "

    hide gen

    jump spirits_000
