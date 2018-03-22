###############################
#
# LET GO DEFINITIONS GO IN HERE
#
###############################

define eli = Character("Elijah", callback=speaker("eli"))
define may = Character("Maya", callback=speaker("may"))
define om = Character("Old Man")
define ow = Character("Old Woman")
define dude = Character("Some Dude")
define kid = Character("Some Kid")
define mom = Character("Mom")

image white = "#fff"

###############################
#
# ELI POSE 1 SPRITES
#
###############################

init python:
    EliPose1 = BaseCSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", (578, 1080))

image eli normal1 = EliPose1("eli eyes normal1", "eli mouth normal1")
image eli normal1 close = EliPose1("game_letgo/sprites/Eli/Pose 1/eyes normal close.png", "eli mouth normal1")

image eli smile1 = EliPose1("eli eyes normal1", "eli mouth smile1")
image eli smile1 close = EliPose1("game_letgo/sprites/Eli/Pose 1/eyes normal close.png", "eli mouth smile1")

image eli happy1 = EliPose1("eli eyes normal1", "eli mouth happy1")
image eli happy1 close = EliPose1("game_letgo/sprites/Eli/Pose 1/eyes normal close.png", "eli mouth happy1")

image eli sad1 = EliPose1("eli eyes worried1", "eli mouth sad1")
image eli sad1 close = EliPose1("game_letgo/sprites/Eli/Pose 1/eyes worry close.png", "eli mouth sad1")

image eli worried1 = EliPose1("eli eyes worried1", "eli mouth smile1")
image eli worried1 close = EliPose1("game_letgo/sprites/Eli/Pose 1/eyes worry close.png", "eli mouth smile1")

image eli angry1 = EliPose1("eli eyes angry1", "eli mouth sad1")
image eli angry1 close = EliPose1("game_letgo/sprites/Eli/Pose 1/eyes angry close.png", "eli mouth sad1")

image eli cool1 = EliPose1("eli eyes angry1", "eli mouth smile1")
image eli cool1 close = EliPose1("game_letgo/sprites/Eli/Pose 1/eyes angry close.png", "eli mouth smile1")

image eli goofy1 = EliPose1("eli eyes angry1", "eli mouth happy1")
image eli goofy1 close = EliPose1("game_letgo/sprites/Eli/Pose 1/eyes angry close.png", "eli mouth happy1")

###############################
#
# ELI POSE 2 SPRITES
#
###############################
init python:
    EliPose2 = BaseCSprite("eli", "game_letgo/sprites/Eli/Pose 2/base.png", (615, 1080))

image eli normal2 = EliPose2("eli eyes normal2", "eli mouth normal2")
image eli normal2 close = EliPose2("game_letgo/sprites/Eli/Pose 2/eyes normal close.png", "eli mouth normal2")

image eli smile2 = EliPose2("eli eyes normal2", "eli mouth smile2")
image eli smile2 close = EliPose2("game_letgo/sprites/Eli/Pose 2/eyes normal close.png", "eli mouth smile2")

image eli sad2 = EliPose2("eli eyes worried2", "eli mouth sad2")
image eli sad2 close = EliPose2("game_letgo/sprites/Eli/Pose 2/eyes worry close.png", "eli mouth sad2")

image eli worried2 = EliPose2("eli eyes worried2", "eli mouth normal2")
image eli worried2 close = EliPose2("game_letgo/sprites/Eli/Pose 2/eyes worry close.png", "eli mouth normal2")

image eli angry2 = EliPose2("eli eyes angry2", "eli mouth sad2")
image eli angry2 close = EliPose2("game_letgo/sprites/Eli/Pose 2/eyes angry close.png", "eli mouth sad2")

image eli cool2 = EliPose2("eli eyes angry2", "eli mouth smile2")
image eli cool2 close = EliPose2("game_letgo/sprites/Eli/Pose 2/eyes angry close.png", "eli mouth smile2")


###############################
#
# MAY POSE 1 SPRITES
#
###############################

init python:
    MayPose1 = BaseCSprite("may", "game_letgo/sprites/May/Pose 1/base.png", (496, 920))

image may normal1 = MayPose1("may eyes normal1", "may mouth smile1")
image may normal1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes normal close.png", "may mouth smile1")

image may frown1 = MayPose1("may eyes normal1", "may mouth pout1")
image may frown1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes normal close.png", "may mouth pout1")

