init python:
    sanite = 0
    item_photo = True
    p_chapitre_4_1_7 = False
    p_chapitre_4_3_0 = False

# Le jeu commence ici
label start:

label chapitre_4_0:
    $ sanite = 40

    "Début"
    if sanite <50:
        jump chapitre_4_2_0
    else:
        jump chapitre_4_1_0

label chapitre_4_1_0:
    "Balade"
    jump chapitre_4_1_1

label chapitre_4_1_1:
    "Rencontre"
    menu:
        "Nuit":
            jump chapitre_4_1_2
        
        "Vêtements":
            jump chapitre_4_1_3

        "Seul":
            jump chapitre_4_1_4

label chapitre_4_1_2:
    "Nuit"
    jump chapitre_4_1_5

label chapitre_4_1_3:
    "Vêtements"
    jump chapitre_4_1_6

label chapitre_4_1_4:
    "Seul"
    jump chapitre_4_1_6

label chapitre_4_1_5:
    "Discussion +"
    jump chapitre_4_1_7

label chapitre_4_1_6:
    "Discussion"
    jump chapitre_4_3_0

label chapitre_4_1_7:
    $ p_chapitre_4_1_7 = True

    "Coin"
    if item_photo:
        menu:
            "Utilisez la photo ?":
                jump chapitre_4_item

            "Continuez d'avancé":
                jump chapitre_4_1_8
    else:
        jump chapitre_4_1_8

label chapitre_4_1_8:
    "Encouragement"
    jump chapitre_4_3_2

label chapitre_4_2_0:
    "P/Vien"
    jump chapitre_4_2_1

label chapitre_4_2_1:
    "Discussion-"
    menu:
        "Non":
            jump chapitre_4_2_2

        "Ca va":
            jump chapitre_4_2_3

        "Oui oui":
            jump chapitre_4_2_4

label chapitre_4_2_2:
    "Non"
    jump chapitre_4_2_5

label chapitre_4_2_3:
    "Ca va"
    jump chapitre_4_2_6

label chapitre_4_2_4:
    "Oui oui"
    jump chapitre_4_2_7

label chapitre_4_2_5:
    "Questions"
    jump chapitre_4_3_0

label chapitre_4_2_6:
    "MMH ?"
    jump chapitre_4_3_0

label chapitre_4_2_7:
    "Mon Oeil"
    jump chapitre_4_2_8

label chapitre_4_2_8:
    "Discours"
    jump chapitre_4_2_9

label chapitre_4_2_9:
    "Avertissement"
    jump chapitre_4_3_1

label chapitre_4_3_0:
    $ p_chapitre_4_3_0 = True

    "Vien"
    if item_photo:
        menu:
            "Utilisez la photo ?":
                jump chapitre_4_item

            "Continuez d'avancé":
                jump chapitre_4_3_2
    else:
        jump chapitre_4_3_1

label chapitre_4_3_1:
    "Avert + Encouragement"
    jump chapitre_4_3_2

label chapitre_4_3_2:
    "Fin"

    return

label chapitre_4_item:
    $ item_photo = False

    "VOUS UTILISEZ LA PHOTO POUR OUVRIR UN PASSAGE DIMENSIONEL"
    if p_chapitre_4_1_7:
        jump chapitre_4_1_8
    if p_chapitre_4_3_0:
        jump chapitre_4_3_1


