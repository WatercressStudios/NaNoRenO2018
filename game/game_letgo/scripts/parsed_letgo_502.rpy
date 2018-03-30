label letgo_502:
    $ letgo_badending = True

    voice "C-502-1.mp3" #Maya (shiena)
    may "...No."

    voice "C-502-2.mp3" #Maya (shiena)
    may "I can’t accept this; there has to be a way."

    "Maya…"
    show may frustrated3 cry with dissolve
    voice "C-502-3.mp3" #Maya (shiena)
    may "Again."
    show may frustrated4 cry with dissolve
    voice "C-502-4.mp3" #Maya (shiena)
    may "There has to be something I overlooked."
    show may angry4 cry with dissolve
    voice "C-502-5.mp3" #Maya (shiena)
    may "I’ll rip everything to shreds!"
    show may sad4 cry with dissolve
    voice "C-502-6.mp3" #Maya (shiena)
    may "No… no. I-- You wouldn’t want that and you wouldn’t like it."

    voice "C-502-7.mp3" #Maya (shiena)
    may "Will you still die if I stay here? If I hide long enough, will you be here in the morning?"
    show may sad3 cry with dissolve
    voice "C-502-8.mp3" #Maya (shiena)
    may "I don’t believe it… I don’t believe that you can’t survive today…"
    show eli worried2 with dissolve
    "Maya…"
    show may angry4 cry with dissolve
    voice "C-502-9.mp3" #Maya (shiena)
    may "No, we just got some time together! Why can’t it last!? Why can’t we get through this? Why can’t I get you to believe me?"
    show may angry3 cry with dissolve
    voice "C-502-10.mp3" #Maya (shiena)
    may "{b}{i}How many times does it take!?{/i}{/b}"
    show eli sad1 with dissolve
    "Maya...."
    show may frustrated3 cry with dissolve
    voice "C-502-11.mp3" #Maya (shiena)
    may "A thousand times - I can go that many and more."

    voice "C-502-12.mp3" #Maya (shiena)
    may "How many wishes will it take?"

    voice "C-502-13.mp3" #Maya (shiena)
    may "I refuse to give up on you!"
    show may tired3 cry with dissolve
    voice "C-502-14.mp3" #Maya (shiena)
    may "I refuse to give up on {i}us...{/i}"
    "Maya…"
    show may frustrated3 cry with dissolve
    voice "C-502-15.mp3" #Maya (shiena)
    may "I can’t do this anymore. I can’t!"

    voice "C-502-16.mp3" #Maya (shiena)
    may "I’m… I’m not ready to end this yet, but I can’t go on…"
    show may sad4 cry with dissolve
    voice "C-502-17.mp3" #Maya (shiena)
    may "I’ve tried so hard."

    voice "C-502-18.mp3" #Maya (shiena)
    may "You understand, right?"

    voice "C-502-19.mp3" #Maya (shiena)
    may "No. That’s right."
    show may forcedsmile4 cry with dissolve
    voice "C-502-20.mp3" #Maya (shiena)
    may "I’ll come back someday. I have to give this my best shot."

    stop music fadeout 10.0
    scene black with Dissolve(3.0)

    voice "C-502-21.mp3" #Maya (shiena)
    may "I’ve been through everything - but maybe I’ve forgotten something after all."

    voice "C-502-22.mp3" #Maya (shiena)
    may "I’ll save all the time I can to try and get you to the other side of today."

    voice "C-502-23.mp3" #Maya (shiena)
    may "It can’t be certain. It’s not hopeless yet…"

    voice "C-502-24.mp3" #Maya (shiena)
    may "It’s not. It’s not!"
    voice "C-502-25.mp3" #Maya (shiena)
    may "It’s… not hopeless…"
    #Credits

    stop music fadeout 0.2
    pause 0.2

    $ renpy.movie_cutscene("videos/Let Go Credits.mp4")
    
    jump letgo_601
