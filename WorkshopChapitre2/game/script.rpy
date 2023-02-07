# Le jeu commence ici
label start:

label chapitre_2_0:
    "Départ"
    jump chapitre_2_1

label chapitre_2_1:
    "Desciption Hub"
    jump chapitre_2_2

label chapitre_2_2:
    "Zone"
    menu: 
        "Balcon":
            jump chapitre_2_3

        "Monter":
            jump chapitre_2_5

        "Descencre":
            jump chapitre_2_7
        
label chapitre_2_3:
    "Vous êtes au balcon"
    jump chapitre_2_2

label chapitre_2_4:
    "Vue 1"
    menu:
        "Hub":
            jump chapitre_2_2
        
        "Fen":
            jump chapitre_2_6

label chapitre_2_5:
    "Vous êtes monter"
    jump chapitre_2_4

label chapitre_2_6:
    "Salle Fen"
    jump chapitre_2_8

label chapitre_2_7:
    "Vous êtes descendu"
    jump chapitre_2_8

label chapitre_2_8:
    "Une grande salle"
    menu:
        "Porte/B":
            jump chapitre_2_9

        "Porte 2":
            jump chapitre_2_10

        "Porte 1":
            jump chapitre_2_11

label chapitre_2_9:
    "Vous avez pris la porte B"
    jump chapitre_2_8

label chapitre_2_10:
    "Vous avez pris la porte 2"
    menu:
        "Retournez en arrière":
            jump chapitre_2_8
        "Avancer vers le Monstre":
            jump chapitre_2_13

label chapitre_2_11:
    "Vous avez pris la porte 1"
    menu:
        "Retournez en arrière":
            jump chapitre_2_8
        "Avancer vers Avert":
            jump chapitre_2_12

label chapitre_2_12:
    "Avert"
    menu:
        "Retournez dans la grande Salle":
            jump chapitre_2_8
        
        "Pre-fin":
            jump chapitre_2_14

label chapitre_2_13:
    "Agrougrou le monstre"
    menu:
        "Pre-fin":
            jump chapitre_2_14

        "Revenir en arrière":
            jump chapitre_2_10

label chapitre_2_14:
        "Pre-fin LETS GOO"
        jump chapitre_2_fin

label chapitre_2_fin:
    "LE CHAPITRE EST FINI GGWP"