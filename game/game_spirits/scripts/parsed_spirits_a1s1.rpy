label spirits_a1s1:
    #do some sort of fading into the background from the title splash at the end of Scene 0.  Should be something outside related to the school or the dorm

    pause 3.0

    #hang at the screen for a bit with either House or Relaxed/School music to set the tone before moving to the text

    play music bgmspirits_relax

    "Our cab drives up to the school building, comes through the gates, and stops at the curb."

    "I grab my bags and walk into the dorm - only to run into a smiling woman the second I cross the threshold."

    scene spirits foyer

    show hmom happy1 at centerleft

    show alx neutral1 at centerright

    with dissolve

    #show hmom happy/welcoming

    #show alex relaxed/neutral

    voice "C-2-1.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Hello! Are you Alex Kartha?"

    "I nod."

    voice "C-2-2.mp3" #House Mother "Jianmei" (Vivi)
    hmom "G-Greetings! I’m Fang Jianmei, the school’s housemother. You can call me Sam."

    voice "C-2-3.mp3" #House Mother "Jianmei" (Vivi)
    hmom "...Or Jian, or Sam-Jian, or Mother. Anything will work, really!"

    "Jianmei is youthful at a glance, but up close… she has enough wrinkles to be at least thirty or forty years old."

    "She keeps grinning, but is clearly out of breath for something. Does her job keep her {i}that{/i} busy? And more importantly: why is she running around in heels?"

    "...How does she not trip?"

    voice "C-2-4.mp3" #Alex (Bonnie Mitchel)
    alx "Yeah, I’m Alex. It’s nice to be here."

    voice "C-2-5.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Glad to hear it! Welcome to Oxton Academy, Alex!  Do you need help with your bags?"

    voice "C-2-6.mp3" #Alex (Bonnie Mitchel)
    alx "N-No thanks; I’ve got it."

    #show house mother neutral/upset
    show hmom sad1 with dissolve

    voice "C-2-7.mp3" #House Mother "Jianmei" (Vivi)
    hmom "No, seriously! I can help! It must be hard with that arm, so I can assist you!"

    #show alex exasperated
    show alx sad1 with dissolve

    voice "C-2-8.mp3" #Alex (Bonnie Mitchel)
    alx "You don’t need to, please! I’m used to it."

    voice "C-2-9.mp3" #House Mother "Jianmei" (Vivi)
    hmom "...Are you sure?"

    show alx bitter1 with dissolve

    voice "C-2-10.mp3" #Alex (Bonnie Mitchel)
    alx "Yes, absolutely."

    "My bags aren’t that heavy - but at this point, I probably wouldn’t be able to say yes even if they were filled with bricks."

    "My stubbornness is probably going to get me killed one of these days..."

    voice "C-2-11.mp3" #House Mother "Jianmei" (Vivi)
    hmom "...Okay."

    #show house mother welcoming/happy
    show hmom happy1 with dissolve

    voice "C-2-12.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Regardless, welcome to Oxton again! Come now, hurry! Let’s get you to your room!"

    show hmom:
        easein 0.6 xpos 0.5

    pause 1.5

    voice "C-2-13.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Alex, what are you waiting for!? You can move faster than-- Ah!"

    show hmom:
        rotate -5
        ypos 1.1
    with dissolve

    play sound "game_spirits/sfx/Thud.ogg"

    show hmom:
        easein 0.2 ypos 1.8
    with vpunch

    pause 0.2

    show alx sad1 with dissolve

    hide hmom with easeoutbottom

    "Ah, she fell."

    #show house mother flustered
    show hmom sad1 close at center with easeinbottom

    voice "C-2-14.mp3" #House Mother "Jianmei" (Vivi)
    hmom "I-I’m fine, everyone! I just tripped."

    "...Does this happen often?"

    scene black with dissolve

    pause 0.5

    scene spirits upstairs lounge with dissolve
    #scene artemis house hallway

    show hmom happy1 close at center

    show alx neutral1 at centerright

    with dissolve

    "Jianmei guides me through the carpeted halls; the floor below screams with every step as if it’ll crumble under our weight."

    "Expensive art pieces hang on the walls - more than I can count on my fingers. The windows opposite are colorful, and seem like they’d be more fitting in a chapel."

    "Expensive lights and chandeliers hang from the ceiling from threads that look like they haven’t been repaired in fifty years - if that."

    voice "C-2-15.mp3" #House Mother "Jianmei" (Vivi)
    hmom "So! What do you think? Great place, isn’t it?"

    #show alex neutral/small smile

    voice "C-2-16.mp3" #Alex (Bonnie Mitchel)
    alx "It’s… nice. I think I’ll be able to settle in here just fine."

    show hmom sad1 with dissolve

    voice "C-2-17.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Are you okay?"

    show alx sad1 with dissolve

    voice "C-2-18.mp3" #Alex (Bonnie Mitchel)
    alx "Well, yes. Why?"

    voice "C-2-19.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Like… you seem sad somehow. - or tense. Anxious, maybe?  Un-relaxed."

    show alx angry1 blush with dissolve

    voice "C-2-20.mp3" #Alex (Bonnie Mitchel)
    alx "R-Really, there’s no need to worry about that."

    voice "C-2-21.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Well, my instincts are rarely wrong. Are you uncomfortable?"

    show alx bitter1 close with dissolve

    voice "C-2-22.mp3" #Alex (Bonnie Mitchel)
    alx "I’m fine. Please."

    "I’m fine."

    "{i}I’m fine.{/i}"

    "{i}{b}I’m fine.{/b}{/i}"

    "There’s nothing wrong here… Everything is going to be okay."

    voice "C-2-23.mp3" #House Mother "Jianmei" (Vivi)
    hmom "...You can talk to me if you want?"

    show alx sheepish1 with dissolve

    voice "C-2-24.mp3" #Alex (Bonnie Mitchel)
    alx "It’s really nothing. Things at home just… get a little stressful is all."

    #show house mother confused

    voice "C-2-25.mp3" #House Mother "Jianmei" (Vivi)
    hmom "How so?"

    voice "C-2-26.mp3" #Alex (Bonnie Mitchel)
    alx  "Well, let’s say things... feel {i}off,{/i} somehow. Certain memories rile me up, so I’m still trying to relax and adjust."

    voice "C-2-27.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Does it have to do with how you lost your arm?"

    show alx bitter1 with dissolve

    "I can feel her {i}staring{/i} at it. Why does everyone always ask that? I’m sick of talking about it!"

    #show alex tense

    voice "C-2-28.mp3" #Alex (Bonnie Mitchel)
    alx "I don’t want to talk about it."

    show hmom happy1 with dissolve
    #show house mother smile

    voice "C-2-29.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Alright. Well, maybe some smiles would help then?"

    voice "C-2-30.mp3" #Alex (Bonnie Mitchel)
    alx "I’ll be fine, there’s no need--"

    voice "C-2-31.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Please, Alex? {i}Pleeeeease!{/i}"

    show alx bitter1 close blush with dissolve

    "..."

    show alx sheepish1 with Dissolve(1.5) #show alex awkward

    "I curve my mouth upwards and into a smile."

    "...It feels unnatural, like trying to screw in a nail with a rope."

    show hmom happy1 close with dissolve

    voice "C-2-32.mp3" #House Mother "Jianmei" (Vivi)
    hmom "See? You look better already!"

    "I appreciate her good intentions, but this is the last thing I need right now."

    #show alex relaxed/neutral

    voice "C-2-33.mp3" #Alex (Bonnie Mitchel)
    alx "Thank you. How much longer to the room?"

    voice "C-2-34.mp3" #House Mother "Jianmei" (Vivi)
    hmom "It’s at the end of this hall. Follow me!"

    show alx sheepish1:
        ease 0.6 align (1.0, 1.0) alpha 0
    show hmom happy1:
        ease 0.6 align (1.0, 1.0) alpha 0

    pause 0.2

    scene black with dissolve

    "We round another corner, and come across a hall that seems to go on for an eternity."

    "Each door that we pass by takes longer to reach than the last - until finally, we reach the end."

    "Jianmei stands by it, practically bouncing on her heels."

    scene spirits dorm hallway

    show hmom happy1 close: #show house mother happy
        xanchor 0.5
        yalign 1.0
        xpos 0.4
        ypos 1.03

    show alx neutral1:
        xanchor 0.5
        yalign 1.0
        xpos 0.6
        ypos 1.03

    with dissolve

    pause 0.2

    show hmom:
        linear 0.1 ypos 1.0
        linear 0.1 ypos 1.03

    voice "C-2-35.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Do you wanna open it, or should I?"

    show alx sheepish1 with dissolve

    voice "C-2-36.mp3" #Alex (Bonnie Mitchel)
    alx "Can I?"

    show hmom sad1 with dissolve

    voice "C-2-37.mp3" #House Mother "Jianmei" (Vivi)
    hmom "That’s fine, that’s fine!"

    "I swear, she sounds disappointed."

    show alx neutral1 at right with ease

    pause 0.2

    play sound "game_spirits/sfx/Open Door.ogg"

    stop music fadeout 1.0

    scene black with dissolve

    scene spirits alex bedroom empty

    with dissolve

    show alx neutral1 at centerright with easeinright

    pause 1.0

    play music bgmspirits_main

    "The room is small, but nice. There’s a twin bed on one side, a closet next to the door, and some sort of… weird tiny door, too?"

    show alx sheepish1 at center with ease

    pause 0.75

    show hmom happy1 at right with easeinright

    voice "C-2-38.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Room 5-22, the twenty-second room in the fifth hall."

    voice "C-2-39.mp3" #House Mother "Jianmei" (Vivi)
    hmom "How do you like it? It’s a bit less renovated than the others, but we had to make do  since this was on such short notice."

    voice "C-2-40.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Don’t ask about the door; it’s been closed as long as I’ve been working here. I think it leads nowhere anyway, so… nothing to worry about!"

    show alx scared1 with dissolve

    "That’s exactly what someone would say if there {i}was{/i} something to worry about."

    show alx sheepish1 with dissolve

    voice "C-2-41.mp3" #Alex (Bonnie Mitchel)
    alx "...I like it. It’s quieter than something closer to the entrance, and it seems pretty comfortable."

    voice "C-2-42.mp3" #House Mother "Jianmei" (Vivi)
    hmom "That’s great, Alex!  Do you need anything, or can you get things put away on your own?"

    show alx happy1 with dissolve

    voice "C-2-43.mp3" #Alex (Bonnie Mitchel)
    alx "I’ll be fine. It’s easier to do this kind of stuff alone."

    voice "C-2-44.mp3" #House Mother "Jianmei" (Vivi)
    hmom "Alright, your room keys are on the desk. Have fun!"

    hide hmom with easeoutright

    #hide house mother

    #show alex relieved

    "Jianmei closes the door behind her - and at long last, I’m left alone."

    show alx sad1 with dissolve

    voice "C-2-45.mp3" #Alex (Bonnie Mitchel)
    alx "Finally…"

    show alx sad1 at left with ease

    pause 0.1

    hide alx with dissolve

    "I crash onto the bare mattress as soon as I’m alone. That… was not very easy."

    "Never in my life could I have imagined a housemother would be the scariest thing at boarding school."

    "I always expected it’d be bullies, or homework, or haunted dorm rooms."

    "Naniji would find this hilarious, I’m sure."

    "She’d be laughing her head off and I’d never hear the end of it."

    scene black with dissolve

    "After a few minutes of doing nothing, I get up and start pulling things out of my bags."

    scene spirits alex bedroom clean

    show alx happy1 at centerright

    with dissolve

    "I make the bed, hang up my clothes, and set my watercolours and used textbooks on the desk."

    "Come to think of it, Naniji and I bought these in quite a hurry… I haven’t even had time to look at them."

    show alx neutral1 at center with ease

    play sound "game_spirits/sfx/Thud.ogg"

    pause 0.35

    "As I move closer to the tiny door from earlier, however, my prosthetic swings a little too enthusiastically and bangs against the lock."

    stop music

    show alx scared1 with dissolve

    "My heart sinks and my stomach churns. It hasn’t done this since--"

    #show alex confused

    "What the hell?"

    play music bgmspirits_gen

    hide alx

    show spirits alex bedroom clean:
        zoom 2.5
        ease 0.6 xalign 0.8 yalign 0.18

    pause 0.65

    show spirits clawmarks as claws:
        xpos 0.515 ypos 0.09

    with dissolve


    "On closer inspection, the door is covered in scratches and claw marks."

    "Almost like… small fingers, covered in blood, tried to tear it open."

    "I don’t like this."

    "{i}I don’t like this at all.{/i}"

    #show alex horrified

    "Why is this here?"

    "What {i}is{/i} this, even?"

    "Why is this here!?"

    "This isn’t normal, this isn’t normal."

    "This shouldn’t be here..."

    "This shouldn’t--"

    play sound "game_letgo/sfx/Punch,Shove.ogg"

    scene white
    pause 0.01
    scene black

    #quick white flash before screen cuts to black.

    scene spirits alex bedroom clean

    show alx angry1 close at center

    with dissolve

    #show alex shocked/in pain

    voice "C-2-46.mp3" #Alex (Bonnie Mitchel)
    alx "Ow!"

    voice "C-2-47.mp3" #Alex (Bonnie Mitchel)
    alx "Ugh..."

    show alx angry1 with dissolve

    voice "C-2-48.mp3" #Alex (Bonnie Mitchel)
    alx "That hurt! Like, {b}{i}really{/i}{/b} hurt."

    "My head--"

    "This is going to trigger a migraine, isn’t it? It better not! I can’t deal with that today."

    show alx sad1 with dissolve

    "What the hell hit me, anyway?"

    #show alex confused

    "I look up toward the ceiling. There’s nowhere for things to fall from."

    scene spirits box closed with dissolve

    "When I turn around, there’s an upturned box laying on the floor."

    "It has an arched lid and is made of pine, but there’s metal woven into the material."

    "Why is it here? I sure as hell didn’t bring it."

    "Does it belong to the school? More importantly: how did it hit my head?"

    #choice, open the box or don’t open.
    menu:
        "..."

        "Open it.":
            #play relaxed/school

            "...There shouldn’t be anything dangerous in there; it’s just a silly box."

            #Choose to open

            "..."

            #some sort of a heartbeat sound effect

            "..."

            "I click the lock on it open and raise the top..."

            scene spirits box open with dissolve

            "..."

            "...It’s empty."

            #show alex awkward

            #play relaxed/school

            "Thank god for that. I didn’t know if I was about to scream or not."

        "Don't open it.":
            #show alex flustered

            "N-No. It’s impolite to just go looking around like that."

    "I need to stop freaking out. I’m overreacting to everything."

    "Besides, I’m not going back there - never again."

    #merge paths here

    scene spirits alex bedroom clean

    show alx bitter1:
        xanchor 0.5
        yalign 1.0
        xpos 0.6
        ypos 1.3

    pause 0.2

    show alx bitter1:
        easein 0.8 ypos 1.0

    pause 0.2

    #scene alex’s bedroom v0

    #show alex relaxed

    show alx sad1 at centerleft with ease

    "I slide the box under my bed for now. It seems like the best place for it, for the time being."

    "It probably just fell from one of the shelves above the door."

    "...And I’m probably just imagining things."

    "Probably."

    "...I need to calm down."

    "It’s okay. Everything’s okay."

    "Everything’s going to be fine."

    jump spirits_a1s2
