define dav = Character ("david (vous)", color = "#ffffff",what_size=30,what_color="#ffffff",window_background="#c5c5c55e")
define dav_pense = Character ("david (vous)", color = "#aaaaaa",what_size=30,what_color="#aaaaaa",window_background="#c5c5c55e")
define n = Character ("narateur", color = "#ffffff00",what_size=30,what_color="#dadde4be",window_background="#0000005e")

define X = Character ("Monsieur X")

init python:
    sanite = 0
    item_photo = True
    p_chapitre_4_1_7 = False
    p_chapitre_4_3_0 = False

# Le jeu commence ici
label start:

label chapitre_4_0:
    $ sanite = 60

    if sanite < 50:
        n "Vous émergez peu à peu de votre torpeur"
        n "Vous avez l’esprit encore chamboulé"
        n "Qu’est-ce qui est réel, qu’est-ce qui ne l’est pas"
        n "Tout vient se heurter dans votre tête"
        jump chapitre_4_2_0
    else:
        n "Vous marchez en vous assurant que ce qu’il y avait derrière vous a bien disparu"
        n "Vous soupirez de soulagement tandis que quel que soit la créature qui vous poursuivait n’était désormais plus qu’un écho lointain"
        n "Vous regardez aux alentours pour voir un environnement familier"
        jump chapitre_4_1_0

label chapitre_4_1_0:
    n "Seriez vous de retour chez vous ?"
    n "Vous voguez à travers la ville."
    n "La nuit tombée, les lumières éclairent votre chemin tel un guide."
    n "Après quelques minutes de marche, vous vous trouvez devant une porte."
    n "Un scepticisme vous prend, après tout ce que vous avez endurer dans les pièces d’avant c’était trop beau"
    n "Sans doute avez vous juste manquez l’ennemi de cette salle, l’heure est aux réjouissances"
    n "Vous ouvrez la porte"
    dav "..."
    dav "C’est le même lieu qu’au début"
    dav "Est-ce une hallucination,une mauvaise blague,un défi ?"
    n "Ces pensées affluent telle une cascade."
    n "Vous refaites le chemin,tel que vous l’avez fait précédemment."
    n "Après quelque temps vous vous retrouvez devant une porte."
    n "En l’ouvrant vous retrouver le même lieu que le début."
    dav "Impossible"
    dav "Mais est-ce vraiment impossible ?"
    n "Vous répétez ce processus plusieurs fois."
    n "En vain."
    n "Quelles sont les limites du possible dans ce lieu"
    dav "Des animaux qui parlent, des entités surnaturelles, des cauchemars vivants."
    n "Une légère tape sur l’épaule vous fait sursauter."
    n "Vous vous retournez pour faire face à une personne."
    X "Salutations"
    n "Vous faites un pas en arrière."
    dav "..."
    X "Qui es-tu ?"
    n "Vous hésitez avant de parler et ravalez votre salive"
    dav "David"
    X "David…"
    X "Tu veux sortir d’ici ?"
    n "Vous hocher la tête"
    X "Suis-moi alors"
    n "Vous suivez l’individu"
    n "Après quelques temps il s’arrête sur un banc"
    X "Assieds-toi donc."
    n "Vous vous exécutez"
    X "Dis moi, qu’est ce qui amène des gens tel que toi, dans un endroit comme celui-ci ?"
    X "Je ne sais pas"
    n "La personne vous regarde d’un air inquisiteur"
    dav "Quoi ?"
    X "Non, Rien"
    n "Silence..."
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
    $ sanite += 10

    n "Vous parlez de la nuit avec [X]"
    n "[X] lève la tête"
    X "..."
    X "Ah oui"
    X "Il n’y a que ça ici, avec le temps on s’y fait"
    X "J’attend impatiemment l’instant où le jour reviendra"
    X "..."
    X "Mais…"
    X "Je commence à douter qu’il arrive un jour."
    n "Vous regardez X qui observe le ciel d’un air mélancolique"
    X "A une époque j'étais fasciné par les étoiles, l’univers, les galaxies"
    X "A force de les côtoyées quotidiennement ce sont devenues des confidentes"
    X "Elles ne me posent pas de questions incessantes, pas de remarques qui blessent, seulement une écoute attentive"
    X "..."
    X "J’imagine que toi aussi tu es une oreille attentive"

    jump chapitre_4_1_5

label chapitre_4_1_3:
    n "Vous demandez à [X] pourquoi ce choix de vêtements"
    n "[X] vous regarde d'un air jugeur"
    n "La conversation tourne vite à l’impasse"
    X "C’est silencieux généralement ici"
    X "Je ne me rappelle pas la dernière fois où il y avait du bruit dans le coin"
    X "Je ne me rappelle même pas depuis quand je suis la"
    n "[X] laisse un soupir"
    X "Mieux vaut ne pas prendre racine ici"

    jump chapitre_4_1_6

label chapitre_4_1_4:
    n "Vous demandez à X pourquoi il est seul"
    n "[X] vous observe, son regard ne vous fixe pas, comme si il était dans la lune"
    X "Je ne me suis jamais poser la question"
    X "C’est devenu si habituel que cela ne m’a jamais effleuré l’esprit"
    X "Je suppose qu’avec le temps on s’habitue à tout"
    X "Mais depuis que tu es là ça à changer"
    X "Je sais que cela ne fait pas si longtemps que tu es arrivé"
    X "Et bien que tu compte repartir aussi vite, avoir de la compagnie, aussi peu de temps cela change beaucoup de chose"
    n "Vous regardez [X], vous ne savez pas où vous mettre"
    X "Pardon, tu dois être mal à l’aise."
    X "Hâtons le pas, si tu le veux bien"

    jump chapitre_4_1_6

