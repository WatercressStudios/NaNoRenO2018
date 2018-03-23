###############################
#
# CHEAT SHEET
#
###############################

### show eli ###

# normal1
# smile1
# happy1
# sad1
# worried1
# angry1
# cool1
# goofy1

# normal2
# smile2
# sad2
# worried2
# angry2
# cool2


### show may ###

# normal1
# frown1
# adore1
# confused1
# aww1
# worried1
# sad1
# challenge1
# cheeky1
# angry1
# shout1
# sadshout1
# forcedsmile1
# suspicious1

# normal2
# happy2
# worried2
# nervous2
# aww2
# sheepish2
# angry2
# frustrated2
# proud2
# cheeky2

# normal3
# smile3
# forcedsmile3
# happy3
# sigh3
# sad3
# tired3
# angry3
# proud3
# frustrated3

# normal4
# smile4
# forcedsmile4
# sad4
# angry4
# frustrated4


### scene background ###

# city nearby sunset
# city outlook night
# downtown bridge night
# downtown cafe inside
# downtown cafe outside
# downtown nice night
# downtown night
# downtown1
# downtown2
# lights1 night
# lights2 night
# mall escalator
# mall1
# mall2
# park hill night
# park lake
# park lake path
# park lake sunset
# park podium
# park road
# park road night
# park swing
# park trees sunset
# road long
# road night
# suburb house
# suburb night
# suburb1
# suburb2
# suburb3
# town night
# townsquare cafe inside
# townsquare cafe outside
# townsquare night
# townsquare1
# townsquare2


### play music ###

# play music bgmloop3comedy_intro noloop fadeout 1.0
# queue music bgmloop3comedy_loop loop
# play music bgmloop4reveal fadeout 1.0
# play music bgmloop5kite fadeout 1.0
# play music bgmloop5bye_intro noloop fadeout 1.0
# queue music bgmloop5bye_loop loop


### play ambience ###

# play ambience "game_letgo/ambience/Bus Drive.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Cafe.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Downtown Day.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Downtown Night.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Mall.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Near Downtown Bridge Night.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Outlook Night.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Park Day.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Park Night.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Roads Night.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Suburban Houses.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Town Center Plaza.ogg" fadeout 2.0 fadein 2.0
# play ambience "game_letgo/ambience/Town Center Plaza Night.ogg" fadeout 2.0 fadein 2.0


### play sound ###

# play sound "game_letgo/sfx/Car Screeching.ogg"
# play sound "game_letgo/sfx/Climbing up Stairs.ogg"
# play sound "game_letgo/sfx/Clocktower 3PM.ogg"
# play sound "game_letgo/sfx/Clothes Shuffle.ogg"
# play sound "game_letgo/sfx/Crush.ogg"
# play sound "game_letgo/sfx/Disturbing Bass.ogg"
# play sound "game_letgo/sfx/Ice Slip.ogg"
# play sound "game_letgo/sfx/Kettle Rustle.ogg"
# play sound "game_letgo/sfx/Key fumble,open door.ogg"
# play sound "game_letgo/sfx/Manhole Thud.ogg"
# play sound "game_letgo/sfx/May Eli Run.ogg"
# play sound "game_letgo/sfx/Piano Crash.ogg"
# play sound "game_letgo/sfx/Pouring Two Cups of Tea.ogg"
# play sound "game_letgo/sfx/Punch,Shove Serious.ogg"
# play sound "game_letgo/sfx/Punch,Shove.ogg"
# play sound "game_letgo/sfx/Rope Snap.ogg"
# play sound "game_letgo/sfx/Sirens.ogg"
# play sound "game_letgo/sfx/Snow Footsteps.ogg"
# play sound "game_letgo/sfx/Snowball.ogg"
# play sound "game_letgo/sfx/Tumbling Down.ogg"
# play sound "game_letgo/sfx/Wind Gust.ogg"


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

