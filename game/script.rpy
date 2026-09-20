# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("???")
define mc = Character("You")

define fisherName = "???"
define fisher = Character(fisherName)


# define centred_left = Character(None,
#     #what_size=20, #Font size
#     what_xalign=0.1, #Centers text within the window
#     window_xalign=0, #Centers the window horizontally
#     window_yalign=0.5, #Centers the window vertically
#     what_text_align=0.5, #Centers text within the window, just in case
#     window_background=None,#Removes the window, so only the text shows
#     #what_outlines=[(3, "#000000", 2, 2), (3, "#282", 0, 0)],
#     #Gives an outline
#     #what_slow_cps=20 #Speed at which the text appears (slow)
#     )

# define centred_right = Character(None,
#     #what_size=20, #Font size
#     what_xalign=0.7, #Centers text within the window
#     window_xalign=0, #Centers the window horizontally
#     window_yalign=0.5, #Centers the window vertically
#     what_text_align=0.5, #Centers text within the window, just in case
#     window_background=None,#Removes the window, so only the text shows
#     #what_outlines=[(3, "#000000", 2, 2), (3, "#282", 0, 0)],
#     #Gives an outline
#     #what_slow_cps=20 #Speed at which the text appears (slow)
#     )


# The game starts here.

define right_centred_text = Character

init:
    # https://www.renpy.org/wiki/renpy/doc/tutorials/Adding_Graphics_to_Your_Story
    image black = "#000000"
    image bg portal = "/images/bg/9-19-vn-doodle.png"

    image bg portal1 = "/images/bg/9-19-vn-doodle-portal-1.png"
    image bg portal2 = "/images/bg/9-19-vn-doodle-portal-2.png"

