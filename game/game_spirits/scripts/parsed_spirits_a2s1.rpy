label spirits_a2s1:
    if caelumAlive == True:
        jump spirits_a2s1_alive
    jump spirits_a2s1_dead

label spirits_a2s1_alive:

    scene black with dissolve

    "When Caelum leaves, I realize I’m still nervous; it all returns in an instant - from the knot in my stomach to the lump in my throat."

    "What the spirit told me yesterday keeps echoing in my head; I even dreamed of searching for the \"last step.\""

    play music bgmspirits_main fadeout 0.5

    scene spirits alex bedroom clean with dissolve

    show alx neutral1 with dissolve

    "Of course, as soon I wake up, I don’t remember what it looks like or the process of finding it."

    "Then again, the dream could have been wrong."

    "Usually, I believe that dreams are prophetic - typically warnings - but I don’t think an answer will come so easily this time."

    "I guess I’ll have to search for it with every ounce of my energy. "

    show alx neutral1 close with dissolve

    "I try doing some breathing exercises while I go through my morning routine."

    "After all, the amount of stuff I’ve been dealing with lately should send me to the hospital with some kind of heart trouble."

    show alx neutral1:
        ease 1 align (0.2,1.0)
        ease 2 align (0.8,1.0)
        ease 1 align (0.5,1.0)

    "I pace back and forth to burn off nervous energy, because something is telling me I’m just waiting for another surprise."

    "I think I just really need to calm down. A lot."

    show alx neutral1 close with dissolve

    "I breathe in one more time and twist my doorknob..."

    play sound "game_spirits/sfx/Open Door.ogg"
    play music bgmspirits_cae

    show alx surprised1:
        ease 0.2 align (0.2,1.0)

    show cae scared1 at right with easeinright

    voice "C-9-1.mp3" #Caelum (Daniel Acosta)
    cae "OH MY GOD, ALEX."

    "Caelum rushes into my room and doesn’t even give me a chance to speak. He almost knocks me over - and just as I’m about to yell at him; I notice his expression…"

    voice "C-9-2.mp3" #Caelum (Daniel Acosta)
    cae "When I left your room last night, I was walking in the hallway. There’s was no one around."

    voice "C-9-3.mp3" #Caelum (Daniel Acosta)
    cae "But I felt this cold breeze and there were chills going down my spine."

    voice "C-9-4.mp3" #Caelum (Daniel Acosta)
    cae "I saw it:  a monster, a huge smoke cloud."

    voice "C-9-5.mp3" #Caelum (Daniel Acosta)
    cae "It was coming after me. It knows me, and it wants me under its grip."

    voice "C-9-6.mp3" #Caelum (Daniel Acosta)
    cae "I held out my crucifix, since I didn’t know what else to do, and when I turned around, it was {i}charging{/i} toward me--"

    voice "C-9-7.mp3" #Caelum (Daniel Acosta)
    cae "And it was holding up something…. sharp? Almost like a spade, I think?"

    voice "C-9-8.mp3" #Caelum (Daniel Acosta)
    cae "And I didn't even think. I just hurled my crucifix at it and ran."

    show alx sad1 with dissolve

    "Caelum is wearing a mixture of confusion and fear; he’s second-guessing everything he has just seen - but I believe him. After what I’ve experienced, I almost have to."

    voice "C-9-9.mp3" #Caelum (Daniel Acosta)
    cae "N - no biggie, I mean, that crucifix was just a gift from my dad anyway, so I was going to pawn it off first chance I got…"

    show cae scared1:
        ease 1 align (0.5,1.0)

    "I lead him to my bed, give him pillows, and an animal plush… but nothing’s working."

    voice "C-9-10.mp3" #Caelum (Daniel Acosta)
    cae "Alex, I don’t completely know what you’re going through and I don’t think anyone else will believe it - but I want you to know that I do."

    voice "C-9-11.mp3" #Caelum (Daniel Acosta)
    cae "I don’t know what’s going to happen after this."

    voice "C-9-12.mp3" #Caelum (Daniel Acosta)
    cae "Can I just stay here for awhile?"

    "I want to say that he shouldn’t be here, but I let him stay anyway."

    "Silence hangs between us for several long moments; we sort of bask in each other’s presence, despite the tension."

    scene spirits dorm hallway with dissolve

    show alx sad1 at right with dissolve
    show cae scared1 at left with dissolve

    "When he finally leaves, I watch him walk down the hall. He looks back at me as if fearing it’ll be the last time we ever see one another…"

    hide cae with dissolve

    "But somehow, I don’t think so."

    stop music

    jump spirits_a2s2


