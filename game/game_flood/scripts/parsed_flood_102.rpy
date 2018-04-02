label flood_102:
    scene flood diner with dissolve

    stop ambience
    play sound "game_flood/sfx/splash.ogg"
    "{b}Splash!{/b}"
    #music jazz??? something for a run down coffee shop idk
    
    play music "game_flood/music/cafe.mp3" fadein 1.0
    show oph scared close

    voice "game_flood/voice/C-102-1.ogg" #Ophelia (Cospcaptor)
    oph "{b}ACK!{/b} {i}Pbt, ptoo, ptooie...{/i}"
    #voice: annoyed
    
    show oph scared
    
    voice "game_flood/voice/C-102-2.ogg" #Waitress (Allison Seils)
    wai "There. You awake now, sweetcheeks?"
    "I sputter to life, cold ice water splashing down my rosy cheeks."
    
    show oph irritated
    
    "Through irritated eyes, I see a waitress standing across from me, an exasperated look painted on her face. Looking to be in about her mid-30s, bags were already forming under her eyes."
    voice "game_flood/voice/C-102-3.ogg" #Waitress (Allison Seils)
    wai "I hope you had a {i}pleasant{/i} nap."
        
    menu:
        "Hey, what's the big idea!?":
            
            show oph weirdedout
            
            voice "game_flood/voice/C-102-4.ogg" #Ophelia (Cospcaptor)
            oph "Hey, what the hell was that!? You can't treat your customers like that!"
            voice "game_flood/voice/C-102-5.ogg" #Waitress (Allison Seils)
            wai "If you actually {i}bought{/i} anything, maybe you would've gotten the VIP treatment."
            voice "game_flood/voice/C-102-6.ogg" #Ophelia (Cospcaptor)
            oph "What VIP treatment!?"
            voice "game_flood/voice/C-102-7.ogg" #Waitress (Allison Seils)
            wai "I could've dumped premium, volcano-filtered water on your face instead."
            voice "game_flood/voice/C-102-8.ogg" #Ophelia (Cospcaptor)
            oph "Oh, that's tempting."
            voice "game_flood/voice/C-102-9.ogg" #Waitress (Allison Seils)
            wai "You want special treatment, go to Starbucks."
            
        "Nice to see you too...":
            
            show oph neutral
            
            voice "game_flood/voice/C-102-10.ogg" #Ophelia (Cospcaptor)
            oph "Morning to you too..."
            voice "game_flood/voice/C-102-11.ogg" #Waitress (Allison Seils)
            wai "The least you could do is pretend to smile."
            voice "game_flood/voice/C-102-12.ogg" #Ophelia (Cospcaptor)
            oph "Can't while my face is wet. It'd cause wrinkles."
            voice "game_flood/voice/C-102-13.ogg" #Waitress (Allison Seils)
            wai "You can borrow my rag."
            voice "game_flood/voice/C-102-14.ogg" #Ophelia (Cospcaptor)
            oph "I don't even know where your rag has been..."
            
        "Could you splash me with coffee instead?":
            
            show oph irritated
            
            voice "game_flood/voice/C-102-15.ogg" #Ophelia (Cospcaptor)
            oph "I need my caffeine fix, couldn't you have splashed me with coffee instead?"
            voice "game_flood/voice/C-102-16.ogg" #Waitress (Allison Seils)
            wai "That'd be 2.50."
            voice "game_flood/voice/C-102-17.ogg" #Ophelia (Cospcaptor)
            oph "I know you still have the same pot on from an hour ago. You barely ever change it."
            voice "game_flood/voice/C-102-18.ogg" #Waitress (Allison Seils)
            wai "It matures the flavour to keep it on."
            voice "game_flood/voice/C-102-19.ogg" #Ophelia (Cospcaptor)
            oph "That's a load of...  ugh, whatever."

    show oph neutral close at flip

    "Rubbing my face, I look around my new settings. Aside from the overabundance of moisture splashed upon my person, it's much dryer in here than it was a second ago."
    
    show oph neutral
    
    "Right, I'm remembering now. I staggered into a late-night café. I must've taken a nap at the counter..."
    voice "game_flood/voice/C-102-20.ogg" #Waitress (Allison Seils)
    wai "We're closing soon. You should get packed up."
    
    show oph neutral close
    
    "I groan, burying my head in my hands."
    voice "game_flood/voice/C-102-21.ogg" #Waitress (Allison Seils)
    wai "Hey, no buts, alright? I gotta open in the morning too, and I don't need you keeping me here all night."
    voice "game_flood/voice/C-102-22.ogg" #Waitress (Allison Seils)
    wai "'Sides, shouldn't you be back home with your folks?"
    
    show oph defensive
    
    voice "game_flood/voice/C-102-23.ogg" #Ophelia (Cospcaptor)
    oph "I'm almost 18, I can take care of myself..."
    voice "game_flood/voice/C-102-24.ogg" #Waitress (Allison Seils)
    wai "Coulda fooled me. You look like shit. Don't you get any real sleep?"
    voice "game_flood/voice/C-102-25.ogg" #Ophelia (Cospcaptor)
    oph "...What do you care about my damn sleep schedule."
    voice "game_flood/voice/C-102-26.ogg" #Waitress (Allison Seils)
    wai "Hey, keep it down!"
    voice "game_flood/voice/C-102-27.ogg" #Waitress (Allison Seils)
    wai "I'm just trying to look out for you, alright? Go home, get some shut-eye. Dumb kids like you stay up late all the time, and it's murder on your growing bodies."
    voice "game_flood/voice/C-102-28.ogg" #Ophelia (Cospcaptor)
    
    show oph irritated
    
    oph "Growing body- I {i}just said{/i} I'm 18."
    voice "game_flood/voice/C-102-29.ogg" #Waitress (Allison Seils)
    wai "So? Still growing."
    "She turned her back to me. I stuck out my tongue in turn, before burying my head in my hands."
    
    hide oph
    scene black with dissolve
    
    "She didn't get it. I could barely get any sort of sleep."
    "I tried, I really did. But every time I do, there's this horrible, nagging inkling in my head."
    #the flood cg sepia?
    "It's always there. The beating waves, the horrible, droning sound of dripping water."
    "The Flood's only gotten worse, and it's filling me with this horrible feeling of dread all my life."
    "Every night, the water rises a little bit higher, and every night I slip a little more into the deep end."
    "What's going to happen if the Flood consumed everything? Would I be okay?"
    
    scene flood diner with dissolve
    show oph scared
    
    voice "game_flood/voice/C-102-30.ogg" #Waitress (Allison Seils)
    wai "The weather's calling for rain overnight. You should go home, before it hits."
    
    show oph surprised
    
    "As she relays this to me, a sinking feeling hits my stomach. My eyes go blank with dread."
    "Oh God... it can't be an omen, can it...?"
    "I can't stay here. I can't go home. I need to think."
    "Hoisting myself from the bar, I give the waitress a slight nod."
    voice "game_flood/voice/C-102-31.ogg" #Ophelia (Cospcaptor)
    oph "...Thanks, I... good luck."
    "The waitress didn't regard me, still washing a small pile of accumulated dishes. I shamble out the front door."

    hide oph

    scene flood cafe outside with dissolve
    play ambience "game_flood/ambience/rain.ogg"

    show oph neutral

    "It's dark outside. It must've gotten really late."
    "I glance at my pocket watch real quick."
    "...It's midnight."
    "The night is young. How annoying."
    "I can't last like this, I need a game plan."
    "Seeking out a vending machine, I examine their selection."
    "Espresso shots, energy drinks, colas, some high-sugar fruit drinks."

    "Fiddling about with my wallet, I put enough loose change in to buy one of each."
    play sound "game_flood/sfx/vending.ogg"
    "And one by one, the machine dispenses each of them. Thankfully, my backpack has room to spare."
    "I don't want to go back to sleep. I can't. Because I can't shake the feeling that, if I do, something is going to go terribly wrong."
    "I look skywards, and see the hazy overcast of the clouds above. Mocking me with their presence." 
    "The backstreets of the city never looked particularly inviting to a girl like me, and the area's overall poorly lit."
    "Maybe I should head someplace else for the time being. If I get my legs working, I can get the caffeine circulating." 
    "Go for a run. Get the heart-rate going. It's gonna be a long night."
    
    show oph neutral 
    "Yeah, that's what I'll do. Maybe I can live this potentially last night in willful ignorance. I can pretend that the night's just like every other night, and that my dreams are meaningless."
    
    scene flood street with dissolve
    "Walking down the street, I can feel the cold front moving in. It's a nice feeling, refreshing despite the oppressive humidity that follows."

    "My footsteps make a light splashing sound, as the ground is still wet from the last rain we had. A nice reflection comes off of it, illuminating the world around me with the light from the nearby lamps."

    stop ambience
    play sound "game_flood/sfx/soda.ogg"
    "I pop open my first can, drinking the acidic contents, shaking myself awake. I haven't slept well in a while, and I know that I mustn't sleep now."

    "I finish my sip, looking at the outside of the can, for the lack of anything better to do."

    stop music fadeout 1.0
    show oph surprised
    voice "game_flood/voice/C-201-1.ogg" #Ophelia (Cospcaptor)
    oph "Ack!"

    "Involuntarily leaping back, I stare at the creature that's landed upon my hand. It's a moth, small and fluffy, looking like a mote of dim color in the lamp's light."

    show oph weirdedout
    voice "game_flood/voice/C-201-2.ogg" #Ophelia (Cospcaptor)
    oph "A… a moth?"

    play music "game_flood/music/moth.mp3" fadein 1.0
    
    "It didn't fly away with my sudden movement. Something must be wrong with it, right? In its eyes, I should be a predator."

    "A large, strange beast known to crush its fellow creatures."

    show oph neutral
    "But, alas, it's still here, on my hand."

    show oph smile
    "It turns to me, the antennae on it twitching slightly. The large, black eyes stare into mine, the cute little legs crawling back and forth upon my finger."

    voice "game_flood/voice/C-201-3.ogg" #Ophelia (Cospcaptor)
    oph "Hello, little guy. What're you looking for?"

    show oph neutral
    voice "game_flood/voice/C-201-4.ogg" #Ophelia (Cospcaptor)
    oph "Some food? I dunno if this energy drink would be that good for you."

    show oph tiredsmile
    voice "game_flood/voice/C-201-5.ogg" #Ophelia (Cospcaptor)
    oph "You don't seem very interested in it either."

    voice "game_flood/voice/C-201-6.ogg" #Ophelia (Cospcaptor)
    oph "Hmm."

    hide oph with dissolve
    "Maybe it sees the light bouncing off of my face? The warmth of my finger?"

    "It's a relatively big guy, too. It's nothing to me, but I'm sure it has some weight to it."

    "Walking over to a nearby light, I hold my hand up towards the bulbs."

    play ambience "game_flood/ambience/moth.ogg"
    "Launching, it hovers around the light, bouncing between the three orbs. It doesn't quite touch them, though, as I'd expect a normal moth to."

    "Eventually, it leaves this one, flying towards the next."
    
    show oph surprised
    voice "game_flood/voice/C-201-7.ogg" #Ophelia (Cospcaptor)
    oph "Hey, hang on!"
    
    hide oph with easeoutright
    "I rush after it, wiping my wet hair from my eyes. I trot to a stop next to the new light, staring at the moth again."

    scene flood alley with dissolve
    "It continues this same behavior, traveling from light to light, exploring it but never quite settling."

    "None of these lights are quite attractive enough to it. It doesn't seem to want to stay in one place for too long, having a bit of a wanderlust."

    "It's a wanderer."

    show oph tiredsmile with dissolve
    voice "game_flood/voice/C-201-8.ogg" #Ophelia (Cospcaptor)
    oph "You don't like to sit still for too long, do you…"

    "I keep following it, the activity helping to keep me awake. It's good exercise, as it's not exactly a slow little guy."

    show oph neutral close
    voice "game_flood/voice/C-201-9.ogg" #Ophelia (Cospcaptor)
    oph "Yeah, I feel ya. I'm never quite satisfied myself. No matter how beautiful these lights are, they just… they don't make me feel content."

    show oph defensive
    voice "game_flood/voice/C-201-10.ogg" #Ophelia (Cospcaptor)
    oph "I guess I'm not quite okay with just being content, anyways. Who wants to be {i}just okay{/i} with their position in life?"

    show oph defensive close
    voice "game_flood/voice/C-201-11.ogg" #Ophelia (Cospcaptor)
    oph "Nobody wants to settle. Right?"

    show oph irritated close
    voice "game_flood/voice/C-201-12.ogg" #Ophelia (Cospcaptor)
    oph "Or everyone does, and I'm the odd one out."

    show oph smile
    voice "game_flood/voice/C-201-13.ogg" #Ophelia (Cospcaptor)
    oph "I'm glad I'm not the only one, though. You're like me."

    show oph smile close
    voice "game_flood/voice/C-201-14.ogg" #Ophelia (Cospcaptor)
    oph "It's good having someone else with you."

    show oph scared close
    voice "game_flood/voice/C-201-15.ogg" #Ophelia (Cospcaptor)
    oph "Being alone… being alone is scary."

    "It's terrifying."

    show oph smile
    voice "game_flood/voice/C-201-16.ogg" #Ophelia (Cospcaptor)
    oph "Well, that's why we should stick together! Just you and me, okay? Just for tonight."

    show oph smile close
    voice "game_flood/voice/C-201-17.ogg" #Ophelia (Cospcaptor)
    oph "Then we can go our separate ways, bouncing from place to place, light to light as we always have."

    show oph smile
    voice "game_flood/voice/C-201-18.ogg" #Ophelia (Cospcaptor)
    oph "That's okay, right?"

    scene flood moth with dissolve

    "The moth stops at the end of the street, having no more lamps to fly to. It turns to me, standing on the lamp and looking me in the eye."

    "It dances from side to side, moving in fluid, yet jittery movements. It's smooth, yet fast at the same time."

    "I take its silence as a yes, and walk up to the lamp, leaning against it. Looking up at the thing, I smile, feeling oddly {i}okay{/i} right now."

    "I know it's crazy, but I feel a sort of kinship with him. Two beasts of the same kind."

    "Him, in his fluffy splendor, and me, in my…"

    "Well. I'm a hot mess. Err, a cold mess? The point is that I'm a mess, okay?"

    "He and I are going to figure this mess out, together. I just don't quite know how, yet. But we'll get there, right?"

    stop ambience 
    scene flood alley with dissolve
    stop music fadeout 1.0
    "It begins to jump up and down, getting restless again."
    
    play music "game_flood/music/city.mp3" fadein 1.0
    
    "That's my signal. I take a look at my map."
    jump map

