define dav = Character ("david (vous)", color = "#ffffff",what_size=30,what_color="#ffffff",window_background="#c5c5c55e")
define dav_pense = Character ("david (vous)", color = "#aaaaaa",what_size=30,what_color="#aaaaaa",window_background="#c5c5c55e")
define n = Character ("narateur", color = "#ffffff00",what_size=30,what_color="#dadde4be",window_background="#0000005e")


#PERSO A RAJOUTER
define X = Character ("Monsieur X")
define Z = Character ("Esprit")

init python:
    sanite = 60
    item_photo = True


    #VARIABLE A RAJOUTER
    try_observer = False
    try_fuir = False

# Le jeu commence ici
label start:

label chapitre_4_0:

    if sanite < 50:
        #Début -
        n "{cps=45}Vous émergez peu à peu de votre torpeur."
        n "{cps=45}Vous avez l’esprit encore chamboulé."
        scene bg depression un
        n "{cps=45}Qu’est-ce qui est réel, qu’est-ce qui ne l’est pas."
        n "{cps=45}Tout vient se heurter dans votre tête."
        jump chapitre_4_2_0
    else:
        #Début +
        n "{cps=45}Vous marchez en vous assurant que ce qu’il y avait derrière vous a bien disparu."
        n "{cps=45}Vous soupirez de soulagement tandis que quel que soit la créature qui vous poursuivait n’était désormais plus qu’un écho lointain."
        n "{cps=45}Vous regardez aux alentours pour voir un environnement familier."
        scene bg depression un
        jump chapitre_4_1_0

label chapitre_4_1_0:
    #Balade
    n "{cps=45}Seriez vous de retour chez vous ?"
    n "{cps=45}Vous voguez à travers la ville."
    n "{cps=45}La nuit tombée, les lumières éclairent votre chemin tel un guide."
    n "{cps=45}Après quelques minutes de marche, vous vous trouvez devant une porte."
    n "{cps=45}Un scepticisme vous prend, après tout ce que vous avez endurer dans les pièces d’avant c’était trop beau."
    n "{cps=45}Sans doute avez vous juste manquez l’ennemi de cette salle, l’heure est aux réjouissances."
    n "{cps=45}Vous ouvrez la porte."
    dav "{cps=45}..."
    dav "{cps=45}C’est le même lieu qu’au début."
    dav "{cps=45}Est-ce une hallucination,une mauvaise blague,un défi ?"
    n "{cps=45}Ces pensées affluent telle une cascade."
    n "{cps=45}Vous refaites le chemin,tel que vous l’avez fait précédemment."
    n "{cps=45}Après quelque temps vous vous retrouvez devant une porte."
    n "{cps=45}En l’ouvrant vous retrouver le même lieu que le début."
    dav "{cps=45}Impossible."
    dav "{cps=45}Mais est-ce vraiment impossible ?"
    n "{cps=45}Vous répétez ce processus plusieurs fois."
    n "{cps=45}En vain."
    n "{cps=45}Quelles sont les limites du possible dans ce lieu."
    dav "{cps=45}Des animaux qui parlent, des entités surnaturelles, des cauchemars vivants."
    n "{cps=45}Une légère tape sur l’épaule vous fait sursauter."
    n "{cps=45}Vous vous retournez pour faire face à une personne."
    show x standby
    X "{cps=45}Salutations."
    n "{cps=45}Vous faites un pas en arrière."
    dav "{cps=45}..."
    X "{cps=45}Qui es-tu ?"
    n "{cps=45}Vous hésitez avant de parler et ravalez votre salive."
    dav "{cps=45}David"
    X "{cps=45}David..."
    X "{cps=45}Tu veux sortir d’ici ?"
    n "{cps=45}Vous hocher la tête."
    X "{cps=45}Suis-moi alors."
    n "{cps=45}Vous suivez l’individu."
    scene bg depression quatre
    show x standby
    n "{cps=45}Après quelques temps il s’arrête sur un banc."
    X "{cps=45}Assieds-toi donc."
    n "{cps=45}Vous vous exécutez."
    X "{cps=45}Dis moi, qu’est ce qui amène des gens tel que toi, dans un endroit comme celui-ci ?"
    X "{cps=45}Je ne sais pas."
    n "{cps=45}La personne vous regarde d’un air inquisiteur."
    dav "{cps=45}Quoi ?"
    X "{cps=45}Non, Rien."
    n "{cps=45}Silence..."
    jump chapitre_4_1_1

