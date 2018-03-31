label spirits_a2s7:
    scene spirits alex bedroom clean with dissolve

    show alx angry1 at centerright with dissolve

    play music bgmspirits_main fadeout 0.5

    #scene alex’s bedroom v1 

    #show alex concentrating 

    #play music house 

    if life == 3:
        "Sitting down at my desk, I pull up one of my assigned readings for English. I’m behind, but if I work hard, I can catch up." 

        "After several minutes of reading, I feel....{i}her{/i} tugging at my arm again." 

        "What does she want this time? I’m done, I’m not going to listen. She can do what she wants, but she can’t control me." 

        show alx surprised1 with dissolve
        #show alex in pain

        "As I ignore her, the pain in my arm increases. A dull, throbbing agony begins to pound on my head as well." 

        "Fine! If that’s how she wants to play it... I stand up and grab my pain medication, taking a low dose that will at least take care of the pain in my temple." 

        "Ugh, she’s still pulling?"

        "Screw it. I reach into my blouse, above my bra strap, and unbuckle my prosthetic arm. With Genevieve pulling so hard on it, it comes flying out of my flaccid sleeve like a rocket."

        show alx happy1 with dissolve
        "I can hear Genevieve cursing at the far end of the room, and can’t help but smile."

        "Now I can finally get back to--"

        play sound "game_letgo/sfx/Punch,Shove.ogg"
        stop music fadeout 0.1
        show alx surprised1 close with hpunch:
            linear 0.2 rotate -30 align (0.4,0.0)
            pause 0.2
            easeout 0.5 rotate -50 pos (0.2,0.8)

        "A powerful force slams into me so hard it knocks me out of my chair. My whole body careens into the floor, the back of my head painfully kissing the hardwood."

        "What the--"

        show gen angry1 at center:
            alpha 0.0
            linear 3 alpha 1
        pause 1

        "It’s Genevieve. She’s wrangling my whole body. It’s not just my arm; somehow, it’s like she’s physically sitting on my chest."

        "I can the outline of her spirit… she’s not grabbing me at all. In fact, I can’t tell where my arm ends and hers begins."

        voice "C-15-1.mp3" #Alex (Bonnie Mitchel)
        alx "Genevieve! Cut it out--"

        show gen:
            linear 1 ypos 1.05
        "Is she… It’s like she’s slithering {i}up{/i} my arm, into…?"

        play music bgmspirits_gen fadeout 0.5

        voice "C-15-2.mp3" #Alex (Bonnie Mitchel)
        alx "Oh my god. Genevieve. What are you doing? You can’t-- Please, you can’t--"

        show gen:
            linear 1 ypos 1.1

        "But she is. She’s going {i}inside{/i} me. I can {i}feel{/i} her, like two arms in one sleeve!"

        show gen:
            linear 1 ypos 1.15

        "My legs are already going numb. No - the feeling is incomprehensible, as if my brain has no idea how to make sense of the sensation."

        show gen:
            linear 1 ypos 1.2

        "I can see my limbs thrashing, but I have no idea if {i}I’m{/i} the one moving them."

        "No. No, no, no. Please, god, no."

        voice "C-15-3.mp3" #Alex (Bonnie Mitchel)
        alx "Get out! Dammit, get out! This isn’t funny!"

        show gen:
            linear 1 ypos 1.25

        "And then.. I stop. My legs settle themselves, and I can feel them again - but I can’t move them at all. They won’t even budge."

        voice "C-15-4.mp3" #Alex (Bonnie Mitchel)
        alx "Genevieve! Please! I’ll do whatever you want; just don’t do this!" 

        show gen:
            linear 1 ypos 1.3

        "But she ignores me. I can feel the chaos inside moving from my legs to my chest. I have no idea how to stop it."

        "When Genevieve reaches my head, what then…?"

        show gen:
            linear 1 ypos 1.35

        voice "C-15-5.mp3" #Alex (Bonnie Mitchel)
        alx "This can’t be happening, this can’t be happening, this {b}{i}can’t be happening!{/i}{/b}"

        "What do I do?"

        show gen:
            linear 1 ypos 1.35

        "There’s a ballpoint pen that rolled off the desk. Maybe-- I mean, I certainly don’t have any better ideas..."

        "Reaching out, I twist it around and stab myself in the leg." 

        show gen surprised1 with hpunch:
            linear 0.1 ypos 1.3
            linear 0.1 ypos 1.35

        play sound "game_letgo/sfx/Punch,Shove.ogg"
        "I stab, and stab, and stab - but the pen is too blunt to do more than gouge through my tights and the outer layer of skin."

        "Ugh… it hurts…" 

        "Is it hurting her just as much?"

        "After my leg is screaming in pain, the phantom seems to pause somewhere in my breast."

        show gen:
            ease 10 ypos 1.1

        "It’s working… She’s stopped…? I can feel it retreating…"

        "I push myself up and slowly drag myself away from the desk. My whole body is thoroughly drenched in sweat."

        "My legs are still unresponsive; it’s like my entirely body has been split in half."

        voice "C-15-6.mp3" #Alex (Bonnie Mitchel)
        alx "Give… give them back..."

        "It sounds like she’s listening. I can feel her pulling out…"

        "Wait, no!"

        stop music fadeout 2.5
        show gen angry1:
            ease 0.2 ypos 1.05
            pause 0.05
            easeout 2 ypos 2.0
            

        "Suddenly she comes {i}crashing{/i} back, even faster than before. Oh my god, at this rate--"

        play sound "game_letgo/sfx/Punch,Shove.ogg"
        scene black with Dissolve(0.1)

        "{size=-10}No...{/size}"
        
        if caelumAlive == True:
            jump spirits_a3s2 ##Sacrifice Ending (previously called Caelum Possessed)
        else:
            jump spirits_a3s3 ##Forever Ending (previously called Alex Possessed)

    else:
        "Sitting down at my desk, I mull over my case notes." 

    if hasDiary == True:

        "Genevieve’s father acted erratically, and the house servants were concerned for his daughter’s safety." 

    if hasLetter == True:

        "He didn’t think she was really his daughter. He was so suspicious of his wife, he wrote to her friends asking if they’d seen her cheating." 

    if hasAmmo == True:

        "There was ammunition hidden in a bookcase." 

    "Genevieve was locked her in her room - this room - and her father wouldn’t let her out." 

    "He had a gun, and it seems like he was willing to use it." 

    "But if he killed Genevieve, where would he hide her body?"

    "The evidence I have now isn’t enough to go to the police, so I’ll have to find it on my own."

    "All of a sudden I feel a tugging on my arm - not painful, but insistent. It’s leading me towards the small, strange door." 

    show alx bitter1 with dissolve
    show alx:
        ease 1.0 xpos 0.6
    #Show alex tense

    "I stand up and follow." 
    hide alx

    show spirits alex bedroom clean:
        zoom 2.5
        ease 0.6 xalign 0.8 yalign 0.18

    pause 0.65

    show spirits clawmarks as claws:
        xpos 0.515 ypos 0.09

    with dissolve
    #scene clawmarks

    "I press my hand against the lock, and then the tugging stops." 

    "What does she want? I know the door’s here… but what does she expect me to find?" 

    stop music fadeout 2.0
    "As I press against it further, however, I feel the wood give away ever-so-slightly. My heart jumps." 

    hide spirits clawmarks as claws
    show spirits alex bedroom clean:
        zoom 1.0
        ease 0.6 xalign 0.5 yalign 0.5
    show alx surprised1
    #show alex surprised

    "Maybe there isn’t \"{i}nothing{/i}\" behind it after all." 

    play sound "game_spirits/sfx/Rattling Doorknob.ogg"
    "I instantly stand up and grab a bobby pin. I begin to fiddle with the lock. After several long, frustrating minutes, I manage to turn it." 

    play sound "game_spirits/sfx/Open Door.ogg"
    play music bgmspirits_sthings fadeout 0.5
    scene black with dissolve
    #scene black

    #play music stranger things

    "With a great effort, I push the small door in, cracking the paint and blowing dust and dirt across the floor." 

    "At first, there’s a disused dumbwaiter shaft; it seemingly vanishes into an abyss, and the ladder is so rickety it’s almost a cliche."

    "Then, a small, dirt path vanishes into the void."

    if caelumAlive == True:

        play sound "game_spirits/sfx/Text Send.ogg"

        "I have to tell Caelum! Instantly, I pull out my phone to text him - but he doesn’t reply. All I see is a ‘read’ notification and then there are footsteps." 

        scene spirits alex bedroom clean with dissolve

        show alx neutral1 at centerleft with dissolve
        show cae surprised1 at centerright with easeinright

        #scene alex’s bedroom v1

        #show caelum winded/excited 

        voice "C-15-7.mp3" #Caelum (Daniel Acosta)
        cae "What the hell?" 

        show alx surprised1 with dissolve
        #show alex excited

        voice "C-15-8.mp3" #Alex (Bonnie Mitchel)
        alx "I know, right?" 

        show alx bitter1 with dissolve
        #show alex nervous

        voice "C-15-9.mp3" #Alex (Bonnie Mitchel)
        alx "Maintenance is going to kill me." 

        show cae neutral1 with dissolve

        voice "C-15-10.mp3" #Caelum (Daniel Acosta)
        cae "We’ll figure out an excuse. Come on, don’t you want to see where it leads?" 

        "I do, I really, really do. I fully expect it to be somewhere horrible, but… I have to know." 

        show alx angry1 close with dissolve
        #show alex determined

        voice "C-15-11.mp3" #Alex (Bonnie Mitchel)
        alx "Yeah. Let’s finish this." 

        scene black with dissolve
        #scene black

        "Together, we descend the latter and crawl through the passageway. Thank god I’m not claustrophobic…"

        "After an awkward shuffle down a sudden slope, I finally pull myself into a larger and dimly-lit chamber."

        "With a thud, I land on my feet; Caelum follows suit soon after."

        "Lifting up my phone, I look around." 

        scene spirits cellar with dissolve
        show alx scared1 at centerleft with dissolve
        show cae scared1 at center with dissolve
        #scene cellar

        #show alex horrified/upset/scared

        #show caelum horrified/upset/scared 

        "Those skeletons on the floor… they’re Halloween decorations, right? They have to be..." 

        show cae:
            ease 0.6 xpos 0.6
        pause 0.1
        show alx:
            ease 0.6 xpos 0.4

        "Caelum clutches at my arm, and I take a step backwards." 

        voice "C-15-12.mp3" #Alex (Bonnie Mitchel)
        alx "They’re… They’re not… They can’t be--" 

        voice "C-15-13.mp3" #Caelum (Daniel Acosta)
        cae "Alex…"

        "One of them is wearing a nightgown - the same as Genevieve’s."

        "My stomach sinks and churns. Oh god… here she is."

        show alx sad1 with dissolve
        #show alex sad

        voice "C-15-14.mp3" #Alex (Bonnie Mitchel)
        alx "It’s {i}her.{/i}" 

        show cae sad1 with dissolve
        voice "C-15-15.mp3" #Caelum (Daniel Acosta)
        cae "She’s here. It’s… it’s over?" 

        voice "C-15-16.mp3" #Alex (Bonnie Mitchel)
        alx "I-I think so? I don’t know what--" 

        stop music fadeout 2.0
        
        play sound "game_spirits/sfx/Alex Scream.ogg"
        #play sound alex scream in pain

        show alx angry1 blush close with hpunch
        #show alex in pain/upset

        "Fiery pain shoots through my missing hand. There’s no semblance of anything else - just agony, rolling over it and through it. I fall to my knees."

        show cae surprised1
        #show caelum upset

        voice "C-15-17.mp3" #Caelum (Daniel Acosta)
        cae "Alex!" 

        "Suddenly, all I can hear is Genevieve." 

        voice "C-15-18.mp3" #Genevieve (Lasli Tran)
        gen "Run! It’s him, it’s him, he’s coming, he’s angry, you have to get away-- You have to get out of here; if you die, this was all for {i}nothing{/i}!" 

        show cae scared1
        voice "C-15-19.mp3" #Caelum (Daniel Acosta)
        cae "Alex, what’s happening!?" 

        "All of a sudden, the pain stops." 

        show alx sad1 with dissolve
        voice "C-15-20.mp3" #Alex (Bonnie Mitchel)
        alx "We have to go. Something’s coming, something bad…" 

        play music bgmspirits_wra fadeout 0.5

        #scene CG wraith 
        #play music wraith’s theme
        show red:
            alpha 0.0
            ease 0.2 alpha 0.5
            ease 0.2 alpha 0.0
        pause 0.4
        hide red

        "A dread sweeps over me, flooding into my veins. I haven’t known sensations like this since I woke up in that hospital bed, without a hand and without parents." 

        voice "C-15-21.mp3" #Caelum (Daniel Acosta)
        cae "What the hell is that?" 

        show alx scared1
        voice "C-15-22.mp3" #Alex (Bonnie Mitchel)
        alx "You can see it?" 

        voice "C-15-23.mp3" #Caelum (Daniel Acosta)
        cae "Umm… yeah; it’s a giant smoke monster?" 

        show red:
            alpha 0.0
            ease 0.2 alpha 0.5
            ease 0.2 alpha 0.0
        pause 0.4
        hide red

        voice "C-15-24.mp3" #Wraith (Kenneth Faircloth)
        wra "You have made a terrible mistake, meddling in matters you do not understand. And now, you shall perish."

        show alx angry1 with dissolve

        voice "C-15-25.mp3" #Alex (Bonnie Mitchel)
        alx "I know what you are." 

        if duties == 3:

            show cae angry1 with dissolve
            voice "C-15-26.mp3" #Caelum (Daniel Acosta)
            cae "You killed your own daughter. You locked her up like an {i}animal{/i}."

            voice "C-15-27.mp3" #Caelum (Daniel Acosta)
            cae "Do you know how deeply it cuts to realize your parent {i}hates{/i} you? What gives you the right to judge someone like that?"

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-28.mp3" #Wraith (Kenneth Faircloth)
            wra "You do not know what you speak of. She was no child of mine." 

            voice "C-15-29.mp3" #Alex (Bonnie Mitchel)
            alx "You were real worried about that, huh? Wrote around asking all your wife’s friends if she was sleeping around?" 

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-30.mp3" #Wraith (Kenneth Faircloth)
            wra "You insolent child, you know {i}nothing{/i} of--" 

            voice "C-15-31.mp3" #Alex (Bonnie Mitchel)
            alx "What does it matter? Family isn’t blood. She was raised in your home, born to your wife. You couldn’t find it in your heart to love her?" 

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-32.mp3" #Wraith (Kenneth Faircloth)
            wra "You know nothing of honor, of the pressures to uphold your name--" 

            voice "C-15-33.mp3" #Caelum (Daniel Acosta)
            cae "That’s bullshit! You cared more about your family name than your own daughter?" 

            "I’m angrier than I’ve been in a long, long time. I can’t tell if that’s him messing with my emotions, or if it’s just how I feel." 

            "He’s in my way. I need to do this, or else everything was for nothing - and what purpose do I have anymore, if that’s the case?" 

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-34.mp3" #Wraith (Kenneth Faircloth)
            wra "Stop this. You will never leave this place alive." 

            "I have to do something." 

            "The gun is in my back pocket… and the ammo is in my other one. I’d forgotten about it, somehow, with everything that’d happened." 

            "This world - the one I’ve been forced to deal with ever since the accident on the tracks…" 

            "If they can hurt me, why can’t I hurt them?"

            voice "C-15-35.mp3" #Caelum (Daniel Acosta)
            cae "You think if we go missing, they won’t look for us? They’ll find this place and the world will know what you did." 

            "My fingers shake as I push the bullets into the barrel." 

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-36.mp3" #Wraith (Kenneth Faircloth)
            wra "You think I will let them find you?" 

            "I carefully set the gun into my prosthetic hand and point it at the wraith, pulling the hammer back. Caelum stares at me like I’ve lost my mind. I think I have." 

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-37.mp3" #Wraith (Kenneth Faircloth)
            wra "What are you doing, girl?" 

            voice "C-15-38.mp3" #Alex (Bonnie Mitchel)
            alx "If you can hurt me, then I can hurt you." 

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-39.mp3" #Wraith (Kenneth Faircloth)
            wra "Put it down, girl. You stupid girl, put it down, put it--"

            stop music fadeout 0.1

            play sound "game_spirits/sfx/Gunshot.ogg"

            scene black

            pause 1.0

            scene spirits cellar with Dissolve(3.0)
            
            play music bgmspirits_sthings

            show alx scared1 at centerleft with dissolve
            show cae surprised1 centerright dissolve

            #play sound gunshot 

            #scene black

            #scene cellar

            #play music hospitalization 

            #show alex shocked/unnerved

            #show caelum surprised/shocked

            "What did I do?" 

            voice "C-15-40.mp3" #Caelum (Daniel Acosta)
            cae "Alex…" 

            voice "C-15-41.mp3" #Alex (Bonnie Mitchel)
            alx "I don’t know. I don’t know." 

            voice "C-15-42.mp3" #Alex (Bonnie Mitchel)
            alx "Can we just leave? Please." 

            show cae sad1 dissolve
            #show caelum worried

            voice "C-15-43.mp3" #Caelum (Daniel Acosta)
            cae "Alright." 

            scene black with dissolve
            #scene black

            "Caelum goes first this time, crawling down the tunnel and lighting the way. I follow after him, still shaking." 

            "Why did I do that? Without thinking, I just… shot him. He was dead, but I used a gun. And he’s gone."

            scene spirits alex bedroom clean with dissolve
            show alx sad1 at center with  dissolve
            show cae sad1 at centerright with dissolve
            #scene alex’s bedroom v1 

            #show alex sad

            #show caelum worried

            "I can feel Genevieve holding my hand, clutching it tightly - but not painfully or possessively." 

            show gen happy1 at centerleft with Dissolve(2.0)
            #show genevieve neutral/happy

            voice "C-15-44.mp3" #Genevieve (Lasli Tran)
            gen "Thank you." 

            "Caelum can’t see her, but I stare off into space long enough and far enough for him to guess what’s happening. He says nothing, and I appreciate that." 

            hide gen with Dissolve(2.0)
            #hide genevieve

            "And, without another word, she vanishes. I can’t feel her, see her, or hear her…" 

            stop music fadeout 5.0
            "I sink down onto my bed, suddenly overcome by a crushing loneliness."

            "What do I do now? What… am I?" 

            voice "C-15-45.mp3" #Caelum (Daniel Acosta)
            cae "I’m going to go get Jianmei, alright?" 

            "All I can do is nod." 
            
            jump spirits_a3s4 ##Surrender Ending; formerly called the Hospitalization ending

        else:
            show cae angry1 with dissolve
            voice "C-15-46.mp3" #Caelum (Daniel Acosta)
            cae "You killed your own daughter. You locked her up like an {i}animal{/i}."

            voice "C-15-47.mp3" #Alex (Bonnie Mitchel)
            alx "You had a family and you threw them away." 

            voice "C-15-48.mp3" #Caelum (Daniel Acosta)
            cae "Do you know how deeply it cuts to realize your parent {i}hates{/i} you? What gives you the right to judge someone like that?"


            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-49.mp3" #Wraith (Kenneth Faircloth)
            wra "Neither of you know anything about family--" 

            voice "C-15-50.mp3" #Alex (Bonnie Mitchel)
            alx "Oh, what do you know? You’re a terrible person." 

            voice "C-15-51.mp3" #Alex (Bonnie Mitchel)
            alx "You murdered a young girl because you thought she wasn’t your own." 

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-52.mp3" #Wraith (Kenneth Faircloth)
            wra "I will not listen to your--" 

            voice "C-15-53.mp3" #Caelum (Daniel Acosta)
            cae "What are you going to do to stop us?"

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-54.mp3" #Wraith (Kenneth Faircloth)
            wra "Do you not fear me, child?" 

            "I’m angry - angrier than I’ve been in a long, long time. I can’t tell if that’s him messing with my emotions, or if it’s just how I feel." 

            "I need to {i}end{/i} him. He shouldn’t exist; Genevieve deserves peace, and he deserves nothingness." 

            "But he has real power… I need to get us out of here." 

            voice "C-15-55.mp3" #Alex (Bonnie Mitchel)
            alx "It doesn’t matter. Even if we die here, you’ll still be ruined."

            voice "C-15-56.mp3" #Alex (Bonnie Mitchel)
            alx "All you care about is your precious name, isn’t it? That’s why you killed her?" 

            voice "C-15-57.mp3" #Alex (Bonnie Mitchel)
            alx "If we die here, they’ll come looking for us. They’ll find us and this room. They’ll read my notes. You’re finished." 

            "The wraith just laughs wickedly in response."

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-58.mp3" #Wraith (Kenneth Faircloth)
            wra "The path here can be blocked anew. Notes can be sabotaged."

            voice "C-15-59.mp3" #Wraith (Kenneth Faircloth)
            wra "I have remained hidden for a century. Do you really think I would be thwarted by mongrels like you?"

            voice "C-15-60.mp3" #Alex (Bonnie Mitchel)
            alx "You just don’t get it, do you?"

            show alx happy1 with dissolve

            voice "C-15-61.mp3" #Alex (Bonnie Mitchel)
            alx "The world’s moved past you, old man. Changed in ways far beyond your comprehension."

            voice "C-15-62.mp3" #Alex (Bonnie Mitchel)
            alx "You think I just wrote my notes down on paper? Guess again, dipshit. I made blog posts."

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-63.mp3" #Wraith (Kenneth Faircloth)
            wra "What nonsense is this…?"

            voice "C-15-64.mp3" #Alex (Bonnie Mitchel)
            alx "There’s a thing called the internet; you don’t really need to know how it works. Just know that I basically forwarded my findings to every human being in the universe."

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-65.mp3" #Wraith (Kenneth Faircloth)
            wra "You… You tell fantastical lies…"

            show cae happy1 with dissolve

            voice "C-15-66.mp3" #Caelum (Daniel Acosta)
            cae "Nah, man. The internet’s totally a thing."

            voice "C-15-67.mp3" #Caelum (Daniel Acosta)
            cae "(Also, did that gaseous skeleton man just accuse somebody {i}else{/i} of being fantastical?)"

            voice "C-15-68.mp3" #Alex (Bonnie Mitchel)
            alx "You can’t even hide our {i}bodies{/i}. We both have GPS-trackable devices on us. Good luck disabling them when you don’t even have thumbs!"

            voice "C-15-69.mp3" #Alex (Bonnie Mitchel)
            alx "\"Can’t thwart you?\" I thwarted you two hours ago, sunshine."

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-70.mp3" #Wraith (Kenneth Faircloth)
            wra "Lies… Lies!!!"

            voice "C-15-71.mp3" #Alex (Bonnie Mitchel)
            alx "Nope. This has come to an end. Nothing left for you but to cross over."

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-72.mp3" #Wraith (Kenneth Faircloth)
            wra "No… You lie. You lie! I’ll kill you all…"

            "But it’s too late; many inky, umbral tendrils rise from the ground and start to spool themselves around his bones."

            "He thrashes against them - but it’s no use. The obsidian strings leash themselves to him, like a macabre marionette in reverse-gravity."

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-73.mp3" #Wraith (Kenneth Faircloth)
            wra "No! I reject this! My business is {i}not{/i} complete!"

            voice "C-15-74.mp3" #Caelum (Daniel Acosta)
            cae "Sounds fake, but okay."

            "Whatever incomprehensible power is behind this - if any - doesn’t seem to agree. He continues descending shakily into the earth, as though dragged into Hell."

            "Where {i}is{/i} he going, anyway? I suppose I don’t even want to know."

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-75.mp3" #Wraith (Kenneth Faircloth)
            wra "Genevieve… you worthless bastard child… What have you wrought--"

            stop music fadeout 1.0

            "And then it’s done. The top of his gaseous skull sinks into the earth."

            "I sit there for a moment, relishing in the silence. Caelum just stands beside me, hands nonchalantly sliding into his pockets."

            play music bgmspirits_cae

            show cae surprised1 blush with dissolve

            voice "C-15-76.mp3" #Caelum (Daniel Acosta)
            cae "You know… I don’t {i}actually{/i} have my phone on me."

            show alx happy1 close blush with dissolve

            voice "C-15-77.mp3" #Alex (Bonnie Mitchel)
            alx "It’s fine. I didn’t actually write a blog, either."

            "I hear a girlish giggling in the distance, and I feel a delicate hand slide into my own."

            "Genevieve is warmer than I thought it was possible for a wayward spirit to feel."

            show gen happy1 at left with Dissolve(2.0)
            #show genevieve happy

            voice "C-15-78.mp3" #Genevieve (Lasli Tran)
            gen "He always {i}was{/i} an idiot."

            show alx happy1 with dissolve

            voice "C-15-79.mp3" #Alex (Bonnie Mitchel)
            alx "People like him typically are."

            show cae neutral1 with dissolve
            "Caelum raises an eyebrow at my apparent non-sequitur, but when he notices me staring into space, it seems to click."

            show cae happy1 with dissolve
            voice "C-15-80.mp3" #Caelum (Daniel Acosta)
            cae "Oh, uh, hello, um, Genevieve."

            voice "C-15-81.mp3" #Genevieve (Lasli Tran)
            gen "Hello there."

            voice "C-15-82.mp3" #Alex (Bonnie Mitchel)
            alx "She says \"hello.\""

            voice "C-15-83.mp3" #Genevieve (Lasli Tran)
            gen "Thank you, Alex. You’re a miracle worker."

            voice "C-15-84.mp3" #Alex (Bonnie Mitchel)
            alx "You good, now?"

            voice "C-15-85.mp3" #Genevieve (Lasli Tran)
            gen "I am. I’ll be leaving shortly."

            #show genevieve sad

            voice "C-15-86.mp3" #Genevieve (Lasli Tran)
            gen "But I’ve made a bit of other unfinished business for myself."

            show gen sad1 with dissolve
            voice "C-15-87.mp3" #Genevieve (Lasli Tran)
            gen "I’m sorry for the pain I brought you during my… disorientation. I was desperate, barely more than an animal."

            voice "C-15-88.mp3" #Genevieve (Lasli Tran)
            gen "Being adrift for so long… it sickens one’s soul. That’s not an excuse, but..."

            voice "C-15-89.mp3" #Genevieve (Lasli Tran)
            gen "I should never have harmed you. Please, accept my apology!"

            voice "C-15-90.mp3" #Alex (Bonnie Mitchel)
            alx "It’s fine. I know you’ve had a rough time of it. Go on."

            "In all honesty, I’m not sure I actually forgive her - but if her father’s fate has taught me anything, she just needs to {i}believe{/i} I do."

            show gen happy1 with dissolve
            #show genevieve happy

            voice "C-15-91.mp3" #Genevieve (Lasli Tran)
            gen "Thank you, Alex Kartha. You have my eternal gratitude."

            voice "C-15-92.mp3" #Alex (Bonnie Mitchel)
            alx "Say hi to your mom for me."

            "She grins wide, and vanishes."

            stop music fadeout 5.0
            hide gen with Dissolve(2.0)

            "And then, silence. There’s no presence, no spectral resonance."

            "No pain."

            "None at all."

            voice "C-15-93.mp3" #Caelum (Daniel Acosta)
            cae "So, uh…"

            voice "C-15-94.mp3" #Caelum (Daniel Acosta)
            cae "Not to ruin the moment or anything, but we’ve still got a basement full of old skeletons."

            voice "C-15-95.mp3" #Caelum (Daniel Acosta)
            cae "Do we call the police, or, like, archaeologists?"

            voice "C-15-96.mp3" #Alex (Bonnie Mitchel)
            alx "Let’s… let’s just head back up to the room for now."
            
            if firstTrueEndFlag == True and secondTrueEndFlag == True and duties < 3:
                show black with Dissolve(2.0)
                jump spirits_a3s1 ## Demolition Ending
            
            scene spirits alex bedroom clean with Dissolve(2.0)
            show alx neutral1 at center with  dissolve
            show cae neutral1 at centerright with dissolve

            jump spirits_a3s4 ##Surrender Ending; formerly called the Hospitalization ending

    else:
        "Genevieve wanted me to find this. This ends now. I can finish this."

        "I descend the ladder and crawl through the passageway. Thank god I’m not claustrophobic."

        "At the very least, I’m glad I didn’t do my laundry yesterday; the dirt is going to merit it."

        "After an awkward shuffle down a sudden slope, I finally pull myself into a larger chamber. With a thud, I land on my feet."

        "Lifting up my phone, I look around the room." 

        scene spirits cellar with dissolve
        show alx scared1 with dissolve

        #scene cellar

        #show alex horrified/upset/scared

        "Those skeletons on the floor… they’re Halloween decorations, right? They have to be..." 

        voice "C-15-97.mp3" #Alex (Bonnie Mitchel)
        alx "They’re-- They’re not...They can’t be!"   

        "Staring ahead, I notice one is wearing a nightgown - the same as Genevieve’s."

        "My stomach drops and churns. Oh god... Here she is." 

        show alx sad1 with dissolve
        #show alex sad

        voice "C-15-98.mp3" #Alex (Bonnie Mitchel)
        alx "It’s her." 

        "And as I turn around, I notice a discarded old spade beside a heap of freshly moved earth, next to a corner of red fabric."

        show alx scared1 close with dissolve
        "No, no, no!"

        "It’s not-- it’s not, he’s not… He can’t be here." 

        "I don’t want to look. I can’t-- I can’t see him like that." 

        "I have to get help." 

        stop music fadeout 2.0
        
        play sound "game_spirits/sfx/Alex Scream.ogg"
        #play sound alex scream in pain

        show alx angry1 blush close with hpunch

        #play sound alex scream in pain

        #show alex in pain/upset

        "Burning pain shoots through my missing hand. There’s no semblance of it being there - just agony, rolling over it and burning through; I fall to my knees."

        "Suddenly, all I can hear is Genevieve." 

        voice "C-15-99.mp3" #Genevieve (Lasli Tran)
        gen "Run! It’s him, it’s him, he’s coming, he’s angry, you have to get away-- You have to get out of here; if you die, this was all for {i}nothing{/i}!" 
         
        "What does she mean? Who’s… {i}him{/i}?"

        "All of a sudden, the pain stops." 

        play music bgmspirits_wra fadeout 0.5

        show red:
            alpha 0.0
            ease 0.2 alpha 0.5
            ease 0.2 alpha 0.0
        pause 0.4
        hide red

        #scene CG wraith 

        #play music wraith’s theme

        "Dread sweeps over me, flooding into my veins. I haven’t known depression like this since I woke up in that hospital bed, without a hand and without parents." 

        voice "C-15-100.mp3" #Wraith (Kenneth Faircloth)
        wra "You have made a terrible mistake. You have meddled in matters you do not understand. And now, you shall perish."

        show alx scared1 with dissolve

        voice "C-15-101.mp3" #Alex (Bonnie Mitchel)
        alx "I know what you are." 

        show alx angry1 with dissolve

        voice "C-15-102.mp3" #Alex (Bonnie Mitchel)
        alx "You’re a murderer. You killed Caelum! He had nothing to do with any of this." 

        show red:
            alpha 0.0
            ease 0.2 alpha 0.5
            ease 0.2 alpha 0.0
        pause 0.4
        hide red

        voice "C-15-103.mp3" #Wraith (Kenneth Faircloth)
        wra "A man, leaving my daughter’s bedroom? I could not allow it." 

        voice "C-15-104.mp3" #Alex (Bonnie Mitchel)
        alx "Your daughter is dead! {i}You{/i} killed her!" 

        show red:
            alpha 0.0
            ease 0.2 alpha 0.5
            ease 0.2 alpha 0.0
        pause 0.4
        hide red

        voice "C-15-105.mp3" #Wraith (Kenneth Faircloth)
        wra "It is the principle of--"

        voice "C-15-106.mp3" #Alex (Bonnie Mitchel)
        alx "And you killed him. You killed him, and nobody knows, nobody really {i}cares{/i}!" 

        voice "C-15-107.mp3" #Alex (Bonnie Mitchel)
        alx "They all think he ran away. But he didn’t, and I’m the only one who knows that. The only one who knows he’s dead."

        voice "C-15-108.mp3" #Alex (Bonnie Mitchel)
        alx "Do you have any idea how much that sucks?" 

        show red:
            alpha 0.0
            ease 0.2 alpha 0.5
            ease 0.2 alpha 0.0
        pause 0.4
        hide red

        voice "C-15-109.mp3" #Wraith (Kenneth Faircloth)
        wra "I do not care--" 

        voice "C-15-110.mp3" #Alex (Bonnie Mitchel)
        alx "Well, you should, you asshole. He was a decent person! He cared about people. He cared about {i}me.{/i}" 

        voice "C-15-111.mp3" #Alex (Bonnie Mitchel)
        alx "I’m going to ruin you - for Caelum, for Genevieve, and for anyone else you might be thinking of hurting."

        "I’m angrier than I’ve been in a long, long time. I can’t tell if that’s him messing with my emotions, or if it’s just how I feel." 

        "I need to stop him. It’s my duty. Why do I have this power if I don’t use it?" 

        show red:
            alpha 0.0
            ease 0.2 alpha 0.5
            ease 0.2 alpha 0.0
        pause 0.4
        hide red

        voice "C-15-112.mp3" #Wraith (Kenneth Faircloth)
        wra "Stop this. You will never leave this place alive." 

        "I have to do something." 

        if hasAmmo == True:

            "The gun is in my back pocket and the ammo is in my other one. I’d forgotten about it, somehow, with everything that’s happened." 

            "This world - the one I’ve been forced to deal with ever since the accident on the tracks…" 

            "If they can hurt me, why can’t I hurt them?"

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-113.mp3" #Wraith (Kenneth Faircloth)
            wra "I will rip you apart." 

            "My fingers are steady as I push the bullets into the barrel." 

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-114.mp3" #Wraith (Kenneth Faircloth)
            wra "You think I will let them find you?" 

            "I carefully set the gun into my prosthetic hand and point it at the wraith, pulling the hammer back. I don’t know what I’m doing - but at the same time, I’ve never been more sure of myself."

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-115.mp3" #Wraith (Kenneth Faircloth)
            wra "What are you doing, girl?" 

            voice "C-15-116.mp3" #Alex (Bonnie Mitchel)
            alx "If you can hurt me, then I can hurt you." 

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-117.mp3" #Wraith (Kenneth Faircloth)
            wra "Put it down, girl. You stupid girl, put it down, put it--"

            stop music fadeout 0.1

            play sound "game_spirits/sfx/Gunshot.ogg"

            scene black

            pause 1.0

            scene spirits cellar with Dissolve(3.0)
            
            play music bgmspirits_sthings

            show alx scared1 with dissolve

            #play sound gunshot 

            #scene black

            #scene cellar

            #play music genevieve 

            #show alex tense

            #show genevieve happy 

            show gen happy1 at centerleft with Dissolve(2.0)

            voice "C-15-118.mp3" #Genevieve (Lasli Tran)
            gen "I can’t thank you enough, Alex." 

            voice "C-15-119.mp3" #Genevieve (Lasli Tran)
            gen "You’ve saved me from this-- this hell." 

            "I’m still reeling from what just happened. Did that really work?" 

        else:
        
            "This… it can’t end like this."

            "This {i}bastard{/i} killed my only friend. I can’t stand the sight of him."

            "No. I won’t! I won’t let this floating garbage dump get away with everything he’s done."

            "I’m going to hurt him worse than he’s ever hurt anyone."

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-120.mp3" #Wraith (Kenneth Faircloth)
            wra "Heh heh heh… So juvenile. Such impotent rage."

            voice "C-15-121.mp3" #Wraith (Kenneth Faircloth)
            wra "I’ll decorate this chamber with your entrails."

            voice "C-15-122.mp3" #Wraith (Kenneth Faircloth)
            wra "If I kill you violently enough, perhaps you’ll do us the honor of joining us forever--"

            stop music fadeout 0.5
            show alx with hpunch:
                pause 0.5
                easeout 0.5 zoom 2.0 alpha 0.0 ypos 1.5

            voice "C-15-123.mp3" #Alex (Bonnie Mitchel)
            alx "Yyaaaaaaaaaaahhhhhhhhhhhhh!"

            "My body moves as if on its own. Ironically, as if possessed."

            "I don’t remember having picked up the spade, but my prosthetic hand drives it straight into the phantom’s chest."

            play sound "game_letgo/sfx/Punch,Shove.ogg"
            "Rather than go straight through, it finds purchase in the spectral mass of Mr. Bourlon’s sternum and smashes his gaseous body into the wall. His translucent bones rattle like the model in a biology classroom."

            show red:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            voice "C-15-124.mp3" #Wraith (Kenneth Faircloth)
            wra "Urrk… What…"

            voice "C-15-125.mp3" #Alex (Bonnie Mitchel)
            alx "Cross over, you piece of shit."

            "I withdraw the spade, and his gaseous form clatters to the dirt."

            "I don’t allow him even a moment to breathe - or whatever it is a ghost would do. I smash his bones with the spade again and again and again."

            voice "C-15-126.mp3" #Alex (Bonnie Mitchel)
            alx "Cross over!"

            play sound "game_letgo/sfx/Punch,Shove.ogg"
            show red with hpunch:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red
            #play sound sfx crunch

            voice "C-15-127.mp3" #Alex (Bonnie Mitchel)
            alx "Cross over! Cross over!"

            play sound "game_letgo/sfx/Punch,Shove.ogg"
            show red with hpunch:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red
            #play sound sfx crunch

            #pause 0.2

            play sound "game_letgo/sfx/Punch,Shove.ogg"
            show red with hpunch:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red
            #play sound sfx crunch

            voice "C-15-128.mp3" #Alex (Bonnie Mitchel)
            alx "You fucker, cross {i}over{/i}!"

            play sound "game_letgo/sfx/Punch,Shove.ogg"
            show red with hpunch:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red
            #play sound sfx crunch

            "His bones are snapping under the sheer force of my blows."

            "At some point, the old spade snaps in half at the wooden handle - and, caught off-balance, I come tumbling down onto the smoking pile of broken bones."

            "But the fire inside me doesn’t pale even for a moment. I drive my prosthetic into what remains of the skull, the plastic bending and cracking under the weight of my strikes."

            voice "C-15-129.mp3" #Alex (Bonnie Mitchel)
            alx "Crossovercrossovercrossovercrossover {i}yyyyyyyyaaaaaaaaaaaaaaaaaahhhhhh!!!!{/i}"

            play sound "game_letgo/sfx/Punch,Shove.ogg"
            show red with hpunch:
                alpha 0.0
                ease 0.2 alpha 0.5
                ease 0.2 alpha 0.0
            pause 0.4
            hide red

            "I hit him one last time - and my prosthesis blasts apart, along with the dome of his skull."

            "It’s just bones now. The gaseous miasma that remains is more like the shadow of an extinguished match."

            "My whole body aches… My heart is pounding at a million beats per second..."

            "...Did I win?"

            "No… There’s an inky, string-like miasma unraveling out of the ground… surrounding him…"

            "He’s recovering. I only disabled him."

            hide alx
            show alx scared1 with dissolve

            voice "C-15-130.mp3" #Alex (Bonnie Mitchel)
            alx "No…"

            "Oh… wait… what?"

            "More of the inky, abyssal thread spools out, wrapping around the broken heap. Soon, it’s as though he’s mummified in shadow."

            "And then…"

            "As though trapped in a tar pit, the umbral cocoon sinks into the earth."

            "After a moment, a cool, clear serenity passes over me. I can’t feel the ghost’s presence at all."

            show alx sad1 with dissolve

            voice "C-15-131.mp3" #Alex (Bonnie Mitchel)
            alx "Does that mean…?"

            play music bgmspirits_sthings

            show gen happy1 at centerleft with Dissolve(2.0)

            #play music genevieve

            #show alex tense

            #show genevieve happy

            voice "C-15-132.mp3" #Genevieve (Lasli Tran)
            gen "He’s… he’s finally descended into Perdition."

            voice "C-15-133.mp3" #Genevieve (Lasli Tran)
            gen "How did you know your arm could rend his spirit?"

            voice "C-15-134.mp3" #Alex (Bonnie Mitchel)
            alx "Honestly, I didn’t give it a lot of thought."

            voice "C-15-135.mp3" #Genevieve (Lasli Tran)
            gen "I don’t even know what to say. You’re magnificent! You’ve freed me."

            voice "C-15-136.mp3" #Alex (Bonnie Mitchel)
            alx "..."

            show gen sad1 with dissolve

            voice "C-15-137.mp3" #Genevieve (Lasli Tran)
            gen "Are you… are you alright?"

            voice "C-15-138.mp3" #Alex (Bonnie Mitchel)
            alx "I don’t know yet."

            "I sigh, feeling like I haven’t slept in years."

            show alx sad1 close with dissolve

            voice "C-15-139.mp3" #Alex (Bonnie Mitchel)
            alx "Caelum’s still dead, so I guess not."

        voice "C-15-140.mp3" #Genevieve (Lasli Tran)
        gen "Your friend has passed. I cannot sense him. This is a good thing." 

        voice "C-15-141.mp3" #Genevieve (Lasli Tran)
        gen "It is my time, as well." 

        show gen sad1 with dissolve
        #show genevieve sad 

        voice "C-15-142.mp3" #Genevieve (Lasli Tran)
        gen "I apologize for my actions. I was disoriented, afraid, angry… I should not have harmed you." 

        "I honestly don’t know if I forgive her, but I understand - and that’s a start." 

        show alx sad1 with dissolve
        voice "C-15-143.mp3" #Alex (Bonnie Mitchel)
        alx "It’s alright. Go, Genevieve." 

        "I don’t want her to stay any longer than she has to. She’s been waiting to leave this house for a century." 

        show gen happy1 with dissolve
        voice "C-15-144.mp3" #Genevieve (Lasli Tran)
        gen "Yes. Thank you, Alex Kartha." 

        stop music fadeout 5.0
        hide gen with Dissolve(2.0)
        #hide genevieve 

        "And just like that, she’s gone." 

        scene black with Dissolve(2.0)
        #scene black

        "As I climb out of the cellar and into a desolate room, I wonder, how many spirits are out there?" 

        "Wandering Earth, desperate for release? If I can sense them, don’t I have a duty to help them?"

        "So no one dies like Caelum did - so no one spends a hundred years afraid and angry like Genevieve did." 

        "Maybe that could be my calling. It’s strange, but… nothing about my life has ever seemed normal."

        "It’s about time I leaned into it." 

        #scene black
        play music bgmspirits_gen fadeout 0.5
        jump spirits_a3s5 ##Servitude ending

    jump spirits_a3s1
