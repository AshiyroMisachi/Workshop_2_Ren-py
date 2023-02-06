# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#c8ffc8")

init python:
    oui = False
    non = False
    sanite = 80


# Le jeu commence ici
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
                jump suite

label choice_1:
    $ oui = True
    "Tu as dit oui ? Tu va mourir"
    jump suite

label choice_2:
    $ non = True

    "Tu as dit non ? fait gaffe à ton cul"
    jump suite

label suite: 
    "Bon maintenant on va essayé de mangé des crêpes"
    if oui:
        "PAM TU ES MORT"
    elif non: 
        "Tu veux quoi comme sirop pour ta crêpe ?"
    else: 
        "Enfaite tu m'ennui j'me tire"