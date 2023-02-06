# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")

init python:
    oui = False
    non = False
    sanite = 80
    cont = 0
    qte_counter = 0

label qte_setup(time_start, time_max, interval, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple
    # can change to call screen qte_button to switch to button mode

    $ cont = _return
    # 1 if key was hit in time, 0 if key not
    return

#########################################
#FUNCTION
#########################################
'''
"Function"/pseudo-function
calls the qte screen
parameters are:
    - amount of time given
    - total amount of time (is usually the same as above)
    - timer decreasing interval
    - the x alignment of the bar/box
    - the y alignment of the bar/box
'''

############################################
#SSCREEN
############################################
screen qte_simple:
    #key input qte

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_simple')])
    # timer, using variables from label qte_setup
    # false is the condition if the timer runs out - and this will be reached if the user doesn't get hit the key on time

    vbox:
        xalign x_align
        yalign y_align
        spacing 25
        # vbox arrangement

        button: 
            action Return(1)
            xalign 0.5
            xysize 100, 100
            background "#fff"

        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"
                # this is the part that changes the colour to red if the time reaches less than 25%


#Le jeu commence ici
label start:

    e "Vous venez de créer un nouveau jeu Ren'Py."

    e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

label room:

    e "Aidhaugdayudauigda"

    e "fhezuczad"
    if sanite == 100:
        menu: 

            "Oui":
                jump choice_1
            
            "Non":
                jump choice_2

            ". . .":
                jump suite
    elif sanite == 80:
        menu:
            "Oui mais moins bien":
                jump choice_1
            
            "Non mais moins bien":
                jump choice_2

            ". . . mais moins bien":
                jump qte_test

label choice_1:
    $ oui = True
    "Tu as dit oui ? Tu va mourir"
    jump suite

label choice_2:
    $ non = True

    "Tu as dit non ? fait gaffe à ton cul"
    jump suite

label qte_test:
    "Le monstre apparait !{w=0.5}{nw}"
    while qte_counter != 5:
            call qte_setup(1.0, 1.0, 0.1, renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
            pause 0.5
            if cont == 1 and qte_counter < 4:
                $ qte_counter += 1
                extend " boum... boum..{w=0.5}{nw}"
            elif cont == 1:
                $ qte_counter += 1
                extend " boum... boum..{w=0.5}{nw}"
                "Le monste ne t'as pas vu ouf !"
            
    jump suite

label suite: 
    "Bon maintenant on va essayé de mangé des crêpes"
    if oui:
        "PAM TU ES MORT"
    elif non: 
        "Tu veux quoi comme sirop pour ta crêpe ?"
    else: 
        "Enfaite tu m'ennui j'me tire"

#label start:
#
#    $ cont = 0 #continue variable
#
#    # "Function Call" - see label qte_setup for detail on "function"
#    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomise the location
#
#    while cont != 10:
#        call qte_setup(1.0, 1.0, 0.1, renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
#        pause .5
#        # to repeat the qte events until it is missed
#
#    if cont == 10:
#        "{b}YOU WIN{b}"
#    else:
#        "{b}GAME OVER{/b}"
#
#    return



