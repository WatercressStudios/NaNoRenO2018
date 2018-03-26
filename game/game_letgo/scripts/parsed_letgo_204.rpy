label letgo_204:
    scene letgo city nearby sunset with Dissolve(1.0)
    play music bgmloop2death_intro noloop fadeout 1.0
    queue music bgmloop2death_loop loop

    "We leave the old neighborhood behind and start climbing the big hill in town. It’s a bit more difficult than usual - probably because it’s darker than I’m used to."

    #fade in appropriate bg
    play sound "game_letgo/sfx/Snow Footsteps.ogg"
    play ambience "game_letgo/ambience/Outlook Night.ogg" fadeout 2.0 fadein 2.0
    scene letgo park hill night with dissolve

    "It’s a surprisingly nice night for a walk - and doubly nice to see Maya snuggling into her scarf. I’m not sure she realizes she’s doing it, but I’m not about to stop her."

    play sound "game_letgo/sfx/Wind Gust.ogg"

    "We’re still holding hands as we walk - though I have my left hand in her right, with our close arms around each other’s backs."
    "I can hear our feet crunching through the snow on the ground while a playful wind gathers and sends stray snowflakes around us."

    "If there’s glass out there, please don’t tap it because that would be annoying!"

    #may at left
    show may happy2:
        xanchor 0.5
        yalign 1.0
        xpos 0.65
    with dissolve

    voice "C-204-1.mp3" #Maya (shiena)
    may "This… I can get used to this."

    "No kidding."

    #eli at right
    show eli cool1 behind may:
        xanchor 0.5
        yalign 1.0
        xpos 0.8
    with dissolve

    #eli at right
    voice "C-204-2.mp3" #Elijah (Michael Potok)
    eli "Same, for sure. We’ll take our time to do this in every season."

    show may sadshout1 with dissolve
    pause 0.5
    show may normal1 close with dissolve

    "She gets this weird look, but then smiles brilliantly."

    voice "C-204-3.mp3" #Elijah (Michael Potok)
    eli "There you are."

    show eli:
        easein 0.7 xpos 0.69 ypos 1.07
    pause 0.5
    show eli:
        xpos 0.8 ypos 1.0
    with ease

    "I take a moment to kiss her forehead, which causes her to snort."

    show may adore1 with dissolve

    voice "C-204-4.mp3" #Maya (shiena)
    may "Wow, is it second grade?"

    voice "C-204-5.mp3" #Elijah (Michael Potok)
    eli "Pffft-- no, not at all! I’d already be at home doing chores if it was second grade."

    show may happy2 with dissolve

    voice "C-204-6.mp3" #Maya (shiena)
    may "Well, we should find a bench. I think there’s a place where we can see the whole city."

    "We walk a bit farther - though she breaks off and runs ahead of me."


    voice "C-204-7.mp3" #Maya (shiena)
    may "Bet you can’t catch me before the end of the block!"

    hide may cheeky2 with easeoutright

    voice "C-204-8.mp3" #Elijah (Michael Potok)
    eli "Bet you I can!"

    hide eli cool1 with easeoutright
    #both of them laughing

    scene black with dissolve

    play sound "game_letgo/sfx/May Eli Run.ogg"

    "The air is a bit more biting as I run for her."

    "Everything feels so slow, like the world is trying hard to give me one more minute - one more moment to see her happy face looking back as I press on."
    stop sound fadeout 5.0

    "This feels so familiar - but I catch up, pulling her off the ground and twirling her; she gives a small giggle."

    scene letgo city outlook night

    voice "C-204-9.mp3" #Maya (shiena)
    may "Okay, okay! You got me!"

    voice "C-204-10.mp3" #Elijah (Michael Potok)
    eli "Wow, I’m out of breath. Want to… ah. Get ourselves onto that bench?"

    voice "C-204-11.mp3" #Maya (shiena)
    may "Sure!"

    "We sit at last. Man, I can feel my sore legs now! My body’s {i}reeeaally{/i} not going to be happy with me in the morning."

    "I lean back, watching the point where the stars and city lights become one. Blowing snow glitters in the moonlight, creating a truly beautiful scene."

    "It’s been a long day - a great one. I don’t think I can ask for better."

    voice "C-204-12.mp3" #Elijah (Michael Potok)
    eli "Today was the best."

    voice "C-204-13.mp3" #Maya (shiena)
    may "It was totally fun; we have to do this again when there’re more lights set up."

    "Maybe not sightseeing exactly, but… I don’t think I’ll ever be able to see things the same."

    voice "C-204-14.mp3" #Elijah (Michael Potok)
    eli "Let’s just spend some time out here, together. That’s all I want right now."

    voice "C-204-15.mp3" #Maya (shiena)
    may "I can do that."

    "She sounds so happy and content - but there’s something more, even though I can’t imagine what it could be."

    "The white snow continues drifting beneath the inky blue-black night sky… The wind plays a song through the trees and houses - just for us."

    "It’s so… {i}warm.{/i}"

    #bg scene starts to unfocus or fade

    "It’s beautiful…"

    "{i}You’re{/i} beautiful…"

    voice "C-204-16.mp3" #Elijah (Michael Potok)
    eli "I want to see you with white hair someday. Smiling just like you are now."

    voice "C-204-17.mp3" #Maya (shiena)
    may "You will never know how much I want that for you, too."

    voice "C-204-18.mp3" #Elijah (Michael Potok)
    eli "Hey, would it be alright just to rest on your lap for a little?"

    voice "C-204-19.mp3" #Maya (shiena)
    may "Oh… wow, you want to take a nap~? That’s fine."

    "I’m weirdly tired. Maybe because we’ve done so much today?"

    "Well, at least it’ll be a happy ending."

    #scene to black

    "Will you be okay? Will you grow old? Will you be happy?"

    "That’s all I could ever want…"

    "..."

    voice "C-204-20.mp3" #Maya (shiena)
    may "Eli?"

    "..."

    stop music fadeout 10.0

    voice "C-204-21.mp3" #Maya (shiena)
    may "Come on, Eli. Let’s go."

    voice "C-204-22.mp3" #Maya (shiena)
    may "Elijah! Did you fall asleep? Please wake up… please?"

    voice "C-204-23.mp3" #Maya (shiena)
    may "Come on. It’s not funny anymore!"

    voice "C-204-24.mp3" #Maya (shiena)
    may "Oh no. No no no."

    voice "C-204-25.mp3" #Maya (shiena)
    may "{i}{b}Elijah!{/b}{/i}"

    voice "C-204-26.mp3" #Maya (shiena)
    may "Come on, come on! Don’t do this!"

    play music "game_letgo/sfx/Sirens.ogg" fadein 8.0
    #sirens that grow increasingly loud

    voice "C-204-27.mp3" #Maya (shiena)
    may "Why? Why like this?"

    voice "C-204-28.mp3" #Maya (shiena)
    may "...The fall. It was the fall! You {i}were{/i} hurt!"


    #maya crying

    voice "C-204-29.mp3" #Maya (shiena)
    may "Come {i}on{/i} Elijah! Why aren’t you breathing!?"

    voice "C-204-30.mp3" #Maya (shiena)
    may "Hey! Someone help us!"

    "..."

    stop music fadeout 1.0

    scene black
    with Dissolve(3.0)

    stop ambience fadeout 2.0
    play sound "game_letgo/sfx/Sirens.ogg"
    
    pause 2.0

    play ambience "game_letgo/ambience/Downtown Night.ogg" fadeout 2.0 fadein 2.0

    voice "C-204-31.mp3" #Maya (shiena)
    may "...We ended up at the hospital."

    voice "C-204-32.mp3" #Maya (shiena)
    may "Brain hemorrhage, they said. He didn’t feel anything when he went to sleep. There was nothing I could have done by that point."

    voice "C-204-33.mp3" #Maya (shiena)
    may "No, no, no! It can’t end like this!"

    voice "C-204-34.mp3" #Maya (shiena)
    may "You were just… we were just talking! No, you can’t die!"

    voice "C-204-35.mp3" #Maya (shiena)
    may "I can’t… I can’t accept this."

    voice "C-204-36.mp3" #Maya (shiena)
    may "I’m sorry, Elijah. I’m so sorry…"

    stop ambience fadeout 0.1
    #rewind
    play audio "game_letgo/sfx/Disturbing Bass.ogg"
    scene letgo rewind with Dissolve(9.5)

    jump letgo_301