label spirits_a2s1_dead:
    #continuing from Act 1 Scene 7, fade into Genevieve’s theme

    scene spirits alex bedroom night clean with dissolve

    show alx sad1 close with dissolve

    "..."

    show alx sad1 with dissolve

    "And in the end, I’m wide awake at three in the morning."

    "Shit."

    show alx surprised1 with dissolve

    "How did Caelum even get in here, anywhere?"

    show alx neutral1 close with dissolve

    "Actually, I probably just left my door unlocked. Naniji always used to call me out on it…"

    show alx sad1 close with dissolve

    "...And Mom, and Dad too."

    voice "C-9-13.mp3" #Papa (N/A)
    Dad "Oooooh, it’s the curse of \"constantly forgetting to lock your door!\""

    voice "C-9-14.mp3" #Papa (N/A)
    Dad "{i}Ooooooooh!{/i}"

    show alx sad1 close with dissolve

    "...Fuck."

    "I don’t want to think about that."

    "If I go any further down that rabbit hole, I’m going to start screaming again; then Caelum will come running back again, and we’ll just repeat the same events."

    "This has to be another dream."

    "All of it."

    "The ghosts, the school, Caelum, my parents…"

    "I just wish I could forget about all of this for once."

    "Or wake up - that would be nice."

    "I’ll go insane if I don’t."

    "Sometimes, I can’t even tell what’s real and what’s in my head."

    "I’m doubting everything I know, because I can’t have confidence in anything."

    "Even the laws of physics hate me; what if it’s just a poltergeist, instead of gravity?"

    "Very funny, Alex."

    "Is going my parents’ way better than whatever {i}this{/i} is?"

    "No. I don’t want that at all."

    "I’d be giving up on myself if I chose that path."

    "Everything up to this point would have been for nothing. I’m not going to let that happen - that much is true."

    "Whether it’s for Naniji’s sake, Mom’s, Dad’s, Caelum’s, or some ghost’s…"

    "Even for my own..."

    "I’m not going to let this break me."

    "I’m not going to let this chance go to waste."

    "I’ll have to promise myself that, if anything."

    "...But for now, I should sleep."

    "If I can’t, I’ll just… relax until morning."

    scene black with dissolve

    "I can figure out what to do then."

    $renpy.pause(1.0, hard = True)

    #fade to black, hang here for a while

    show red:
        alpha 0.8

    play sound "game_letgo/sfx/crush.ogg"

    #cut to bloody visual effect or tint the screen dark red with some screen shake, give a gruesome sound-effect like a shovel bashing into a head.

    #hang here for a bit more

    $renpy.pause(1.0, hard = True)

    "What the hell?"

    stop ambience

    play music bgmspirits_wra

    #wraith’s theme

    "There’s a sound..."

    play sound "game_letgo/sfx/crush.ogg"

    show red
    with hpunch

    #repeat screen shake and sound effect

    "No, a {i}cacophony{/i} - and a loud one, at that."

    "It’s coming from somewhere, but where."

    "Where it is coming from?"

    play sound "game_letgo/sfx/crush.ogg"

    "It’s painful."

    "It hurts!"

    "What is this!?"

    play sound "game_letgo/sfx/crush.ogg"

    #repeat repeatedly more

    "What is this?"

    "It {i}burrows{/i} into my ears, unrelentingly."

    "I hate it."

    "It won’t stop."

    "It’s painful."

    "So painful..."

    "And it’s hateful, whatever it is."

    play sound "game_letgo/sfx/crush.ogg"

    #repeat repeatedly

    "Full of pain, disgust, misery, and {i}hatred.{/i}"

    "And hatred, and hatred, and hatred, and hatred."

    "Hatehatehatehatehatehatehatehatehatehatehatehatehatehate."

    "I hate this!"

    "Why won’t it stop…?"

    "For hours."

    "For days."

    "For years."

    "How long has this been going on?"

    "How much {i}hate{/i} can one sound hold?"

    play sound "game_letgo/sfx/crush.ogg"

    $renpy.pause(2.0, hard = True)

    play sound "game_letgo/sfx/crush.ogg"

    $renpy.pause(2.0, hard = True)

    play sound "game_letgo/sfx/crush.ogg"

    #repeat repeatedly, before shifting back to Alex’s room BG

    play music bgmspirits_main

    show spirits alex bedroom clean with dissolve

    show alx sad1 close with dissolve

    "Morning."

    play sound "game_letgo/sfx/crush.ogg" fadeout 1.0 fadein 1.0

    "The noise has slowed down…"

    play sound "game_letgo/sfx/crush.ogg" fadeout 1.0 fadein 1.0

    "But it refuses to stop."

    play sound "game_letgo/sfx/crush.ogg" fadeout 1.0 fadein 1.0

    "Why won’t it?"

    play sound "game_letgo/sfx/crush.ogg" fadeout 1.0 fadein 1.0

    "I get up and try to ignore it."

    play sound "game_letgo/sfx/crush.ogg" fadeout 1.0 fadein 1.0

    "It’s time to go to school."

    stop music

    jump spirits_a2s2
