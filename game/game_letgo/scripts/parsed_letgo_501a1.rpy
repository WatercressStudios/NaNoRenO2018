label letgo_501a1:
    play sound "game_letgo/sfx/Clocktower 3PM.ogg"
    play ambience "game_letgo/ambience/Town Center Plaza.ogg" fadeout 0.1 fadein 0.1

    scene letgo townsquare1 with Dissolve(3.0)
    show eli normal1 with dissolve
    "..."

    "I rub my arms and shake the snow off my boots. It’s getting chilly around here…"

    "I’ve been waiting for a while now - enough time to do {i}three{/i} different runs of the confession."

    "I’m starting to feel so confident that I’m actually putting off the fourth one... for now, anyway."
    
    play music bgmletgo_intro noloop fadeout 1.0
    queue music bgmletgo_loop loop

    show eli normal2 with dissolve
    voice "C-501a1-1.mp3" #Elijah (Michael Potok)
    eli "Hey Tree, what do you think’s taking her so long? Do you think I should, you know, call or text her again?"

    "A cold breeze rustles its branches and a handful of snow falls on top of my head."
    show eli angry2 with dissolve
    voice "C-501a1-2.mp3" #Elijah (Michael Potok)
    eli "Hey! Quit it!"

    "I quickly swipe the icy crystals away from my beanie. None of the bypassers seem to mind me talking to myself - or maybe they do just aren’t showing it."
    show eli normal2 with dissolve
    voice "C-501a1-3.mp3" #Elijah (Michael Potok)
    eli "Naw, you’re right. I don’t wanna appear too needy. She probably didn’t see the time or something. She does that sometimes - lets time slip through her fingers."

    voice "C-501a1-4.mp3" #Elijah (Michael Potok)
    eli "At least I have you for company..."
    show eli normal1 with dissolve
    "Leaning against the tree, I tilt my head up upwards and glance over at the biggest clock in town."

    "Twenty minutes. Maya’s twenty minutes late. She’s been late before, but…"
    show eli worried1 with dissolve
    voice "C-501a1-5.mp3" #Elijah (Michael Potok)
    eli "She’s probably not coming, huh?"

    "I hope she’s okay. I should send her another text, just in case."

    "Letting out a disappointed sigh, I slowly close my eyes."
    scene black with dissolve

    "I’ve always loved the sounds in this plaza: the people, the cafe, the clocktower, the rustling branches."

    "I feel the edge of my mouth curving upwards into a smile."

    voice "C-501a1-6.mp3" #Elijah (Michael Potok)
    eli "Hey, Tree, have I ever told you about the time I realized I was in love with her? We were right here, and--"
    
    stop music fadeout 0.1
    play sound "game_letgo/sfx/Snowball.ogg"

    "My thoughts are interrupted by a snowball."

    scene letgo townsquare1 with dissolve
    show eli goofy1 with dissolve:
        align (0.0, 1.0)

    voice "C-501a1-7.mp3" #Elijah (Michael Potok)
    eli "May!?"

    show may cheeky1 with dissolve:
        align (1.0, 1.0)

    "There she is, wearing the biggest grin on her face. One of her arms is clearly in a post-throwing position, while the other is armed with more icy ammo."

    voice "C-501a1-8.mp3" #Elijah (Michael Potok)
    eli "What are you--"

    show may:
        ease 0.2 align (0.95, 1.0)
        ease 0.5 align (1.0, 1.0)
    pause 0.3

    play sound "game_letgo/sfx/Snowball.ogg"

    "Another snowball makes contact - with my face this time. I can practically taste the ice in my mouth."
    show eli angry1 with dissolve
    voice "C-501a1-9.mp3" #Elijah (Michael Potok)
    eli "Oh, you’re so on! {i}Bring it!{/i}"

    play music bgmloop1comedy_intro noloop fadeout 1.0
    queue music bgmloop1comedy_loop loop

    "I start laughing while gathering my own ammunition."

    show eli:
        ease 0.2 align (0.05, 1.0)
        ease 0.5 align (0.0, 1.0)
    pause 0.3
    play sound "game_letgo/sfx/Snowball.ogg"

    show may cheeky2 with dissolve
    voice "C-501a1-10.mp3" #Maya (shiena)
    may "Nuh, too slow!"

    show may challenge1 with dissolve

    show may:
        ease 0.4 align (0.8, 1.0)
        pause 0.1
        ease 0.4 align (0.9, 1.0)
        pause 0.1
        ease 0.4 align (0.75, 1.0)
        pause 0.1
        ease 0.5 align (1.0, 1.0)
        repeat

    "She laughs as she expertly dodges my flying snowballs. If I thought that would be the end of it, I was wrong."

    show may:
        ease 0.6 align (1.0, 1.0)
    "Maya turns around and rapidly launches a couple high-velocity snowballs at me, one after the other!"
    show may cheeky1 with dissolve
    "Ack! Since when is she a pro-baseballer!? It’s like she’s been practicing this for days!"

    #Omg Sagi you are fucking rough, 'for days', fuck me dude

    play sound "game_letgo/sfx/Snowball.ogg"
    "Hearing a yelp behind me, I spin around and spot a random kid with snow all over his face. He glances down at the snowball in my hands and starts gathering his own."
    show eli worried1
    voice "C-501a1-11.mp3" #Elijah (Michael Potok)
    eli "Wait, stop, I swear that one wasn’t me--"

    play sound "game_letgo/sfx/Snowball.ogg"
    "Ignoring my protests, the kid lobs his, misses, and hits another bystander."

    "Oh no."

    "Pretty soon it’s The American Civil War, only it’s everyone against everyone. People are actually coming out of cafes and shops to join the fight!"
    show may shout1:
        ease 1.0 align (0.3, 1.0)
    voice "C-501a1-12.mp3" #Maya (shiena)
    may "Come on!"

    show may:
        ease 0.5 align (0.65, 1.0)
    pause 0.1
    show eli:
        ease 0.5 align (0.35, 1.0)

    "Maya suddenly grabs my arm and pulls me behind the tree. It seems we’re now in an unofficial truce, using it for cover as we lob one snowball after another at strangers."
    show may suspicious1 with dissolve
    voice "C-501a1-13.mp3" #Maya (shiena)
    may "So, don’t you have something to tell me?"

    show eli goofy1 with dissolve
    voice "C-501a1-14.mp3" #Elijah (Michael Potok)
    eli "Huh?"

    "I duck just in time to avoid an icy projectile. She’s looking at the plastic flowers I put down at the base of the tree earlier."
    show eli happy1
    voice "C-501a1-15.mp3" #Elijah (Michael Potok)
    eli "Oh yeah!"
    show eli worried1
    voice "C-501a1-16.mp3" #Elijah (Michael Potok)
    eli "Wait, right now? It’s basically the Battle of Yorktown out there!"

    "As if to accentuate my point, someone yells {i}\"on my mark, fire!\"{/i} and a great flurry of snowballs fly from one group to another."
    show eli cool1
    voice "C-501a1-17.mp3" #Elijah (Michael Potok)
    eli "Actually, you know what..."

    voice "C-501a1-18.mp3" #Elijah (Michael Potok)
    eli "Screw it, let’s do it!"

    "I turn to her bravely, and..."

    voice "C-501a1-19.mp3" #Elijah (Michael Potok)
    eli "May, we’ve known each other for a long time, and… {i}watch out!{/i}"

    #what a baller, dude
    show eli goofy1 dissolve:
        ease 0.3 align (0.4, 1.0)
    show may aww1 dissolve:
        ease 0.3 align (0.6, 1.3)
    "I quickly pull her towards me, out of the path of a double-projective, resulting in two narrow misses. It looks like the battle’s intensifying!"

    voice "C-501a1-20.mp3" #Maya (shiena)
    may "Umm..."

    "Her body heat draws my attention back to her. She’s leaning against my chest, looking up at me with her large brown eyes. There’s a hint of a blush on her cheeks."
    show eli worried1 with dissolve
    voice "C-501a1-21.mp3" #Elijah (Michael Potok)
    eli "Uh, uh, I’m sorry! I--"
    show may adore1 with dissolve
    voice "C-501a1-22.mp3" #Maya (shiena)
    may "Oh, for crying out loud."

    show eli goofy1 with dissolve
    show may:
        ease 0.2 align (0.6, 1.0)

    stop music fadeout 2.0

    "Maya suddenly tiptoes and kisses me on the lips. I feel my head clouding over and my own cheeks burning. Is this really happening?"

    show eli:
        ease 0.5 align (0.35, 1.0)
    show may:
        ease 0.5 align (0.65, 1.0)

    "When we finally part, she leans over and picks up the plastic flowers."

    voice "C-501a1-23.mp3" #Maya (shiena)
    may "I like you too, Eli."

    image letgo townsquare1 black = "#000"

    play music bgmloop1romantic_intro noloop fadeout 1.0
    queue music bgmloop1romantic_loop loop

    show letgo townsquare1 black with Dissolve(2.0)
    show may happy2 with dissolve:
        align (0.65, 1.0)
    show eli smile1 with dissolve:
        align (0.35, 1.0)
    "The entire world falls away at that moment until it’s just the two of us left. We slowly smile at each other, and I feel a warmth rising in my chest."

    "Nothing can distract me now."

    voice "C-501a1-24.mp3" #Elijah (Michael Potok)
    eli "Shall we go?"

    "She nods. We take each other’s hands and run out of the plaza."
    show eli:
        ease 1.0 alpha 0
    show may:
        ease 1.0 alpha 0
    pause 1.0

    jump letgo_501a2