label chapitre_4_1_1:
    menu:
        "Nuit":
            jump chapitre_4_1_2
        
        "Vêtements":
            jump chapitre_4_1_3

        "Seul":
            jump chapitre_4_1_4

label chapitre_4_1_2:
    #Nuit
    $ sanite += 10
    if sanite > 100:
        $ sanite = 100

    n "{cps=45}Vous parlez de la nuit avec [X]."
    n "{cps=45}[X] lève la tête."
    show x etoile
    X "{cps=45}..."
    X "{cps=45}Ah oui."
    X "{cps=45}Il n’y a que ça ici, avec le temps on s’y fait."
    X "{cps=45}J’attend impatiemment l’instant où le jour reviendra."
    X "{cps=45}..."
    X "{cps=45}Mais..."
    X "{cps=45}Je commence à douter qu’il arrive un jour."
    n "{cps=45}Vous regardez X qui observe le ciel d’un air mélancolique."
    X "{cps=45}A une époque j'étais fasciné par les étoiles, l’univers, les galaxies."
    X "{cps=45}A force de les côtoyées quotidiennement ce sont devenues des confidentes."
    X "{cps=45}Elles ne me posent pas de questions incessantes, pas de remarques qui blessent, seulement une écoute attentive."
    X "{cps=45}..."
    X "{cps=45}J’imagine que toi aussi tu es une oreille attentive."
    n "{cps=45}Vous vous relevez avec [X]."

    jump chapitre_4_1_5

label chapitre_4_1_3:
    #Vêtements
    $ sanite -= 10
    if sanite < 0:
        $sanite = 0

    n "{cps=45}Vous demandez à [X] pourquoi ce choix de vêtements."
    n "{cps=45}[X] vous regarde d'un air jugeur."
    show x regret
    n "{cps=45}La conversation tourne vite à l’impasse."
    X "{cps=45}C’est silencieux généralement ici."
    X "{cps=45}Je ne me rappelle pas la dernière fois où il y avait du bruit dans le coin."
    X "{cps=45}Je ne me rappelle même pas depuis quand je suis la."
    n "{cps=45}[X] laisse un soupir."
    X "{cps=45}Mieux vaut ne pas prendre racine ici."
    n "{cps=45}Vous vous relevez avec [X]."

    jump chapitre_4_1_6

label chapitre_4_1_4:
    #Seul
    n "{cps=45}Vous demandez à X pourquoi il est seul."
    show x etoile
    n "{cps=45}[X] vous observe, son regard ne vous fixe pas, comme si il était dans la lune."
    X "{cps=45}Je ne me suis jamais poser la question."
    X "{cps=45}C’est devenu si habituel que cela ne m’a jamais effleuré l’esprit."
    X "{cps=45}Je suppose qu’avec le temps on s’habitue à tout."
    X "{cps=45}Je sais que cela ne fait pas si longtemps que tu es arrivé."
    X "{cps=45}Et bien que tu compte repartir aussi vite, avoir de la compagnie, aussi peu de temps cela change beaucoup de chose."
    n "{cps=45}Vous regardez [X], vous ne savez pas où vous mettre."
    show x standby 
    X "{cps=45}Pardon, tu dois être mal à l’aise."
    X "{cps=45}Hâtons le pas, si tu le veux bien."
    n "{cps=45}Vous vous relevez avec [X]."

    jump chapitre_4_1_6

