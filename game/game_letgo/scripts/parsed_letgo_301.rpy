label letgo_301:
    #Continues directly from somewhere in 101 or 102, right after the cafe is mentioned
    #We’ll probably edit the transition later because yeah

    scene letgo clocktower eli may

    play sound "game_letgo/sfx/Clocktower 3PM.ogg"
    play ambience "game_letgo/ambience/Town Center Plaza.ogg" fadeout 0.1 fadein 0.1

    "..."

    "We've finally confessed out love for each other, and May's already shifting her feet impatiently, as if she can't wait to go."

    "What am I doing? It's freezing cold out here and I’m babbling at May like an idiot!"

    menu:
        "Let's have coffee (disabled)":
            pass
        "Don't have coffee (disabled)":
            pass
        "Let's head downtown":
            pass

    play music bgmloop2distorted_intro noloop fadeout 1.0
    queue music bgmloop2distorted_loop loop

    scene letgo townsquare2 with dissolve
    show eli normal1 at flip:
        xanchor 0.5
        yalign 1.0
        xpos 0.4
        ypos 1.03
    show may normal1 at flip:
        xanchor 0.5
        yalign 1.0
        xpos 0.6
        ypos 1.03
    with dissolve

    pause 0.5

    show may happy2 close at flip:
        linear 0.1 ypos 1.0
        linear 0.1 ypos 1.03
        linear 0.1 xpos 0.59

    voice "C-301-1.mp3" #Maya (shiena)
    may "Oh, hey! We should head to a cafe downtown!"

    show eli smile1 with dissolve

    voice "C-301-2.mp3" #Elijah (Michael Potok)
    eli "Huh?"

    voice "C-301-3.mp3" #Maya (shiena)
    may "I mean, you promised me a coffee - and it’s our first date, right? Who needs to stick around here when we can start things off with a bang!"

    "That’ll cut into my pocket a bit more than I was expecting, but I guess she has a point. And she seems pretty into the idea, too!"

    voice "C-301-4.mp3" #Elijah (Michael Potok)
    eli "Alright. Got somewhere in mind?"

    show may sad1 close at flip with dissolve

    voice "C-301-5.mp3" #Maya (shiena)
    may "Uh..."

    show may challenge1 with dissolve

    voice "C-301-6.mp3" #Maya (shiena)
    may "It’s downtown! There’s gotta be {i}something{/i} that’ll work."

    "I shrug. It’s a little strange for her to suggest something without an actual idea, but I don’t mind."

    voice "C-301-7.mp3" #Elijah (Michael Potok)
    eli "Alright, sure. Whatever y--"

    show may:
        easein 0.1 xpos 0.485
    show eli worried1

    "In a flash, she grabs my hand."

    voice "C-301-8.mp3" #Maya (shiena)
    may "Great!"

    hide may
    hide eli
    with easeoutleft

    scene black with Dissolve (1.0)

    play ambience "game_letgo/ambience/Bus Drive.ogg" fadeout 0.1 fadein 0.1

    #black screen
    #BUS NOISES

    "Without time to think, I find myself on a bus headed downtown with May."

    "Soon enough, we get to another stop. I start to stand."

    voice "C-301-9.mp3" #Maya (shiena)
    may "No, wait! Not this one!"

    voice "C-301-10.mp3" #Elijah (Michael Potok)
    eli "Huh?"

    voice "C-301-11.mp3" #Maya (shiena)
    may "There’s... a place I want to check out!"

    voice "C-301-12.mp3" #Elijah (Michael Potok)
    eli "What happened to coffee?"

    voice "C-301-13.mp3" #Maya (shiena)
    may "I came up with something better!"

    voice "C-301-14.mp3" #Elijah (Michael Potok)
    eli "You did? What is it?"

    voice "C-301-15.mp3" #Maya (shiena)
    may "..."

    voice "C-301-16.mp3" #Maya (shiena)
    may "It’s a secret."

    voice "C-301-17.mp3" #Elijah (Michael Potok)
    eli "{i}Aaaalrighty…{/i} I’ll trust you."

    voice "C-301-18.mp3" #Maya (shiena)
    may "Guaranteed to be the best date we’ve ever had!"

    "We share a quick laugh."

    "At the next stop, May stands up."

    voice "C-301-19.mp3" #Maya (shiena)
    may "Alrighty! This should be good!"

    "We exit the bus, and..."

    scene letgo downtown1

    play ambience "game_letgo/ambience/Downtown Day﻿.ogg" fadeout 0.1 fadein 0.1

    show eli smile1:
        xanchor 0.5
        yalign 1.0
        xpos 0.325
    show may normal1:
        xanchor 0.5
        yalign 1.0
        xpos 0.18

    "I crack a smile."

    voice "C-301-20.mp3" #Elijah (Michael Potok)
    eli "Oh, the hospital? Pretty out-there idea for a first date, May!"

    show may frown1 with dissolve

    voice "C-301-21.mp3" #Maya (shiena)
    may "H-Huh!?"

    voice "C-301-22.mp3" #Maya (shiena)
    may "We’re not going to the hospital!"

    show may challenge1 with dissolve

    voice "C-301-23.mp3" #Maya (shiena)
    may "We’re going somewhere... {i}close{/i} to it!"

    voice "C-301-24.mp3" #Elijah (Michael Potok)
    eli "Well, yeah. You just seemed pretty eager... Thought you could use some teasing."

    show may frown1 with dissolve

    voice "C-301-25.mp3" #Maya (shiena)
    may "O-Oh."

    show may cheeky2 with dissolve

    voice "C-301-26.mp3" #Maya (shiena)
    may "Pull that again and I might have to send you to a hospital for real."

    voice "C-301-27.mp3" #Elijah (Michael Potok)
    eli "Ha! I’d like to see you try."

    "I squeeze her hand and we start walking."

    show may:
        ease 0.8 align (1.0, 1.0) alpha 0
    show eli:
        ease 0.8 align (1.0, 1.0) alpha 0

    scene black with dissolve

    scene letgo downtown2

    show eli normal1 at flip:
        xanchor 0.5
        yalign 1.0
        xpos 0.7
    show may challenge1 at flip:
        xanchor 0.5
        yalign 1.0
        xpos 0.865
    with dissolve

    voice "C-301-28.mp3" #Maya (shiena)
    may "Ah, you aren’t so tough."

    show eli cool2 at flip with dissolve

    voice "C-301-29.mp3" #Elijah (Michael Potok)
    eli "Oh yeah?"

    show may proud2 at flip with dissolve

    voice "C-301-30.mp3" #Maya (shiena)
    may "I could get the jump on you, no problem."

    voice "C-301-31.mp3" #Elijah (Michael Potok)
    eli "Not after you’ve said that, you can’t. I’ll keep an eye out."

    show may cheeky1 close at flip with dissolve

    voice "C-301-32.mp3" #Maya (shiena)
    may "Hmm, got me there. Poison, maybe?"

    voice "C-301-33.mp3" #Elijah (Michael Potok)
    eli "I just won’t eat any food you give me."

    show may angry2 at flip with dissolve

    voice "C-301-34.mp3" #Maya (shiena)
    may "What!? {i}Never?{/i}"

    voice "C-301-35.mp3" #Elijah (Michael Potok)
    eli "Not ever."

    voice "C-301-36.mp3" #Maya (shiena)
    may "That’s gonna put a serious strain on our relationship, you know."

    voice "C-301-37.mp3" #Elijah (Michael Potok)
    eli "But threatening to send me to the hospital is fair game?"

    show may cheeky2 at flip with dissolve

    voice "C-301-38.mp3" #Maya (shiena)
    may "Ooooooh, so it’s all {i}my{/i} fault!"

    show eli smile2 close at flip with dissolve

    voice "C-301-39.mp3" #Elijah (Michael Potok)
    eli "Haha~! Kinda, yeah."

    voice "C-301-40.mp3" #Maya (shiena)
    may "God, Eli. I never took you for the kinda guy who has to win every argument!"

    show eli smile2 close at flip with dissolve

    voice "C-301-41.mp3" #Elijah (Michael Potok)
    eli "Oh, yeah. I’m a real handful."

    show may confused1 at flip with dissolve

    voice "C-301-42.mp3" #Maya (shiena)
    may "What am I gonna do with you? If you’re gonna be that way, just imagine the fires we’d start if we tried to order a pizza!"

    show eli worried2 close at flip with dissolve

    voice "C-301-43.mp3" #Elijah (Michael Potok)
    eli "Your fault for liking pineapple."

    show may adore1 at flip with dissolve

    voice "C-301-44.mp3" #Maya (shiena)
    may "Ooooh, that’s low."

    voice "C-301-45.mp3" #Elijah (Michael Potok)
    eli "You were pretty much asking for it."

    show may cheeky2 at flip with dissolve

    pause 0.05

    show may cheeky2 at flip:
        linear 0.1 xpos 0.82
        linear 0.1 xpos 0.865

    "She throws a light punch at me."

    #I am officially making it Watercress tradition that each game have a jab at pineapple pizza.
    #Even though I like pineapple pizza.

    show eli smile1 close at flip
    show may normal1 close at flip
    with dissolve

    show may:
        ease 0.8 align (0.0, 1.0) alpha 0
    show eli:
        ease 0.8 align (0.0, 1.0) alpha 0

    scene black with dissolve

    "We have a good laugh about it and make our way onward, toward May’s supposed plan."

    scene letgo city nearby sunset with dissolve
    play ambience "game_letgo/ambience/Near Downtown Bridge Night.ogg" fadeout 0.1 fadein 0.1

    jump letgo_302
