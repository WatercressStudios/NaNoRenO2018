label spirits_a1s5:
    play music bgmspirits_main fadeout 0.5

    scene spirits alex bedroom messy with dissolve

    show alx neutral1 with dissolve

    #show alex pjs sleepy

    #music house

    "When I wake up again, I try not to think about it."

    "Of course, my room is still a mess. The spirit wasn’t going to clean up for me - and why would it?"

    "I don’t feel like going to class after that - but at the same time, I don’t want to be here for a second longer."

    "I’ll tidy up after classes, I guess."

    "I pick out a shirt and skirt, brush my hair, and contemplate my parents’ photo. The glass is cracked and I don’t want anyone to see it, so I lay it face-down on the desk."

    show alx:
        ease 0.3 align (0.6,1.0)
        ease 0.1 align (0.5,1.0)
    pause 0.3
    play sound "game_letgo/sfx/Punch,Shove.ogg"
    show alx sad1 close
    #show alex tense

    "When I turn around, I feel my arm catch against something."

    #play sound crash

    show alx angry1 with dissolve

    "Is it the ghost again? I don’t have time for this right now!"

    "Or ever, really…"

    "But instead of her, it’s the box from yesterday. I kneel down and look inside to see…"

    stop music fadeout 1.0

    show spirits gun as gunicon:
        xanchor 0.5
        yalign 1.0
        xpos 0.5
        ypos 0.5
    with Dissolve(1.0)

    "A gun."

    #scene box open w/ gun

    hide gunicon
    play music bgmspirits_sthings fadeout 0.5

    show alx scared1

    #show alex shocked/surprised/horrified

    "Where did this even come from? It wasn’t there yesterday!"

    "My heart races. I need to lie down… I feel like I can’t breathe."

    "I’m horrified and overwhelmed and frantic, all in a single moment."

    show spirits gun as gunicon:
        xanchor 0.5
        yalign 1.0
        xpos 0.5
        ypos 0.5
    with Dissolve(1.0)

    "When I look again, there it is: a {b}{i}gun{/b}{/i}, in my room."

    "I could be expelled for having this! I won’t be able to explain where it came from - and even if I did, no one would believe me."

    hide gunicon

    "I need to get rid of it."

    play sound "game_spirits/sfx/Open Door.ogg"

    scene spirits dorm hallway with dissolve

    show alx angry1 at right with easeinright

    #scene hallway

    #show alex determined/upset

    "I grab my backpack and rush into the hall. Oddly enough, no one else is around…"

    "Thank god."

    "It’s as if the spirit cleared the way - as if this is some sort of test, but I’m sure there’s more to it than that."

    show alx:
        parallel:
            ease 1.0 align (0.5,1.0)
        parallel:
            pause 0.5
            ease 0.5 alpha 0
    pause 0.5
    
    scene spirits stairs with dissolve

    #hide alex

    #scene black

    "I don’t let the fear slow me down; I descend the stairs without missing a single step and feel the cool air buffet my face."

    "I haven’t even been here a day! Why did this have to happen {i}now?{/i} Where would I bury a gun?"

    scene black with dissolve

    "I run to the side of Artemis Hall and kneel down in the bushes. Pushing aside the pines, I begin to dig."

    "Thankfully, the earth is soft."

    "Once the gun is covered, I leave - hoping I can make it to my first class without being too late."

    jump spirits_a1s6