label chapitre_4_1_5:
    #Discussion +
    scene bg depression trois
    show x standby 
    n "{cps=45}Vous lui demandez ce que lui fait ici."
    X "{cps=45}Moi ?"
    X "{cps=45}Je sais plus trop, comment je suis arrivé là, cela fait bien longtemps maintenant."
    show x etoile
    X "{cps=45}Je crois que j’était venu avec un objectif en tête mais j’ai oublié."
    n "{cps=45}Vous vous sentez distant de l’homme."
    n "{cps=45}Vous lui poser alors la question qui vous taraude de demander."
    dav "{cps=45}Si tu sais où se situe la sortie pourquoi ne pas partir."
    n "{cps=45}[X] s’arrête."
    X "{cps=45}..."
    X "{cps=45}Je ne sais pas."
    X "{cps=45}Je suis bien ici, pas de stress, pas de demande, moi et rien que moi."
    X "{cps=45}Parfois je me sens seul,..., mais seulement parfois."
    X "{cps=45}Prendre une telle décision, ce n'est pas quelque chose à faire à la légère."
    X "{cps=45}Choisir c’est renoncer."
    X "{cps=45}Je me le répète sans cesse."
    X "{cps=45}Avec le temps, même le monstre qui tape à ta porte devient peu à peu plus docile."
    X "{cps=45}Je sais que je parle beaucoup du temps, mais c’est un peu la seule chose que j’ai."
    X "{cps=45}Je me complais dedans, il guérit tous les maux, soigne tous les traumatismes."
    X "{cps=45}..."
    X "{cps=45}Je divague."
    show x standby
    X "{cps=45}Depuis aussi longtemps que je puisse me souvenir, je ne me rappelle pas de ma dernière interaction."
    X "{cps=45}Désolée..."
    X "{cps=45}..."

    jump chapitre_4_1_7

label chapitre_4_1_6:
    #Discussion
    scene bg depression trois
    show x standby
    n "{cps=45}Vous lui demandez ce que lui fait ici."
    X "{cps=45}Moi ?"
    X "{cps=45}Je sais plus trop, comment je suis arrivé là, cela fait bien longtemps maintenant."
    show x etoile
    X "{cps=45}Je crois que j’était venu avec un objectif en tête mais j’ai oublié."
    n "{cps=45}Vous vous sentez distant de l’homme."
    n "{cps=45}Vous lui poser alors la question qui vous taraude de demander."
    dav "{cps=45}i tu sais où se situe la sortie pourquoi ne pas partir."
    n "{cps=45}[X] s’arrête."
    X "{cps=45}..."
    X "{cps=45}Je ne sais pas."
    X "{cps=45}Je suis bien ici, pas de stress, pas de demande, moi et rien que moi."
    X "{cps=45}Parfois je me sens seul,..., mais seulement parfois."
    X "{cps=45}Prendre une telle décision, ce n'est pas quelque chose à faire à la légère."
    X "{cps=45}Choisir c’est renoncer."
    X "{cps=45}Je me le répète sans cesse."
    X "{cps=45}Avec le temps, même le monstre qui tape à ta porte devient peu à peu plus docile."
    X "{cps=45}Je sais que je parle beaucoup du temps, mais c’est un peu la seule chose que j’ai."
    X "{cps=45}Je me complais dedans, il guérit tous les maux, soigne tous les traumatismes."
    X "{cps=45}..."
    X "{cps=45}Je divague."
    show x standby
    X "{cps=45}Depuis aussi longtemps que je puisse me souvenir, je ne me rappelle pas de ma dernière interaction."
    X "{cps=45}Désolée.."
    X "{cps=45}..."
    jump chapitre_4_3_0

label chapitre_4_1_7:
    #Coin
    show x standby
    X "{cps=45}Tien regarde, c’est l’endroit où je vien me reposer."
    X "{cps=45}C’est calme par ici."
    X "{cps=45}Je suis content de marcher avec toi."
    X "{cps=45}Continuons."
    n "{cps=45}[X] à l'air heureux."

    if item_photo:
        menu:
            "Donnez la photo":
                jump chapitre_4_item

            "Continuez d'avancé":
                jump chapitre_4_1_8
    else:
        jump chapitre_4_1_8

