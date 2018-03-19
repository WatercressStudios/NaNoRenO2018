###############################
#
# MAIN MENU DEFINITIONS GO IN HERE
#
###############################

init python:
    renpy.music.register_channel("ambience", mixer="sfx", loop=True, stop_on_mute=True, tight=True, file_prefix='', file_suffix='', buffer_queue=True, movie=False)
  
  
    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
  
    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)
  
    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
       
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

image white = "#fff"
image red = "#600"
image splashscreen_title = "gui/splashscreen_title.png"
image menu_fireplace = "gui/main_menu.png"
image book = "gui/book.png"
image story_menu = "gui/story_menu.png"
image spirits_select = "gui/spirits_select.png"
image letgo_select = "gui/letgo_select.png"
image flood_select = "gui/flood_select.png"

###############################
#
# STORY SELECT IMAGE MAPS
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
        ground "gui/letgo_select.png"
        idle "gui/letgo_select.png"
        hover "gui/letgo_select.png"

        hotspot (675, 142, 533, 426):
            unhovered Jump("unhovered_storyselect")
            clicked Jump("start_letgo")

screen storyselect_flood:
    tag storyselect
    imagemap:
        ground "gui/flood_select.png"
        idle "gui/flood_select.png"
        hover "gui/flood_select.png"

        hotspot (1389, 225, 408, 451):
            unhovered Jump("unhovered_storyselect")
            clicked Jump("start_flood")

###############################
#
# SPLASH SCREEN
#
###############################
label splashscreen:
    scene black
    show splashscreen_title with dissolve:
        yalign 0.0
        easein 20.0 yalign 1.0
    pause 20.0
    scene white with dissolve
    hide splashscreen_title with dissolve
    scene menu_fireplace with Dissolve(2.0)
    return   

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
    
    jump spirits_000

label start_letgo:
    scene letgo_select
    scene black with dissolve
    "Let Go story chosen"
    
    jump letgo_000
    
label start_flood:
    scene flood_select
    scene black with dissolve
    "Flood story chosen"
    
    jump flood_000
