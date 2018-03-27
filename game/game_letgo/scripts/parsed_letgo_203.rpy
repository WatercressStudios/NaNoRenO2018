label letgo_203:
    scene black with dissolve
    pause 0.5
    scene letgo suburb house with dissolve
    # define ow character "Old Woman"
    # define om character "Old Man"

    #bg moar christmas-y lights!

    #eli at right
    show eli smile1 at right with easeinright

    voice "C-203-1.mp3" #Elijah (Michael Potok)
    eli "Woah. Some old couple has some goodies set out!"

    #may at left
    show may normal1:
        xanchor 0.5
        yalign 1.0
        xpos 0.675
    with dissolve

    voice "C-203-2.mp3" #Maya (shiena)
    may "Holiday at the Ritz Tour, huh?"

    show eli cool1 close with dissolve

    voice "C-203-3.mp3" #Elijah (Michael Potok)
    eli "Oh my god, I can smell cider and hot chocolate. Want to go warm up a bit? We’ve been walking for a while."

    show may adore1 with dissolve

    voice "C-203-4.mp3" #Maya (shiena)
    may "Well, it’s pretty cold out. Won’t hurt any to stop for a bit and warm up."

    show may normal1:
        xpos 0.5
    with ease
    show eli cool1:
        xpos 0.79
    with ease

    voice "C-203-5.mp3" #Old Woman (Ashe Thurman)
    ow "Why hello! You’re lucky; we just got some fresh hot milk and water for the next tour! They'll be another fifteen minutes or so, but we like to be prepared."

    voice "C-203-6.mp3" #Old Man (Adam Warren)
    om "Oh, a young couple at that."

    show eli worried1 with dissolve

    voice "C-203-7.mp3" #Elijah (Michael Potok)
    eli "How can you tell?"

    voice "C-203-8.mp3" #Old Man (Adam Warren)
    om "Just by looking, you tell me you're happy and excited. And where you look, haha!"

    show eli sad1

    voice "C-203-9.mp3" #Old Woman (Ashe Thurman)
    ow "Oh, honey… don’t tease them too much!"

    show may sheepish2:
        xpos 0.55
    with ease

    voice "C-203-10.mp3" #Maya (shiena)
    may "Do you think they're nuts or anything? I mean, not a lot of people offer free stuff anymore."

    show eli normal2:
        xpos 0.83
    with dissolve

    voice "C-203-11.mp3" #Elijah (Michael Potok)
    eli "I, for one, welcome the crazies with hot cocoa and cider."

    show may cheeky1:
        xpos 0.5
    with ease

    voice "C-203-12.mp3" #Maya (shiena)
    may "Ha, can't choose between them?"

    show eli normal2 close with dissolve

    voice "C-203-13.mp3" #Elijah (Michael Potok)
    eli "My dear loves, chocolate and tart cider, shall simply take turns!"

    #May snort/laugh

    show may aww1 with dissolve

    voice "C-203-14.mp3" #Maya (shiena)
    may "You don't say! Well, guess they'll have to wait until I look like that lady, then."

    "I had to laugh, though…"

    "Growing old together... I hadn't really thought about it too much before."
    "I can almost see it - and I hope she’s still smiling just as much as she is tonight when she gets wrinkles and white hair."

    "That would be worth the world to me."

    show may normal1 with dissolve

    voice "C-203-15.mp3" #Old Woman (Ashe Thurman)
    ow "So, young lady, would you like something to drink? It's actual cocoa in the white cups, but the ones with a black band are made from the sugar-free powder."

    show may happy2 with dissolve

    voice "C-203-16.mp3" #Maya (shiena)
    may "Ooh, do you have marshmallows?"

    show may:
        ease 0.8 align (0.0, 1.0) alpha 0
    pause .5
    hide may

    "The old lady led her away, and suddenly I’m alone again."

    show eli normal1
    "Or I would be, if not for the tap on my shoulder as I take a cider. The steam billows up, carrying the scent of apples and spices to my nose."

    "As I sip on it, I turn around."

    show eli at flip with dissolve

    voice "C-203-17.mp3" #Old Man (Adam Warren)
    om "You look… relieved, young man - and tense!"

    voice "C-203-18.mp3" #Elijah (Michael Potok)
    eli "First dates are kind of a big deal, haha~! Anyone’s going to be a bit nervous."

    voice "C-203-19.mp3" #Old Man (Adam Warren)
    om "Oh my. And to think, when I first met my wife, there was a big hullabaloo! Well, son. There's good reason to be tense."

    voice "C-203-20.mp3" #Elijah (Michael Potok)
    eli "Isn't some confidence-building in order?"

    show eli worried2 with dissolve

    "I kind of laugh."
    "After all, this isn’t exactly the sort of thing I expected at a neighborhood’s yearly \"good natured\" competition to see who can raise their light bills the highest."

    "You know, they kind of remind me of us - but the old lady’s black and the man seems… I dunno, Scandinavian?"

    voice "C-203-21.mp3" #Old Man (Adam Warren)
    om "A lot of couples don't make it. But this is what it looks like to beat the odds! Hahaha!"

    voice "C-203-22.mp3" #Elijah (Michael Potok)
    eli "Oh. That's… nice?"

    voice "C-203-23.mp3" #Old Man (Adam Warren)
    om "I hazard that you're a new couple, yes?"

    show eli normal2 with dissolve

    voice "C-203-24.mp3" #Elijah (Michael Potok)
    eli "Yeah, just today! We’ve been friends for a long time; we’ve worked together..."

    voice "C-203-25.mp3" #Elijah (Michael Potok)
    eli "We don’t anymore though - and, well, it’s been tough seeing each other when it’s {i}not{/i} crazy. We’ve been through a lot."

    voice "C-203-26.mp3" #Old Man (Adam Warren)
    om "Sounds like you’ve got something a lot of young men never do."

    voice "C-203-27.mp3" #Elijah (Michael Potok)
    eli "And what’s that?"

    # HACK SPLIT THIS VOICE LINE INTO THREE PARTS
    voice "C-203-28.mp3" #Old Man (Adam Warren)
    om "If you don’t make the time, you’ll never find the time to be together."
    voice "C-203-28b.mp3" #Old Man (Adam Warren)
    om "So many young men forget that they’ve got to make room for the special moments."
    voice "C-203-28c.mp3" #Old Man (Adam Warren)
    om "We only ever have so many - and I say that at my ripe old age!"

    "You know, that made a lot of sense to me."

    hide eli

    show letgo suburb house:
        zoom 1.6
        xalign 0.8
        ease 0.6 xalign 0.2 yalign 0.8
    with dissolve
    show may happy2 close at flip:
        xanchor 0.5
        yalign 1.0
        xpos 0.3
    with dissolve

    "I glance over at Maya, and she’s huddled with the old lady, talking up a storm."
    "Though I can’t really tell what they’re going on about. It’s kind of warbly. Maybe I have some wax in my ears?"

    "The house seems warm, bright. The windows that I can see through are full of knick-knacks and pictures."

    "For some reason, an old cloth kite was hung in one."
    "It looked battered and like it had been sewn together in places, oiled with streamers still hanging, the tails looking as if they were still in flight."

    scene letgo suburb house
    show eli normal1:
        xanchor 0.5
        yalign 1.0
        xpos 0.83
    with dissolve

    voice "C-203-29.mp3" #Elijah (Michael Potok)
    eli "What’s that over there? A fan of a certain old musical?"

    voice "C-203-30.mp3" #Old Man (Adam Warren)
    om "Oh! That was one of the first kites I made when I met my dear wife. It wasn’t the best I'd made, but I kept it."

    # HACK WHERE ARE THE VOICE LINES??
    om "That one? That was the day I first knew I loved her. A plane can float along the breeze, free as it can be - but a kite, well."
    om "It needs a connection. We each fly because the string holds our sails taut. We help each other be free."

    "I hadn’t thought about our new relationship like that. Some of my friends often moan and groan about things tying them down, but May..."

    show eli happy1 with dissolve

    voice "C-203-31.mp3" #Elijah (Michael Potok)
    eli "Light as a feather. That’s how she makes me feel. I hope I can make her feel like that, too."

    #scene black with dissolve
    scene letgo suburb house
    show eli normal1:
        xanchor 0.5
        yalign 1.0
        xpos 0.6
    show may normal1:
        xanchor 0.5
        yalign 1.0
        xpos 0.4
    with ease

    "She and I each grabbed a fresh cup when she came back, giving a few parting words to the friendly old couple."

    show eli normal1:
        xpos 0.51
    with ease

    "I grasped her hand, feeling just... blown away by how lucky I am to have her with me. It seems like she felt the same for me..."

    voice "C-203-32.mp3" #Maya (shiena)
    may "Can you imagine this, Eli?"

    voice "C-203-33.mp3" #Elijah (Michael Potok)
    eli "I can imagine us like this, if that’s what you’re talking about."

    show may sad1 with dissolve

    voice "C-203-34.mp3" #Maya (shiena)
    may "That-- That would be..."

    show may sad1 close:
        easein .35 xpos 0.45

    pause 1.0

    "She actually chokes up and embraces me for a good minute or two."

    show may aww1 with dissolve
    show may:
        xpos 0.4
    with ease

    voice "C-203-35.mp3" #Maya (shiena)
    may "That would be all I could ever ask for and so much more, Eli - except, maybe you could accept pineapple as a pizza topping."

    show eli cool1 with dissolve

    voice "C-203-36.mp3" #Elijah (Michael Potok)
    eli "Never! That’s a dessert waiting to happen."

    "I hoped the day would never end - but the sun is painting the sky a beautiful burnt orange; lavender set in as the stars began peeking out. Then comes the moon."

    play ambience "game_letgo/ambience/Park Night.ogg" fadeout 2.0 fadein 2.0
    stop music fadeout 2.0
    scene letgo suburb night with Dissolve(1.0)

    "We leave the old couple, walking hand in hand, now up the way from what I hope will someday be our own future."

    "The lights continue creating a halo around us on this calm, snowy night."

    jump letgo_204
