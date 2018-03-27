label letgo_202:
    scene letgo suburb3 with Dissolve(1.0)

    show eli goofy1 with dissolve:
        align (0.35, 1.0)
    show may adore1 with dissolve:
        align (0.65, 1.0)

    "We decide to walk to the part of town where the big decorations are - though we didn’t exactly hold hands."

    "Some of the sidewalks aren’t exactly as well-shoveled as they could be…"

    #show Maya, is there a way to have her sprite ‘slide’ around the screen?

    show may shout1 with dissolve
    show may:
        ease 0.5 align (0.7, 1.0)
        pause 0.2
        ease 1.0 align (0.6, 1.0)
        repeat

    voice "C-202-1.mp3" #Maya (shiena)
    may "Whoa-woah!"

    "She yelled just a little - waving her arms as she slid around the sidewalk on a patch of ice."

    show eli worried2 with dissolve

    voice "C-202-2.mp3" #Elijah (Michael Potok)
    eli "This has gotta be either the folks that went down to Florida or just came from there, because wow. Haven’t they heard of salt?"

    show eli:
        ease 0.5 align (0.45, 1.0)
    pause 0.3
    show may:
        ease 0.5 align (0.65, 1.0)

    "I help steady her, then walk as carefully as I can... Well, I thought I was, anyway."

    #Eli slides off screen right (if we can do that)
    show eli:
        ease 0.5 align (0.35, 1.0)
    pause 0.7

    play sound "game_letgo/sfx/Ice Slip.ogg"

    show eli:
        easeout 1.0 align (-0.5, 1.0)

    voice "C-202-3.mp3" #Elijah (Michael Potok)
    eli "Crap crap shiiii--!"

    # sfx crunch/crash/snow crunch

    play sound "game_letgo/sfx/Crush.ogg"

    # eli laughing

    voice "C-202-4.mp3" #Elijah (Michael Potok)
    eli "Ow, ow ow! Wow, for a moment, it felt like October."

    "My poor head. The snow-covered pavement is a lot harder than it looks."

    show may angry2 with dissolve

    voice "C-202-5.mp3" #Maya (shiena)
    may "You alright?"

    "May looked and sounded a little nervous there. I’m not a klutz... okay, not {i}often.{/i}"

    "I push myself off the ground."

    show eli worried1 with dissolve:
        align (0.35, 1.0)

    voice "C-202-6.mp3" #Elijah (Michael Potok)
    eli "Ow. Okay, well I feel like I’m at least in one piece."


    show may worried2 with dissolve

    voice "C-202-7.mp3" #Maya (shiena)
    may "Should we go check it out? We can do this another night if you want to turn back."

    show eli goofy1 with dissolve

    voice "C-202-8.mp3" #Elijah (Michael Potok)
    eli "Haha, I’m fine, I just have a snowy butt."

    show may cheeky1 with dissolve

    voice "C-202-9.mp3" #Maya (shiena)
    may "A {i}showy{/i} butt, too!"

    voice "C-202-10.mp3" #Elijah (Michael Potok)
    eli "Pfft, Maymay...."

    show eli smile2 with dissolve

    voice "C-202-11.mp3" #Elijah (Michael Potok)
    eli "We’ll head back once we get through this street and I’ll take some aspirin or something. Ready for some sights almost pretty as you?"

    show may aww1 with dissolve

    voice "C-202-12.mp3" #Maya (shiena)
    may "Flattery really gets you everywhere, Eli."

    "The sky suddenly started to clear up; a few flakes fell, lazily floating down on the slightest of breezes. They dusted her hair and made a delicate crown of snow."

    "Maya really is beautiful. I’m lucky to have someone in my life like her. I think, even if she turned me down, I’d have been okay with staying friends." 

    "But she said yes! I’m surprised, of course - and the happiest I’ve been in a long time… every second together drags on, but in a good way."

    scene letgo suburb2 with Dissolve(1.0)
    show may angry2 with dissolve:
        align (0.65, 1.0)

    voice "C-202-13.mp3" #Maya (shiena)
    may "Finally, some shoveled {i}and{/i} salted sidewalks."

    show eli normal1 with dissolve:
        align (0.35, 1.0)

    voice "C-202-14.mp3" #Elijah (Michael Potok)
    eli "No kidding. Now I can do {i}this!{/i}"

    # eli sprite moves to may 
    show eli:
        ease 1.0 align (0.45,1.0)
    show may adore1 with dissolve

    "There’s something warm and precious about a first kiss; the flowers fall and the petals are dusted with now - but silk washes clean."

    "...Huh. I should write that down later. She picks up the flowers and carefully puts them in her pocket before we continue."

    #may at right, eli at left

    show eli:
        ease 1.0 align (0.35,1.0)

    pause 0.5
    show may aww2 with dissolve

    voice "C-202-15.mp3" #Maya (shiena)
    may "That was unexpected. And pretty nice."

    "I lead her forward, never glancing back."

    "Dammit, I’m doing that right now. Oh well."

    "I know she’s there behind me, and I can’t help but savour every second of it."
    
    jump letgo_203