label letgo_401:
    #All va lines from here up to the next comment are the same exact ones as in the first scene

    play sound "game_letgo/sfx/Clocktower 3PM.ogg"
    play ambience "game_letgo/ambience/Town Center Plaza.ogg" fadeout 0.1 fadein 0.1

    scene black with dissolve

    "..."

    voice "C-401-1.mp3" #Elijah (Michael Potok)
    eli "Okay, Eli, relax. This isn't something you haven't done before."

    voice "C-401-2.mp3" #Elijah (Michael Potok)
    eli "Well, I guess it is? Regardless..."

    voice "C-401-3.mp3" #Elijah (Michael Potok)
    eli "Just… just breathe, okay? Slow down, stop thinking, and act natural. That's all you have to do."

    voice "C-401-4.mp3" #Elijah (Michael Potok)
    eli "Things will be okay. They’ll end up… okay. They always do. The world's a good place, and you're a good man."

    voice "C-401-5.mp3" #Elijah (Michael Potok)
    eli "Nothing will go wrong."

    voice "C-401-6.mp3" #Elijah (Michael Potok)
    eli "Breathe. Relax."

    scene townsquare2 with dissolve
    show eli cool2 with dissolve:
        align (0.35, 1.0)

    "I lean against the tall tree next to me, my winter coat padding my shoulder from the rough bark. It's a nice, large, and sturdy tree - as it always has been."

    "Here, amid the picturesque snow... this is where I plan on confessing to Maya, my childhood friend."

    #New VA lines start here

    show may angry3 with dissolve:
        align (0.65, 1.0)

    show eli worried1
    voice "C-401-7.mp3" #Maya (shiena)
    may "Elijah!"

    "I jump up, completely caught off-guard."

    "She's early, but that's not what surprises me."

    "Something's {i}wrong.{/i}"

    "She never calls me by my full name."

    "Turning to her, I see her for the first time today. She's… different. {i}Sickly{/i}. May looks awful."

    show eli worried2
    voice "C-401-8.mp3" #Elijah (Michael Potok)
    eli "May? What's wrong? Are you okay? You don't loo--"

    menu:
        "Let's have coffee (disabled)":
            pass
        "Don't have coffee (disabled)":
            pass
        "Let's head downtown (disabled)":
            pass
        "Tell Eli everything":
            pass

    "Snatching my arm, she yanks me off my feet. I fall against her, barely regaining my balance as she pulls me away."

    "I attempt to apologize for falling into her - but she interrupts, dragging me away from the tree."

    voice "C-401-9.mp3" #Elijah (Michael Potok)
    eli "May, please, what's going on? Did I do something wrong?"
    show may tired3
    voice "C-401-10.mp3" #Maya (shiena)
    may "You keep dying."
    stop ambience fadeout 1.0
    play music bgmloop4reveal fadein 2.0 fadeout 1.0
    "What."
    show eli worried1
    voice "C-401-11.mp3" #Elijah (Michael Potok)
    eli "May? What do you mean?"
    show may frustrated3
    voice "C-401-12.mp3" #Maya (shiena)
    may "Shut up and follow me. We need to talk. Alone."

    voice "C-401-13.mp3" #Elijah (Michael Potok)
    eli "I-- Okay, okay, just stop grabbing me so tight!"
    show eli angry2
    "Her nails dig into my wrist, and I can feel my skin tear."

    "What's going on with her?"

    "Dying? What the hell?"

    scene road long
    hide eli
    hide may
    "She drags me through the alley and the road, down streets and around corners. At first I'm utterly disoriented, completely lost - but after a while, I understand."

    "We're on our way to her apartment. It's been a while since I've been there…"

    "Honestly, I used to go there all the time for movie nights, but we couldn't keep it up."

    "Why today? Is she afraid of my confession? Did something happen over Thanksgiving? Is her family okay?"

    "Oh god, I hope they’re okay! I mean, it's probably me being an idiot, but…"

    "My heart beats faster, and the pit in my stomach only grows worse. With all of the possibilities flying through my head, I feel sick."

    "She tears open the apartment complex’s door, leading me to the staircase. She stomps up them, and I'm half-tempted to ask her to quiet down for her neighbors' sake - but I don't think that would be appropriate."

    #Show maya room with dissolve
    "Fumbling for her keys, she opens the door and thrusts me inside."

    "Rushing past me, I follow her into the bedroom. Other than a messy bed, it looks just like it always has."

    "She turns to me, tears in her eyes."
    show may tired3 with dissolve:
        align (0.65, 1.0)

    show eli worried2 with dissolve:
        align (0.35, 1.0)

    voice "C-401-14.mp3" #Elijah (Michael Potok)
    eli "May, I'm worried, and confused, and I don't understand what's going on. You know you can trust me with anything, right?"
    show may sad3
    voice "C-401-15.mp3" #Maya (shiena)
    may "I don't know what to do with you anymore."

    "Her voice is deep, quiet, shaking. She tries to avoid eye contact, looking to the ground."
    show eli worried1
    voice "C-401-16.mp3" #Elijah (Michael Potok)
    eli "M-Me? Whatever I did, I'm sorry. We can work through this together, yeah? Like we always have?"
    show may sad4
    "She crosses her arms, staring at the carpet beneath her feet. Silence fills the room, eerie and terrifying."
    show may forcedsmile4
    "It drags on."
    show may sad4
    "Even longer…"
    show may frustrated4
    "She tries to start talking, but stops herself. She doesn't seem to know exactly what to say."
    show may sad4
    voice "C-401-17.mp3" #Maya (shiena)
    may "Eli…"
    show eli worried2
    voice "C-401-18.mp3" #Elijah (Michael Potok)
    eli "May?"

    voice "C-401-19.mp3" #Maya (shiena)
    may "What if you knew… what if you knew someone you love is about to die?"

    voice "C-401-20.mp3" #Elijah (Michael Potok)
    eli "...What?"

    voice "C-401-21.mp3" #Maya (shiena)
    may "What if you knew that, no matter how hard you fought - no matter what you did, that person would {i}always{/i} die? That you'd never be able to save them?"
    show eli worried1
    voice "C-401-22.mp3" #Elijah (Michael Potok)
    eli "Did something happen over Thanksgiving? Something with your family? Everyone was so healthy last time I saw them."
    show may angry4
    voice "C-401-23.mp3" #Maya (shiena)
    may "No! Eli, shut the fuck up for once! Of course it isn't my family!"
    show eli sad2
    "Her cries rattle me to the core, so I take a step back."

    "What's going on? What did I do?"

    "She looks like a ghost. The tears begin to stream down her face - and they don't stop no matter how many times she uses the cuff of her jacket to wipe them away."

    "I reach forward to help her, but she shoves my hand away."

    voice "C-401-24.mp3" #Elijah (Michael Potok)
    eli "Talk to me, Maya. That's why you brought me here, right?"
    show may frustrated4
    voice "C-401-25.mp3" #Maya (shiena)
    may "Do you think I'm crazy, Eli?"

    "The question catches me so off-guard, I stumble over myself."
    show eli worried1
    voice "C-401-26.mp3" #Elijah (Michael Potok)
    eli "What? Of course not. I’d never think that!"
    show may sad4
    "She hugs herself even harder, her knuckles whitening, and she sobs."

    "On reflex, I step forward and hold her tight. She cries into my chest, the tears struggling to dampen to my coat."

    "The plastic flowers in my hand drop to the floor."

    voice "C-401-27.mp3" #Maya (shiena)
    may "You're dying, Eli."

    #just writing that line sends shivers down my spine. I CAN'T WAIT for 'sausage' to voice this ;D

    "What."

    "Wait, what!?"

    voice "C-401-28.mp3" #Maya (shiena)
    show may frustrated4
    may "I've tried so, so many times - but no matter what I do, you always die. Be it in a car crash, or by a fall, or by some other stupid fucking thing, you {i}always{/i} die."

    "She's not making any sense. Has she been having..."
    show eli worried2
    voice "C-401-29.mp3" #Elijah (Michael Potok)
    eli "Nightmares?"
    show may angry4
    voice "C-401-30.mp3" #Maya (shiena)
    may "Reality {i}is{/i} the nightmare, Eli. I'm stuck in a loop, reliving the same day over, and over, and over, and over and over again."
    show may sad4
    voice "C-401-31.mp3" #Maya (shiena)
    may "I swear, I've been trying to save you for years."

    "A loop? Like, Groundhog Day? That only happens in movies. Our life is too, well, {i}normal{/i} for that."
    show eli worried1
    voice "C-401-32.mp3" #Elijah (Michael Potok)
    eli "I… I don't know what to say."

    "I really don't. This is completely unexpected. She's gotta be joking, right?"

    "She looks up at me with her racoon eyes."
    show may frustrated4
    voice "C-401-33.mp3" #Maya (shiena)
    may "Of course you don't believe me. You {i}never{/i} do."

    "Never? So, she's apparently told me before, and I didn't believe her?"

    "...Can I? This type of thing doesn't happen."

    "Right?"

    "But it's {i}her.{/i} She wouldn't lie to me about this - not in the state she's in now."
    show eli normal1
    "Sighing, I stare deeply into her eyes."
    show eli angry1
    voice "C-401-34.mp3" #Elijah (Michael Potok)
    eli "Whoever didn't believe you - that version of me - I'm sorry I wasn't there to kick him straight."
    show eli normal1
    voice "C-401-35.mp3" #Elijah (Michael Potok)
    eli "But you're obviously torn up about this. I believe you, and we can work through this together, okay?"
    show eli smile1
    show may smile4
    "I reach up, gently trailing my fingers through her hair, pulling her up towards me. I kiss her on her forehead and hug her tightly."

    voice "C-401-36.mp3" #Elijah (Michael Potok)
    eli "So, I'll make you some tea, okay? Collect your thoughts and we can talk about this. Is that okay?"

    "She nods quietly and we separate. I watch her sit on the bed, head in her hands, and I can hear her trying to slow her breathing."

    "She's having a panic attack - and, naturally, this isn't a normal one."

    "How would I react if she were the one I couldn't save?"

    "I wouldn't ever stop trying. Even if I had to live the same day until the end of time - and even then..."

    "God, I still find it hard to believe…"

    "But that doesn't matter! I believe in {i}her{/i}, and that's all that matters right now. I have to be there for her, no matter how ridiculous the situation."

    "I love her, after all."
    hide may with dissolve
    hide eli with dissolve
    #scene may kitchen with dissolve
    show eli sad1
    play music bgmletgo_intro noloop fadein 2.0 fadeout 1.0
    queue music bgmletgo_loop loop
    "After one final lingering stare, I leave the room and go through her cabinets. I find the kettle in no time at all, since it’s nestled away in the same cabinet it's always been in."

    "She's nothing if not a creature of habit."

    "The metal object rattles in my hands."
    show eli worried1
    "I can't seem to stop it from doing so. My hands are shaking."

    "It's my turn to focus on my breathing, slowing it down. Seeing her so distraught has me shaking. I don't like this, and the pit's still there."

    "The concept of a Groundhog Day scenario is so foreign - so alien - to me that I don't even know where to begin. Even theorycrafting, how would it work? What's the way to escape it?"

    "You'd normally have to trigger some event. Some moral has to be learned - someone has to be saved…"

    "But if she's tried every moral, every trigger... If she's tried to save me every time and it always ends the same, then what? What's the solution?"

    "I pour some tap water into the kettle, and set the stove to heat it up."

    "She has to try something new. That's the obvious solution. If it really is based around my death, and she's constantly trying to save me, well…"
    show eli sad2
    "Then there's only one solution."

    "Right?"

    "I sit back against the countertop, silently thinking to myself as the pot warms up. I'll make her some soothing citrus tea. That should help her a little bit."

    "Really, it's to keep her hands - to keep her - busy. The warm drink and the subtle movements will help keep her mind off of the big issue. It'll also help her feel at home, as if this is just another day."

    "I struggle to keep myself from thinking about literally anything, as I need to be {i}present{/i} for her; I can't be my usual \"head in the clouds, too fast to follow\" self."
    show eli cool1
    "With slow, deliberate actions, I retrieve the tea and catch the kettle before it screams at me."

    "I pour two cups and dip the tea bags in. With a single moment of hesitation, I move to her bedroom."
    hide eli
    show may sad3 with dissolve:
        align (0.65, 1.0)

    show eli cool1 with dissolve:
        align (0.35, 1.0)

    "She's still in the same stance from  when I left."
    play music bgmloop4reveal fadein 2.0 fadeout 1.0
    "She's still crying - and while her breathing is a bit slower, it immediately hastens as I enter the room."
    show eli sad1
    "My hand hovers nearby, offering the drink - but she's too lost to accept it right now. Electing to place it on the nearby nightstand, I walk opposite her and lean against the wall."

    voice "C-401-37.mp3" #Elijah (Michael Potok)
    eli "I wish I could understand the gravity of this situation, but I really can't… Regardless, I'm still going to try my damndest to help you."
    show may tired3
    voice "C-401-38.mp3" #Maya (shiena)
    may "...There's nothing you can help me with. I wanted to tell you about what's happening to me, but I don’t really know what you can do."

    voice "C-401-39.mp3" #Maya (shiena)
    may "I'm torturing myself. I'm torturing you."

    voice "C-401-40.mp3" #Maya (shiena)
    may "I'm a sinking ship tied to an empty harbor."

    voice "C-401-41.mp3" #Maya (shiena)
    may "...And I want it all to end."

    voice "C-401-42.mp3" #Elijah (Michael Potok)
    eli "Maybe you haven't tried everything, Maya."
    show may angry4
    voice "C-401-43.mp3" #Maya (shiena)
    may "Of course I've tried everything! I've spent an endless amount of time trying new things, but there aren't any choices open to me."

    voice "C-401-44.mp3" #Elijah (Michael Potok)
    eli "Maya."
    show eli normal1
    "I speak out with a finality, my words reaching her, commanding her to slow down - to listen."
    show may sad4
    "She looks up to me, her hands buried in her ragged hair."

    voice "C-401-45.mp3" #Maya (shiena)
    may "...What, Elijah?"
    show eli sad1
    voice "C-401-46.mp3" #Elijah (Michael Potok)
    eli "There's one thing you haven't tried, isn't there?"

    voice "C-401-47.mp3" #Maya (shiena)
    may "I- What? What could that possibly be?"

    voice "C-401-48.mp3" #Elijah (Michael Potok)
    eli "Think about what you've been trying to do each time."
    show may angry4
    voice "C-401-49.mp3" #Maya (shiena)
    may "I've been trying to save yo-- No!"

    voice "C-401-50.mp3" #Elijah (Michael Potok)
    eli "Maya."
    show may frustrated4
    voice "C-401-51.mp3" #Maya (shiena)
    may "That's {i}not{/i} an option."

    voice "C-401-52.mp3" #Elijah (Michael Potok)
    eli "Maybe you have to…"
    show may sad3
    voice "C-401-53.mp3" #Maya (shiena)
    may "No, stop. Shut up! Don't you {i}dare{/i} say it."

    voice "C-401-54.mp3" #Elijah (Michael Potok)
    eli "Maybe you have to let me die."
    show may sad4
    show eli sad2
    voice "C-401-55.mp3" #Elijah (Michael Potok)
    eli "Maybe you have to let me go."

    voice "C-401-56.mp3" #Maya (shiena)
    may "No no no! No no no no no. I refuse!"
    show may angry4
    voice "C-401-57.mp3" #Elijah (Michael Potok)
    eli "Maya."

    voice "C-401-58.mp3" #Maya (shiena)
    may "Please God… No."
    show may sad4
    "I grab her by the shoulder, crouching down in front of her. She gives up on wiping her face, again succumbing to the tears."

    voice "C-401-59.mp3" #Elijah (Michael Potok)
    eli "You have to try something different. You're hurting, and seeing you like this is hurting me, too, Maya."

    voice "C-401-60.mp3" #Elijah (Michael Potok)
    eli "You have to, for our sake. If you do and it fails, I'll still be here - and if it succeeds, then that's what you were supposed to do in the first place."

    voice "C-401-61.mp3" #Elijah (Michael Potok)
    eli "I can tell you what I think you need to do, but {i}you{/i} have to make the choice."

    "She finally makes eye contact with me - her dark eyes like empty wells. Her face is flushed and red."

    voice "C-401-62.mp3" #Maya (shiena)
    may "Please."

    voice "C-401-63.mp3" #Maya (shiena)
    may "Don't leave me!"

    voice "C-401-64.mp3" #Elijah (Michael Potok)
    eli "You have to make the choice, Maya."
    stop music fadeout 2.0
    menu:
        "Let Go.":
            jump letgo_402
        "It can't end like this.":
            jump letgo_502