label chapitre_4_1_8:
    #Encouragement
    scene bg depression deux
    show x standby
    X "{cps=45}Bon, eh bien voilà, c’est la sortie."
    n "{cps=45}Devant vous il y a une grille."
    X "{cps=45}Oui ça paraît bizarre mais c’est bien la sortie de ce lieu."
    n "{cps=45}Vous êtes septiques."
    dav "{cps=45}Pourquoi tu ne sors pas, toi ?"
    X "{cps=45}J’ai appris à accepter cet endroit."
    X "{cps=45}Mais ne t’inquiète pas pour moi."
    X "{cps=45}Focalise toi sur ton périple, tu es le protagoniste de ton histoire ne l’oublie pas."
    dav "{cps=45}Mais, et toi ?"
    n "{cps=45}[X] marque une longue pause."
    n "{cps=45}Il vous regarde en souriant."
    X "{cps=45}Tu sais."
    X "{cps=45}Je suis doué pour donner des conseils, mais pas pour les suivres."
    X "{cps=45}En tout cas j'espère que tu trouveras le réconfort que tu cherches."
    X "{cps=45}Continue vers l’avant."
    X "{cps=45}Quelque soit les obstacles sur ton chemin,continue d'avancer."
    X "{cps=45}Cours vers l'avenir, et si tu ne peux pas courir marche."
    X "{cps=45}Si tu ne peut pas marcher rampe, mais continue toujours vers ce destin qui est le tien."
    X "{cps=45}Car n’oublie jamais que personne ne le fera pour toi."
    hide x standby
    n "{cps=45}[X] se tourne et continue de marcher."
    n "{cps=45}Le silence de la nuit résonne à nouveau."
    n "{cps=45}Vous passez par la grille."

    jump chapitre_4_3_2

label chapitre_4_2_0:
    #P/Vien
    n "{cps=45}Vous entendez des bruits de pas qui se rapprochent."
    n "{cps=45}Ils se rapprochent."
    n "{cps=45}Encore plus près."
    n "{cps=45}Ils sont juste ici..."
    n "{cps=45}Les bruits s'arrêtent."
    show x wakeup:
        xalign 0
        yalign 0
    X "{cps=45}Ça va ?"
    n "{cps=45}Vous ouvrez les yeux pour voir un homme se pencher sur vous."
    jump chapitre_4_2_1

label chapitre_4_2_1:
    #Discussion -
    X "{cps=45}Allô ?"
    X "{cps=45}Tu m’as pas l’air bien en point."
    X "{cps=45}J’ai besoin d’une réponse est-ce que ça va ?"
    menu:
        "Non":
            jump chapitre_4_2_2

        "Ça va":
            jump chapitre_4_2_3

        "Oui oui":
            jump chapitre_4_2_4

label chapitre_4_2_2:
    #Non
    $sanite += 10
    if sanite > 100:
        $sanite = 100
    dav "{cps=45}Non"
    X "{cps=45}Ah"
    X "{cps=45}Eh bien commençons par t'enlever le sol, c’est un bon début je pense."
    n "{cps=45}L’homme vous aide à vous relever."
    hide x wakeup
    show x standby
    jump chapitre_4_3_0

label chapitre_4_2_3:
    #Ça va
    dav "{cps=45}Ça va."
    X "{cps=45}Mouais j'en doute fort."
    X "{cps=45}Tien prend ma main."
    n "{cps=45}Vous attrapez la main de l’homme."
    hide x wakeup
    show x standby
    X "{cps=45}Voilà."
    X "{cps=45}Alors dis moi qu’est ce que tu fait dans le coin ?"
    dav "{cps=45}Je m'échappait d’un monstre quand j’ai atterri là."
    X "{cps=45}Tu cherche la sortie je présume ?"
    dav "{cps=45}Ça serait bien oui."
    X "{cps=45}Suis-moi."
    jump chapitre_4_3_0

label chapitre_4_2_4:
    #Oui oui
    $ sanite -=10
    if sanite < 0:
        $sanite = 0
    dav "{cps=45}Oui oui."
    X "{cps=45}Ça ne t’avance à rien de mentir tu sais."
    X "{cps=45}Allez prend ma main on va te sortir de là."
    n "{cps=45}Vous attrapez la main de l’homme."
    hide x wakeup
    show x standby
    X "{cps=45}C’est déjà mieux."
    X "{cps=45}Alors dit moi qu’est ce que tu fait dans le coin."
    dav "{cps=45}Je cherche a sortir de cet endroit."
    X "{cps=45}Je vois."
    X "{cps=45}Je veux bien t’y amener à condition que tu vienne faire une ballade avec moi."

    jump chapitre_4_2_8

