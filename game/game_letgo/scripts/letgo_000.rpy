###############################
#
# LET GO DEFINITIONS GO IN HERE
#
###############################

define eli = Character("Elijah", callback=speaker("eli"))
define may = Character("Maya")
define om = Character("Old Man")
define ow = Character("Old Woman")
define dude = Character("Some Dude")
define kid = Character("Some Kid")
define mom = Character("Mom")

image white = "#fff"

# Create such a character.
define eli = Character("Elijah", callback=speaker("eli"))

image eli normal1 = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "eli eyes normal1",
        (0, 0), WhileSpeaking("eli", "eli mouth normal1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking.png"),
    )
image eli normal1 eyes closed = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Eyes Closed.png",
        (0, 0), WhileSpeaking("eli", "eli mouth normal1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking.png"),
    )

image eli smile1 = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "eli eyes normal1",
        (0, 0), WhileSpeaking("eli", "eli mouth happy1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Mouth Closed.png"),
    )
image eli smile1 eyes closed = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Eyes Closed.png",
        (0, 0), WhileSpeaking("eli", "eli mouth happy1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Mouth Closed.png"),
    )

image eli happy1 = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "eli eyes normal1",
        (0, 0), WhileSpeaking("eli", "eli mouth happy1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking Smiling.png"),
    )
image eli happy1 eyes closed = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Eyes Closed.png",
        (0, 0), WhileSpeaking("eli", "eli mouth happy1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking Smiling.png"),
    )

image eli sad1 = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "eli eyes worried1",
        (0, 0), WhileSpeaking("eli", "eli mouth normal1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking.png"),
    )
image eli sad1 eyes closed = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Composites/Worried Eyes Closed.png",
        (0, 0), WhileSpeaking("eli", "eli mouth normal1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking.png"),
    )

image eli worried1 = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "eli eyes worried1",
        (0, 0), WhileSpeaking("eli", "eli mouth happy1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Mouth Closed.png"),
    )
image eli worried1 eyes closed = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Composites/Worried Eyes Closed.png",
        (0, 0), WhileSpeaking("eli", "eli mouth happy1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Mouth Closed.png"),
    )

image eli angry1 = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "eli eyes angry1",
        (0, 0), WhileSpeaking("eli", "eli mouth normal1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking.png"),
    )
image eli angry1 eyes closed = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Composites/Angry Eyes Closed.png",
        (0, 0), WhileSpeaking("eli", "eli mouth normal1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking.png"),
    )

image eli cool1 = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "eli eyes angry1",
        (0, 0), WhileSpeaking("eli", "eli mouth happy1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Mouth Closed.png"),
    )
image eli cool1 eyes closed = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Composites/Angry Eyes Closed.png",
        (0, 0), WhileSpeaking("eli", "eli mouth happy1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Mouth Closed.png"),
    )
    
image eli determined1 = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "eli eyes angry1",
        (0, 0), WhileSpeaking("eli", "eli mouth happy1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking Smiling.png"),
    )
image eli determined1 eyes closed = LiveComposite(
        (578, 1080),
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Neutral Eyes Open Mouth Closed.png",
        (0, 0), "game_letgo/sprites/Eli/Pose 1/Composites/Angry Eyes Closed.png",
        (0, 0), WhileSpeaking("eli", "eli mouth happy1", "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking Smiling.png"),
    )

image eli eyes normal1:
    "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Eyes Opened.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Eyes Closed.png"
    .25
    repeat

image eli eyes worried1:
    "game_letgo/sprites/Eli/Pose 1/Composites/Worried Eyes Opened.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "game_letgo/sprites/Eli/Pose 1/Composites/Worried Eyes Closed.png"
    .25
    repeat

image eli eyes angry1:
    "game_letgo/sprites/Eli/Pose 1/Composites/Angry Eyes Opened.png"
    choice:
        3.5
    choice:
        2.5
    choice:
        1.5
    # This randomizes the time between blinking.
    "game_letgo/sprites/Eli/Pose 1/Composites/Angry Eyes Closed.png"
    .25
    repeat

image eli mouth normal1:
    "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Mouth Closed.png"
    .2
    "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking.png"
    .2
    repeat

image eli mouth happy1:
    "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Speaking Smiling.png"
    .2
    "game_letgo/sprites/Eli/Pose 1/Composites/Neutral Mouth Closed.png"
    .2
    repeat


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

    show eli normal1 eyes closed
    eli "eli normal1 eyes closed... eli normal1 eyes closed... eli normal1 eyes closed... eli normal1 eyes closed... eli normal1 eyes closed... eli normal1 eyes closed... "

    show eli smile1
    eli "eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... eli smile1... "

    show eli smile1 eyes closed
    eli "eli smile1 eyes closed... eli smile1 eyes closed... eli smile1 eyes closed... eli smile1 eyes closed... eli smile1 eyes closed... eli smile1 eyes closed... "

    show eli happy1
    eli "eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... eli happy1... "

    show eli happy1 eyes closed
    eli "eli happy1 eyes closed... eli happy1 eyes closed... eli happy1 eyes closed... eli happy1 eyes closed... eli happy1 eyes closed... eli happy1 eyes closed... "

    show eli sad1
    eli "eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... eli sad1... "

    show eli sad1 eyes closed
    eli "eli sad1 eyes closed... eli sad1 eyes closed... eli sad1 eyes closed... eli sad1 eyes closed... eli sad1 eyes closed... eli sad1 eyes closed... eli sad1 eyes closed... "

    show eli worried1
    eli "eli worried1... eli worried1... eli worried1... eli worried1... eli worried1... eli worried1... eli worried1... eli worried1... eli worried1... eli worried1... "

    show eli worried1 eyes closed
    eli "eli worried1 eyes closed... eli worried1 eyes closed... eli worried1 eyes closed... eli worried1 eyes closed... eli worried1 eyes closed... "

    show eli angry1
    eli "eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... eli angry1... "

    show eli angry1 eyes closed
    eli "eli angry1 eyes closed... eli angry1 eyes closed... eli angry1 eyes closed... eli angry1 eyes closed... eli angry1 eyes closed... eli angry1 eyes closed... "

    show eli cool1
    eli "eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... eli cool1... "

    show eli cool1 eyes closed
    eli "eli cool1 eyes closed... eli cool1 eyes closed... eli cool1 eyes closed... eli cool1 eyes closed... eli cool1 eyes closed... eli cool1 eyes closed... "

    show eli determined1
    eli "eli determined1... eli determined1... eli determined1... eli determined1... eli determined1... eli determined1... eli determined1... eli determined1... "

    show eli determined1 eyes closed
    eli "eli determined1 eyes closed... eli determined1 eyes closed... eli determined1 eyes closed... eli determined1 eyes closed... eli determined1 eyes closed... "

    hide eli
    jump letgo_000
