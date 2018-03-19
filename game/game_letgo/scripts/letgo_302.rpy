label letgo_302:
    #Rewind point

    "While we’re crossing the river, she stops."

    may "Alright! We’re here!"

    eli "Huh. I was expecting something a little more... indoors?"

    may "Y-Yeeeaaah, wellll... The outdoors is free! Gotta spare a dime wherever we can, right?"

    eli "Mhm."

    "I grin at her."

    eli "So your idea of \"starting the relationship off with a bang\" is to go downtown and try not to spend money?"

    may "That’s--!"

    "I wave my hand."

    eli "Just teasing again. This is a great spot!"

    eli "Fresh air - well, fresh as you can get around here, anyway... And the view is amazing!"

    may "R-Right."

    "I head to the side of the bridge and lean forward on the guard rail. It’s a little low for me, but I manage by stooping a bit. May follows next to me."

    "..."

    eli "Hey. Mind if I ask you something?"

    may "You’re asking me something already, right?"

    eli "Right, it’s just..."

    eli "Is something bothering you?"

    may "Huh?"

    eli "You’ve just been a little off today - and, well... If anything’s wrong, I want you to know I’ll be there for you."

    show may sad

    may "..."

    show may happy

    may "You’re such a cheese ball!"

    may "I’m acting strange? Of {i}course{/i} I am, Eli! It’s our first date!"

    may "It’d be wrong if I {i}wasn’t.{/i}"

    eli "Butterflies, huh?"

    "I smile at her."

    eli "Alright. Well if something’s ever wrong, I just want you to know we can talk about it."

    may "You don’t say? C’mon, Eli, that’s Relationships 101!"

    eli "Ha. Yeah, you’re right. I’m worried about n--"

    #sfx wham

    "After suddenly being shoved by a rushing passerby, I find myself tumbling over the bar! With the river frozen over like that, I..."

    #do... something with the UI to represent the fact that our pov character is currently falling off a bridge

    may "Aah!"

    #horrible crushing sound

    scene black

    may "Are you {i}kidding{/i} me!?"

    #Do the um... The rewind thing. I have no idea how we’re coding this. The rewind point is to the start of 302.

    show bg river

    "We have a good laugh about it and make our way onward, toward May’s supposed plan."

    "She’s been pretty secretive about this. Where are we even going?"

    #####

    menu:

        "Stay at the bridge.":
            jump letgo_302

        "Onward!":
            jump letgo_302softdrink

    ###

label letgo_302softdrink:

    "We keep moving along."

    eli "We getting any closer?"

    "..."

    eli "May?"

    may "Yeah."

    "Oof."

    "She’s getting a little hard to talk to."

    eli "Hey. Wanna hear a joke?"

    may "Huh?"

    eli "A joke. You wanna hear one?"

    may "That’s..."

    show may smile

    may "Sure."

    "...Crap."

    "I don’t actually have any."

    "But it’ll be fine! May has a very... lenient sense of humor."

    eli "Did you ever hear the joke about the snakes?"

    may "Nope!"

    eli "It was..."

    may "You’re not {i}really{/i} gonna say \"hiss-terical,\" are you?"

    "Whoops."

    "So much for lenient."

    eli "No way! That’s way too corny."

    may "Phew. Had me worried there for a second!"

    "..."

    may "So..."

    may "What {i}were{/i} you gonna say?"

    eli "Oh, you know. Something... snakey."

    may "Uh-huh."

    show bg crowd

    "I couldn’t quite keep up the conversation as we made our way into a more crowded part of the city."

    eli "Lotta people out tonight."

    may "Yep."

    "Aaaand shot down again."

    eli "May, listen, I--"

    dude "Woah!"

    #sfx thud

    #If there’s some trend we do with deaths (blackouts, cutting music, etc), do it here

    "Suddenly, someone runs into me!"

    "I fall backwards onto the sidewalk and feel a cold, wet sensation on my chest."

    may "Eli!"

    #If the music changed, change it back

    "Seems he spilled soda on me."

    dude "Sorry, dude! Didn’t watch where I was goin’!"

    "He helps me up."

    dude "Totes in a rush right now, but here’s something for ruining your shirt, man."

    "He hands me five dollars and runs off into the distance."

    eli "Phew. That was weird."

    #rewind point

    show may fucked up

    #should be voiced as deep breathing, or something to that effect
    may "..."

    eli "May?"

    may "God dammit..."

    eli "May!"

    may "Huh?"

    "I smile at her."

    #Choice will go here on the second loop

    jump letgo_302escalator

    ###