label chapitre_4_1_5:
    "Discussion +"
    jump chapitre_4_1_7

label chapitre_4_1_6:
    "Discussion"
    jump chapitre_4_3_0

label chapitre_4_1_7:
    "Coin"

    if item_photo:
        menu:
            "Donnez la photo":
                jump chapitre_4_item

            "Continuez d'avancé":
                jump chapitre_4_1_8
    else:
        jump chapitre_4_1_8

label chapitre_4_1_8:
    X "Bon, eh bien voilà, c’est la sortie"
    n "Devant vous il y a une fenêtre"
    X "Oui ça paraît bizarre mais c’est bien la sortie de ce lieu"
    n "Vous êtes septiques"
    dav "Pourquoi tu ne sors pas, toi ?"
    X "J’ai appris à accepter cet endroit"
    X "Mais ne t’inquiète pas pour moi"
    X "Focalise toi sur ton périple, tu es le protagoniste de ton histoire ne l’oublie pas"
    dav "Mais, et toi ?"
    n "[X] marque une longue pause"
    n "Il vous regarde en souriant"
    X "Tu sais"
    X "Je suis doué pour donner des conseils, mais pas pour les suivres"
    X "En tout cas j'espère que tu trouveras le réconfort que tu cherches."
    X "Et n’oublie jamais,tu es le maître de ton destin, continue vers l’avant."
    X "Quelque soit les obstacles sur ton chemin,continue d'avancer."
    X "Cours vers ton destin, et si tu ne peux pas courir marche."
    X "Si tu ne peut pas marcher rampe, mais continue toujours vers ce destin qui est tien"
    X "Car n’oublie jamais que personne ne le fera pour toi"
    n "[X] se tourne et continue de marcher"
    n "Le silence de la nuit résonne à nouveau"
    n "Vous passez par la fenêtre"
    jump chapitre_4_3_2

label chapitre_4_2_0:
    n "Vous entendez des bruits de pas qui se rapprochent"
    n "Ils se rapprochent"
    n "Encore plus près"
    n "Ils sont juste ici…"
    n "Les bruits s'arrêtent"
    X "Ça va ?"
    n "Vous ouvrez les yeux pour voir un homme se pencher sur vous"
    jump chapitre_4_2_1

label chapitre_4_2_1:
    X "Allô ?"
    X "Tu m’as pas l’air bien en point."
    X "J’ai besoin d’une réponse est-ce que ça va ?"
    menu:
        "Non":
            jump chapitre_4_2_2

        "Ça va":
            jump chapitre_4_2_3

        "Oui oui":
            jump chapitre_4_2_4

label chapitre_4_2_2:
    dav "Non"
    X "Ah"
    X "Eh bien commençons par t'enlever le sol, c’est un bon début je pense."
    "L’homme vous aide à vous relever."
    jump chapitre_4_3_0

label chapitre_4_2_3:
    "Ca va"
    jump chapitre_4_3_0

label chapitre_4_2_4:
    "Oui oui"
    jump chapitre_4_2_8

label chapitre_4_2_8:
    "Discours"
    jump chapitre_4_2_9

label chapitre_4_2_9:
    X "Bon, eh bien voilà, c’est la sortie"
    n "Devant vous il y a une fenêtre"
    X "Oui ça paraît bizarre mais c’est bien la sortie de ce lieu"
    n "Vous êtes septique"
    dav "Pourquoi tu ne sors pas, toi ?"
    X "J’ai appris à accepter cet endroit"
    X "Mais ne t’inquiète pas pour moi"
    X "Focalise toi sur ton périple, tu es le protagoniste de ton histoire ne l’oublie pas"
    dav "Mais, et toi ?"
    n "[X] marque une longue pause"
    X "Depuis que tu es arrivé cet endroit, à un air malsain."
    X "J’ai un mauvais pressentiment concernant les choses qui pourraient t’arriver par-delà cette fenêtre"
    X "Quoi-qu’il advienne sache que quelque part, quelqu’un s’impatiente de ton retour"
    X "Ne les fait pas attendre"

    jump chapitre_4_3_1

label chapitre_4_3_0:
    X "T’es tu déjà demandé le but de la vie ?"
    X "Nous avons beau exister, le temps est inexorable et finit toujours par nous rattraper."
    X "Et pour remédier à cela, en tant qu’humains nous avons créé ces buts, ces désirs, ces espérances."
    X "Cette course à vouloir obtenir les objets de ses désirs, quand on l’achève, qu’est-ce qu’il nous reste ?"
    X "Je me pose la question parfois"
    X "..."
    X "Désolé, vu que je n’ai que du temps sur les bras j’essaye d’analyser notre mentalité d’homme"

    if item_photo:
        menu:
            "Donnez la photo ?":
                jump chapitre_4_item

            "Continuez d'avancé":
                jump chapitre_4_1_8
    else:
        jump chapitre_4_1_8

label chapitre_4_3_2:
    "Fin"

    return

label chapitre_4_item:
    $ item_photo = False
    $ sanite += 20

    n "Vous donnez la photo à [X]"
    X "Oh....."
    n "....."
    n "....."
    n "[X] contemple la photo"
    X "Ça me rappelle des jours heureux"
    X "Tu as déjà eu des amis avec lesquelles tu pouvais avoir des conversations profondes ?"
    X "Être compris, se sentir écouté et apprécié ça fait toujours bizarre"
    
    jump chapitre_4_1_8
 