image may adore1 = MayPose1("may eyes squint1", "may mouth smile1")
image may adore1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes normal close.png", "may mouth smile1")

image may confused1 = MayPose1("may eyes squint1", "may mouth sad1")
image may confused1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes normal close.png", "may mouth sad1")

image may aww1 = MayPose1("may eyes worried1", "may mouth happy1")
image may aww1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes worry close.png", "may mouth happy1")

image may worried1 = MayPose1("may eyes worried1", "may mouth angry1")
image may worried1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes worry close.png", "may mouth angry1")

image may sad1 = MayPose1("may eyes worried1", "may mouth sad1")
image may sad1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes worry close.png", "may mouth sad1")

image may challenge1 = MayPose1("may eyes angry1", "may mouth happy1")
image may challenge1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes angry close.png", "may mouth happy1")

image may cheeky1 = MayPose1("may eyes sad1", "may mouth happy1")
image may cheeky1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes angry close.png", "may mouth happy1")

image may angry1 = MayPose1("may eyes angry1", "may mouth angry1")
image may angry1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes angry close.png", "may mouth angry1")

image may shout1 = MayPose1("may eyes angry1", "may mouth shout1")
image may shout1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes angry close.png", "may mouth shout1")

image may sadshout1 = MayPose1("may eyes sad1", "may mouth shout1")
image may sadshout1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes angry close.png", "may mouth shout1")

image may forcedsmile1 = MayPose1("may eyes sad1", "may mouth smile1")
image may forcedsmile1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes angry close.png", "may mouth smile1")

image may suspicious1 = MayPose1("may eyes sad1", "may mouth sad1")
image may suspicious1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes angry close.png", "may mouth sad1")


###############################
#
# MAY POSE 2 SPRITES
#
###############################

init python:
    MayPose2 = BaseCSprite("may", "game_letgo/sprites/May/Pose 2/base.png", (420, 915))



###############################
#
# MAY POSE 3 SPRITES
#
###############################

init python:
    MayPose2 = BaseCSprite("may", "game_letgo/sprites/May/Pose 3/base.png", (507, 930))


###############################
#
# ELI POSE 1 COMPOSITE PARTS
#
###############################

image eli eyes normal1 = blinkeyes("game_letgo/sprites/Eli/Pose 1/eyes normal open.png", "game_letgo/sprites/Eli/Pose 1/eyes normal close.png")

image eli eyes worried1 = blinkeyes("game_letgo/sprites/Eli/Pose 1/eyes worry open.png", "game_letgo/sprites/Eli/Pose 1/eyes worry close.png")

image eli eyes angry1 = blinkeyes("game_letgo/sprites/Eli/Pose 1/eyes angry open.png", "game_letgo/sprites/Eli/Pose 1/eyes angry close.png")

image eli mouth normal1 = FlapMouth("eli", "game_letgo/sprites/Eli/Pose 1/mouth close.png", "game_letgo/sprites/Eli/Pose 1/mouth normal open.png")

image eli mouth sad1 = FlapMouth("eli", "game_letgo/sprites/Eli/Pose 1/mouth normal open.png", "game_letgo/sprites/Eli/Pose 1/mouth close.png")

image eli mouth smile1 = FlapMouth("eli", "game_letgo/sprites/Eli/Pose 1/mouth close.png", "game_letgo/sprites/Eli/Pose 1/mouth smile open.png")

image eli mouth happy1 = FlapMouth("eli", "game_letgo/sprites/Eli/Pose 1/mouth smile open.png", "game_letgo/sprites/Eli/Pose 1/mouth close.png")

###############################
#
# ELI POSE 2 COMPOSITE PARTS
#
###############################

image eli eyes normal2 = blinkeyes("game_letgo/sprites/Eli/Pose 2/eyes normal open.png", "game_letgo/sprites/Eli/Pose 2/eyes normal close.png")

image eli eyes worried2 = blinkeyes("game_letgo/sprites/Eli/Pose 2/eyes worry open.png", "game_letgo/sprites/Eli/Pose 2/eyes worry close.png")

image eli eyes angry2 = blinkeyes("game_letgo/sprites/Eli/Pose 2/eyes angry open.png", "game_letgo/sprites/Eli/Pose 2/eyes angry close.png")

image eli mouth normal2 = FlapMouth("eli", "game_letgo/sprites/Eli/Pose 2/mouth normal.png", "game_letgo/sprites/Eli/Pose 2/mouth open normal.png")

