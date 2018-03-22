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
# MAY POSE 1 SPRITES
#
###############################

init python:
    MayPose1 = BaseCSprite("may", "game_letgo/sprites/May/Pose 1/base.png", (496, 920))

image may normal1 = MayPose1("may eyes normal1", "may mouth smile1")
image may normal1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes normal close.png", "may mouth smile1")

image may shout1 = MayPose1("may eyes angry1", "may mouth shout1")
image may sadshout1 = MayPose1("may eyes sad1", "may mouth shout1")
image may shout1 close = MayPose1("game_letgo/sprites/May/Pose 1/eyes angry close.png", "may mouth shout1")


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

    show may shout1
    may "may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... may shout1... "

    show may sadshout1
    may "may sadshout1... may sadshout1... may sadshout1... may sadshout1... may sadshout1... may sadshout1... may sadshout1... may sadshout1... may sadshout1... "

    show may shout1 close
    may "may shout1 close... may shout1 close... may shout1 close... may shout1 close... may shout1 close... may shout1 close... may shout1 close... may shout1 close... "

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

    hide eli
    jump letgo_000
