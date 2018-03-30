label letgo_601:
    play music bgmletgo_intro noloop fadeout 1.0
    queue music bgmletgo_loop loop
    "I pull a pillow around my head, straining against the sun. Please, {i}please{/i}, don't make me wake up."

    "I don't want to."

    "I don't want to see what today has in store for me. It certainly won’t be good."

    "There won't be a good ending for me - or for him."

    "I pull the sheets back up over my face to hide - but they do very little to dull the sunlight."

    "Fine. I submit."

    #Open eyes, Maya's room
    scene letgo house bedroom with dissolve
    "Opening my eyes, I struggle and swing my feet down to the floor."

    "My phone's screen is black - and I'm tempted to keep it that way forever. But…"

    "I need to know the date. I {i}need{/i} to know."

    "Unlocking it, I get my answer."

    "I'm out of the loop."

    "I'm free."

    "That also means…"

    "He was right."

    #Internal monologue from this point onto the next comment is only to appear of Scene 502 was the scene you received, rather than 501

    if letgo_badending:
        "After so much time..."

        "Years and years."

        "Decades, even."

        "Probably more..."

        "I'm finaly free from the hell that was that day."

        "I'm sorry, Eli. I couldn't save you."

        "You were right, you know. From the very beginning, you were right. I failed, in the end, as you knew I would."

        "You're dead and gone."

        "Forever."

        "I... hurt. So much."

        "Time does that to a soul."

        "I may be a young woman in body, but of soul?"

        "No, of soul I'm old. I'm {i}ancient{/i}."

        "It took me so long to come to the same conclusion you did. I'm here now, though. And I remember that promise I made so, so long ago."

    #This is the end of the 502 specific monologue.

    "My hair tangles around me, and I haphazardly comb it with my cold hands."

    "I'm a mess."

    "His flowers mock me."
    #Put CG Here
    scene letgo flowers with Dissolve(2.0)
    "Pulling them close, I study each petal in great detail. Plastic, obviously, since I'm allergic to most flowers; this is the last trace of him that I have in my life now."

    "Sure, he could have lived - but I know deep down that that's not the case."

    "I pet the plastic petals, squeeze the stem, and run my hands along the leaves."

    "He was holding them so tight when he gave them to me… He bent the stem a bit."

    "They still smell like him."

    scene letgo flowers close with Dissolve(2.0)

    "I hug them close, pressing them so hard to my chest that I threaten to bend them myself."

    "I miss you, Eli."

    "I love you."

    scene letgo flowers with dissolve

    "A light knocking on the door tears me from my thoughts - and I look up to see my mother walk in."

    "I guess she's the messenger this time."

    voice "C-601-1.mp3" #Mom (N/A)
    mom "Maya…"

    voice "C-601-2.mp3" #Maya (shiena)
    may "Yes, Mom?"

    voice "C-601-3.mp3" #Mom (N/A)
    mom "I have some…"

    "She looks away, her eyes red from tears."

    "We all loved Eli."

    "She doesn't quite understand that I already know what she's going to tell me."

    voice "C-601-4.mp3" #Maya (shiena)
    may "It's okay Mom, you can tell me."

    voice "C-601-5.mp3" #Mom (N/A)
    mom "Eli… he passed away last night."

    scene letgo flowers cry with dissolve

    "Dammit Maya, you've heard this a thousand times before - no, you've {i}seen{/i} this a thousand times before."

    "Why are you crying now?"

    voice "C-601-6.mp3" #Mom (N/A)
    mom "I'm so sorry, I know you loved him very much."

    "She reaches in close for a hug, and I do nothing to stop her."

    scene letgo flowers close with dissolve

    "Quietly, I sob into her shoulder."

    "I'm glad she got to the point, though. I'm tired of not knowing."

    "I'm tired of that sick anticipation - that panic attack that happens just before you get news you know you are going to get, but desperately want to avoid."

    "I hate that."

    voice "C-601-7.mp3" #Maya (shiena)
    may "Did he suffer?"

    voice "C-601-8.mp3" #Mom (N/A)
    mom "No. He died in his sleep - without any pain. That's all we know so far, but…"

    voice "C-601-9.mp3" #Maya (shiena)
    may "That's enough. Just knowing he went peacefully, happy… That's all that matters."

    if not letgo_badending:

        voice "C-601-10.mp3" #Maya (shiena)
        may "We had a good day yesterday. He confessed to me, and we spent our entire day together."

        "Now it’s her turn to burst into tears - that strange, motherly empathy kicking in. She feels my pain in a way very few can."

        voice "C-601-11.mp3" #Maya (shiena)
        may "The last thing he remembered - the last day he experienced - was a very, very happy one."

    voice "C-601-12.mp3" #Maya (shiena)
    may "If nothing else, we can have solace in that."

    "My words seem cold, uncaring, unkind - but I mean them. I'm… broken, but I still have a heart."

    "I still love him."

    "We sit like this for what seems like hours, my mom and I."

    "And in between us, Eli's flowers feel warm in my hands."

    "I made you a promise."

    stop music fadeout 5.0
    scene letgo flowers close sun with Dissolve(3.0)
    scene letgo flowers cry sun with Dissolve(1.0)
    scene letgo flowers sun with Dissolve(1.0)

    "I'll see you again one day. I swear it."

    "Goodbye."

    scene black with Dissolve(2.0)
    scene menu_fireplace with Dissolve(2.0)
