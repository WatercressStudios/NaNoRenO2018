label spirits_a1s4:
    "I head back to my room and quickly pull on my pajamas - anything to keep my mind off of things."

    "Unfortunately, though, the guilt only intensifies. I shouldn’t have lied to them - but it’s not like I can tell anyone the truth, either."

    #scene alex’s bedroom

    #show alex worried/sad/scared

    "I’ve got school tomorrow; I should just… sleep. I have enough on my mind without worrying about things like this."

    "It’s probably nothing. Maybe they won’t bother me... "

    "You know how to deal with this, Alex! Just {i}relax…{/i}"

    #stop music fadeout 2.0

    #hide alex 

    "I unstrap my prosthetic arm and slide it off, settle down into my newly-made bed, and close my eyes."

    "It shouldn’t take {i}too{/i} long to go to sleep, right?"

    #scene alex’s bedroom v3 

    "It’s when I’ve woken up that I realized I actually managed to."

    "Something’s wrong, though. I was dreaming about… my… kindergarten teacher? She was holding my hand, and we were going to the--"

    "No, that’s wrong." 

    "She’s-- {i}Someone’s{/i} still holding it."

    "And it’s the hand that isn’t there anymore."

    "…" 

    #play music genevieve’s theme

    #show alex pjs upset

    "No! No, no, {i}no!{/i} Not here, please…"

    "Please. I don’t want this!"

    "I just want a new start; I want to go to school - to be {i}normal!{/i}"

    "Why does this have to happen to me, of all people?"

    "The hand holding mine begins to tug. The sensation is uncomfortable - almost painful - but certainly isn’t the worst I’ve experienced."

    "What do I do? Try to ignore it and go to sleep? It’s-- God, is it really three in the morning? I have class tomorrow!" 

    "Wait a second…"

    "What happened to the room?"

    "All my stuff… it’s everywhere. I have to clean this up, don’t I?"

    "Ugh, I’ll do it in the morning. I’m not giving whoever - {i}what{/i}ever - did this the satisfaction."

    "You can deal with this, Alex. You’ve been doing it for years, after all."

    "I lie back down and close my eyes. If I can ignore it, it’ll just go away…"

    "But as soon as I decide to do so, the tugging intensifies. I can feel the other hand squeezing mine - fingers digging into my skin, scratching at flesh that isn’t there."

    "It isn’t there. It isn’t real… It’s not there."

    "{i}It’s not there.{/i}"

    "God, it hurts!" 

    voice "C-5-1.mp3" #Genevieve (Lasli Tran)
    gen "Please." 

    "{b}{i}It’s not there!{/i}{/b} No one is there!"

    "I don’t want to talk to it. Talking to {i}them{/i} never leads to anything good!"

    voice "C-5-2.mp3" #Genevieve (Lasli Tran)
    gen "I know you can hear me." 

    voice "C-5-3.mp3" #Genevieve (Lasli Tran)
    gen "You’re the only one who can." 

    voice "C-5-4.mp3" #Genevieve (Lasli Tran)
    gen "Aren’t you curious?" 

    "God, it isn’t going to go away, is it?" 

    "Knowing more about it could be useful - and engaging with it might prevent future pain."

    "I guess my hands-- {i}hand{/i} is tied."

    "Ugh, why can’t I live somewhere without spirits?" 

    #show alex pjs upset snarky/tense

    voice "C-5-5.mp3" #Alex (Bonnie Mitchel)
    alx "Fine. You win… But can you let go?" 

    "The pressure stops, but this spirit… ghost… whatever it is, is still holding on."

    "They take my hand - the one they can feel, touch, and hurt - and use it to control me."

    "I try to ignore them."

    "I can run, or fight, or plead… but it’s no use."

    "It’s {i}never{/i} any use."

    #show alex pjs neutral

    $ questionCounter = 0 

    $ correctQuestions = 0

    $ questionFlags = set()
    
    jump questionMenu

label questionMenu:
    
    menu:
        
        "What questions do I even ask it?" 

        "How did you die?" if 'howded' not in questionFlags:
            $ questionCounter += 1
            $ questionFlags.add('howded')
            jump SpiritsHowded

        "What is your name?" if 'urname' not in questionFlags:
            $ correctQuestions += 1
            $ questionCounter += 1
            $ questionFlags.add('urname')
            jump SpiritsUrname

        "Why don’t you just cross over?" if 'gtfo' not in questionFlags:
            $ questionCounter += 1
            $ questionFlags.add('gtfo')
            jump SpiritsGTFO

        "How can I help you?" if 'wutup' not in questionFlags:
            $ correctQuestions += 1
            $ questionCounter += 1
            $ questionFlags.add('wutup')
            jump SpiritsWutUp

        "Are you alone?" if 'onlyu' not in questionFlags:
            $ questionCounter += 1
            $ questionFlags.add('onlyu')
            jump SpiritsOnlyU

