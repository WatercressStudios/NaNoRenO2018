###############################
#
# CHEAT SHEET
#
###############################

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

define alx = Character("Alex")
define cae = Character("Caelum")
define hmom = Character("Jianmei")
define gen = Character("Genevieve")
define wra = Character("Wraith")
define caex = Character("Hallway Boy") #Caelum voice
define ama = Character("Mama")
define Dad = Character("Papa")
define n = Character(None, kind=nvl)
define cxx = Character("Caelum...?") #Caelum voice
define gez = Character("Genevieve") #Mix voiced
define gex = Character("Genevieve") #Mix voiced
define nurse = Character("Nurse")


###############################
#
# SPIRITS STORY START
#
###############################

label spirits_000:
    $ persistent.last_story = "spirits"

    jump spirits_a1s0
    "SPIRITS END (remove once scripts are in)"
