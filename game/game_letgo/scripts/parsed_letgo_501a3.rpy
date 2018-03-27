label letgo_501a3:
    play ambience "game_letgo/ambience/Suburban Houses.ogg" fadeout 2.0 fadein 2.0
    play sound "game_letgo/sfx/May Eli Run.ogg"
    scene letgo road long with dissolve
    # show old couple

    voice "C-501a3-1.mp3" #Maya (shiena)
    may "*Huff*, *huff*, *huff*..."
    
    scene letgo suburb3 with dissolve

    voice "C-501a3-2.mp3" #Elijah (Michael Potok)
    eli "*Huff*, *huff*, *wheeze*..."

    scene letgo suburb house with dissolve

    show eli worried1 with dissolve:
        align (0.35, 1.0)

    voice "C-501a3-3.mp3" #Elijah (Michael Potok)
    eli "May, why did we have to run?"

    "The sweet old couple in front of us seem just as startled by our sudden appearance."
    play music bgmloop5kite fadeout 1.0
    # slightly out of breath
    show may shout1 with dissolve:
        align (0.65, 1.0)
    voice "C-501a3-4.mp3" #Maya (shiena)
    may "We’d like to buy a kite, please."

    show eli sad1 with dissolve

    "Huh? What is she saying? This isn’t a shop - and it doesn’t even seem like they know us!"

    voice "C-501a3-5.mp3" #Maya (shiena)
    may "A kite like that one!"

    "Maya’s pointing at an old-style cloth kite by the window. It looks battered, like it’s been sewn together in spots."

    "Does that kite even fly? Why would Maya want that one?"

    "For some reason, the old man isn’t phased by Maya’s strange request."
    "Instead, he steps into his garage and produces a large cloth kite that looks exactly like the one Maya pointed at, only brand new."

    "Maya tries to open her wallet - but the old man stops her."
    show may suspicious1 with dissolve
    voice "C-501a3-6.mp3" #Maya (shiena)
    may "Are you sure?"

    voice "C-501a3-7.mp3" #Old Man (Adam Warren)
    om "Of course. She’s never flown before, so you’ll be doing us a favor."

    voice "C-501a3-8.mp3" #Old Woman (Ashe Thurman)
    ow "Be sure to make some good memories with it."
    show may happy2 with dissolve
    show eli smile2 with dissolve
    voice "C-501a3-9.mp3" #Maya (shiena)
    may "Thank you!"
    show may proud2 with dissolve
    voice "C-501a3-10.mp3" #Maya (shiena)
    may "{i}Come on, Eli!{/i}"
    show may:
        ease 0.5 align (0.80,1.0)
    pause 0.1
    show eli:
        ease 0.5 align (0.55,1.0)
        
    voice "C-501a3-11.mp3" #Elijah (Michael Potok)
    eli "Ack, slow down!"
    play sound "game_letgo/sfx/May Eli Run.ogg"
    scene letgo suburb house with dissolve
    pause 0.2
    scene letgo suburb3 with dissolve
    pause 0.2
    scene letgo road long with dissolve
    pause 0.2
    scene letgo park lake with dissolve

    show eli goofy1 with dissolve:
        align (0.55, 1.0)
    show may happy2 with dissolve:
        align (0.85, 1.0)
    voice "C-501a3-12.mp3" #Maya (shiena)
    may "Here, let me hold the kite. Take the spool and go thirty feet in that direction. Keep the line taut!"

    show may:
        ease 0.5 align (1.0, 1.0)
    show eli smile2 with dissolve
    show eli:
        ease 1.3 align (0.0, 1.0)
    pause 1.3

    voice "C-501a3-13.mp3" #Elijah (Michael Potok)
    eli "Okay, but since when do you know how to fly kites?"

    show may cheeky2 with dissolve
    voice "C-501a3-14.mp3" #Maya (shiena)
    may "I don’t. I’m looking it up right now."

    "Wait, what?"
    show eli worried1 with dissolve
    "I turn around and see that she’s pulled her gloves off to use her phone. She’s serious?"

    "Who are you and what have you done to my Maya!?"
    show may happy2 with dissolve
    voice "C-501a3-15.mp3" #Maya (shiena)
    may "Okay, here’s the deal: when you feel the breeze on your back, pull the line and I’ll toss the kite up. We have to do this at the same time, so pay attention!"

    voice "C-501a3-16.mp3" #Elijah (Michael Potok)
    eli "Wait, when you say \"pull,\" how much are we talking--"

    show may shout1 with dissolve
    voice "C-501a3-17.mp3" #Maya (shiena)
    may "There’s a breeze! Do it now!"

    show eli sad1 with dissolve
    voice "C-501a3-18.mp3" #Elijah (Michael Potok)
    eli "Huh!?"

    show may cheeky2 with dissolve
    "Before I can ask for a timeout, Maya tosses the kite up into the air!"

    "Oh crap!"

    "I pull the line, but I’m too late. The kite flops lamely onto the ground."

    show eli worried1 with dissolve

    voice "C-501a3-19.mp3" #Elijah (Michael Potok)
    eli "Shit, sorry--"

    show may shout1 with dissolve
    voice "C-501a3-20.mp3" #Maya (shiena)
    may "One more time!"

    "Without missing a beat, Maya lifts the kite up and gets into position. She’s really into this!"

    show eli cool2 with dissolve

    "I guess I should take this seriously as well."

    "So, I mentally prepare myself and I wait… until I feel a breeze on my back."

    show eli happy1 with dissolve

    voice "C-501a3-21.mp3" #Elijah (Michael Potok)
    eli "Now!"

    "I quickly pull on the line. This time I can feel a strangely satisfying resistance - and before I know it, the kite starts to rise high into the orange sky."

    show eli happy1 with dissolve
    voice "C-501a3-22.mp3" #Elijah (Michael Potok)
    eli "Holy shit, it’s going up! It’s {i}actually{/i} going up!"

    show may angry2 with dissolve

    voice "C-501a3-23.mp3" #Maya (shiena)
    may "Don’t stop! You have to keep pulling!"

    voice "C-501a3-24.mp3" #Elijah (Michael Potok)
    eli "Are you sure? It’s flying!"

    show may shout1 with dissolve

    voice "C-501a3-25.mp3" #Maya (shiena)
    may "Yes! Do it!"

    show eli cool1 with dissolve

    "I pull more of the line in - and as if the connection to me is all it needed, the kite starts soaring even higher."

    scene letgo kite with Dissolve(2.0)
    #holy shit these guys /really/ fucking love their kite flying

    voice "C-501a3-26.mp3" #Elijah (Michael Potok)
    eli "Oh my god, this is {i}freaking amazing!{/i}"

    "I can't help shouting with joy. The adrenaline is intoxicating - I can feel my heart is pounding!"

    "Of all the things I thought I'll do, I never once thought I'd fly a kite!"

    "Maya runs over and nearly knocks me over with her hug."
    play sound "game_letgo/sfx/Punch,Shove.ogg"

    voice "C-501a3-27.mp3" #Elijah (Michael Potok)
    eli "Ooph!"

    stop music fadeout 2.0
    scene letgo park lake sunset with dissolve
    show eli worried1 with dissolve:
        align (0.4, 1.0)
    show may adore1 with dissolve:
        align (0.6, 1.0)

    "The spool slips from my hands and the kite glides away into the trees."

    voice "C-501a3-28.mp3" #Elijah (Michael Potok)
    eli "Oh shit, the kite! Wait here, I’ll get--"

    show may happy2 with dissolve
    voice "C-501a3-29.mp3" #Maya (shiena)
    may "Leave it."

    jump letgo_501a4
