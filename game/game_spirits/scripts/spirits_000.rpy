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
define Naniji = Character("Naniji")
define caex = Character("Hallway Boy") #Caelum
define ama = Character("Mama")
define Dad = Character("Papa")
define n = Character(None, kind=nvl)


###############################
#
# SPIRITS STORY START
#
###############################

label spirits_000:
    $ persistent.last_story = "spirits"
    
    jump spirits_a1s0
    "SPIRITS END (remove once scripts are in)"