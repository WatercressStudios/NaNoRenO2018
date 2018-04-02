label letgo_302:
    #Rewind point

    "While we’re crossing the river, she stops."

    show may normal1 at flip:
        xanchor 0.5
        yalign 1.0
        xpos 0.5
    with easeinleft

    voice "C-302-1.mp3" #Maya (shiena)
    may "Alright! We’re here!"

    show eli normal1 at flip behind may:
        xanchor 0.5
        yalign 1.0
        xpos 0.3
    with easeinleft

    voice "C-302-2.mp3" #Elijah (Michael Potok)
    eli "Huh. I was expecting something a little more... indoors?"

    show may worried1 with dissolve

    voice "C-302-3.mp3" #Maya (shiena)
    may "Y-Yeeeaaah, wellll... The outdoors is free! Gotta spare a dime wherever we can, right?"

    voice "C-302-4.mp3" #Elijah (Michael Potok)
    eli "Mhm."

    show eli cool1 with dissolve

    "I grin at her."

    voice "C-302-5.mp3" #Elijah (Michael Potok)
    eli "So your idea of \"starting the relationship off with a bang\" is to go downtown and try not to spend money?"

    show may frustrated2 with dissolve

    voice "C-302-6.mp3" #Maya (shiena)
    may "That’s--!"

    "I wave my hand."

    show eli smile1 close with dissolve

    voice "C-302-7.mp3" #Elijah (Michael Potok)
    eli "Just teasing again. This is a great spot!"

    show eli smile1 with dissolve

    voice "C-302-8.mp3" #Elijah (Michael Potok)
    eli "Fresh air - well, fresh as you can get around here, anyway... And the view is amazing!"

    show may worried1 with dissolve

    voice "C-302-9.mp3" #Maya (shiena)
    may "R-Right."

    show eli:
        xpos 0.8
    with ease

    #hide may    
    show may worried1:
        xanchor 0.5
        yalign 1.0
        xpos 0.5
    with dissolve

    "I head to the side of the bridge and lean forward on the guard rail. It’s a little low for me, but I manage by stooping a bit. May follows next to me."

    "..."

    voice "C-302-10.mp3" #Elijah (Michael Potok)
    eli "Hey. Mind if I ask you something?"

    voice "C-302-11.mp3" #Maya (shiena)
    may "You’re asking me something already, right?"

    voice "C-302-12.mp3" #Elijah (Michael Potok)
    eli "Right, it’s just..."

    voice "C-302-13.mp3" #Elijah (Michael Potok)
    eli "Is something bothering you?"

    voice "C-302-14.mp3" #Maya (shiena)
    may "Huh?"

    voice "C-302-15.mp3" #Elijah (Michael Potok)
    eli "You’ve just been a little off today - and, well... If anything’s wrong, I want you to know I’ll be there for you."

    show may worried2 with dissolve

    voice "C-302-16.mp3" #Maya (shiena)
    may "..."

    show may happy2 close with dissolve

    voice "C-302-17.mp3" #Maya (shiena)
    may "You’re such a cheese ball!"

    voice "C-302-18.mp3" #Maya (shiena)
    may "I’m acting strange? Of {i}course{/i} I am, Eli! It’s our first date!"

    voice "C-302-19.mp3" #Maya (shiena)
    may "It’d be wrong if I {i}wasn’t.{/i}"

    voice "C-302-20.mp3" #Elijah (Michael Potok)
    eli "Butterflies, huh?"

    "I smile at her."

    voice "C-302-21.mp3" #Elijah (Michael Potok)
    eli "Alright. Well if something’s ever wrong, I just want you to know we can talk about it."

    voice "C-302-22.mp3" #Maya (shiena)
    may "You don’t say? C’mon, Eli, that’s Relationships 101!"

    voice "C-302-23.mp3" #Elijah (Michael Potok)
    eli "Ha. Yeah, you’re right. I’m worried about n--"

    stop music fadeout 0.1

    play sound "game_letgo/sfx/Punch,Shove Serious.ogg"

    show may angry1
    show eli worried1:
        ease 0.8 align (1.0, 1.0) alpha 0
    with hpunch

    "After suddenly being shoved by a rushing passerby, I find myself tumbling over the bar! With the river frozen over like that, I..."

    #do... something with the UI to represent the fact that our pov character is currently falling off a bridge

    voice "C-302-24.mp3" #Maya (shiena)
    may "Aah!"

    show may sadshout1:
        easein 0.2 xpos 0.8

    pause 0.5

    play sound "game_letgo/sfx/Crush.ogg"
    #horrible crushing sound

    scene black with Dissolve(1.0)

    voice "C-302-25.mp3" #Maya (shiena)
    may "Are you {i}kidding{/i} me!?"

    play sound "game_letgo/sfx/Disturbing Bass Short.ogg"
    scene letgo rewind with dissolve

    #Do the um... The rewind thing. I have no idea how we’re coding this. The rewind point is to the start of 302.

    scene letgo city nearby sunset with dissolve

    play music bgmloop3comedy_intro noloop fadeout 1.0
    queue music bgmloop3comedy_loop loop

    "We have a good laugh about it and make our way onward, toward May’s supposed plan."

    "She’s been pretty secretive about this. Where are we even going?"

    #####

    menu:

        "Stay at the bridge. (disabled)":
            jump letgo_302

        "Onward!":
            jump letgo_302softdrink

    ###

