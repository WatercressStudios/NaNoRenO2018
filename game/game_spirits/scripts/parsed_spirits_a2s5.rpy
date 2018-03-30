label spirits_a2s5:

    scene black with dissolve

    scene spirits alex bedroom clean with dissolve

    play music bgmspirits_relax fadein 3.0

    play sound "game_spirits/sfx/Clamor.ogg"

    "I wake up earlier than usual - but why?"

    "My alarm clock hasn’t gone off yet, and I almost want to fade back into sleep…"

    play sound "game_spirits/sfx/Clamor.ogg"

    "But then I hear someone grunting in the hallway, and there are objects thudding against the floor. Maybe it’s for the best."

    "It’s not like I have much of a choice anyway.."

    "During my morning ritual, I realize something:"

    "I’m behind on all of my assignments. The teachers are lenient about it, but the guilt is just building up."

    "Actually, I think I woke up because of this vague dream I had…"

    "In it, I sat in class, opened up a folder, and started sifting through the papers for a specific assignment."

    "Almost every single one was covered in red marks."

    "It’s a sign that my academic duties are being neglected… It’s all because of these ghosts just wrecking my life."

    scene spirits dorm hallway

    show alx sad1:
        xanchor 0.5
        yalign 1.0
        xpos 1.0
        ypos 1.2
        rotate -25

    show hmom sad1 at centerleft

    with dissolve

    "I look outside my room, but it’s just Jianmei moving boxes from the attic."

    scene spirits alex bedroom clean

    show alx bitter1 at right

    with dissolve

    "I would like to help, but I have a lot on my plate right now."

    "So I sit at my desk and decide to do a worksheet."

    scene black with dissolve

    "It’s an easy assignment, so I speed through it."

    "Wow… there’s a lot - and I’ve only been here a few days!"

    play sound "game_spirits/sfx/Clamor.ogg"

    "I work and work, until Jianmei’s intense racket permeates all of my senses."

    "I don’t understand how or why she’s doing it by herself."

    "I guess it doesn’t hurt to give myself a break; I have plenty of time."

    "Then I realize… I have to do laundry, too! God, I hate doing laundry."

    "I guess I have no choice but to leave my room."

    scene spirits dorm hallway

    show alx sad1:
        xanchor 0.5
        yalign 1.0
        xpos 1.0
        ypos 1.2
        rotate -25

    show hmom sad1 at center

    with dissolve

    "I open my door and peek outside; the hallway is a mess right now."

    "Jianmei hears me come out and looks over, sweat dripping down her forehead. She must be getting one hell of a workout"

    voice "C-13-1.mp3" #Alex (Bonnie Mitchel)
    alx "Would you like some help? You’re struggling a lot."

    "Maybe if I do, I’ll get some peace and quiet."

    "Besides, no one should have to deal with that much work. It’s inhumane."

    voice "C-13-2.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Oh yes! Please, please!"

    hide alx
    show alx neutral1 with dissolve:
        xanchor 0.5
        yalign 1.0
        xpos 1.0
    with dissolve

    show alx neutral1 at centerright with ease

    pause 0.3

    hide alx neutral1 with dissolve

    play sound "game_spirits/sfx/Ladder.ogg"

    "Jianmei pulls out a cloth and dabs her forehead. I climb up the ladder and see the attic for the first time."

    scene spirits loft

    show alx sad1 at centerright

    with dissolve

    "Thankfully, there isn't anything out of the ordinary. I'm dealing with enough oddities these days that a few boxes are a welcome sight."

    "Well, \"a few\" is an understatement - and each is filled with god knows what."

    "There's a broken lamp and a dilapidated rocking chair in the corner. The light's dim, which makes it hard to see things unless they’re right in front of you."

    "It smells heavily of dust and mildew. Jianmei climbs up and directs me to a few boxes that she deems takeable."

    "I two small boxes up and tuck them under my arms like suitcases - but then, from the corner of my eye, I see something slip out from underneath one."

    show spirits letter as clue at truecenter with dissolve

    "I look down; it's a piece of paper. My hands are kind of full, though, and I don’t want to waste Jianmei’s time. She's already exhausted."

    "Something keeps urging me to look at it. Ugh, do I really have to?"

    menu:
        "Read the note.":

            $ hasLetter = True

            $ duties += 1

            "\"{i}To My Dearest Cornelius Bourlon,{/i}\""

            "\"{i}I hope this letter finds you well. I must admit, I was quite shocked when I received your previous correspondence.{/i}\""

            "\"{i}While she visited before her passing, Mrs. Bourlon did not leave the grounds of my estate. I assure you, no inappropriate conduct of any sort took place.{/i}\""

            "\"{i}Furthermore, I must confess that she hardly seemed to be the sort of woman to commit the acts you inquired about.{/i}\""

            "\"{i}I am aware this is a delicate subject...{/i}\""

            "\"{i}But I knew Mrs. Bourlon to be a respectable, kind, forgiving woman. I am certain she would never even think of betraying your trust.{/i}\""

            "\"{i}Please pass along my dearest wishes to young Miss Genevieve.{/i}\""

            "\"{i}Sincerely, Mrs. Jonathan Balister{/i}\""

            if 'urname' not in questionFlags and hasDiary == False:

                $ Genevieve = "Genevieve"

                "\"Young Miss Genevieve,\" huh?"

                "Somehow, that name strikes a chord with me. I think I'd be willing to bet I've learned the name of my ghostly acquaintance."

            else:

                "...This letter mentions Genevieve."

            if hasDiary == False:

                "Her father wrote to this person asking if... if his dead wife had been fooling around?"

                "Why did it matter so much, all of the sudden?"

                "Does this have something to do with Genevieve's murder?"

            else:

                "So, at some point before he murdered his daughter - and everyone else in the house - Genevieve's father was asking friends of his late wife if she'd ever fooled around."

                "Based on his actions, I've got a feeling he'd decided on the answer."

                "But still... to murder your daughter simply because you didn't think she was your own... Who would be so depraved?"

            "Ugh, I can't think about this right now. I'll add it to my notes when I'm not standing in the middle of a mold smörgåsbord."

            hide clue with dissolve

            "Quickly folding the letter into my pocket, I heave up the boxes I can and make my way toward the stepladder."

        "Check it later.":
            $ hasLetter = False
            $ life += 1
            "I decide to put one box down and pick up the paper. I want to hurry up because I have other, more important things to do - but…"

            hide alx with dissolve

    voice "C-13-3.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Watch your step! It’s a long way down."

    voice "C-13-4.mp3" #Alex (Bonnie Mitchel)
    alx "Ha, I’ll try."

    scene black with dissolve

    play sound "game_spirits/sfx/Ladder.ogg"

    "Eventually, we clean out the attic - and by the time we’re done, I’m itching all over from the dust and filth."

    "Also my back hurts. But I’m young, I will live, and I still have a whole day ahead of me."

    stop music fadeout 1.0

    jump spirits_a2s6