define bgmloop3comedy_intro = "game_letgo/music/A Macabre Comedy Intro.ogg"
define bgmloop3comedy_loop = "game_letgo/music/A Macabre Comedy Loop.ogg"
define bgmloop4reveal = "game_letgo/music/The Truth.ogg"
define bgmloop5kite = "game_letgo/music/Soaring.ogg"
define bgmloop5bye_intro = "game_letgo/music/This is Goodbye Intro.ogg"
define bgmloop5bye_loop = "game_letgo/music/This is Goodbye Loop.ogg"


init python:
    define_images("game_letgo/bgs", 2, False, ["letgo"])

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

image may normal2 = MayPose2("may eyes normal2", "may mouth normal2")
image may normal2 close = MayPose2("game_letgo/sprites/May/Pose 2/eyes normal close.png", "may mouth normal2")

image may happy2 = MayPose2("may eyes happy2", "may mouth happy2")
image may happy2 close = MayPose2("game_letgo/sprites/May/Pose 2/eyes normal close 2.png", "may mouth happy2")

image may worried2 = MayPose2("may eyes worried2", "may mouth displeased2")
image may worried2 close = MayPose2("game_letgo/sprites/May/Pose 2/eyes worried close.png", "may mouth displeased2")

image may nervous2 = MayPose2("may eyes worried2", "may mouth normal2")
image may nervous2 close = MayPose2("game_letgo/sprites/May/Pose 2/eyes worried close.png", "may mouth normal2")

image may aww2 = MayPose2("may eyes worried2", "may mouth happy2")
image may aww2 close = MayPose2("game_letgo/sprites/May/Pose 2/eyes worried close.png", "may mouth happy2")

image may sheepish2 = MayPose2("may eyes sheepish2", "may mouth happy2")
image may sheepish2 close = MayPose2("game_letgo/sprites/May/Pose 2/eyes worried close 2.png", "may mouth happy2")

image may angry2 = MayPose2("may eyes angry2", "may mouth displeased2")
image may angry2 close = MayPose2("game_letgo/sprites/May/Pose 2/eyes angry close.png", "may mouth displeased2")

image may frustrated2 = MayPose2("may eyes frustrated2", "may mouth displeased2")
image may frustrated2 close = MayPose2("game_letgo/sprites/May/Pose 2/eyes angry close 2.png", "may mouth displeased2")

image may proud2 = MayPose2("may eyes angry2", "may mouth happy2")
image may proud2 close = MayPose2("game_letgo/sprites/May/Pose 2/eyes angry close.png", "may mouth happy2")

image may cheeky2 = MayPose2("may eyes frustrated2", "may mouth happy2")
image may cheeky2 close = MayPose2("game_letgo/sprites/May/Pose 2/eyes angry close 2.png", "may mouth happy2")

###############################
#
# MAY POSE 3 SPRITES
#
###############################

init python:
    MayPose3 = BaseCSprite("may", "game_letgo/sprites/May/Pose 3/base.png", (416, 906))

image may normal3 = MayPose3("may eyes normalaway3", "may mouth normal3")
image may normal3 close = MayPose3("game_letgo/sprites/May/Pose 3/eyes normal close.png", "may mouth normal3")

image may smile3 = MayPose3("may eyes frown3", "may mouth smile3")
image may smile3 close = MayPose3("game_letgo/sprites/May/Pose 3/eyes frown close.png", "may mouth smile3")

image may forcedsmile3 = MayPose3("may eyes frownaway3", "may mouth smile3")
image may forcedsmile3 close = MayPose3("game_letgo/sprites/May/Pose 3/eyes frown close.png", "may mouth smile3")

image may happy3 = MayPose3("may eyes normal3", "may mouth smile3")
image may happy3 close = MayPose3("game_letgo/sprites/May/Pose 3/eyes normal close.png", "may mouth smile3")

image may sigh3 = MayPose3("may eyes normalaway3", "may mouth smile3")
image may sigh3 close = MayPose3("game_letgo/sprites/May/Pose 3/eyes normal close.png", "may mouth smile3")