label letgo_302softdrink:


    "We keep moving along."


    play ambience "game_letgo/ambience/Downtown Night.ogg" fadeout 0.1 fadein 0.1
    scene letgo downtown bridge night

    show may worried1:
        xanchor 0.5
        yalign 1.0
        xpos 0.4
    show eli normal1:
        xanchor 0.5
        yalign 1.0
        xpos 0.6

    with dissolve

    voice "C-302-26.mp3" #Elijah (Michael Potok)
    eli "We getting any closer?"

    "..."

    voice "C-302-27.mp3" #Elijah (Michael Potok)
    eli "May?"

    voice "C-302-28.mp3" #Maya (shiena)
    may "Yeah."

    show eli worried2 with dissolve

    "Oof."

    "She’s getting a little hard to talk to."

    show eli cool1 with dissolve

    voice "C-302-29.mp3" #Elijah (Michael Potok)
    eli "Hey. Wanna hear a joke?"

    show may sad1 with dissolve

    voice "C-302-30.mp3" #Maya (shiena)
    may "Huh?"

    voice "C-302-31.mp3" #Elijah (Michael Potok)
    eli "A joke. You wanna hear one?"

    voice "C-302-32.mp3" #Maya (shiena)
    may "That’s..."

    show may happy2 close with dissolve

    voice "C-302-33.mp3" #Maya (shiena)
    may "Sure."

    "...Crap."

    "I don’t actually have any."

    "But it’ll be fine! May has a very... lenient sense of humor."

    voice "C-302-34.mp3" #Elijah (Michael Potok)
    eli "Did you ever hear the joke about the snakes?"

    voice "C-302-35.mp3" #Maya (shiena)
    may "Nope!"

    voice "C-302-36.mp3" #Elijah (Michael Potok)
    eli "It was..."

    show may cheeky1 with dissolve

    voice "C-302-37.mp3" #Maya (shiena)
    may "You’re not {i}really{/i} gonna say \"hiss-terical,\" are you?"

    "Whoops."

    "So much for lenient."

    show eli normal2 close with dissolve

    voice "C-302-38.mp3" #Elijah (Michael Potok)
    eli "No way! That’s way too corny."

    voice "C-302-39.mp3" #Maya (shiena)
    may "Phew. Had me worried there for a second!"

    "..."

    voice "C-302-40.mp3" #Maya (shiena)
    may "So..."

    show may cheeky2 with dissolve

    voice "C-302-41.mp3" #Maya (shiena)
    may "What {i}were{/i} you gonna say?"

    voice "C-302-42.mp3" #Elijah (Michael Potok)
    eli "Oh, you know. Something... snakey."

    show may forcedsmile1 with dissolve

    voice "C-302-43.mp3" #Maya (shiena)
    may "Uh-huh."

    scene black with wiperight

    pause 0.5

    scene letgo downtown night
    show may worried1 at flip:
        xanchor 0.5
        yalign 1.0
        xpos 0.4
        ypos 1.03
    show eli normal1 at flip behind may:
        xanchor 0.5
        yalign 1.0
        xpos 0.25
        ypos 1.03
    with wiperight

    "I couldn’t quite keep up the conversation as we made our way into a more crowded part of the city."

    voice "C-302-44.mp3" #Elijah (Michael Potok)
    eli "Lotta people out tonight."

    voice "C-302-45.mp3" #Maya (shiena)
    may "Yep."

    "Aaaand shot down again."

    voice "C-302-46.mp3" #Elijah (Michael Potok)
    eli "May, listen, I--"

    #sfx thud

    #If there’s some trend we do with deaths (blackouts, cutting music, etc), do it here

    stop ambience
    play sound "game_letgo/sfx/Punch,Shove Serious.ogg"

    show eli sad1:
        linear 0.1 ypos 1.0
        linear 0.1 ypos 1.03
        linear 0.1 xpos 0.2
    with hpunch
    hide eli with easeoutbottom

    show may sadshout1 at flip:
        easein 0.2 xpos 0.35

    "Suddenly, someone runs into me!"

    "I fall backwards onto the sidewalk and feel a cold, wet sensation on my chest."

    voice "C-302-47.mp3" #Maya (shiena)
    may "Eli!"

    play ambience "game_letgo/ambience/Downtown Night.ogg" fadeout 0.1 fadein 0.1
    #If the music changed, change it back

    "Seems he spilled soda on me."

    show eli worried1 at flip:
        xanchor 0.5
        yalign 1.0
        xpos 0.20
        ypos 1.03
    with easeinbottom

    "With an apology, he helps me up."

    "He explains himself being in a rush, apologizing again."

    "He hands me five dollars and runs off into the distance."

    voice "C-302-48.mp3" #Elijah (Michael Potok)
    eli "Phew. That was weird."

    #rewind point

    show may worried1 close with dissolve

    #should be voiced as deep breathing, or something to that effect
    voice "C-302-49.mp3" #Maya (shiena)
    may "..."

    voice "C-302-50.mp3" #Elijah (Michael Potok)
    eli "May?"

    show may angry1 with dissolve

    voice "C-302-51.mp3" #Maya (shiena)
    may "God dammit..."

    voice "C-302-52.mp3" #Elijah (Michael Potok)
    eli "May!"

    voice "C-302-53.mp3" #Maya (shiena)
    may "Huh?"

    show eli smile2 with dissolve

    "I smile at her."

    #Choice will go here on the second loop

    jump letgo_302escalator

    ###