image eli mouth sad2 = FlapMouth("eli", "game_letgo/sprites/Eli/Pose 2/mouth frown.png", "game_letgo/sprites/Eli/Pose 2/mouth open normal.png")

image eli mouth smile2 = FlapMouth("eli", "game_letgo/sprites/Eli/Pose 2/mouth normal.png", "game_letgo/sprites/Eli/Pose 2/mouth open smile.png")

###############################
#
# MAYA POSE 1 COMPOSITE PARTS
#
###############################

image may eyes normal1 = blinkeyes("game_letgo/sprites/May/Pose 1/eyes normal open.png", "game_letgo/sprites/May/Pose 1/eyes normal close.png")

image may eyes squint1 = blinkeyes("game_letgo/sprites/May/Pose 1/eyes normal squint.png", "game_letgo/sprites/May/Pose 1/eyes normal close.png")

image may eyes worried1 = blinkeyes("game_letgo/sprites/May/Pose 1/eyes worry squint.png", "game_letgo/sprites/May/Pose 1/eyes worry close.png")

image may eyes angry1 = blinkeyes("game_letgo/sprites/May/Pose 1/eyes angry open.png", "game_letgo/sprites/May/Pose 1/eyes angry close.png")

image may eyes sad1 = blinkeyes("game_letgo/sprites/May/Pose 1/eyes angry squint.png", "game_letgo/sprites/May/Pose 1/eyes angry close.png")

image may mouth angry1 = FlapMouth("may", "game_letgo/sprites/May/Pose 1/mouth frown close.png", "game_letgo/sprites/May/Pose 1/mouth big open.png")

image may mouth pout1 = FlapMouth("may", "game_letgo/sprites/May/Pose 1/mouth frown close.png", "game_letgo/sprites/May/Pose 1/mouth small open.png")

image may mouth sad1 = FlapMouth("may", "game_letgo/sprites/May/Pose 1/mouth small open.png", "game_letgo/sprites/May/Pose 1/mouth frown close.png")

image may mouth shout1 = FlapMouth("may", "game_letgo/sprites/May/Pose 1/mouth small open.png", "game_letgo/sprites/May/Pose 1/mouth big open.png")

image may mouth smile1 = FlapMouth("may", "game_letgo/sprites/May/Pose 1/mouth smile close.png", "game_letgo/sprites/May/Pose 1/mouth small open.png")

image may mouth happy1 = FlapMouth("may", "game_letgo/sprites/May/Pose 1/mouth smile close.png", "game_letgo/sprites/May/Pose 1/mouth big open.png")


###############################
#
# LET GO STORY START
#
###############################

label letgo_000:
    $ persistent.last_story = "letgo"

    #jump letgo_101

    menu:
        "From beginning":
            jump letgo_101
        "End of Loop 1":
            jump letgo_104
        "End of Loop 2":
            jump letgo_204
        "End of Loop 3":
            jump letgo_303
        "The Choice in Loop 4 (one goes to Bad Ending)":
            jump letgo_401
        "End of Loop 4 (towards Good Ending)":
            jump letgo_402
        "Good Ending Loop 5":
            jump letgo_501a4
        "Bad Ending Loop 5":
            jump letgo_502
        "Show Eli and May's expressions":
            jump letgo_expressions