label chapitre_4_2_8:
    #Discours
    X "{cps=45}Tu m’as l’air sacrément mal en point, ça va aller ?"
    X "{cps=45}Quoi que, vu ta réponse de tout à l'heure, pas sûr que tu sois honnête avec moi."
    X "{cps=45}En te voyant j’ai l’impression que tu as vécu une sacrée épopée par là-bas."
    n "{cps=45}Vous lui demandez ce que lui fait ici."
    X "{cps=45}Moi ?"
    X "{cps=45}Je sais plus trop, comment je suis arrivé là, cela fait bien longtemps maintenant."
    X "{cps=45}Je crois que j’était venu avec un objectif en tête mais j’ai oublié."
    n "{cps=45}Vous vous sentez distant de l’homme."
    n "{cps=45}Vous lui poser alors la question qui vous taraude de demander."
    dav "{cps=45}Si tu sais où se situe la sortie pourquoi ne pas partir."
    n "{cps=45}[X] s’arrête."
    show x etoile
    X "{cps=45}..."
    X "{cps=45}Je ne sais pas."
    X "{cps=45}Je suis bien ici, pas de stress, pas de demande, moi et rien que moi."
    X "{cps=45}Parfois je me sens seul,..., mais seulement parfois."
    X "{cps=45}Prendre une telle décision, ce n'est pas quelque chose à faire à la légère."
    X "{cps=45}Choisir c’est renoncer."
    X "{cps=45}Je me le répète sans cesse."
    X "{cps=45}Avec le temps, même le monstre qui tape à ta porte devient peu à peu plus docile."
    X "{cps=45}Je sais que je parle beaucoup du temps, mais c’est un peu la seule chose que j’ai."
    X "{cps=45}Je me complais dedans, il guérit tous les maux, soigne tous les traumatismes."
    X "{cps=45}..."
    X "{cps=45}Je divague."
    show x standby
    X "{cps=45}Depuis aussi longtemps que je puisse me souvenir, je ne me rappelle pas de ma dernière interaction."
    X "{cps=45}Désolée..."
    X "{cps=45}..."
    X "{cps=45}On arrive à l’endroit en question."
    X "{cps=45}Nos chemins vont devoirs se séparés."
    n "{cps=45}Vous arrivez à une ancienne cabane."
    jump chapitre_4_2_9

label chapitre_4_2_9:
    #Avert+Encouragement
    scene bg depression deux
    show x pensif
    X "{cps=45}Bon, eh bien voilà, c’est la sortie."
    n "{cps=45}Devant vous il y a une grille."
    X "{cps=45}Oui ça paraît bizarre mais c’est bien la sortie de ce lieu."
    n "{cps=45}Vous êtes septique."
    dav "{cps=45}Pourquoi tu ne sors pas, toi ?"
    X "{cps=45}J’ai appris à accepter cet endroit."
    X "{cps=45}Mais ne t’inquiète pas pour moi."
    X "{cps=45}Focalise toi sur ton périple, tu es le protagoniste de ton histoire ne l’oublie pas."
    dav "{cps=45}Mais, et toi ?"
    n "{cps=45}[X] marque une longue pause."
    n "{cps=45}Il vous regarde en souriant."
    X "{cps=45}Tu sais."
    X "{cps=45}Je suis doué pour donner des conseils, mais pas pour les suivres."
    X "{cps=45}En tout cas j'espère que tu trouveras le réconfort que tu cherches."
    X "{cps=45}Et n’oublie jamais,tu es le maître de ton destin, continue vers l’avant."
    X "{cps=45}Quelque soit les obstacles sur ton chemin,continue d'avancer."
    X "{cps=45}Cours vers ton destin, et si tu ne peux pas courir marche."
    X "{cps=45}Si tu ne peut pas marcher rampe, mais continue toujours vers ce destin qui est tien."
    X "{cps=45}Car n’oublie jamais que personne ne le fera pour toi."
    hide x pensif
    n "{cps=45}X se tourne et continue de marcher."
    n "{cps=45}Le silence de la nuit résonne à nouveau."
    n "{cps=45}Vous passez par la grille."

    jump chapitre_4_1_8

