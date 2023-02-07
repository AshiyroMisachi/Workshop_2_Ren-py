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
    has_baton = False

label qte_setup(time_start, time_max, interval, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple
    $ cont = _return
    return

screen qte_simple:
    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_simple')])

    vbox:
        xalign x_align
        yalign y_align
        spacing 25

        button: 
            action Return(1)
            xalign 0.5
            xysize 100, 100
            background Animation ("#FFFFFF",0.1,"#FFDDDD",0.1,"#FFCCCC",0.1,"#FFBBBB",0.1,"#FFAAAA",0.1,"#FF9999",0.1,"#FF8888",0.1,"#FF7777",0.1,"#FF6666",0.1,"#FF5555",0.1,"#FF4444",0.1,"#FF3333",0.1,"#FF2222",0.1,"#FF1111",0.1,"#FF0000",0.1,"#CF0000") 

screen baton:
    modal False
    imagebutton:
        xpos 20 ypos 430
        idle "baton.png"
        hover "baton.png"
        action [SetVariable("has_baton", True), Hide("baton")]

screen inventory:
    modal False
    frame:
        xalign 0.0 yalign 0.0
        hbox:
            if has_baton:
                add "baton.png"


#Le jeu commence ici
label start:
    show screen inventory
    show screen baton
    e "Vous venez de créer un nouveau jeu Ren'Py."

    e "Après avoir ajouté une histoire, des images et de la musique, vous pourrez le présenter au monde entier !"

label room:
    hide screen baton

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
            call qte_setup(1.5, 1.5, 0.1, renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
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
        if has_baton:
            "OH NON TU M'A EU AVEC TON BATON"
        else:
            "PAM TU ES MORT"
    elif non: 
        "Tu veux quoi comme sirop pour ta crêpe ?"
    else: 
        "Enfaite tu m'ennui j'me tire"