image may sad3 = MayPose3("may eyes frown3", "may mouth sad3")
image may sad3 close = MayPose3("game_letgo/sprites/May/Pose 3/eyes frown close.png", "may mouth sad3")

image may tired3 = MayPose3("may eyes frownaway3", "may mouth normal3")
image may tired3 close = MayPose3("game_letgo/sprites/May/Pose 3/eyes frown close.png", "may mouth normal3")

image may angry3 = MayPose3("may eyes angry3", "may mouth sad3")
image may angry3 close = MayPose3("game_letgo/sprites/May/Pose 3/eyes angry close.png", "may mouth sad3")

image may frustrated3 = MayPose3("may eyes angryaway3", "may mouth sad3")
image may frustrated3 close = MayPose3("game_letgo/sprites/May/Pose 3/eyes angry close.png", "may mouth sad3")



###############################
#
# MAY POSE 4 SPRITES
#
###############################

init python:
    MayPose4 = BaseCSprite("may", "game_letgo/sprites/May/Pose 4/base.png", (507, 930))

image may normal4 = MayPose4("may eyes frown4", "may mouth normal4")
image may normal4 close = MayPose4("game_letgo/sprites/May/Pose 4/eyes frown close.png", "may mouth normal4")

image may smile4 = MayPose4("may eyes frown4", "may mouth smile4")
image may smile4 close = MayPose4("game_letgo/sprites/May/Pose 4/eyes frown close.png", "may mouth smile4")

image may forcedsmile4 = MayPose4("may eyes frownaway4", "may mouth smile4")
image may forcedsmile4 close = MayPose4("game_letgo/sprites/May/Pose 4/eyes frown close.png", "may mouth smile4")

image may sad4 = MayPose4("may eyes frownaway4", "may mouth normal4")
image may sad4 close = MayPose4("game_letgo/sprites/May/Pose 4/eyes frown close.png", "may mouth normal4")

image may angry4 = MayPose4("may eyes angry4", "may mouth normal4")
image may angry4 close = MayPose4("game_letgo/sprites/May/Pose 4/eyes angry close.png", "may mouth normal4")

image may frustrated4 = MayPose4("may eyes angryaway4", "may mouth normal4")
image may frustrated4 close = MayPose4("game_letgo/sprites/May/Pose 4/eyes angry close.png", "may mouth normal4")


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
# MAYA POSE 2 COMPOSITE PARTS
#
###############################

image may eyes normal2 = blinkeyes("game_letgo/sprites/May/Pose 2/eyes normal open.png", "game_letgo/sprites/May/Pose 2/eyes normal close.png")

image may eyes happy2 = blinkeyes("game_letgo/sprites/May/Pose 2/eyes normal open.png", "game_letgo/sprites/May/Pose 2/eyes normal close 2.png")

image may eyes worried2 = blinkeyes("game_letgo/sprites/May/Pose 2/eyes worried open.png", "game_letgo/sprites/May/Pose 2/eyes worried close.png")

image may eyes sheepish2 = blinkeyes("game_letgo/sprites/May/Pose 2/eyes worried open.png", "game_letgo/sprites/May/Pose 2/eyes worried close 2.png")

image may eyes angry2 = blinkeyes("game_letgo/sprites/May/Pose 2/eyes angry open.png", "game_letgo/sprites/May/Pose 2/eyes angry close.png")

image may eyes frustrated2 = blinkeyes("game_letgo/sprites/May/Pose 2/eyes angry open.png", "game_letgo/sprites/May/Pose 2/eyes angry close 2.png")

image may mouth normal2 = FlapMouth("may", "game_letgo/sprites/May/Pose 2/mouth smile close.png", "game_letgo/sprites/May/Pose 2/mouth small open.png")

image may mouth happy2 = FlapMouth("may", "game_letgo/sprites/May/Pose 2/mouth smile close.png", "game_letgo/sprites/May/Pose 2/mouth big open.png")

