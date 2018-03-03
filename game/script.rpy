# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image menu_fireplace = "gui/main_menu.png"
image book = "gui/book.png"
image storyselect = "gui/storyselect.png"

###############################
#
# STORY SELECT IMAGE MAP
#
###############################

screen storyselect:
    imagemap:
        ground "gui/main_menu.png"
        idle "gui/storyselect.png"
        hover "gui/storyselect_hover.png"

        hotspot (266, 280, 500, 800) action Jump("start_letgo")
        hotspot (777, 280, 500, 800) action Jump("start_spirits")
        hotspot (1280, 280, 500, 800) action Jump("start_flood")

# The game starts here.

label start:
    scene menu_fireplace
    show book

    hide book with easeoutbottom
    scene storyselect with dissolve

    "Talky talky prologue."
    "Choose a story."

    call screen storyselect with dissolve

label start_letgo:
    scene black with dissolve
    "Let Go story chosen"
    
    return
    
label start_spirits:
    scene black with dissolve
    "Spirits story chosen"
    
    return
    
label start_flood:
    scene black with dissolve
    "Flood story chosen"
    
    return