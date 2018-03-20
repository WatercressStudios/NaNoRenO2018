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

image eli normal1 = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="eli eyes normal1", mouth="eli mouth normal1")

image eli normal1 close = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="game_letgo/sprites/Eli/Pose 1/eyes normal close.png", mouth="eli mouth normal1")

image eli smile1 = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="eli eyes normal1", mouth="eli mouth smile1")

image eli smile1 close = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="game_letgo/sprites/Eli/Pose 1/eyes normal close.png", mouth="eli mouth smile1")

image eli happy1 = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="eli eyes normal1", mouth="eli mouth happy1")

image eli happy1 close = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="game_letgo/sprites/Eli/Pose 1/eyes normal close.png", mouth="eli mouth happy1")

image eli sad1 = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="eli eyes worried1", mouth="eli mouth sad1")

image eli sad1 close = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="game_letgo/sprites/Eli/Pose 1/eyes worry close.png", mouth="eli mouth sad1")

image eli worried1 = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="eli eyes worried1", mouth="eli mouth smile1")

image eli worried1 close = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="game_letgo/sprites/Eli/Pose 1/eyes worry close.png", mouth="eli mouth smile1")

image eli angry1 = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="eli eyes angry1", mouth="eli mouth sad1")

image eli angry1 close = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="game_letgo/sprites/Eli/Pose 1/eyes angry close.png", mouth="eli mouth sad1")

image eli cool1 = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="eli eyes angry1", mouth="eli mouth smile1")

image eli cool1 close = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="game_letgo/sprites/Eli/Pose 1/eyes angry close.png", mouth="eli mouth smile1")
    
image eli goofy1 = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="eli eyes angry1", mouth="eli mouth happy1")

image eli goofy1 close = CSprite("eli", "game_letgo/sprites/Eli/Pose 1/base.png", size=(578, 1080), eyes="game_letgo/sprites/Eli/Pose 1/eyes angry close.png", mouth="eli mouth happy1")

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
        "End of Loop 4":
            jump letgo_402
        "End of Good Ending Loop 5":
            jump letgo_501a4
        "End of Bad Ending Loop 5":
            jump letgo_502
        "Show Eli's expressions":
            jump letgo_eli_expressions

label letgo_eli_expressions:
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