image may mouth displeased2 = FlapMouth("may", "game_letgo/sprites/May/Pose 2/mouth frown close.png", "game_letgo/sprites/May/Pose 2/mouth small open.png")

###############################
#
# MAYA POSE 3 COMPOSITE PARTS
#
###############################

image may eyes normal3 = blinkeyes("game_letgo/sprites/May/Pose 3/eyes normal open.png", "game_letgo/sprites/May/Pose 3/eyes normal close.png")

image may eyes normalaway3 = blinkeyes("game_letgo/sprites/May/Pose 3/eyes normal away.png", "game_letgo/sprites/May/Pose 3/eyes normal close.png")

image may eyes frown3 = blinkeyes("game_letgo/sprites/May/Pose 3/eyes frown open.png", "game_letgo/sprites/May/Pose 3/eyes frown close.png")

image may eyes frownaway3 = blinkeyes("game_letgo/sprites/May/Pose 3/eyes frown away.png", "game_letgo/sprites/May/Pose 3/eyes frown close.png")

image may eyes angry3 = blinkeyes("game_letgo/sprites/May/Pose 3/eyes angry open.png", "game_letgo/sprites/May/Pose 3/eyes angry close.png")

image may eyes angryaway3 = blinkeyes("game_letgo/sprites/May/Pose 3/eyes angry away.png", "game_letgo/sprites/May/Pose 3/eyes angry close.png")

image may mouth normal3 = FlapMouth("may", "game_letgo/sprites/May/Pose 3/mouth normal close.png", "game_letgo/sprites/May/Pose 3/mouth open.png")

image may mouth smile3 = FlapMouth("may", "game_letgo/sprites/May/Pose 3/mouth smile close.png", "game_letgo/sprites/May/Pose 3/mouth open.png")

image may mouth sad3 = FlapMouth("may", "game_letgo/sprites/May/Pose 3/mouth open.png", "game_letgo/sprites/May/Pose 3/mouth normal close.png")


###############################
#
# MAYA POSE 4 COMPOSITE PARTS
#
###############################

image may eyes frown4 = blinkeyes("game_letgo/sprites/May/Pose 4/eyes frown open.png", "game_letgo/sprites/May/Pose 4/eyes frown close.png")

image may eyes frownaway4 = blinkeyes("game_letgo/sprites/May/Pose 4/eyes frown away.png", "game_letgo/sprites/May/Pose 4/eyes frown close.png")

image may eyes angry4 = blinkeyes("game_letgo/sprites/May/Pose 4/eyes angry open.png", "game_letgo/sprites/May/Pose 4/eyes angry close.png")

image may eyes angryaway4 = blinkeyes("game_letgo/sprites/May/Pose 4/eyes angry away.png", "game_letgo/sprites/May/Pose 4/eyes angry close.png")

image may mouth normal4 = FlapMouth("may", "game_letgo/sprites/May/Pose 4/mouth normal close.png", "game_letgo/sprites/May/Pose 4/mouth open.png")