label letgo_expressions:
    show may normal1
    may "may normal1... may normal1... may normal1... may normal1... may normal1... may normal1... may normal1... may normal1... may normal1... may normal1... may normal1... "

    show may normal1 close
    may "may normal1 close... may normal1 close... may normal1 close... may normal1 close... may normal1 close... may normal1 close... may normal1 close... "

    show may frown1
    may "may frown1... may frown1... may frown1... may frown1... may frown1... may frown1... may frown1... may frown1... may frown1... may frown1... may frown1... "

    show may frown1 close
    may "may frown1 close... may frown1 close... may frown1 close... may frown1 close... may frown1 close... may frown1 close... may frown1 close... may frown1 close... "

    show may adore1
    may "may adore1... may adore1... may adore1... may adore1... may adore1... may adore1... may adore1... may adore1... may adore1... may adore1... may adore1... "

    show may adore1 close
    may "may adore1 close... may adore1 close... may adore1 close... may adore1 close... may adore1 close... may adore1 close... may adore1 close... may adore1 close... "

    show may confused1
    may "may confused1... may confused1... may confused1... may confused1... may confused1... may confused1... may confused1... may confused1... may confused1... "

    show may confused1 close
    may "may confused1 close... may confused1 close... may confused1 close... may confused1 close... may confused1 close... may confused1 close... may confused1 close... "

    show may aww1
    may "may aww1... may aww1... may aww1... may aww1... may aww1... may aww1... may aww1... may aww1... may aww1... may aww1... may aww1... may aww1... may aww1... "

    show may aww1 close
    may "may aww1 close... may aww1 close... may aww1 close... may aww1 close... may aww1 close... may aww1 close... may aww1 close... may aww1 close... may aww1 close... "

    show may worried1
    may "may worried1... may worried1... may worried1... may worried1... may worried1... may worried1... may worried1... may worried1... may worried1... may worried1... "

    show may worried1 close
    may "may worried1 close... may worried1 close... may worried1 close... may worried1 close... may worried1 close... may worried1 close... may worried1 close... "

    show may sad1
    may "may sad1... may sad1... may sad1... may sad1... may sad1... may sad1... may sad1... may sad1... may sad1... may sad1... may sad1... may sad1... may sad1... "

    show may sad1 close
    may "may sad1 close... may sad1 close... may sad1 close... may sad1 close... may sad1 close... may sad1 close... may sad1 close... may sad1 close... may sad1 close... "

    show may challenge1
    may "may challenge1... may challenge1... may challenge1... may challenge1... may challenge1... may challenge1... may challenge1... may challenge1... may challenge1... "

    show may challenge1 close
    may "may challenge1 close... may challenge1 close... may challenge1 close... may challenge1 close... may challenge1 close... may challenge1 close... "

    show may cheeky1
    may "may cheeky1... may cheeky1... may cheeky1... may cheeky1... may cheeky1... may cheeky1... may cheeky1... may cheeky1... may cheeky1... may cheeky1... may cheeky1... "

    show may cheeky1 close
    may "may cheeky1 close... may cheeky1 close... may cheeky1 close... may cheeky1 close... may cheeky1 close... may cheeky1 close... may cheeky1 close... "

    show may angry1
    may "may angry1... may angry1... may angry1... may angry1... may angry1... may angry1... may angry1... may angry1... may angry1... may angry1... may angry1... "

    show may angry1 close
    may "may angry1 close... may angry1 close... may angry1 close... may angry1 close... may angry1 close... may angry1 close... may angry1 close... may angry1 close... "

    show may shout1
    may "may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... "

    show may shout1 close
    may "may shout1 close... may shout1 close... may shout1 close... may shout1 close... may shout1 close... may shout1 close... may shout1 close... may shout1 close... "

    show may sadshout1
    may "may sadshout1... may sadshout1... may sadshout1... may sadshout1... may sadshout1... may sadshout1... may sadshout1... may sadshout1... may sadshout1... "

    show may sadshout1 close
    may "may sadshout1 close... may sadshout1 close... may sadshout1 close... may sadshout1 close... may sadshout1 close... may sadshout1 close... may sadshout1 close... "

    show may forcedsmile1
    may "may forcedsmile1... may forcedsmile1... may forcedsmile1... may forcedsmile1... may forcedsmile1... may forcedsmile1... may forcedsmile1... may forcedsmile1... "

    show may forcedsmile1 close
    may "may forcedsmile1 close... may forcedsmile1 close... may forcedsmile1 close... may forcedsmile1 close... may forcedsmile1 close... may forcedsmile1 close... "

    show may suspicious1
    may "may suspicious1... may suspicious1... may suspicious1... may suspicious1... may suspicious1... may suspicious1... may suspicious1... may suspicious1... "

    show may suspicious1 close
    may "may suspicious1 close... may suspicious1 close... may suspicious1 close... may suspicious1 close... may suspicious1 close... may suspicious1 close... "

    hide may

    show eli normal1
    eli "eli normal1... eli normal1... eli normal1... eli normal1... eli normal1... eli normal1... eli normal1... eli normal1... eli normal1... eli normal1... eli normal1... "

    show eli normal1 close
    eli "eli normal1 close... eli normal1 close... eli normal1 close... eli normal1 close... eli normal1 close... eli normal1 close... eli normal1 close... "

    show eli smile1
    eli "eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... "

    show eli smile1 close
    eli "eli smile1 close... eli smile1 close... eli smile1 close... eli smile1 close... eli smile1 close... eli smile1 close... eli smile1 close... eli smile1 close... "

    show eli happy1
    eli "eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... "

    show eli happy1 close
    eli "eli happy1 close... eli happy1 close... eli happy1 close... eli happy1 close... eli happy1 close... eli happy1 close... eli happy1 close... eli happy1 close... "

    show eli sad1
    eli "eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... "

    show eli sad1 close
    eli "eli sad1 close... eli sad1 close... eli sad1 close... eli sad1 close... eli sad1 close... eli sad1 close... eli sad1 close... eli sad1 close... eli sad1 close... "

    show eli worried1
    eli "show eli worried1... show eli worried1... show eli worried1... show eli worried1... show eli worried1... show eli worried1... show eli worried1... "

    show eli worried1 close
    eli "eli worried1 close... eli worried1 close... eli worried1 close... eli worried1 close... eli worried1 close... eli worried1 close... eli worried1 close... "

    show eli angry1
    eli "eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... "

    show eli angry1 close
    eli "eli angry1 close... eli angry1 close... eli angry1 close... eli angry1 close... eli angry1 close... eli angry1 close... eli angry1 close... eli angry1 close... "

    show eli cool1
    eli "eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... "

    show eli cool1 close
    eli "eli cool1 close... eli cool1 close... eli cool1 close... eli cool1 close... eli cool1 close... eli cool1 close... eli cool1 close... eli cool1 close... "

    show eli goofy1
    eli "eli goofy1... eli goofy1... eli goofy1... eli goofy1... eli goofy1... eli goofy1... eli goofy1... eli goofy1... eli goofy1... eli goofy1... eli goofy1... "

    show eli goofy1 close
    eli "eli goofy1 close... eli goofy1 close... eli goofy1 close... eli goofy1 close... eli goofy1 close... eli goofy1 close... eli goofy1 close... eli goofy1 close... "

    show eli normal2
    eli "eli normal2... eli normal2... eli normal2... eli normal2... eli normal2... eli normal2... eli normal2... eli normal2... eli normal2... eli normal2... "

    show eli normal2 close
    eli "eli normal2 close... eli normal2 close... eli normal2 close... eli normal2 close... eli normal2 close... eli normal2 close... eli normal2 close... eli normal2 close... "

    show eli smile2
    eli "eli smile2... eli smile2... eli smile2... eli smile2... eli smile2... eli smile2... eli smile2... eli smile2... eli smile2... eli smile2... eli smile2... "

    show eli smile2 close
    eli "eli smile2 close... eli smile2 close... eli smile2 close... eli smile2 close... eli smile2 close... eli smile2 close... eli smile2 close... eli smile2 close... "

    show eli sad2
    eli "eli sad2... eli sad2... eli sad2... eli sad2... eli sad2... eli sad2... eli sad2... eli sad2... eli sad2... eli sad2... eli sad2... eli sad2... eli sad2... "

    show eli sad2 close
    eli "eli sad2 close... eli sad2 close... eli sad2 close... eli sad2 close... eli sad2 close... eli sad2 close... eli sad2 close... eli sad2 close... eli sad2 close... "

    show eli worried2
    eli "eli worried2... eli worried2... eli worried2... eli worried2... eli worried2... eli worried2... eli worried2... eli worried2... eli worried2... eli worried2... "

    show eli worried2 close
    eli "eli worried2 close... eli worried2 close... eli worried2 close... eli worried2 close... eli worried2 close... eli worried2 close... eli worried2 close... "

    show eli angry2
    eli "eli angry2... eli angry2... eli angry2... eli angry2... eli angry2... eli angry2... eli angry2... eli angry2... eli angry2... eli angry2... eli angry2... "

    show eli angry2 close
    eli "eli angry2 close... eli angry2 close... eli angry2 close... eli angry2 close... eli angry2 close... eli angry2 close... eli angry2 close... eli angry2 close... "

    show eli cool2
    eli "eli cool2... eli cool2... eli cool2... eli cool2... eli cool2... eli cool2... eli cool2... eli cool2... eli cool2... eli cool2... eli cool2... eli cool2... "

    show eli cool2 close
    eli "eli cool2 close... eli cool2 close... eli cool2 close... eli cool2 close... eli cool2 close... eli cool2 close... eli cool2 close... eli cool2 close... "

    hide eli
    jump letgo_000
