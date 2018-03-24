label spirits_a2s3:
    "Lunches are provided in the dining hall, but it's just so crowded and raucous in there."

    "It’s easier to head back to Artemis Hall. Jianmei doesn’t make lunches, but she keeps an emergency stock of food in the fridge - whatever she feels like making on any given day, I guess."

    "It's a nice alternative to the much richer fare they serve in the cafeteria."

    if caelumAlive == True:

        "Caelum didn't turn up in any of our morning classes, so I'm hoping to find him around here…"

        "Maybe I'll knock on his bedroom door."

    else:

        "I invited Caelum with me, but he told me he was skipping his lunch period to look up the history of Artemis Hall."

        "It isn’t significant enough to have any plaques out front - so as far as I can tell, it’s just an old manor-style house that was bought up with the land under it when the academy expanded."

        "I think Caelum might (understandably) be a little reticent to hang around here, too, after last night…"

    "There are a couple of other girls coming back with me down the walkway, but I don't know any of them. One of them waves at me when she notices me looking, so I tentatively wave back."

    #scene foyer 

    "I think I'm going to eat in my bedroom today. It'll be nice to have a little time to myself."

    "Jianmei’s listening to speed metal in her office, so I just proceed to the kitchen and serve myself."

    "I grab a little variety pack from the fridge: an onigiri, a caesar wrap, and an egg roll; then, I head on my merry way."

    "It’s only when I’ve made it to the stairs that it finally clicks."

    "\"Check under the last step...\""

    "But under the bottom step of the main staircase? What is it she wants me to find?"

    "Maybe I shouldn't do this right now… I mean, I've got all this food…"

    "On the other hand, with migraines like mine, having free time isn’t always a guarantee..."

    menu:

        "Should I just get this out of the way?"

        "If I just look…":

            $ hasDiary = True

            voice "C-11-1.mp3" #Alex (Bonnie Mitchel)
            alx "Ugh, fine. At least if I do this, she can't say I didn't."

            "I place my food atop an old table and lean down to fiddle with the bottom step."

            "It’s not as easy or loose as it seems to be - since maintenance has probably rectified any problems."

            "If that’s the case, then this will have to be the end of it… There’s no way I’m getting underneath there without a claw hammer."

            "And even then, where would I get one? Would I really be crazy enough to try?"

            "Wait… maybe under the floorboards?"

            "Pushing down on the varnished wood does nothing, but when I push it toward the stairs…"

            "Aha! The floorboard slides right {i}under{/i} the last step."

            "Underneath the board is a small, leather-bound diary; its pages are browned and frayed."

            "I mean, I don’t have any proof it’s {i}actually{/i} a diary; it could be some kind of technical manual, for all I know - or even a phone book."

            "But let’s be real, it’s a diary. It’s {i}always{/i} a diary."

            voice "C-11-2.mp3" #Alex (Bonnie Mitchel)
            alx "And I guess now I have to read it…"

            "Setting the board back into place, I shove the book into my pocket, grab my food, and head back upstairs."

        "No. This can wait.":

            $ hasDiary = False

            "I don’t want to do this right now. I’d feel ridiculous."

            "Besides, I only have so much time to eat before class."

            "Sighing, I take my food and ascend the staircase, leaving the problem behind me."

    if caelumAlive == False:

        "As I walk past Caelum’s bedroom, I notice that the door is closed."

        "That’s mildly distressing; I certainly thought he’d just be sick in bed or something."

        "I walk up and give a light - but hesitant - knock."

        voice "C-11-3.mp3" #Alex (Bonnie Mitchel)
        alx "Caelum? Are you there?"

        "No answer…"

        "Maybe he just had a doctor’s appointment or something? With an endocrinologist or therapist?"

        "Something like that, I hope. I’ll ask Jianmei later."

    if hasDiary == True:

        "Walking into my room, I sit down at the desk, set my lunch aside for a moment, and crack open the diary."

        "The paper is musty and smells disgusting - but there’s fewer rat droppings on it than expected, so that’s something, I guess?"

        "I’m {i}definitely{/i} going to wash my hands after this."

        "I gently flip through the pages. They’re all written in the same hand, and entries end about a third of the way through."

        "The first is dated January 1918 - which is helpful - but it mostly complaints about servants."

        "Skimming through the next few entries, I think the woman who wrote this was a servant herself… but it also seems she presided over the others."

        nvl clear

        n "{i}\"March 3: Genevieve didn’t come down from her room today. Mr. Bourlon says she has suddenly taken ill. \"{/i}"

        n "{i}\"I find that quite difficult to believe. His daughter has always been such a hale and hearty girl. Just yesterday, she was running around outside, climbing trees.\"{/i}"

        nvl clear

        if 'urname' in questionFlags:
            "Genevieve Bourlon… that’s what the ghost told me her name was."
        else:
            "Genevieve Bourlon… could that be the demanding ghost’s name?"

        nvl clear

        n "{i}\"I’d hoped to check on the young miss, but Mr. Bourlon has insisted she be quarantined until her fever breaks. He says that with so many servants in the house, he fears a larger outbreak.\"{/i}"

        n "{i}\"He’s even confiscated all the keys to her room. We aren’t to come to the second floor anymore - not without his escort.\"{/i}"

        n "{i}\"It all just seems a little strange to me. I suppose he hasn’t acted quite right since Mrs. Bourlon passed...\"{/i}"

        "Geez… what the heck could have happened? I skim ahead a few pages, looking for any other mention of Genevieve’s name."

        nvl clear

        n "{i}\"March 14: I probably risk my life by even writing this. \"{/i}"

        n "{i}\"Genevieve is dead. Of that, I am certain. \"{/i}"

        n "{i}\"Late last night, quite discomforted, I emerged from my quarters to brew a bit of tea. As I passed the master’s study, I noticed his pistol and sword had been removed from their display above the fireplace.\"{/i}"

        n "{i}\"I heard movement in the upper story - but as I crept to the staircase, I could see no candlelight. I suspected an intruder was in the house. \"{/i}"

        n "{i}\"Then, I heard the most ghastly shriek.\"{/i}"
        
        n "{i}\"I grabbed the poker from the fireplace and made my way up the stairs, lest the young lady be debauched.\"{/i}"

        n "{i}\"But what I saw in the moonlight was unspeakable.\"{/i}"

        n "{i}\"Genevieve was beyond my help. She had been impaled, right through the heart, by her father’s sword.\"{/i}"

        n "{i}\"But that wasn’t the end of it. As though possessed by the devil himself, Mr. Bourlon pulled out his blade with a sickening squelch and--\"{/i}"

        nvl clear

        "Crap crap crap crap… I have had {i}quite{/i} enough of that."

        "Ugh. I guess that ends the mystery of what happened to Genevieve."

        "Locked in her room and murdered by her father… Why? For what reason?"

        "I skip to the last entry, hoping it has some answers; unfortunately, it’s just more of the same."

        nvl clear

        n "{i}\"March 21: Everyone is dead. \"{/i}"

        n "{i}\"He slew the manservants first. God only knows why. \"{/i}"

        n "{i}\"He claimed he relieved them of duty, but I heard the gunshots go off somewhere deep in the bowels of the house. \"{/i}"

        n "{i}\"Every night since then, another maidservant has vanished. I pray that at least some of them have simply escaped this horrible place in the night - but in my heart I hold little hope. \"{/i}"

        n "{i}\"If only he hadn’t sold the horses, I’d have some hope at freedom… But there’s none to be found, and no way of taking the automobile. \"{/i}"

        n "{i}\"If I want to live, I’m going to have to kill Mr. Bourlon before he has a chance to kill me. \"{/i}"

        n "{i}\"Everett, if I fail in my task, know that you’re the only man I ever loved. \"{/i}"

        nvl clear

        "I… I get the feeling she didn’t succeed."

        "Dammit. Just how many people died in this house?"

    else: 

        "Walking to my room, I put on a classical literature podcast and sit down at my desk with my food."

        "It feels nice to just relax - and I actually have an appetite for the first time in what feels like forever! I’m going to gobble down as much as I can before the nausea sets in…"

        "I should really do this more often. Jianmei’s whatever-sandwiches are every bit as good as her dinners."

        "..."

        "By the time I’ve finished licking my fingers, I still have about thirty minutes left before class."

        voice "C-11-4.mp3" #Alex (Bonnie Mitchel)
        alx "I should probably call Naniji, since I haven’t really spoken to her in a few days…"

        "It’ll be nice to hear her voice. I miss her already."

        "Grabbing my phone, I find Naniji in my contacts and dial her number."

        "It’s so reassuring to hear her voice after everything I’ve been through these last couple days. I almost wish I was back with her."

        voice "C-11-5.mp3" #Alex (Bonnie Mitchel)
        alx "...Yes, um, my classes are a lot of fun, actually. We’re keeping bees…"

        voice "C-11-6.mp3" #Alex (Bonnie Mitchel)
        alx "Well, I guess I’ve made one friend. His name’s Caelum…"

        voice "C-11-7.mp3" #Alex (Bonnie Mitchel)
        alx "No, Naniji, it’s not anything like that…"

        voice "C-11-8.mp3" #Alex (Bonnie Mitchel)
        alx "Uh, Catholic, maybe? Oh my god, why are you even asking?"

    jump spirits_a2s4
