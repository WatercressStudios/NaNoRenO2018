label postCreditsNarrative:
#     scene menu_fireplace
#     show book
# 
#     hide book with easeoutbottom

    scene fireplace with Dissolve(2.0)

    "So, that's all of them."

    "The three stories that have made a lasting impact on my life."

    "And here I am, reaping the fruits of my labor."

    "Here I am, at Avitus, a Creative Arts University in Switzerland."

    "It's a long way from Vancouver."

    "I'm a long way from home."

    "Were it not for Avitus, God knows where I'd be."

    "Avitus has shown me a kindness that I quite honestly do not deserve."

    "But second chances aren't about whether or not you deserve them."

    "It's about showing a kindness out of wish, not out of obligation."

    "I'll be sure to pass this kindness on."

    "Listen to others. Help others. Become a person worthy of this chance."

    stop ambience fadeout 3.0
    stop music fadeout 3.0
    scene black with Dissolve(3.0)
    $ renpy.movie_cutscene("videos/Final Credits.mp4")
    scene menu_fireplace with Dissolve(2.0)