# https://www.renpy.org/doc/html/transforms.html#atl
image portal_animated:
    "/images/bg/9-19-vn-doodle-portal-1.png"
    pause 1
    "/images/bg/9-19-vn-doodle-portal-2.png"
    pause 1
    repeat

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # Quick refs for coding for text colour and so on:
    # https://www.renpy.org/doc/html/text.html

    centered "... I think I might be the only person who was first told I was dead by a barista"

    centered "He didn't mean to, of course, {w=0.3}or I'm sure he'd've been more formal about it."
    extend "\n\nHe simply stared right through me, {w=0.3}with those dark brown eyes,{w=0.3} a disposable cup absently between his fingers as he turned to his colleague."

    centered "{color=#c0d8d6}\"Real slow morning today, hey?\"{/color}{space=550}"
    extend "\n{space=550}{color=#d8c0c2}\"Heh. Yeah. 's practically dead in here.\""
    extend """\n\n{color=#c0d8d6}\"Would you mind closing the door?{space=550}
    \nThere's a serious chill in here!\"{/color}{space=550}
    """
    extend "\n\n{color=#c0d8d6}\"... oh. It's already closed.\"{/color}{space=550}"
    extend "\n{space=550}{color=#d8c0c2}\"... creepy.\"{/color}"

    centered "'Rude', I thought, as I walked up to the counter."

    extend """\n\nI would've done so pointedly, if I had enough energy, but.\n
    {w=0.3}Well, {w=0.3}they {i}had{/i} been right about the morning.\n\n
    {w=0.3}But I was still feeling irked."""

    centered """
    Then the customer behind me walked right through me and ordered a latte.
    """
    extend """\n\nDon't get me wrong here, I'm not being figurative; {w=0.5}she phased right {i}through{/i} me. 
    \n\nLike a cold shower curtain brushing your leg during a lukewarm shower, the feeling stuck to me, even as I stumbled backwards. """
    extend """\n\nThey all turned and stared as I {i}thumped{/i} into the entryway door."""

    centered "{i}Embarrassed.{/i}\n\n{w=0.5}That's how I felt. \n\n{w=0.2}Dumb, right?"
    extend "\n\nAs they looked right through me,{w=0.2} past the fingers of rain running down the floor-length windows, {w=0.2}and out into the foggy morning beyond us."

    centered "I'm not sure if I still had a heart at that point, {w=0.2}but that didn't stop that feeling of it lodging in my throat as I stumbled out of the doorway."
    extend "\n\n{w=0.3}I still remember the cheery chime of the entryway door, {w=0.2}the way the rain pooled on the sidewalk, {w=0.2}the dozens of black-draped workers walking through me as I dumbly tried another cafe.\n\n{w=0.5} ...like maybe it'd go differently somehow."

    centered "Eventually, {w=0.2}I settled on a stool by the window.\n\nA customer glanced curiously over as I pulled it over to sit, {w=0.2}gaze skidding over and through me."

    fisher "... I apologise for taking so long."

    "The voice was warm, gentle; {w=0.3}almost like a hug if such a thing wouldn't have skidded right through me."

    fisher "You were terribly difficult to find, {w=0.1}you know. {w=0.3}\nNot many people manage to get all the way to a {i}cafe{/i} after something like this."

    "There was a smile in the voice now, {w=0.2}but I didn't bother looking over."
    "After being ignored by more than a dozen people, {w=0.2}there was no reason to believe they could see me, {w=0.2}let alone talk to me."

    # test - this is how you can change the character's name when you get to know them.
    # $ fisher = Character("Fisher")

    fisher "... After dying."

    mc "...!"

    "That made me look over. \n{w=0.3}They'd said it softly, {w=0.3}like crushing someone slowly would hurt any less."

    fisher "... ha! \n{w=0.1}You must have desperately wanted a coffee. \n\n{w=0.2}Would you like me to fetch you something, {w=0.1}before we depart?"

    mc "What?"

    "My mind tumbled over the words uselessly, like they were meaningless syllables rather than something that held any sort of meaning."

    fisher "... I understand. It is overwhelming, is it not?"

    "There was another pause, and again, I could feel that smile. \n\nIt was placating."
    "As I wrestled with my thoughts, they reached out a shadowy hand to rest on my shoulder, in a gentle pat."

    menu: 
        "It made me feel..."

        "angry":
            "grumpy dialogue >:c"
        "reassured":
            "... Reassured. At least, {i}some{/i} things didn't phase right through me."

    mc "... You can really see me?"

    "My voice sounded hoarse and faint, even to me."
    "Like an idiot, I held up three fingers, {w=0.2}like this stranger was trying to cheat me somehow."

    "I hadn't been expecting them to laugh. It sounded like wind-chimes, stirred gently by the wind."

    "... it stained their next words, making them slip through the air lightly."

    fisher "You're holding up three fingers, {w=0.2}and a very impressive front indeed."

    "Their words carried themselves on another laugh."
    "Not a mean one, though it still jabbed keenly at how I was currently feeling."
    "The stranger seemed to sense this as they leaned forward and pressed their next words softly into the space between us."
    
    fisher "I mean to say, you must be exhausted. \n{w=0.2}You are no longer meant for this place. Please."

    "With a sweeping motion, they stood, and gestured towards the door of the cafe's supply cupboard."
    
    mc "(Why are they gesturing to it like I'm supposed to be impressed...?)"

    fisher "I will be right after you."

    "I couldn't imagine how brooms and extra supplies of sugar and coffee would assist me.\nPerhaps they were mad."
    "... perhaps {i}I{/i} was mad."
    "Mad, or desperate. Because I numbly stood up at their tone anyway."
    "What else could I do?"
    #"Still, they must've been right about me being exhausted, {w=0.1}because I numbly stood up at their tone."
    "Pins and needles ran down my legs. \nHow long had I been sitting for?"

    # walking sound effect would be cool here

    "The four steps to the supply cabinet felt long, {w=0.1}my sneakers squeaking against the plastic tiling of the floor."
    

    menu:
        "My head was filled with so many questions, I could barely pick out a single one..."

        "Who are you?":
            mc "Who are you?"
            "The question slipped out of me as I opened the cupboard door."
            # show bg portal with dissolve
            show portal_animated with dissolve
            "Beyond it, space yawned in all of its infinite majesty."
            "Pillowing plumes of purple, blue and endless darkness winked at me, as if amused by my insignificance."

            "It was so overwhelming, that I had already forgotten what it was that I had asked. \nThe hand on my shoulder made me start."

            fisher "... A friend. I am here to help you."

            "I believed them. \n{w=0.3}That alone should've given me pause..."

            "The room spun as I felt myself get pulled forwards."
            "My damp sneakers gave little to no purchase, squeaking on the cheap, plastic floor, and I felt myself falling..." with vpunch
            # hide bg portal with dissolve
            hide portal_animated with dissolve
            show black

            "... into that infinite, dizzying void of space."

            "end for now <3"



    # show bg portal with dissolve

    # fisher "This is a test."

    # e "I AM SOME TEXT HELLO HELLO c:"

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

# to jump to a label you go
# jump label_name
# c:
# so just leaving these here for future reference
# here's the docs for this: https://www.renpy.org/doc/html/menus.html
label grumpy_dialogue:

label met_fisher: