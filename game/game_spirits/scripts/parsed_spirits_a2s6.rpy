label spirits_a2s6:

    scene spirits classroom with dissolve

    play ambience "game_spirits/ambience/Classroom.ogg" fadeout 2.0 fadein 2.0

    if duties == 2:

        "Today hasn't been going much better than yesterday. I haven't been able to focus on much of anything."

        "A part of me is starting to wonder if I'm even cut out for academic life, anymore."

        "I'm just so preoccupied with all this ghost business... all the other stuff in my life is piling up."

        "Maybe tonight I'll actually have an opportunity to address some of it."

    else:

        "The rest of the day goes smoothly, for once. I'm even able to concentrate on the lectures, for a change!"

        "I guess I haven't been making much progress with the ghost, but I've been making headway in my own life, at least."

        "The last time I ever felt like this was... when Naniji got me this prosthesis, actually."

        scene spirits school hallway with dissolve

        show alx neutral1 at centerleft with dissolve

        if caelumAlive == True:

            "After lunch, Caelum found me at my locker to let me know that his research on Artemis Hall had paid off."

        else:

            "During my lunch period, mostly to satisfy my own curiosity, I looked up the history of Artemis Hall on my phone."

        "Apparently the entire premises was claimed by the state and donated to the Department of Education when the last owner of the house, a retired field officer by the name of Cornelius Bourlon, passed away."

        "He no heirs, apparently, since his only daughter, Genevieve, died of natural causes at the age of fourteen."

        if hasDiary == False:

            show alx sad1 with dissolve

            "What are \"natural causes\" for a teenage girl?"

        else:

            show alx bitter1 with dissolve

            "\"Natural causes,\" {i}yeah{/i}."

        if duties == 0 and 'urname' not in questionFlags:

            $ Genevieve = "Genevieve"

            "Anyway, I'd bet dollars to doughnuts that girl - Genevieve Bourlon - is my ghostly aggressor."

            "Probably a safe bet that Cornelius had something to do with her murder, too."

        "Still, this is something to think about some other time. I've got a huge workload piling up, and I need to start dealing with it."

    stop ambience fadeout 2.0

    scene black with dissolve

    play music bgmspirits_main

    scene spirits study room

    show alx sad1 at centerright with dissolve

    "Homework’s the worst…"

    "Actually, it’s kind of novel to be doing it; I never got any back home, since I was homeschooled."

    "The days here are so much longer than I’m used to. It’s a little wearying."

    "It’s pretty easy to get overwhelmed, too… This four-page assignment is due tomorrow, and I haven’t even started it."

    "At least Artemis Hall has a pretty swanky study room…"

    "Taking a seat at one of the computers, I boot up the word processor and put my name and tomorrow’s date in the document’s header."

    "This would be a cinch - if only Mrs. Wendell hadn’t demanded we cite five sources…"

    "After about half an hour, I finally settle into a groove. I’ve only got a single page written, but I think I’ll be able to hammer out the next three before curfew."

    "I’m finally getting to the main point of my thesis - that the way Helen Keller was covered in our textbook is woefully inadequate - when I feel the weight of a delicate hand on my prosthetic."

    "Which can only mean one thing..."

    play music bgmspirits_gen

    show gen neutral1 behind alx at centerleft with blinds

    voice "C-14-1.mp3" #Genevieve (Lasli Tran)
    gen "I’ve got something for you."

    if caelumAlive == False:
        voice "C-14-2.mp3" #Alex (Bonnie Mitchel)
        alx "Whatever."

    else:
        voice "C-14-3.mp3" #Alex (Bonnie Mitchel)
        alx "‘Kay. Gimme a sec."

    show gen angry1:
        xpos 0.6
    with ease

    pause 0.4

    play sound "game_spirits/sfx/Smashing Keyboard.ogg"

    with hpunch

    "That doesn’t seem to sit well with her. Genevieve doesn’t rake my arm, but she {i}does{/i} pick it up and bounce it repeatedly against the keyboard."

    "My painstakingly-outlined document immediately fills with line after line of nonsense - like a cat just walked across the desk."

    show alx angry1 with dissolve

    voice "C-14-4.mp3" #Alex (Bonnie Mitchel)
    alx "Dammit, seriously? Does it have to happen right now?"

    "This time, the pressure under my temples starts to build into a steadily-oscillating, throbbing pain. Even with the brightness turned down, staring into the monitor makes my eyes ache."

    "Ugh... And we were doing so well…"

    voice "C-14-5.mp3" #Genevieve (Lasli Tran)
    gen "Don't take me lightly."

    voice "C-14-6.mp3" #Genevieve (Lasli Tran)
    gen "I’ve been waiting ages for someone like you to come along - so yes, it has to happen right this second."

    "I guess she’s right, with that inspection coming up…"

    voice "C-14-7.mp3" #Alex (Bonnie Mitchel)
    alx "Why? Do you have somewhere to be?"

    "This time, her nails - the same one that dug those gouges in my bedroom - rake angry lines into my skin."

    voice "C-14-8.mp3" #Genevieve (Lasli Tran)
    gen "{i}Yes.{/i} That's the whole point."

    voice "C-14-9.mp3" #Genevieve (Lasli Tran)
    gen "I am a century late to join my mother. You will assist me in doing so."

    "She angrily yanks on my arm, trying to pull me out of the chair. She’s moving so forcefully, she almost dislocates my residual limb from the socket."

    voice "C-14-10.mp3" #Genevieve (Lasli Tran)
    gen "{i}Come.{/i}"

    menu:

        "Fine.":
            $ hasAmmo = True
            $ duties += 1
            $ secondTrueEndFlag = False
            "…Fine. Whatever. There's no hope at fighting her."

            "The sooner I get this done, the sooner she'll leave me alone."

            "And then, undoubtedly, I'll just find some brand-new disembodied spirit to jerk me around…"

            "Fuck my life…"

            show alx bitter1:
                ease 0.6 align (0.0, 1.0) alpha 0
            show gen neutral1:
                ease 0.6 align (0.0, 1.0) alpha 0

            pause 0.3

            scene black

            scene spirits upstairs lounge with dissolve

            show alx bitter1 at centerright

            show gen neutral1 at right

            with easeinright

            "Genevieve pulls me into the hallway; for a moment, I think she’s gonna drag me to Jianmei’s office - but she stops just outside and looks at one of the old bookshelves lining the corridor."

            "These things are basically just ornamental at this point - row after row of decrepit encyclopedias and other time-weathered tomes."

            voice "C-14-11.mp3" #Alex (Bonnie Mitchel)
            alx "Okay, so it's an old bookshelf. Is there a hidden passage behind it or something?"

            voice "C-14-12.mp3" #Genevieve (Lasli Tran)
            gen "Don't be foolish."

            voice "C-14-13.mp3" #Genevieve (Lasli Tran)
            gen "Second shelf from the top. {i}The Odyssey{/i}. Open it very carefully."

            show alx at left with ease

            play sound "game_spirits/sfx/Alex Sighs.ogg"

            "I sigh, seeing little reason to refuse her. Reaching out, I quickly locate the dusty old book and remove it."

            show gen at centerleft with dissolve

            voice "C-14-14.mp3" #Alex (Bonnie Mitchel)
            alx "Oh, gross. This is the Cary translation. Morris is way better…"

            show gen angry1:
                easein 0.4 xpos 0.275

            voice "C-14-15.mp3" #Genevieve (Lasli Tran)
            gen "Shut up and open it already!"

            show alx angry1 with dissolve

            voice "C-14-16.mp3" #Alex (Bonnie Mitchel)
            alx "Shooting her an aggravated glare, I sigh and crack the book open."

            "It’s been hollowed out on the inside - the lingering outer edges of the pages are stuck together by beeswax or resin."

            "Inside the hollow is a small cardboard box. Something inside clinks loudly when I shake it."

            "Its exterior is printed with a once-colorful label:"

            show spirits ammo as ammunition at truecenter with dissolve

            voice "C-14-17.mp3" #Alex (Bonnie Mitchel)
            alx "Forty-one Long Colt center fire two-hundred grain bullet…"

            "I sigh a second time."

            voice "C-14-18.mp3" #Alex (Bonnie Mitchel)
            alx "Ammunition? This is... ammo."

            show gen neutral1 with dissolve

            voice "C-14-19.mp3" #Genevieve (Lasli Tran)
            gen "Yes."

            if hasLetter == True:

                voice "C-14-20.mp3" #Alex (Bonnie Mitchel)
                alx "For the gun your father used to kill everybody?"

                show gen sad1 with dissolve

                voice "C-14-21.mp3" #Genevieve (Lasli Tran)
                gen "Right."

            else:

                "For the gun Genevieve keeps leaving in my room, I'd guess."

                "Another thing I'm going to have to hide away to avoid expulsion... {i}Great.{/i}"

            hide ammunition with dissolve

            voice "C-14-22.mp3" #Alex (Bonnie Mitchel)
            alx "…Okay?"

            voice "C-14-23.mp3" #Alex (Bonnie Mitchel)
            alx "What does this tell me that I didn't already know?"

            show gen angry1 with dissolve

            voice "C-14-24.mp3" #Genevieve (Lasli Tran)
            gen "It's evidence! Just hold onto it."

            voice "C-14-25.mp3" #Alex (Bonnie Mitchel)
            alx "…Fine."

            voice "C-14-26.mp3" #Alex (Bonnie Mitchel)
            alx "This was {i}clearly{/i} worth the distraction."

            voice "C-14-27.mp3" #Genevieve (Lasli Tran)
            gen "Deal with it. I'll return later."

            hide gen with dissolve

            "Before I can get another word in, she dissipates, her presence departing from the room."

            scene black with dissolve

            scene spirits alex bedroom clean with dissolve

            "Placing the empty shell back onto the shelf, I head to my room and stash away the new \"clue.\" Getting seen with a box of ammo wouldn’t work out much better than getting caught with a gun."

            "Afterwards, I roll onto the bed like a beached whale and just listen to the sound of my own breathing."

            "In a distant room, I can barely hear two of my housemates joyfully singing some pop song I’ve never heard before."

            "I feel tired. Too defeated to move."

            "Eventually, I realize I still have my half-completed assignment on the computer downstairs."

            "Eh. Screw it."

            "Not like any of this matters anyway."

        "No!":
            $ hasAmmo = False
            $ life += 1
            "You know what? I think I've had enough of this."

            show alx angry1:
                easein 0.2 xpos 0.9
            show gen surprised1:
                easein 0.3 xpos 0.75
            with hpunch

            "With all my strength, I forcefully, violently rip my arm back."

            "Genevieve doesn't let go - but she does give a little murmur of surprise, as if she… lost her footing?"

            voice "C-14-28.mp3" #Genevieve (Lasli Tran)
            gen "Have you lost your mind--"

            voice "C-14-29.mp3" #Alex (Bonnie Mitchel)
            alx "You know what, Genevieve? Go fuck yourself."

            voice "C-14-30.mp3" #Alex (Bonnie Mitchel)
            alx "I don't care what you've been through, or how long you've waited."

            voice "C-14-31.mp3" #Alex (Bonnie Mitchel)
            alx "Did you simply assume that because I had brown skin, I'd just be another one of your servants? Piss off. It's the twenty-first century."

            show gen:
                easein 0.7 xpos 0.725

            "She pauses for a moment, her grip slackening. I can tell from the look on her translucent face that I've caught her off-guard."

            show gen angry1 with dissolve

            voice "C-14-32.mp3" #Genevieve (Lasli Tran)
            gen "How cavalier of you. If you even knew how much I've suffered--"

            if caelumAlive == False:
                voice "C-14-33.mp3" #Alex (Bonnie Mitchel)
                alx "You wanna know who’s suffered? My friend. Caelum Bentley. He’s gone missing, and his room reeks of death."

                voice "C-14-34.mp3" #Alex (Bonnie Mitchel)
                alx "You wouldn’t happen to know anything about that, would you?"

                "This time, her grip parts entirely. I almost think I’ve ended the conversation right there - but it returns after a few moments, and her outline again materializes into view."

                "Genevieve looks uncomfortable with the subject."

                show gen sad1 with dissolve

                voice "C-14-35.mp3" #Genevieve (Lasli Tran)
                gen "I… was uncertain. But I did suspect."

                voice "C-14-36.mp3" #Genevieve (Lasli Tran)
                gen "It was the other who killed him. I… my memory fails me often, but I’m certain I’ve never taken a life."

                voice "C-14-37.mp3" #Alex (Bonnie Mitchel)
                alx "Why should I trust any of you? Do you have any idea what you and your kind have put me through?"

                show alx bitter1 close with dissolve

                "Again, a sizzling, trenchant pain feathers along my wrist - and I have to bite my lip to avoid screaming."

                voice "C-14-38.mp3" #Genevieve (Lasli Tran)
                gen "Don’t forget: I still have the power to get you expelled from your beloved academy."

                show alx angry1 with dissolve

                voice "C-14-39.mp3" #Alex (Bonnie Mitchel)
                alx "More threats. Way to reassure me you’re not a murderer."

            else:
                voice "C-14-40.mp3" #Alex (Bonnie Mitchel)
                alx "You think you're the only one who's suffered? Hey, I have to put up with {i}your{/i} bullshit every day."

                voice "C-14-41.mp3" #Alex (Bonnie Mitchel)
                alx "Yours and every {i}other{/i} ghost’s."

                voice "C-14-42.mp3" #Alex (Bonnie Mitchel)
                alx "Hell, at least you'll {i}get{/i} to see your mom again. My parents are gone."

                voice "C-14-43.mp3" #Genevieve (Lasli Tran)
                gen "…What? False. When you pass…"

                voice "C-14-44.mp3" #Alex (Bonnie Mitchel)
                alx "…I'm going to reincarnate, just like they have. We're {i}Hindu{/i}."

            if duties > 0:
                $ secondTrueEndFlag = True

                "She silently considers my words with a plaintive frown, clutching a lock of her spectral curls."

                voice "C-14-45.mp3" #Alex (Bonnie Mitchel)
                alx "I'm here for you. I'm going to help you cross over. But don't you dare forget whose life this is, and who's living it - not for one second."

                voice "C-14-46.mp3" #Genevieve (Lasli Tran)
                gen "Hmmph. You're more of a bearcat than I took you for."

                voice "C-14-47.mp3" #Alex (Bonnie Mitchel)
                alx "I don't know what that means, but sure, thanks."

                voice "C-14-48.mp3" #Genevieve (Lasli Tran)
                gen "I’ll… leave you be, then. For the moment."

                voice "C-14-49.mp3" #Genevieve (Lasli Tran)
                gen "But you should prepare yourself. We'll be putting an end to all of this shortly."

                voice "C-14-50.mp3" #Alex (Bonnie Mitchel)
                alx "Fine. Noted."

                hide gen with Dissolve(1.5)

                stop music fadeout 1.0

                "She dissipates, and I can feel the sensation of her hand evaporating on the spectral residue of my arm."

                "I actually won this round…"

                "Maybe I don't have to be pushed around anymore…"

                if caelumAlive == False:
                    "Maybe it’s time for me to be {i}doing{/i} the pushing."

                else:
                    "Despite myself, I feel a proud little smile curling on my face."

            else:
                $ secondTrueEndFlag = False

                voice "C-14-51.mp3" #Alex (Bonnie Mitchel)
                alx "Look, maybe I'll help you cross over and maybe I won't. It's not your choice to make for me."

                voice "C-14-52.mp3" #Alex (Bonnie Mitchel)
                alx "But this is {i}my{/i} time on this earth, and you will not arbitrate how I spend it."

                show gen angry1:
                    easein 0.1 xpos 0.75
                show alx angry1 close with dissolve
                with hpunch

                "That makes her dig in more deeply than she has before - easily enough to break the skin, if there was actually any there."

                "I can literally see my plastic prosthetic warping under the pressure."

                play sound "game_spirits/sfx/Alex Scream.ogg"

                voice "C-14-53.mp3" #Alex (Bonnie Mitchel)
                alx "Aaaaiiiiee!"

                stop sound

                "But then, all the pain suddenly stops."

                voice "C-14-54.mp3" #Genevieve (Lasli Tran)
                gen "You know… I've just realized something."

                voice "C-14-55.mp3" #Genevieve (Lasli Tran)
                gen "I thought I needed your help to get out of this blasted mausoleum."

                voice "C-14-56.mp3" #Genevieve (Lasli Tran)
                gen "But I can do it all on my own."

                voice "C-14-57.mp3" #Genevieve (Lasli Tran)
                gen "Goodbye for now. Enjoy your precious free time."

                hide gen with Dissolve(2.0)

                show alx sad1 with dissolve

                "She vanishes, and I can't help but feel a bit nervous."

                "It can't have been as easy as that, can it?"

                "Am I free?"

    jump spirits_a2s7
