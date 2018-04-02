label spirits_a2s2:

    scene black with dissolve

    "School is… okay today, so far."

    "Honestly, there just isn’t a lot to talk about in regards to it. Now that I’ve been to all my classes, things have a chance at becoming routine."

    "Caelum is a welcome exception, though. Although he isn’t in all of them - and although there… really isn’t anyone else to talk to - he’s still there. He’s still… himself."

    "I suppose I can say that's comforting."

    if caelumAlive == False:
        "But he wasn’t in class today, though. I suppose he could just be sick, but… it worries me."
    else:
        "He definitely seemed a little on-edge this morning, though, after his close call last night with... {i}whatever{/i} that was. I'm a little concerned for him."

    "I guess it’s probably nothing - for now, anyway. I have a free period now, and although I have my homework - different duties hanging over me - I can push them aside, at least for a while."

    "At the very least, I can take just a few minutes to relax and shift my mind away from  \"school mode.\""

    "..."

    play music bgmspirits_main

    scene spirits dorm hallway with dissolve

    show alx neutral1 with dissolve

    "I open the door to the dorms; the weight of my bag pulls down on my back."

    "As I head towards my room, I take subtle steps through the hallways - paying no attention to anyone I pass by."

    "After a few minutes, I'm there."

    scene spirits alex bedroom clean with dissolve

    show alx neutral1 with dissolve

    "The schoolbag immediately drops onto the floor. The door is rapidly closed behind me, too."

    "I resist the urge to flop onto the bed and begin my eternal slumber; it would just be filled with nightmares again - and the last thing I want is someone checking up on me."

    show alx happy1 with dissolve

    "Once I check my computer, I can {i}finally{/i} unwind."

    "I put the password in, open up the internet, and check everything I need to: school stuff, personal stuff, and emails--"

    "Oh, I… actually have one. It’s school stuff, of course - but I suppose it’s better than nothing."

    show alx surprised1 with dissolve

    voice "C-10-1.mp3" #Alex (Bonnie Mitchel)
    alx "Inspections?"

    "Well, okay? I didn’t really expect them this early, but I guess they were going to happen regardless."

    show alx neutral1 close with dissolve

    voice "C-10-2.mp3" #Alex (Bonnie Mitchel)
    alx "Oh well."

    show alx neutral1 with dissolve

    "I close my laptop and look at the rest of the room. Honestly, I just want to nestle against the mattress; there’s no harm in checking everything else, though."

    "After all, there’s a slim chance the room might, like, light on fire if I actually take a nap."

    "I stand up, take a few steps, and look around."

    show alx surprised1 with dissolve:
        ease 0.2 align (0.2,1.0)

    voice "C-10-3.mp3" #Alex (Bonnie Mitchel)
    alx "What the--"

    show spirits gun as gunicon:
        xanchor 0.5
        yalign 1.0
        xpos 0.5
        ypos 0.5
    with Dissolve(1.0)

    "The gun is back in the box."

    "{i}{b}The gun is back in the box!?{/b}{/i}"

    "I don’t know how, when, or why, but there it is - in plain sight..."

    "In plain sight of the inspectors, who will be here in a few days’ time."

    "That's--"

    "That's going to be a problem."

    hide gunicon

    show alx surprised1 close with dissolve:

    "But it’s fine. I just need to breathe, remove the gun again, put it somewhere else, and--"

    play music bgmspirits_gen fadeout 0.5

    voice "C-10-4.mp3" #Genevieve (Lasli Tran)
    gen "It'll keep coming back."

    show alx surprised1 with dissolve:

    "My body jolts and jumps. Immediately, a bitingly cold and bitterly uncomfortable feeling washes over me."

    "I look around, trying to find the voice; I can almost remember the face I’d seen it talk with bef--"

    voice "C-10-5.mp3" #Genevieve (Lasli Tran)
    gen "I'll keep putting it there."

    show gen neutral1 at centerright:
        alpha 0.2
        linear 2 alpha 1

    "She’s there in front of me. Blonde ringlets, blue eyes, a nightgown… and of course, an ethereal silver tinge."

    "It’s the girl from before - the one who tugged on my hand…"

    "The one who appeared in my nightmare."

    "Why is she here? And more importantly: why did she do this?"

    voice "C-10-6.mp3" #Genevieve (Lasli Tran)
    gen "Until you find my killer, I'll keep putting it back."

    "I remember what she said, back… then, when we had spoken for the first time."

    "She was murdered, and wanted me to help her get justice - but…"

    voice "C-10-7.mp3" #Alex (Bonnie Mitchel)
    alx "How?"

    "The spirit doesn't respond. She just looks at me, a confused expression on her face."

    "It’s as if she doesn't understand what I said. I get it... I guess I can explain."

    voice "C-10-8.mp3" #Alex (Bonnie Mitchel)
    alx "How do I help? How do I find your killer?"

    voice "C-10-9.mp3" #Genevieve (Lasli Tran)
    gen "..."

    voice "C-10-10.mp3" #Genevieve (Lasli Tran)
    gen "Look under the last step."

    voice "C-10-11.mp3" #Alex (Bonnie Mitchel)
    alx "...What?"

    voice "C-10-12.mp3" #Alex (Bonnie Mitchel)
    alx "What do you mean? How do I--"

    show gen neutral1 at centerright:
        alpha 1
        linear 2 alpha 0

    "I’m not graced with a response. Before I can finish - or ask any further questions - she vanishes; it’s as if she wasn’t there in the first place."

    hide gen

    "Almost as if I’ve just been talking to myself…"

    "Look under the last step."

    "The last step of what!? What the hell is that supposed to mean? I want to - I {i}have{/i} to - help, but at this rate I’ll be out of time!"

    "I stand there in the stunned silence for a moment, and think."

    "Last step. Last step… Last… step…"

    "There’s no answer."

    "I stand there, in my room, unable to relax. Unable to figure out anything."

    "I’m doomed, aren’t I?"

    stop music

    jump spirits_a2s3