label chapitre_4_3_0:
    #Vien
    show x pensif
    X "{cps=45}T’es tu déjà demandé le but de la vie ?"
    X "{cps=45}Nous avons beau exister, le temps est inexorable et finit toujours par nous rattraper."
    X "{cps=45}Et pour remédier à cela, en tant qu’humains nous avons créé ces buts, ces désirs, ces espérances."
    X "{cps=45}Cette course à vouloir obtenir les objets de ses désirs, quand on l’achève, qu’est-ce qu’il nous reste ?"
    X "{cps=45}Je me pose la question parfois."
    X "{cps=45}..."
    X "{cps=45}Désolé, vu que je n’ai que du temps sur les bras j’essaye d’analyser notre mentalité d’homme."
    X "{cps=45}Enfin, assez parler de moi, tu dois être dans toutes tes émotions je me trompe ?"
    n "{cps=45}Vous acquiescer."
    X "{cps=45}Dit moi tout, comment tu es arrivé là, et pourquoi ?"
    n "{cps=45}Vous commencez à raconter votre périple à [X]."
    n "{cps=45}Il vous regarde d’un air perplexe."
    n "{cps=45}Au fur et à mesure que vous racontez l’histoire il devient de plus en plus compréhensif."
    X "{cps=45}Perte de mémoire, épopée surnaturelle, on croirait entendre un livre de chair de poule."
    X "{cps=45}Je pense que dans le monde tout est dû à une logique."
    X "{cps=45}Depuis le début tu as rencontré un chat obsédé par un monstre qu’il n’a jamais vu, une créature colérique, une succession de porte qui ont établi un monstre en fonction de tes choix puis tu es arrivé ici."
    X "{cps=45}Une logique devrait lié ces lieux mais j’ai du mal à voir laquelle."
    X "{cps=45}Je ne peux pas vraiment t’aider vu que tu repars si tôt, j’aurais bien voulu mais le temps me manque."
    X "{cps=45}Tien en parlant du loup voici la sortie."
    show x standby

    if item_photo:
        menu:
            "Donnez la photo ?":
                jump chapitre_4_item

            "Continuez d'avancé":
                jump chapitre_4_1_8
    else:
        jump chapitre_4_1_8

label chapitre_4_item:
    $ item_photo = False
    $ sanite += 20

    n "{cps=45}Vous donnez la photo à [X]."
    X "{cps=45}Oh....."
    show x trespensif
    n "{cps=45}....."
    n "{cps=45}....."
    n "{cps=45}[X] contemple la photo."
    X "{cps=45}Ça me rappelle des jours heureux."
    X "{cps=45}Tu as déjà eu des amis avec lesquelles tu pouvais avoir des conversations profondes ?"
    X "{cps=45}Être compris, se sentir écouté et apprécié je ne m’y habitue pas."
    
    jump chapitre_4_1_8
 
label chapitre_4_3_2:
    scene bg aceptation
    n "{cps=45}La teinte de la nuit s’obscurcit encore, jusqu'à ne devenir qu’une horizon sombre."
    n "{cps=45}Un bruit assourdissant vous entoure."
    n "{cps=45}Une figure fantomatique se tient face à vous."
    show esprit base
    n "{cps=45}Le fantôme vous parle,mais vous ne distinguez pas de bouche."
    Z "{cps=45}Ô âme égarée que viens tu faire au sein de l’antichambre ?"
    n "{cps=45}Des sueurs froides vous glissent sur le front."
    jump chapitre_5_0

label chapitre_5_0:
    if try_fuir == False and try_observer == False:
        menu:
            "Parler":
                jump chapitre_5_0_1

            "Fuir":
                jump chapitre_5_0_2

            "Observer":
                jump chapitre_5_0_3
    elif try_fuir == True and try_observer == False:
        menu:
            "Parler":
                jump chapitre_5_0_1

            "Observer":
                jump chapitre_5_0_3
    elif try_fuir == False and try_observer == True:
        menu:
            "Parler":
                jump chapitre_5_0_1

            "Fuir":
                jump chapitre_5_0_2
    else: 
        menu:
            "Parler":
                jump chapitre_5_0_1


