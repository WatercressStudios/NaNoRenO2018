label hopcheck:
    if hope:
        jump daicheck
    else:
        play music "game_flood/music/city.mp3" noloop fadein 1.0
        jump map
        
label daicheck:
    if daisy:
        jump olicheck
    else:
        play music "game_flood/music/city.mp3" noloop fadein 1.0
        jump map
        
label olicheck:
    if oliver:
        jump flood_501
    else: 
        play music "game_flood/music/city.mp3" noloop fadein 1.0
        jump map

label flood_501:
    
    scene flood riverside with dissolve
    play ambience "game_flood/ambience/river.ogg"
    play music "game_flood/music/climax.mp3" noloop fadein 1.0
    "..."
    "... ..."
    "God, what time is it? How long have I been out here for?"
    "It has to be late. My feet are absolutely killing me."
    "And my eyes, and my arms, and... everything."
    "It's hard to keep my eyes open. It's a struggle just to stay awake."
    "I'm fine, I think, I just... need another dose of caffeine. Energy."
    "Maybe if I rest my eyes a little bit..."
    show oph defensive close with dissolve
    voice "game_flood/voice/C-501-1.ogg" #Ophelia (Cospcaptor)
    oph "...Nn..."
    "No, {i}no{/i}, have to stay awake. Otherwise, the Flood is gonna..."
    "Just focus. One step in front of the other. Left, right, left, right."
    "...Left... right... the steps turn to staggers." 

    show oph defensive
    "Forcing myself to stay awake is becoming increasingly difficulty. My movements turn sluggish."
    "The tough concrete looks so inviting. I could just collapse, curl into a ball like a cat, and pass out right here."
    "But the idea of the Flood lingers in the back of my mind. And it's weighing my head down more and more."
    "...Those hated sensations play out across my fatigue mind, like phantom pains needling me further."

    show oph irritated close
    voice "game_flood/voice/C-501-7.ogg" #Ophelia (Cospcaptor)
    oph "C'mon, pull it together..."
    #sfx slap
    show oph irritated
    
    "I slap my cheeks to try and jolt me awake. The effect is sharp, but fleeting, and I soon feel fatigued once more." 
    "I'm not passing out here. I haven't had much of any control over anything that's happened tonight..."
    "I can't control that the Flood will come, eventually, but I can at least determine it on my own terms. And I'm not passing out in the middle of the sidewalk."
    "...I guess that's it. If it comes, it comes. There's not much I can do about it."
    "Can't run away from it. Can't fight back. I suppose this is the end, but..."
    "...I at least want to rest in the comfort of my own home."

    scene black with dissolve
    "Taking a sharp breath, I lurch forward, step by step. The cold winds prop me up, keep me going."
    "Ironically, they keep me pulled into the real world."
    scene flood neighborhood with dissolve
    stop ambience fadeout 1.0
    "The houses along the sides of the street become more and more familiar." 
    "Familiar, identically-constructed houses. I was only looking for one, though."
    voice "game_flood/voice/C-501-8.ogg" #Ophelia (Cospcaptor)
    show oph surprised with dissolve
    oph "Home."
    "Spotting the familiar, two-storey house, my pace quickened a bit, stumbling further along the sidewalk, up the driveway."
    play sound "game_flood/sfx/keys.ogg"
    "Fumbling with my keys, they nearly slip from my unresponsive fingers..."
    play sound "game_flood/sfx/unlock.ogg"
    "...But with some struggle, I wrest the door open. From there, a straight ascent upwards, round the corner, at the end of the hall, and..."
    
    scene flood bedroom with dissolve
    "...My room. No time to gawk at the familiar sights, dimly lit by the faint light of the coming dawn."
    "Trudging forward one, two more steps, I take no further care but to careen forward..."
    play sound "game_flood/sfx/bed.ogg"
    "...And hit the bed, face first, fully clothed."
    #scene black with dissolve
    "Come what may, I'm tired of being afraid. I'm tired of bending over to this Flood."
    "...I'm so... so tired..."
    "When my head hit the pillow, I was already out like a light."
    scene black with dissolve
    stop music fadeout 1.0
    "..."
    "... ..." 
    "... ... ..."
    "Today is my 18th birthday."
    play music "game_flood/music/ending.mp3" noloop fadein 1.0
    "It's been... surprisingly uneventful. After my late-night adventures, I ended up sleeping until four in the afternoon."
    "Oversleeping like that's supposed to be bad for you, but... I feel better rested than I've been in a long time."
    "Mom and Dad're gonna throw me a party later. It's been pushed into the back of my mind."
    "I didn't dream about the Flood tonight. That sense of building dread, and anxiety, it..."
    "...Well, it... it's still kinda there, but... not in the pervasive, metaphorical and literal sense."

    "After a horrible sleep, I'd just... sit in bed, and vegetate for a while. Today, I just wanted to get out. See some things."
    "I guess my mind plays some tricks on me after all. How ironic."
    show flood sunrise with dissolve
    play ambience "game_flood/ambience/tide.ogg" fadein 1.0
    "I dream of the Flood again, but it's... different. Serene, peaceful. The gentle, lapping waves inspire a sense of zen, not dread."
    "Seeing this gets me thinking. The beach is nice this time of year. It'll be a bit before they get really crowded."
    "My eyes lowered on the coming and going tides. The way the hypnotic waves creep closer to shore..."
    "...They say the water levels are rising around the world, too. I guess that's a more literal flood."
    "It'd be harder to ignore if you had it banging about in your skull every day..."
    "I don't know why I came out here specifically. Maybe the sound of the sea, of rushing water..."
    "Maybe it's a little comforting, in a perverse way. Something I adjusted to."
    "...I don't like that, no. I'm an adult now. I can do anything, right?"
    "There's... too much I could do, I guess. Where would I even start?"
    "I feel like I should've figured things out ages ago, but I got... fixated on stuff that, well, didn't matter at all."
    "What was I doing outside all night? Was there a point? Did I just... need to escape?"
    voice "game_flood/voice/C-501-9.ogg" #Ophelia (Cospcaptor)
    oph "..."
    "I guess I can figure it out later. It might be easier to; sleep might even come a bit easier now."
    "I met some weird people last night, too."
    "The opera house's getting demolished, so I could bid it farewell with Oliver. Daisy would probably want to see a familiar face."
    "Hope seemed lonely too... I hope she's doing better now."
    "I'll just enjoy the view a little bit longer. I can take it easy."

    show flood sunrise zoomout with dissolve

    "It's weird. Seeing the sunset like this used to inspire so much dread."
    "I guess it still does. For so long, I'd have a feeling that the worst was yet to come."
    "...That could still be true, in the grand scheme of things, but... I don't know anymore. I don't think I {i}ever{/i} knew."
    "Maybe I should feel powerless, I dunno. I guess it's... liberating, is the right word."
    "I thought that, if I put my mind to it, I could do anything. That's what I was taught, at least."
    "I mean, if I tried, I could do a lot of things, but... there's only so much I was ever able to do."
    "I probably can't save the world. Maybe the Flood will come, one day."
    "There was nothing I could've done, but... I can apply myself, in my own way."
    "...I guess the first thing I could do is pick up some trash along the shoreline too."
    "I'll figure something out. I'm an adult. I'm not over the hill yet, not even close."
    "...Maybe, in all this anxiety, there's a tinge of excitement in me too. Just a bit."

    return
