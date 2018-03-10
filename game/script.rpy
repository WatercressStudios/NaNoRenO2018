# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
image menu_fireplace = "gui/main_menu.png"
image book = "gui/book.png"
image story_menu = "gui/story_menu.png"
image spirits_select = "gui/spirits_select.png"
image letgo_select = "gui/story_menu.png"
image flood_select = "gui/story_menu.png"

###############################
#
# STORY SELECT IMAGE MAP
#
###############################

screen storyselect:
    tag storyselect
    imagemap:
        ground "gui/story_menu.png"
        idle "gui/storyselect.png"
        hover "gui/storyselect_hover.png"

        hotspot (136, 200, 389, 455):
            hovered Jump("hovered_spirits")
            clicked Jump("start_spirits")
        hotspot (675, 142, 533, 426):
            hovered Jump("hovered_letgo")
            action Jump("start_letgo")
        hotspot (1389, 225, 408, 451):
            hovered Jump("hovered_flood")
            action Jump("start_flood")

screen storyselect_spirits:
    tag storyselect
    imagemap:
        ground "gui/spirits_select.png"
        idle "gui/spirits_select.png"
        hover "gui/spirits_select.png"

        hotspot (136, 200, 389, 455):
            unhovered Jump("unhovered_storyselect")
            clicked Jump("start_spirits")

screen storyselect_letgo:
    tag storyselect
    imagemap:
        ground "gui/story_menu.png"
        idle "gui/storyselect.png"
        hover "gui/storyselect_hover.png"

        hotspot (675, 142, 533, 426):
            unhovered Jump("unhovered_storyselect")
            clicked Jump("start_letgo")

screen storyselect_flood:
    tag storyselect
    imagemap:
        ground "gui/story_menu.png"
        idle "gui/storyselect.png"
        hover "gui/storyselect_hover.png"

        hotspot (1389, 225, 408, 451):
            unhovered Jump("unhovered_storyselect")
            clicked Jump("start_flood")

###############################
#
# PROLOGUE STARTS
#
###############################
label start:
    scene menu_fireplace
    show book

    hide book with easeoutbottom

    "Talky talky prologue."
    "Choose a story."

    scene story_menu with dissolve
    jump unhovered_storyselect

label unhovered_storyselect:
    call screen storyselect with dissolve

label hovered_spirits:
    call screen storyselect_spirits with dissolve

label hovered_letgo:
    call screen storyselect_letgo with dissolve

label hovered_flood:
    call screen storyselect_flood with dissolve

###############################
#
# STORY STARTS
#
###############################
    
label start_spirits:
    scene spirits_select
    scene black with dissolve
    "Spirits story chosen"
    
    return

label start_letgo:
    scene letgo_select
    scene black with dissolve
    "Let Go story chosen"
    
    return
    
label start_flood:
    scene flood_select
    scene black with dissolve
    "Flood story chosen"
    
    return