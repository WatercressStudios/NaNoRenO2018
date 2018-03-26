label letgo_201:
    scene letgo clocktower eli may
    
    play sound "game_letgo/sfx/Clocktower 3PM.ogg"
    play ambience "game_letgo/ambience/Town Center Plaza.ogg" fadeout 0.1 fadein 0.1

    "..."

    "The snow-heavy tree I’d confessed to was a very patient - if not very talkative - witness when I got tongue-tied. That must really come from what, hundreds of years of being alive?"

    "How long have we worked together, anyway? Sheesh, I’m still babbling at May like an idiot!"

    scene letgo townsquare2 with dissolve
    show eli sad1 with dissolve:
        align (0.35, 1.0)

    voice "C-201-1.mp3" #Elijah (Michael Potok)
    eli "Maybe I shouldn’t have waited until it was so cold, or maybe--"

    "She raises a hand; the fuzz of her glove makes my nose itch just a little."

    play music bgmloop2distorted_intro noloop fadeout 1.0
    queue music bgmloop2distorted_loop loop

    show may angry2 with dissolve:
        align (0.65, 1.0)

    voice "C-201-2.mp3" #Maya (shiena)
    may "Eli. Eli, listen to me: It’s {i}perfect{/i}. It’s not all that cold. In fact, do you know why this time is perfect?"

    "{i}Perfect?{/i} This is a complete and utter {i}mess{/i} - but she looks so happy, how can I make her mad by arguing against that?"

    show eli smile2 with dissolve

    voice "C-201-2b.mp3" #Elijah (Michael Potok)
    eli "It’s a great time to make snow angels?"

    show may normal1 with dissolve
    #maya laugh sound

    voice "C-201-3.mp3" #Maya (shiena)
    may "What? No! The Lampoon Street neighborhood is setting up already!!"

    "Oh yeah, the neighborhood where everyone goes nuts with holiday decorations!"

    menu:
        "Let's have coffee (disabled)":
            pass
        "Don't have coffee":
            pass

    "It’s after Thanksgiving after all - and of course, as long as snow’s on the ground, it’s not too early to string up some lights. I gotta say, I can’t exactly fault them for getting into the spirit of things…"

    "Besides, it’s {i}their{/i} bills that go up for the season, not mine."

    show eli happy1 with dissolve

    voice "C-201-4.mp3" #Elijah (Michael Potok)
    eli "That’s a great idea! There won’t be too many people this time of year."

    voice "C-201-5.mp3" #Elijah (Michael Potok)
    eli "Oh! I almost forgot."

    "I hold up the delicate-looking flowers and she scrunches her nose for a moment."

    show eli worried1 with dissolve

    voice "C-201-6.mp3" #Elijah (Michael Potok)
    eli "I didn’t forget the other part: plastic and silk; they’ll last forever and won’t give you allergies."

    #Maya sprite gets close to Elijah’s
    show may adore1 with dissolve
    play sound "game_letgo/sfx/Punch,Shove Serious.ogg"
    show may:
        ease 0.5 align (0.5, 1.0)

    "She accepts them and hugs me tight, almost jumping onto me."

    show eli goofy1 with dissolve

    voice "C-201-7.mp3" #Elijah (Michael Potok)
    eli "Wow, that’s better than I expected! Urk... and heavier!"

    show may cheeky1 with dissolve

    voice "C-201-8.mp3" #Maya (shiena)
    may "Deal with it, because they’re wonderful! You always remember the important things when it matters."

    #maya sprite moves back
    show may normal1 with dissolve
    show may:
        ease 1.5 align (0.65, 1.0)

    "She wraps her arm around mine, shaking her boots free from the snow; it falls around her in tight, wet chunks."

    "I wish it was dry and fluffy... It would make crazy drivers less of a problem - even if it makes the world look prettier overall."

    "Not to mention: the snow really does favors for those stockings she’s wearing. Wow!"

    show may proud2 with dissolve

    voice "C-201-9.mp3" #Maya (shiena)
    may "Well, shall we go on our romantic walk together? First night as boyfriend and girlfriend? You know, the things we used to make fun of on Singles Awareness Day?"

    show eli smile2 with dissolve

    voice "C-201-10.mp3" #Elijah (Michael Potok)
    eli "All the sap and more, of course! \"And next spring, on Oxee Channel, the tale of love that bloomed in winter!\""

    show may worried1 with dissolve

    voice "C-201-11.mp3" #Maya (shiena)
    may "God, that would be so embarrassing - especially if it was on TV..."

    show eli happy1 with dissolve

    voice "C-201-12.mp3" #Elijah (Michael Potok)
    eli "Yeah, seeing their confession would probably take half the movie and a quarter of the sequel."

    show may frustrated2 with dissolve

    voice "C-201-13.mp3" #Maya (shiena)
    may "Don’t be silly, it’ll be the whole movie for them! They like the melodrama, and you know it."

    voice "C-201-14.mp3" #Elijah (Michael Potok)
    eli "And the whole will-they, won’t-they... But we don’t have to worry about that now."

    "Nope, not at all. I finally built up the courage and said how I really felt."

    "What a waste of time to wait so long! Well, not a complete waste on reflection; being friends has led to some of the funnest and best times I’ve had. If anything, it just made my feelings stronger."

    hide eli with dissolve
    hide may with dissolve
    #hide talksprites

    play sound "game_letgo/sfx/Snow Footsteps.ogg"

    "Tonight, that’s what really matters: our feelings and time together - the place where we are now, even if I don’t know where we’re going yet."

    "But damn, I’m excited to find out."

    # change bg to suburban snowy area

    jump letgo_202