label letgo_302escalator:

    voice "C-302-54.mp3" #Elijah (Michael Potok)
    eli "I’m fine. Let’s keep going, alright?"

    show may worried1 with dissolve

    voice "C-302-55.mp3" #Maya (shiena)
    may "Y-Yeah..."

    voice "C-302-56.mp3" #Elijah (Michael Potok)
    eli "We should find a place for me to wash up. How about in there?"

    voice "C-302-57.mp3" #Maya (shiena)
    may "Sure."

    scene letgo mall2
    play ambience "game_letgo/ambience/Mall.ogg" fadeout 0.1 fadein 0.1

    show may worried1 at flip:
        xanchor 0.5
        yalign 1.0
        xpos 0.7
        ypos 1.15
    show eli normal1 at flip behind may:
        xanchor 0.5
        yalign 1.0
        xpos 0.5
        ypos 1.15
    with dissolve

    #escalator should be in the background

    voice "C-302-58.mp3" #Elijah (Michael Potok)
    eli "Think I see a bathroom on the second floor."

    "I head toward the escalator."

    show may angry2 at flip:
        linear 0.1 ypos 1.10
        linear 0.1 ypos 1.15

    voice "C-302-59.mp3" #Maya (shiena)
    may "No!"

    show eli worried2 at flip with dissolve

    voice "C-302-60.mp3" #Elijah (Michael Potok)
    eli "Huh?"

    show may aww1 at flip with dissolve

    voice "C-302-61a.mp3" #Maya (shiena)
    may "I mean--"
    voice "C-302-61b.mp3" #Maya (shiena)
    may "Escalators... promote obesity! We should find some stairs and get some cardio!"

    voice "C-302-62.mp3" #Elijah (Michael Potok)
    eli "Haha, what?"

    voice "C-302-63.mp3" #Elijah (Michael Potok)
    eli "May, don’t tell me you’re afraid of escalators."

    show may aww1 close at flip with dissolve

    voice "C-302-64.mp3" #Maya (shiena)
    may "What? No, that’s--"

    voice "C-302-65.mp3" #Elijah (Michael Potok)
    eli "They make these as safe as they can. It’ll be fine!"

    show eli:
        xpos 0.62
    with ease

    pause 0.25

    show eli:
        xpos 0.1
    show may worried1:
        xpos 0.25
    with ease

    "I grab her hand and head over to it."

    voice "C-302-66.mp3" #Maya (shiena)
    may "R-Right."

    "...Hm."

    voice "C-302-67.mp3" #Elijah (Michael Potok)
    eli "Hey. Mind if I ask you something?"

    voice "C-302-68.mp3" #Maya (shiena)
    may "Hmm?"

    voice "C-302-69.mp3" #Elijah (Michael Potok)
    eli "Is something bothering you?"

    show may angry2

    voice "C-302-70.mp3" #Maya (shiena)
    may "N-No. I’m totally fine!"

    show may:
        ease 0.8 alpha 0
    show eli:
        ease 0.8 alpha 0

    pause 0.5

    scene black with dissolve

    scene letgo mall escalator

    show may worried1:
        xanchor 0.5
        yalign 1.0
        xpos 0.4
        ypos 1.05
    show eli normal1 behind may:
        xanchor 0.5
        yanchor 0.5
        yalign 1.0
        xpos 0.6
        ypos 1.05
    with dissolve

    play sound "game_letgo/sfx/Climbing up Stairs.ogg"
    "We start heading upstairs. To make sure we get that cardio May cares about so much, we walk up instead of just standing there."

    voice "C-302-71.mp3" #Elijah (Michael Potok)
    eli "You’ve just been a little off today - and, well... If anything’s wrong, I want you to know I’ll be there for you."

    voice "C-302-72.mp3" #Maya (shiena)
    may "Right, I just... I’m fine. You don’t have to worry about me."

    "I flash her a smile."

    voice "C-302-73.mp3" #Elijah (Michael Potok)
    eli "Alright."

    voice "C-302-74.mp3" #Elijah (Michael Potok)
    eli "But if anything’s on your mind, just know th--"

    stop ambience fadeout 0.5
