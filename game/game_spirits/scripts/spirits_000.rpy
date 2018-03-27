###############################
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
    $ current_story = "spirits"
    
    jump spirits_a1s0
    "SPIRITS END (remove once scripts are in)"