label SpiritsHowded:

    voice "C-5-6.mp3" #Alex (Bonnie Mitchel)
    alx "How did you die?" 

    #play sound gen scream 

    #show alex pjs scared

    "Immediately, the hand holding mine claws at my nonexistent flesh again. A high pitch scream resounds throughout the room - shattering me to the core."

    "For a moment, I’m glad I’m the only one who can hear her - but then that realization dawns on me again; I shiver at the thought."

    "I guess she doesn’t like that? I suppose it {i}is{/i} pretty rude of me."

    #show alex pjs neutral

    if questionCounter < 2:
        jump questionMenu
        
    jump NoMoreQuestions
    
label SpiritsUrname:

    voice "C-5-7.mp3" #Alex (Bonnie Mitchel)
    alx "What is your name?" 

    voice "C-5-8.mp3" #Genevieve (Lasli Tran)
    gen "Genevieve. Genevieve {i}Bourlon{/i}."

    "She spits the surname at me - but the hold on my hand softens like some sick sort of reward."

    "I guess I should be grateful."

    if questionCounter < 2:
        jump questionMenu
        
    jump NoMoreQuestions
    
label SpiritsGTFO:

    voice "C-5-9.mp3" #Alex (Bonnie Mitchel)
    alx "Why don’t you just cross over?" 

    "The spirits who come to me are stuck on Earth, held back by their lingering attachments to this material world."

    "I’ve never understood why they don’t take the Buddhist route and let go."

    #play sound gen scream

    #show alex pjs scared

    "Immediately, the hand holding mine begins tugging again and her scream rips through the air. I guess letting go of old grudges isn’t so simple."

    "No wonder I have nightmares and PTSD. Why do I alone bear this curse?"

    #show alex pjs neutral

    if questionCounter < 2:
        jump questionMenu

    jump NoMoreQuestions
    
label SpiritsWutUp:

    voice "C-5-10.mp3" #Alex (Bonnie Mitchel)
    alx "How can I help you?" 

    voice "C-5-11.mp3" #Genevieve (Lasli Tran)
    gen "Do what I ask." 

    "What does that mean? I’m trying, but I don’t know what she wants." 

    voice "C-5-12.mp3" #Genevieve (Lasli Tran)
    gen "We don’t have much time." 

    if questionCounter < 2:
        jump questionMenu

    jump NoMoreQuestions

label SpiritsOnlyU:

    voice "C-5-13.mp3" #Alex (Bonnie Mitchel)
    alx "Are you alone in this house?"

    "Her hand suddenly clutches my own with an anxious, aggravated pressure - but just as I’m about to yelp in pain, her grip completely slackens."

    "Maybe she’s had a sudden change of heart?"

    voice "C-5-14.mp3" #Genevieve (Lasli Tran)
    gen "...No." 

    voice "C-5-15.mp3" #Genevieve (Lasli Tran)
    gen "But you’re here to help {i}me{/i}."

    voice "C-5-16.mp3" #Genevieve (Lasli Tran)
    gen "That’s all."

    "What’s that supposed to mean?"

    if questionCounter < 2:
        jump questionMenu

    jump NoMoreQuestions

label NoMoreQuestions:
    if correctQuestions == 2:
        $ firstTrueEndFlag = True
    else:
        $ firstTrueEndFlag = False

    voice "C-5-17.mp3" #Genevieve (Lasli Tran)
    gen "I was killed, here, in my room."

    "Someone was murdered in the dormitory? This is supposed to be a {i}school{/i}, isn’t it?"

    voice "C-5-18.mp3" #Genevieve (Lasli Tran)
    gen "I need you to help me get justice." 

    voice "C-5-19.mp3" #Genevieve (Lasli Tran)
    gen "Please." 

    "What do I say? I’ve learned that helping them never leads to anything good - but not helping usually leads to something worse."

    "Do I take the slow poison, or the quick one?"

    "Suddenly, a deep cold washes over me. Terror surges in my chest - but in an instant, the spirit’s presence is gone."

    #show alex pjs confused

    "As she leaves, so does the strange sensation." 

    "I can’t say I’m ungrateful, but it’s strange… Where did she go, and what was that all about?"

    "If I do what she says, maybe she’ll leave me alone. It’s just a shame she talks in riddles."

    "Ugh, it’s too late for this."

    "I can figure things out in the morning. Right now, I need to sleep." 

    "If I can."

    #scene black
    
    jump spirits_a1s5