image may mouth smile4 = FlapMouth("may", "game_letgo/sprites/May/Pose 4/mouth smile close.png", "game_letgo/sprites/May/Pose 4/mouth open.png")


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
    
    show may normal2
    may "may normal2... may normal2... may normal2... may normal2... may normal2... may normal2... may normal2... may normal2... may normal2..."

    show may normal2 close
    may "may normal2 close... may normal2 close... may normal2 close... may normal2 close... may normal2 close... may normal2 close..."

    show may happy2
    may "may happy2... may happy2... may happy2... may happy2... may happy2... may happy2... may happy2... may happy2... may happy2... may happy2... may happy2..."

    show may happy2 close
    may "may happy2 close... may happy2 close... may happy2 close... may happy2 close... may happy2 close... may happy2 close... may happy2 close... may happy2 close..."

    show may worried2
    may "may worried2... may worried2... may worried2... may worried2... may worried2... may worried2... may worried2... may worried2... may worried2..."

    show may worried2 close
    may "may worried2 close... may worried2 close... may worried2 close... may worried2 close... may worried2 close... may worried2 close... may worried2 close..."

    show may nervous2
    may "may nervous2... may nervous2... may nervous2... may nervous2... may nervous2... may nervous2... may nervous2... may nervous2... may nervous2..."

    show may nervous2 close
    may "may nervous2 close... may nervous2 close... may nervous2 close... may nervous2 close... may nervous2 close... may nervous2 close... may nervous2 close..."

    show may aww2
    may "may aww2... may aww2... may aww2... may aww2... may aww2... may aww2... may aww2..."

    show may aww2 close
    may "may aww2 close... may aww2 close... may aww2 close... may aww2 close... may aww2 close... may aww2 close..."

    show may sheepish2
    may "may sheepish2... may sheepish2... may sheepish2... may sheepish2... may sheepish2... may sheepish2... may sheepish2... may sheepish2... may sheepish2..."

    show may sheepish2 close
    may "may sheepish2 close... may sheepish2 close... may sheepish2 close... may sheepish2 close... may sheepish2 close... may sheepish2 close..."

    show may angry2
    may "may angry2... may angry2... may angry2... may angry2... may angry2... may angry2... may angry2... may angry2... may angry2... may angry2... may angry2..."

    show may angry2 close
    may "may angry2 close... may angry2 close... may angry2 close... may angry2 close... may angry2 close... may angry2 close... may angry2 close... may angry2 close..."

    show may frustrated2
    may "may frustrated2... may frustrated2... may frustrated2... may frustrated2... may frustrated2... may frustrated2... may frustrated2... may frustrated2..."

    show may frustrated2 close
    may "may frustrated2 close... may frustrated2 close... may frustrated2 close... may frustrated2 close... may frustrated2 close... may frustrated2 close..."

    show may proud2
    may "may proud2... may proud2... may proud2... may proud2... may proud2... may proud2... may proud2... may proud2..."

    show may proud2 close
    may "may proud2 close... may proud2 close... may proud2 close... may proud2 close... may proud2 close... may proud2 close..."

    show may cheeky2
    may "may cheeky2... may cheeky2... may cheeky2... may cheeky2... may cheeky2... may cheeky2... may cheeky2... may cheeky2..."

    show may cheeky2 close
    may "may cheeky2 close... may cheeky2 close... may cheeky2 close... may cheeky2 close... may cheeky2 close... may cheeky2 close..."

    show may normal3
    may "may normal3... may normal3... may normal3... may normal3... may normal3... may normal3... may normal3... may normal3... may normal3... may normal3... may normal3... "

    show may normal3 close
    may "may normal3 close... may normal3 close... may normal3 close... may normal3 close... may normal3 close... may normal3 close... may normal3 close... "

    show may smile3
    may "may smile3... may smile3... may smile3... may smile3... may smile3... may smile3... may smile3... may smile3... may smile3... may smile3... may smile3... "

    show may smile3 close
    may "may smile3 close... may smile3 close... may smile3 close... may smile3 close... may smile3 close... may smile3 close... may smile3 close... may smile3 close... "

    show may forcedsmile3
    may "may forcedsmile3... may forcedsmile3... may forcedsmile3... may forcedsmile3... may forcedsmile3... may forcedsmile3... may forcedsmile3... may forcedsmile3... "

    show may forcedsmile3 close
    may "may forcedsmile3 close... may forcedsmile3 close... may forcedsmile3 close... may forcedsmile3 close... may forcedsmile3 close... may forcedsmile3 close... "

    show may happy3
    may "may happy3... may happy3... may happy3... may happy3... may happy3... may happy3... may happy3... may happy3... may happy3... may happy3... may happy3... "

    show may happy3 close
    may "may happy3 close... may happy3 close... may happy3 close... may happy3 close... may happy3 close... may happy3 close... may happy3 close... may happy3 close... "

    show may sigh3
    may "may sigh3... may sigh3... may sigh3... may sigh3... may sigh3... may sigh3... may sigh3... may sigh3... may sigh3... may sigh3... may sigh3... may sigh3... may sigh3... "

    show may sigh3 close
    may "may sigh3 close... may sigh3 close... may sigh3 close... may sigh3 close... may sigh3 close... may sigh3 close... may sigh3 close... may sigh3 close... "

    show may sad3
    may "may sad3... may sad3... may sad3... may sad3... may sad3... may sad3... may sad3... may sad3... may sad3... may sad3... may sad3... may sad3... may sad3... "

    show may sad3 close
    may "may sad3 close... may sad3 close... may sad3 close... may sad3 close... may sad3 close... may sad3 close... may sad3 close... may sad3 close... may sad3 close... "

    show may tired3
    may "may tired3... may tired3... may tired3... may tired3... may tired3... may tired3... may tired3... may tired3... may tired3... may tired3... may tired3... "

    show may tired3 close
    may "may tired3 close... may tired3 close... may tired3 close... may tired3 close... may tired3 close... may tired3 close... may tired3 close... may tired3 close... "

    show may angry3
    may "may angry3... may angry3... may angry3... may angry3... may angry3... may angry3... may angry3... may angry3... may angry3... may angry3... may angry3... "

    show may angry3 close
    may "may angry3 close... may angry3 close... may angry3 close... may angry3 close... may angry3 close... may angry3 close... may angry3 close... may angry3 close... "

    show may frustrated3
    may "may frustrated3... may frustrated3... may frustrated3... may frustrated3... may frustrated3... may frustrated3... may frustrated3... may frustrated3... "

    show may frustrated3 close
    may "may frustrated3 close... may frustrated3 close... may frustrated3 close... may frustrated3 close... may frustrated3 close... may frustrated3 close... "

    show may normal4
    may "may normal4... may normal4... may normal4... may normal4... may normal4... may normal4... may normal4... may normal4... may normal4... may normal4... may normal4... "

    show may normal4 close
    may "may normal4 close... may normal4 close... may normal4 close... may normal4 close... may normal4 close... may normal4 close... may normal4 close... "

    show may smile4
    may "may smile4... may smile4... may smile4... may smile4... may smile4... may smile4... may smile4... may smile4... may smile4... may smile4... may smile4... "

    show may smile4 close
    may "may smile4 close... may smile4 close... may smile4 close... may smile4 close... may smile4 close... may smile4 close... may smile4 close... may smile4 close... "

    show may forcedsmile4
    may "may forcedsmile4... may forcedsmile4... may forcedsmile4... may forcedsmile4... may forcedsmile4... may forcedsmile4... may forcedsmile4... may forcedsmile4... "

    show may forcedsmile4 close
    may "may forcedsmile4 close... may forcedsmile4 close... may forcedsmile4 close... may forcedsmile4 close... may forcedsmile4 close... may forcedsmile4 close... "

    show may sad4
    may "may sad4... may sad4... may sad4... may sad4... may sad4... may sad4... may sad4... may sad4... may sad4... may sad4... may sad4... may sad4... may sad4... "

    show may sad4 close
    may "may sad4 close... may sad4 close... may sad4 close... may sad4 close... may sad4 close... may sad4 close... may sad4 close... may sad4 close... may sad4 close... "

    show may angry4
    may "may angry4... may angry4... may angry4... may angry4... may angry4... may angry4... may angry4... may angry4... may angry4... may angry4... may angry4... "

    show may angry4 close
    may "may angry4 close... may angry4 close... may angry4 close... may angry4 close... may angry4 close... may angry4 close... may angry4 close... may angry4 close... "

    show may frustrated4
    may "may frustrated4... may frustrated4... may frustrated4... may frustrated4... may frustrated4... may frustrated4... may frustrated4... may frustrated4... "

    show may frustrated4 close
    may "may frustrated4 close... may frustrated4 close... may frustrated4 close... may frustrated4 close... may frustrated4 close... may frustrated4 close... "

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