#     play music bgmloop3comedy_intro noloop fadeout 1.0
#     queue music bgmloop3comedy_loop loop

    show eli sad1:
        easein 0.3 ypos 1.15
    with vpunch
    show eli:
        rotate 10
        ypos 1.25
    with dissolve

    voice "C-302-75.mp3" #Elijah (Michael Potok)
    eli "Whoah!"

    show eli:
        easein 0.2 ypos 2.0

    show may worried2:
        easein 0.2 xpos 0.5

    "I end up on the wrong part of a step and lose my balance."

    "I make sure to let go of May’s hand so I don’t take her with me, but..."

    voice "C-302-76.mp3" #Maya (shiena)
    may "No!"

    play sound "game_letgo/sfx/Tumbling Down.ogg"
    queue sound "game_letgo/sfx/Crush.ogg"
    #cut to black

    "I tumble down the escalator like a ragdoll."

    show may angry1 close

    voice "C-302-77.mp3" #Maya (shiena)
    may "Arrrrrrgh!"

    voice "C-302-78.mp3" #Maya (shiena)
    may "Come on!"

    play sound "game_letgo/sfx/Disturbing Bass Short.ogg"
    scene letgo rewind with dissolve

    play ambience "game_letgo/ambience/Downtown Night.ogg" fadeout 0.1 fadein 0.1
    scene letgo downtown night 

    show eli smile2 at flip:
        xanchor 0.5
        yalign 1.0
        xpos 0.20
        ypos 1.03
    show may frustrated2 at flip:
        xanchor 0.5
        yalign 1.0
        xpos 0.35
        ypos 1.03
    with dissolve        

    #Do the rewind thing up to the 302escalator label

    #Can just reuse voice lines here, naturally

    voice "C-302-79.mp3" #Maya (shiena)
    may "..."

    show eli worried2 with dissolve

    voice "C-302-80.mp3" #Elijah (Michael Potok)
    eli "May?"

    voice "C-302-81.mp3" #Maya (shiena)
    may "God dammit..."

    voice "C-302-82.mp3" #Elijah (Michael Potok)
    eli "May!"

    voice "C-302-83.mp3" #Maya (shiena)
    may "Huh?"

    show eli smile2 with dissolve

    "I smile at her."

    ###

    menu:

        "Keep going. (disabled)":
            jump letgo_302escalator

        "Stay here for a bit.":
            jump letgo_302cocoa

    ###

