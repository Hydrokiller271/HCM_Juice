# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image langbac = "langbac.png"
image HCM = "hochiminh_hello.png"
image nharong = "ben_nha_rong.png"
define h = Character("Hồ Chí Minh")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/USSR_fl.mp3"
    scene nharong

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show HCM at left

    # These display lines of dialogue.

    h "Xin chào các cháu"

    h "Làm một số câu hỏi nhé?"
    stop music
    # This ends the game.

    return
