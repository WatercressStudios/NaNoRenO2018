label letgo_104:
    scene letgo park trees sunset with dissolve

    play ambience "game_letgo/ambience/Park Night.ogg" fadeout 2.0 fadein 2.0

    "We eventually get up and start heading home."

    "The night was darkening, allowing the moon to come out and light the sidewalk beneath our feet."

    scene letgo road long with dissolve

    play music bgmloop1death_intro noloop fadeout 1.0
    queue music bgmloop1death_loop loop
    play ambience "game_letgo/ambience/Roads Night.ogg" fadeout 2.0 fadein 2.0

    "The sounds of people in the different buildings we pass change the farther we go."

    "We’d normally go our separate ways soon, so now’s the time to say something."

    show eli cool1 with dissolve:
        align (0.35, 1.0)

    voice "C-104-1.mp3" #Elijah (Michael Potok)
    eli "Can I walk you home tonight?"

    show may adore1 with dissolve:
        align (0.65, 1.0)

    voice "C-104-2.mp3" #Maya (shiena)
    may "Sure, I’d like that."

    show may:
        ease 1.0 align (0.55, 1.0)

    "She smiles up at me and takes my hand."

    "Alright, now’s the best time. Try to remember what you were going to say at the tree, dammit!"

    "Everything’s alright, just explain how you feel - in full this time."

    "You know she has feelings for you too. Just ask her out or something!"

    "Keep things simple; don’t go full out..."

    "Or maybe I should spill it all? Tell her I love her more than life and would do anything for her?"

    "Is that coming on too strong? Is strong even good? Oh jeez, say something before we’re on her doorstep!"

    show eli worried2 with dissolve

    voice "C-104-3.mp3" #Elijah (Michael Potok)
    eli "So, Maya… Uhm, I guess I just wanted to clarify what happened earlier…"

    show may cheeky2 with dissolve

    voice "C-104-4.mp3" #Maya (shiena)
    may "You mean when you confessed your feelings for beautiful, funny trees that have always been there for you?"

    show eli smile1 with dissolve

    voice "C-104-5.mp3" #Elijah (Michael Potok)
    eli "Yes, well.. uh, that. See, what I was trying to say was that I really care about you."

    show may shout1 close with dissolve

    voice "C-104-6.mp3" #Maya (shiena)
    may "Oh really?"

    "I patiently wait for her to continue. My feet move on their own and I avoid eye contact."

    "Did I do something wrong?"

    "Should I have said it differently? The important thing is I said it, right? Or maybe it just wasn’t enough..."

    scene letgo road night with dissolve

    "Just calm down; focus on getting her home safely. Watch the sidewalk, watch the car moving this way, watch her eyelashes as she blinks in the bright headlights..."

    show eli smile1 with dissolve:
        align (0.35, 1.0)
    show may nervous2 with dissolve:
        align (0.65, 1.0)

    voice "C-104-7.mp3" #Maya (shiena)
    may "All I can say is that I’ve only wanted you too. I guess I just never knew how to say--"

    "Before she can finish, the car catches some ice on the road."

    stop music fadeout 0.1
    play sound "game_letgo/sfx/Car Screeching.ogg"

    "Tires screech, and the lights dance."

    show may shout1
    show eli angry1

    voice "C-104-8.mp3" #Maya (shiena)
    may "Oh my god, watch out!"

    "The car hits the curb - then comes over the edge toward us."

    show eli:
        ease 0.6 align (0.6, 1.0)

    pause 0.4
    play sound "game_letgo/sfx/Punch,Shove Serious.ogg"

    show may shout1 close:
        ease 0.6 align (1.0, 1.0) alpha 0

    "I push Maya off to the left."

    "The driver’s completely lost control."

    show eli sad1 with dissolve

    "I look over to see that Maya is on the ground a few feet away, trying to get up..."

    "The headlights are blinding."

    "It’s moving too fast."

    "Is Maya okay?"

    voice "C-104-9.mp3" #Elijah (Michael Potok)
    eli "Maya--"

    #"The lights are everywhere."

    play sound "game_letgo/sfx/Car Screeching.ogg"
    pause 1.3
    play sound "game_letgo/sfx/Punch,Shove.ogg"
    stop ambience fadeout 0.1
    stop music fadeout 0.1
    scene black

    "And then, there’s nothing."

    play audio "game_letgo/sfx/Disturbing Bass.ogg"
    scene letgo rewind with Dissolve(9.5)

    jump letgo_201