label letgo_302cocoa:

    scene black with dissolve

    scene letgo downtown cafe outside

    stop music fadeout 20.0

    show eli smile2:
        xanchor 0.5
        yalign 1.0
        xpos 0.6

    show may frustrated2:
        xanchor 0.5
        yalign 1.0
        xpos 0.3

    with dissolve

    voice "C-302-84.mp3" #Maya (shiena)
    may "Wait here. I’ll go get you something."

    voice "C-302-85.mp3" #Elijah (Michael Potok)
    eli "Huh? It’s fine. I can go w--"

    voice "C-302-86.mp3" #Maya (shiena)
    may "Uh-uh. Go sit down and wait."

    voice "C-302-87.mp3" #Elijah (Michael Potok)
    eli "Haha. Aaalright. Never took you for the doting type!"

    voice "C-302-88.mp3" #Maya (shiena)
    may "..."

    voice "C-302-89.mp3" #Maya (shiena)
    may "Right."

    show may at flip

    pause 0.1

    show may:
        ease 0.8 align (0.0, 1.0) alpha 0

    "She walks into a nearby building."

    hide may

    show eli worried2 with dissolve

    "...Leaving me aaaaaaall alone."

    "Out in the cold."

    "With soda on my jacket."

    "Man, what’s gotten into her?"

    "She seemed just like her usual self back by the tree - but as soon as we came downtown, she’s been... off."

    "Is she nervous? Seems kinda unlike her, but I guess this is our first date and all."

    show eli sad1 with dissolve

    "Maybe I did something wrong?"

    "I don’t {i}think{/i} I did - but that’s exactly what someone who made a mistake would think, right?"

    "We can’t start things off like this. I’ll ask when I get the chance."

    "Or I would, but when she finally shows up, I’m a little distracted."

    #Rewind Point

    show may worried1:
        xanchor 0.5
        yalign 1.0
        xpos 0.3

    with easeinleft

    voice "C-302-90.mp3" #Maya (shiena)
    may "Here."

    show may frown1:
        xpos 0.4
    with ease

    pause 0.2

    show may frown1:
        xpos 0.3
    with ease

    "She hands me a clump of paper towels and a cup of hot chocolate."

    show eli smile1 with dissolve

    voice "C-302-91.mp3" #Elijah (Michael Potok)
    eli "Hey, thanks!"

    "I notice she only has the one."

    voice "C-302-92.mp3" #Elijah (Michael Potok)
    eli "...Not treating yourself?"

    jump letgo_302manhole

    #choice on rewind

label letgo_302manhole:

    show may angry1 with dissolve

    voice "C-302-93.mp3" #Maya (shiena)
    may "Don’t really feel like drinking one right now. No biggie."

    voice "C-302-94.mp3" #Elijah (Michael Potok)
    eli "Well, alright."

    voice "C-302-95.mp3" #Maya (shiena)
    may "Let’s go somewhere less crowded."

    voice "C-302-96.mp3" #Elijah (Michael Potok)
    eli "Huh? Alright. I know a street nearby that’s normally pretty empty."

    voice "C-302-97.mp3" #Maya (shiena)
    may "Perfect."

    show eli:
        ease 0.8 align (0.0, 1.0) alpha 0
    show may:
        ease 0.8 align (0.0, 1.0) alpha 0

    scene black

    pause 0.5

    scene letgo downtown nice night

    show eli smile2:
        xanchor 0.5
        yalign 1.0
        xpos 0.7
        ypos 1.03

    show may worried1:
        xanchor 0.5
        yalign 1.0
        xpos 0.55
        ypos 1.03

    with dissolve

    "I lead the way - until soon enough, we’re all alone."

    voice "C-302-98.mp3" #Elijah (Michael Potok)
    eli "Pretty weird to head downtown and then decide you want to be alone. It’s normally pretty hard to do both at once."

    voice "C-302-99.mp3" #Maya (shiena)
    may "Guess I’m weird, then."

    voice "C-302-100.mp3" #Elijah (Michael Potok)
    eli "I like it, though! Keeps things fresh."

    voice "C-302-101.mp3" #Maya (shiena)
    may "You would."

    "..."

    show eli sad2 with dissolve

    "Jeez, it’s like talking to a wall..."

    "I take a long sip of my hot chocolate."

    "...Wait."

    stop ambience fadeout 1.0

    #do the death fakeout music thing again

    "The hot chocolate!?"

    voice "C-302-102.mp3" #Elijah (Michael Potok)
    eli "Shit!"

    show may worried2:
        linear 0.1 ypos 1.00
        linear 0.1 ypos 1.03
        linear 0.1 xpos 0.53

    voice "C-302-103.mp3" #Maya (shiena)
    may "What? What’s wrong!?"

    voice "C-302-104.mp3" #Elijah (Michael Potok)
    eli "You could have poisoned me just now!"

    play ambience "game_letgo/ambience/Downtown Night.ogg" fadeout 0.1 fadein 0.1

    #music turns back to something non-intense

    show may confused1 with dissolve

    voice "C-302-105.mp3" #Maya (shiena)
    may "...Huh?"

    voice "C-302-106.mp3" #Elijah (Michael Potok)
    eli "I said I’d never eat anything you got me because you might have poisoned it, but it totally slipped my mind! You could’ve really gotten me!"

    show may aww1 with dissolve

    voice "C-302-107.mp3" #Maya (shiena)
    may "Heh... You still remember that?"

    show eli cool2 with dissolve

    voice "C-302-109.mp3" #Elijah (Michael Potok)
    eli "‘Course! It was fifteen minutes ago. The fact that I forgot at all is just plain embarrassing..."

    show may forcedsmile1 with dissolve

    voice "C-302-110.mp3" #Maya (shiena)
    may "Oh... Right."

    show may proud2 with dissolve

    voice "C-302-111.mp3" #Maya (shiena)
    may "Well, you’re right. I poisoned it. You’re dead now. Any last words?"

    voice "C-302-112.mp3" #Elijah (Michael Potok)
    eli "Hm..."

    show eli:
        easein 0.9 xpos 0.645

    "I grab her hand."

    voice "C-302-113.mp3" #Elijah (Michael Potok)
    eli "I’ll miss you."

    show may aww2 with dissolve

    voice "C-302-114.mp3" #Maya (shiena)
    may "Oh, you’re such a sap."

    voice "C-302-115.mp3" #Elijah (Michael Potok)
    eli "Hey, I love some good sap! Why do you think I confessed my love to a tree?"

    show may aww2 close with dissolve

    voice "C-302-116.mp3" #Maya (shiena)
    may "Pfft!"

    show may cheeky1 with dissolve

    voice "C-302-117.mp3" #Maya (shiena)
    may "That’s why I took you to the city, y’know."

    voice "C-302-118.mp3" #Maya (shiena)
    may "Get you farther from the competition."

    show eli goofy1 with dissolve

    voice "C-302-119.mp3" #Elijah (Michael Potok)
    eli "Hmm. I dunno... Buildings can be pretty sexy, too."

    voice "C-302-120.mp3" #Maya (shiena)
    may "Yeah?"

    voice "C-302-121.mp3" #Elijah (Michael Potok)
    eli "Just take a look."

    scene letgo lights1 night with Dissolve(1.75)

    play music bgmloop1romantic_intro noloop fadeout 1.0
    queue music bgmloop1romantic_loop loop

    #I require that this background be at least a little bit sexy

    voice "C-302-122.mp3" #Maya (shiena)
    may "Hey, you’re right."

    voice "C-302-123.mp3" #Elijah (Michael Potok)
    eli "Makes you feel small, but... In a good way, I think. Nice and humbling."

    voice "C-302-124.mp3" #Maya (shiena)
    may "...Yeah."

    "..."

    voice "C-302-125.mp3" #Elijah (Michael Potok)
    eli "Hey. Mind if I ask you something?"

    "..."

    voice "C-302-126.mp3" #Maya (shiena)
    may "...Yeah. Yeah, I mind."

    voice "C-302-127.mp3" #Maya (shiena)
    may "Whatever you’re thinking, just... Keep thinking it."

    "She squeezes my hand."

