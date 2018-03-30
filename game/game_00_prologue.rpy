###############################
#
# MAIN MENU DEFINITIONS GO IN HERE
#
###############################

init:
    transform blinkeyes(eyes1, eyes2):
        eyes1
        choice:
            3.5
        choice:
            2.5
        choice:
            1.5
        # This randomizes the time between blinking.
        eyes2
        .25
        repeat

    transform flapmouth(mouth1, mouth2):
        mouth1
        .2
        mouth2
        .2
        repeat
    transform flip:
        xzoom -1.0
    transform centerleft:
        xpos 0.25
        ypos 0.0
        xanchor 0.5
        yalign 1.0
    transform centerright:
        xpos 0.75
        ypos 0.0
        xanchor 0.5
        yalign 1.0        


init python:
    import os
    def define_images(imageFolder, excludeFirstXFolders=0, flip=True, prepend=[]):
        for path in renpy.list_files():
            if path.startswith(imageFolder + "/"):
                path_list = path.split("/")
                if ' ' in path_list[-1]:
                    path_list = path_list[0:-1] + path_list[-1].split()
                path_list[-1] = os.path.splitext(path_list[-1])[0]
                path_list = tuple(prepend + path_list[excludeFirstXFolders:])
                renpy.image(path_list, path)
                if flip:
                    renpy.image(path_list + ("flip", ), im.Flip(path, horizontal=True))

    renpy.music.register_channel("ambience", mixer="sfx", loop=True, stop_on_mute=True, tight=True, file_prefix='', file_suffix='', buffer_queue=True, movie=False)

#     def callback_transition(event, interact=True, **kwargs):
#         if event == "begin":
#             renpy.transition(Dissolve(0.3), layer="master")
#
#     config.all_character_callbacks = [callback_transition]


    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if renpy.music.is_playing('voice') and speaking == name:
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
        speaking = name

#         if event == "show":
#             speaking = name
#         elif event == "slow_done":
#             speaking = None
#         elif event == "end":
#             speaking = None

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

    def FlapMouth(cha, mouth1, mouth2):
        mouth = flapmouth(mouth1, mouth2)
        return WhileSpeaking(cha, mouth, mouth1)

    def CSprite(cha, base, size=None, eyes=None, eyes2=None, mouth=None, mouth2=None, overlay=None):
        if size == None:
            return base
        else:
            if not eyes == None and not eyes2 == None and type(eyes) == str and type(eyes2) == str:
                eyes = blinkeyes(eyes, eyes2)
            if not mouth == None and not mouth2 == None and type(mouth) == str and type(mouth2) == str:
                mouth = FlapMouth(cha, mouth, mouth2)
            if not eyes == None and not mouth == None and not overlay == None:
                return LiveComposite(
                        size,
                        (0, 0), base,
                        (0, 0), eyes,
                        (0, 0), mouth,
                        (0, 0), overlay,
                    )
            elif not eyes == None and not mouth == None and overlay == None:
                return LiveComposite(
                        size,
                        (0, 0), base,
                        (0, 0), eyes,
                        (0, 0), mouth,
                    )
            elif not eyes == None and mouth == None and not overlay == None:
                return LiveComposite(
                        size,
                        (0, 0), base,
                        (0, 0), eyes,
                        (0, 0), overlay,
                    )
            elif eyes == None and not mouth == None and not overlay == None:
                return LiveComposite(
                        size,
                        (0, 0), base,
                        (0, 0), mouth,
                        (0, 0), overlay,
                    )
            elif not eyes == None and mouth == None and overlay == None:
                return LiveComposite(
                        size,
                        (0, 0), base,
                        (0, 0), eyes,
                    )
            elif eyes == None and not mouth == None and overlay == None:
                return LiveComposite(
                        size,
                        (0, 0), base,
                        (0, 0), mouth,
                    )
            elif eyes == None and mouth == None and not overlay == None:
                return LiveComposite(
                        size,
                        (0, 0), base,
                        (0, 0), overlay,
                    )
            else:
                return base

    class BaseCSprite:
        def __init__(self, cha, basesprite, size):
            self.cha = cha
            self.basesprite = basesprite
            self.size = size

        def __call__(self, eyes, mouth, overlay=None, eyes2=None, mouth2=None):
            return CSprite(self.cha, self.basesprite, size=self.size, eyes=eyes, eyes2=eyes2, mouth=mouth, mouth2=mouth2, overlay=overlay)


image white = "#fff"
image red = "#600"
image splashscreen_title = "gui/splashscreen_title.png"
image menu_fireplace = "gui/main_menu.png"
image fireplace = "gui/game_menu.png"
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
    $ current_story = None
    if not persistent.monologueFlag:
        jump monologue
    if 'letgo' and 'flood' and 'spirits' in persistent.storyCompletion:
        jump completeDialogue
    jump returnDialogue
        
label monologue:
    
    $ persistent.storyCompletion = set()
    
    scene menu_fireplace
    show book

    hide book with easeoutbottom

    #This monologue happens when you first load up the game, before selecting a game to play.
    "Did your parents ever read you bedtime stories? Fantasies, epics, poems? Mine never did."

    "If I were weaker, I'd blame them for everything that's happened to me so far."

    "However, I made a promise to myself and to Avitus University. I promised that I'd never blame others ever again. I'm better. I'm learning."

    "I've had quite the amount of time to think, since the incident. The jail cell, the period of uncertainty after, and the plane ride over."

    "In all of this time, you'd think that I'd be worried about my arrest, or my family, or something else entirely."

    "However, here I am, thinking about childrens' stories. Those that my parents never told me."

    "Sydney's parents, they were the ones who told me these stories."

    "Gabe and I would visit them often and listen to them all."

    "Three come to mind specifically."

    "The one about coming to terms with your future, the one about living life beyond trauma, and the one about letting go."

    "'If in Your Dreams; the Flood', 'Beyond Yesterday's Grasp', and 'Let Go.' respectively."

    "Now, how did they go again?"

    $ persistent.monologueFlag = True
    
    jump storyselect
    
label returnDialogue:
    
    scene menu_fireplace
    show book

    hide book with easeoutbottom
    
    "Now, where was I?"
    
    jump storyselect
    
label completeDialogue:
    
    scene menu_fireplace
    show book

    hide book with easeoutbottom
    
    "Time to go down memory lane again, huh?"
    
    jump storyselect

label storyselect:
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

    jump spirits_000

label start_letgo:
    scene letgo_select
    scene black with dissolve

    jump letgo_000

label start_flood:
    scene flood_select
    scene black with dissolve

    jump flood_000


###############################
#
# AFTER LOAD CONFIG FIXES
#
###############################

label after_load:
    if current_story == "letgo":
        $ config.voice_filename_format = "game_letgo/voice/{filename}"
    elif current_story == "flood":
        $ config.voice_filename_format = "{filename}"
    elif current_story == "spirits":
        $ config.voice_filename_format = "game_spirits/voice/{filename}"
    $ persistent.last_story = current_story


###############################
#
# BEFORE MAIN MENU MUSIC PLAY
#
###############################

# label before_main_menu:
#     play music "music/Cautionary Tale (INTRO).ogg" noloop fadeout 2.0
#     queue music "music/Cautionary Tale (LOOP).ogg" loop

