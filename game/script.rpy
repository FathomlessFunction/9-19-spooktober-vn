# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("???")

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

    # test - this is how you can change the character's name when you get to know them.
    # $ fisher = Character("Fisher")

    fisher "This is a test."

    e "I AM SOME TEXT HELLO HELLO c:"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