#     voice "C-302-128.mp3" #Maya (shiena)
#     may "Okay?"

    "Huh?"

    "I let go."

    scene letgo downtown nice night

    show eli sad2:
        xanchor 0.5
        yalign 1.0
        xpos 0.645
        ypos 1.03

    show may worried1:
        xanchor 0.5
        yalign 1.0
        xpos 0.55
        ypos 1.03
    with dissolve

    voice "C-302-129.mp3" #Elijah (Michael Potok)
    eli "Sorry, May, but I don’t think I can do that."

    voice "C-302-130.mp3" #Elijah (Michael Potok)
    eli "It just... It just seems like something’s on your mind. And if that’s true, I want to help."

    voice "C-302-131.mp3" #Maya (shiena)
    may "..."

    voice "C-302-132.mp3" #Maya (shiena)
    may "Nothing’s wrong."

    voice "C-302-133.mp3" #Maya (shiena)
    may "I’m fine. Okay?"

    stop music fadeout 4.0

    "..."

    show may at flip with dissolve
    show may:
        easein 0.5 xpos 0.3

    voice "C-302-135.mp3" #Elijah (Michael Potok)
    eli "Okay."

    show eli:
        easein 0.8 xpos 0.45

    voice "C-302-136.mp3" #Elijah (Michael Potok)
    eli "I believe y--"

    play music bgmloop3comedy_intro noloop fadeout 1.0
    queue music bgmloop3comedy_loop loop

    #oops he’s dying make the screen black or something

    show eli sad1:
        easein 0.3 ypos 1.15
    with vpunch
    show eli:
        rotate 10
        ypos 1.25
    with dissolve

    voice "C-302-137.mp3" #Elijah (Michael Potok)
    eli "Woah!"

    scene black

    play sound "game_letgo/sfx/Ice Slip.ogg"

    "I catch a patch of ice and start to slip, but I don’t land like I’m supposed to."

    "I slipped into an open manhole!"

    "My head bangs into the side, and--"

    play sound "game_letgo/sfx/Manhole Thud.ogg"

    "..."

    voice "C-302-138.mp3" #Maya (shiena)
    may "Dammit..."

    voice "C-302-139.mp3" #Maya (shiena)
    may "{i}Dammit!{/i}"

    voice "C-302-140.mp3" #Maya (shiena)
    may "{i}Why!?{/i}"

    play sound "game_letgo/sfx/Disturbing Bass Short.ogg"
    scene letgo rewind with dissolve

    jump letgo_303
