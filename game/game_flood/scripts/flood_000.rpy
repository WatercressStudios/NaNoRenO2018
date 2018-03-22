###############################
#
# FLOOD DEFINITIONS GO IN HERE
#
###############################

define oph = Character("Ophelia")
define oli = Character("Oliver")
define dai = Character("Daisy")
define hop = Character("Hope")
define wai = Character("Waitress")
define grl = Character("Little Girl") #Hope
define vce = Character("Voice") #Hope's Dad
define dad = Character("Dad")
define mom = Character("Mom")
define sis = Character("Sister")
define ogl = Character("Other Girl")
define per = Character("Performer") #Daisy
define dsy = Character("Daisy") #idk why there are two daisy tags
define old = Character("Old Man") #Oliver
define mgr = Character("Manager")


###############################
#
# FLOOD STORY START
#
###############################

label flood_000:
    $ persistent.last_story = "flood"
    
    jump flood_101
    "FLOOD END (remove once scripts are in)"