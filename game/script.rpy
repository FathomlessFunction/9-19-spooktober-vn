# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("???")

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

    e "I AM SOME TEXT HELLO HELLO c:"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