label chapitre_5_0_1:
    #Parler
    n "{cps=45}Vous engager la conversation."
    n "{cps=45}Vous racontez au fantôme les péripéties qui vous ont amené à cette endroit."
    n "{cps=45}Le fantôme vous observe avec intérêt."
    Z "{cps=45}Donc tu ne connais pas la raison de ta venue ?"
    dav "{cps=45}Oui c’est exact."
    Z "{cps=45}Mmh..."
    n "{cps=45}Le fantôme vous observe attentivement."
    Z "{cps=45}Souhaites-tu connaître la raison derrière ta présence en ces lieux ?"
    n "{cps=45}Vous êtes pris de cours."
    dav "{cps=45}Vous le savez ?"
    Z "{cps=45}Oui."
    dav "{cps=45}Alors dites moi."
    Z "{cps=45}Je ne pense pas que te donner la réponse serait bénéfique."
    Z "{cps=45}Mais sache que c’est toi qui a décidé de venir ici de ton plein gré."
    dav "{cps=45}Quoi ?"
    n "{cps=45}Le fantôme vous regarde avec malice."
    n "{cps=45}Il souris et vous fixe."
    Z "{cps=45}Si tu veux je peux te faire sortir de cet endroit."
    Z "{cps=45}Plus de pièces, plus d’épreuves, seulement ton chez toi."
    Z "{cps=45}En revanche tu peux également à tes risques et périls."
    jump chapitre_5_1_0

label chapitre_5_1_0:
    if sanite != 50:
        menu:
            "Continuez":
                Z "Est-tu sûr ?"
                menu: 
                    "Oui":
                        jump chapitre_5_1
                    "Non":
                        jump chapitre_5_1_0

            "Rentrez chez soi":
                jump chapitre_5_2
    else:
        menu:
            "Rentrez chez soi":
                jump chapitre_5_2


label chapitre_5_0_2:
    $ try_fuir = True
    #Fuir
    n "{cps=45}Votre tête vous crie de partir mais votre corps est figé sur place."
    jump chapitre_5_0

label chapitre_5_0_3:
    $ try_observer = True
    #Observer
    n "{cps=45}Cette figure fantomatique est la seule chose aux alentours"
    n "{cps=45}Un vide comble l’espace."
    jump chapitre_5_0