screen flood_mapselect:
    tag flood_mapselect
    imagemap:
        ground "flood map normal"
        idle "flood mapmoth disabled"
        hover "flood mapmoth hover"

        hotspot (772, 0, 610, 426):
            action Jump("flood_mappark")
        hotspot (83, 269, 599, 558):
            action Jump("flood_mapdowntown")
        hotspot (725, 472, 652, 480):
            action Jump("flood_mapriverside")

label flood_mappark:
    if hope:
        "I've already been there. I should look somewhere else."
        jump map
    else:
        $ hope = True
        jump flood_201

label flood_mapdowntown:
    if daisy:
        "I've already been there. I should look somewhere else."
        jump map
    else:
        $ daisy = True
        jump flood_301

label flood_mapriverside:
    if oliver:
        "I've already been there. I should look somewhere else."
        jump map
    else:
        $ oliver = True
        jump flood_401

label map:
    play sound "game_flood/sfx/map.ogg"
    #Player gets the map

    show oph neutral with dissolve
    voice "game_flood/voice/C-201-19.ogg" #Ophelia (Cospcaptor)
    oph "Well, little one, where to next?"

    call screen flood_mapselect with dissolve

#     menu:
#         "Head to the park.":
#             if hope:
#                 "I've already been there. I should look somewhere else."
#                 jump map
#             else:
#                 $ hope = True
#                 jump flood_201
#         "Check out downtown.":
#             if daisy:
#                 "I've already been there. I should look somewhere else."
#                 jump map
#             else:
#                 $ daisy = True
#                 jump flood_301
#         "See the riverside.":
#             if oliver:
#                 "I've already been there. I should look somewhere else."
#                 jump map
#             else:
#                 $ oliver = True
#                 jump flood_401