label letgo_302escalator:

    eli "I’m fine. Let’s keep going, alright?"

    may "Y-Yeah..."

    eli "We should find a place for me to wash up. How about in there?"

    may "Sure."

    show bg mall

    #escalator should be in the background

    eli "Think I see a bathroom on the second floor."

    "I head toward the escalator."

    may "No!"

    eli "Huh?"

    may "I mean-- Escalators... promote obesity! We should find some stairs and get some cardio!"

    eli "Haha, what?"

    eli "May, don’t tell me you’re afraid of escalators."

    may "What? No, that’s--"

    eli "They make these as safe as they can. It’ll be fine!"

    "I grab her hand and head over to it."

    may "R-Right."

    "...Hm."

    eli "Hey. Mind if I ask you something?"

    may "Huh?"

    eli "Is something bothering you?"

    may "N-No. I’m totally fine!"

    show bg escalator

    "We start heading upstairs. To make sure we get that cardio May cares about so much, we walk up instead of just standing there."

    eli "You’ve just been a little off today - and, well... If anything’s wrong, I want you to know I’ll be there for you."

    may "Right, I just... I’m fine. You don’t have to worry about me."

    "I flash her a smile."

    eli "Alright."

    eli "But if anything’s on your mind, just know th--"

    eli "Whoah!"

    "I end up on the wrong part of a step and lose my balance."

    "I make sure to let go of May’s hand so I don’t take her with me, but..."

    may "No!"

    #horrible tumbling noises
    #cut to black

    "I tumble down the escalator like a ragdoll."

    may "Arrrrrrgh!"

    may "Come on!"

    #Do the rewind thing up to the 302escalator label

    #Can just reuse voice lines here, naturally

    show may fucked up

    may "..."

    eli "May?"

    may "God dammit..."

    eli "May!"

    may "Huh?"

    "I smile at her."

    ###

    menu:

        "Keep going.":
            jump letgo_302escalator

        "Stay here for a bit.":
            jump letgo_302cocoa

    ###

label letgo_302cocoa:

    may "Wait here. I’ll go get you something."

    eli "Huh? It’s fine. I can go w--"

    may "Uh-uh. Go sit down and wait."

    eli "Haha. Aaalright. Never took you for the doting type!"

    may "..."

    may "Right."

    hide may

    "She walks into a nearby building."

    "...Leaving me aaaaaaall alone."

    "Out in the cold."

    "With soda on my jacket."

    "Man, what’s gotten into her?"

    "She seemed just like her usual self back by the tree - but as soon as we came downtown, she’s been... off."

    "Is she nervous? Seems kinda unlike her, but I guess this is our first date and all."

    "Maybe I did something wrong?"

    "I don’t {i}think{/i} I did - but that’s exactly what someone who made a mistake would think, right?"

    "We can’t start things off like this. I’ll ask when I get the chance."

    "Or I would, but when she finally shows up, I’m a little distracted."

    #Rewind Point

    show may

    may "Here."

    "She hands me a clump of paper towels and a cup of hot chocolate."

    eli "Hey, thanks!"

    "I notice she only has the one."

    eli "...Not treating yourself?"

    jump letgo_302manhole

    #choice on rewind

label letgo_302manhole:

    may "Don’t really feel like drinking one right now. No biggie."

    eli "Well, alright."

    may "Let’s go somewhere less crowded."

    eli "Huh? Alright. I know a street nearby that’s normally pretty empty."

    may "Perfect."

    show bg emptystreet

    "I lead the way - until soon enough, we’re all alone."

    eli "Pretty weird to head downtown and then decide you want to be alone. It’s normally pretty hard to do both at once."

    may "Guess I’m weird, then."

    eli "I like it, though! Keeps things fresh."

    may "You would."

    "..."

    "Jeez, it’s like talking to a wall..."

    "I take a long sip of my hot chocolate."

    "...Wait."

    #do the death fakeout music thing again

    "The hot chocolate!?"

    eli "Shit!"

    may "What? What’s wrong!?"

    eli "You could have poisoned me just now!"

    #music turns back to something non-intense

    may "...Huh?"

    eli "I said I’d never eat anything you got me because you might have poisoned it, but it totally slipped my mind! You could’ve really gotten me!"

    may "Heh..."

    may "You still remember that?"

    eli "‘Course! It was fifteen minutes ago. The fact that I forgot at all is just plain embarrassing..."

    may "Oh... Right."

    may "Well, you’re right. I poisoned it. You’re dead now. Any last words?"

    eli "Hm..."

    "I grab her hand."

    eli "I’ll miss you."

    may "Oh, you’re such a sap."

    eli "Hey, I love some good sap! Why do you think I confessed my love to a tree?"

    may "Pfft!"

    may "That’s why I took you to the city, y’know."

    may "Get you farther from the competition."

    eli "Hmm. I dunno... Buildings can be pretty sexy, too."

    may "Yeah?"

    eli "Just take a look."

    show bg citysky

    #I require that this background be at least a little bit sexy

    may "Hey, you’re right."

    eli "Makes you feel small, but... In a good way, I think. Nice and humbling."

    may "...Yeah."

    "..."

    eli "Hey. Mind if I ask you something?"

    "..."

    may "...Yeah. Yeah, I mind."

    may "Whatever you’re thinking, just... Keep thinking it."

    "She squeezes my hand."

    may "Okay?"

    "Huh?"

    "I let go."

    eli "Sorry, May, but I don’t think I can do that."

    eli "It just... It just seems like something’s on your mind. And if that’s true, I want to help."

    may "..."

    may "Nothing’s wrong."

    may "I’m fine."

    may "Okay?"

    "..."

    eli "Okay."

    eli "I believe y--"

    #oops he’s dying make the screen black or something

    eli "Woah!"

    #slip sound

    "I catch a patch of ice and start to slip, but I don’t land like I’m supposed to."

    "I slipped into an open manhole!"

    "My head bangs into the side, and--"

    #thud sfx

    "..."

    may "Dammit..."

    may "{i}Dammit!{/i}"

    may "{i}Why!?{/i}"

    #Do the rewind thing

    jump letgo_303