label chapitre_5_1:
    hide esprit base
    if sanite > 90:
        #Fin ++
        n "{cps=45}Vous continuez d’avancer."
        n "{cps=45}Vous entendez vos pas résonner dans la salle."
        n "{cps=45}Vous avancer dans le silence."
        n "{cps=45}Après quelques pas, une lumière bienveillante rayonne autour de vous."
        n "{cps=45}Des petits cristaux lumineux apparaissent."
        n "{cps=45}Chacun d’entre semble contenir une petite voix."
        n "{cps=45}Alors que vous essayez d’attraper l’un d’entre eux, ils se rapprochent de vous."
        n "{cps=45}Des souvenirs affluent, des souvenirs de vous et d’un autre."
        n "{cps=45}En l’espace d’un instant vous voyez l’intégralité des moments passés avec lui."
        n "{cps=45}Cependant, les cristaux ternissent tandis que vous voyez une série d’accidents."
        n "{cps=45}Un soir pluvieux, un conducteur ivre, un garçon au volant."
        n "{cps=45}Un choc..."
        n "{cps=45}..."
        n "{cps=45}Les couleurs disparaissent."
        n "{cps=45}Vous vous voyez devant une tombe."
        n "{cps=45}Plus de colère, plus de joie,une coquille vide."
        n "{cps=45}..."
        n "{cps=45}La lumière devient de plus en plus brillante."
        n "{cps=45}Les cristaux tombés au sol."
        n "{cps=45}La lumière vous aveugle."
        n "{cps=45}..."
        jump end 

    elif sanite > 50:
        #Fin +
        n "{cps=45}Vous continuez d’avancer."
        n "{cps=45}Vous entendez vos pas résonner dans la salle."
        n "{cps=45}Vous avancer dans ce silence assourdissant."
        n "{cps=45}Un espèce d’amas de lumière se tient devant vous."
        n "{cps=45}Vous sentez un léger réconfort."
        n "{cps=45}Des cristaux flottants dans les airs vous entourent."
        n "{cps=45}Chacun d’eux semble contenir des paroles."
        n "{cps=45}Vous essayer d’en attraper un."
        #QTE
        n "{cps=45}Vous avez beau essayer, ils finissent toujours hors d’atteinte."
        n "{cps=45}La lumière éclaircit de plus en plus la pièce."
        n "{cps=45}Elle devient de plus en plus grande jusqu’à vous aveugler."
        n "{cps=45}..."
        jump chapitre_5_morale

    elif sanite > 10:
        #Fin -
        n "{cps=45}Vous continuez d’avancer."
        n "{cps=45}Vous entendez vos pas résonner dans la salle."
        n "{cps=45}Vous avancer dans ce silence assourdissant."
        n "{cps=45}Au loin vous apercevez une lumière."
        dav "{cps=45}Qu’est ce que c’est que ça ?"
        n "{cps=45}La lumière commence à vaciller."
        n "{cps=45}Le blanc tourne au rouge qui retourne au blanc."
        n "{cps=45}Le sol tremble."
        n "{cps=45}Vous voyez flou."
        n "{cps=45}..." #BRUIT TOMBER PAR TERRE
        jump chapitre_5_morale

    else: 
        #Fin --
        n "{cps=45}Vous continuez d’avancer."
        n "{cps=45}Vous entendez vos pas résonner dans la salle."
        n "{cps=45}Vous avancer dans ce silence assourdissant."
        n "{cps=45}Au loin vous apercevez une lumière."
        dav "{cps=45}Qu’est ce que c’est que ça ?"
        n "{cps=45}La lumière émanant au loin diminue peu à peu"
        n "{cps=45}Le sol tremble."
        n "{cps=45}Vous voyez flou."
        n "{cps=45}Vous entendez une voix au loin."
        n "{cps=45}Seul dans ces affres du désespoir."
        Z "{cps=45}..."
        Z "{cps=45}Je t’avais prévenu."
        Z "{cps=45}Tu aurais pu repartir."
        Z "{cps=45}Tu aurais pu tourner la page."
        Z "{cps=45}Mais non..."
        Z "{cps=45}Serait-ce de la folie ?"
        Z "{cps=45}De l’ignorance ?"
        Z "{cps=45}Ou bien du courage mal placé ?"
        Z "{cps=45}Tu as couru tout seul à ta perte."
        Z "{cps=45}Tenter de te dissuader était une perte de temps."
        Z "{cps=45}Cet endroit sera un cauchemar donc tu ne te réveilleras pas."
        Z "{cps=45}Encore."
        Z "{cps=45}Et encore."
        Z "{cps=45}Et encore..."
        Z "{cps=45}Et encore.........."
        jump end

label chapitre_5_2:
    #FIN NEUTRE
    n "{cps=45}Le fantôme vous observe."
    n "{cps=45}Une lumière aveuglante."
    n "{cps=45}Vous êtes de retour chez vous."
    n "{cps=45}Plus de souffrance, plus de peur."
    n "{cps=45}Vous revenez enfin, comme si rien ne s’était passé."
    n "{cps=45}La tristesse cependant, n’est jamais vraiment partie."
    n "{cps=45}Vous vous rappelez désormais pourquoi vous étiez là-bas."
    jump end

label chapitre_5_morale:
    #Morale
    n "{cps=45}Vous êtes de retour chez vous."
    n "{cps=45}Plus de souffrance, plus de peur."
    n "{cps=45}Vous revenez enfin, comme si rien ne s’était passé."
    n "{cps=45}La tristesse cependant, n’est jamais vraiment partie."
    n "{cps=45}Vous vous rappelez désormais pourquoi vous étiez là-bas."
    jump end

label end:

    return