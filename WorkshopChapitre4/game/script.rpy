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

    if sanite < 50:
        #Début -
        n "Vous émergez peu à peu de votre torpeur."
        n "Vous avez l’esprit encore chamboulé."
        n "Qu’est-ce qui est réel, qu’est-ce qui ne l’est pas."
        n "Tout vient se heurter dans votre tête."
        jump chapitre_4_2_0
    else:
        #Début +
        n "Vous marchez en vous assurant que ce qu’il y avait derrière vous a bien disparu."
        n "Vous soupirez de soulagement tandis que quel que soit la créature qui vous poursuivait n’était désormais plus qu’un écho lointain."
        n "Vous regardez aux alentours pour voir un environnement familier."
        jump chapitre_4_1_0

label chapitre_4_1_0:
    #Balade
    n "Seriez vous de retour chez vous ?"
    n "Vous voguez à travers la ville."
    n "La nuit tombée, les lumières éclairent votre chemin tel un guide."
    n "Après quelques minutes de marche, vous vous trouvez devant une porte."
    n "Un scepticisme vous prend, après tout ce que vous avez endurer dans les pièces d’avant c’était trop beau."
    n "Sans doute avez vous juste manquez l’ennemi de cette salle, l’heure est aux réjouissances."
    n "Vous ouvrez la porte."
    dav "..."
    dav "C’est le même lieu qu’au début."
    dav "Est-ce une hallucination,une mauvaise blague,un défi ?"
    n "Ces pensées affluent telle une cascade."
    n "Vous refaites le chemin,tel que vous l’avez fait précédemment."
    n "Après quelque temps vous vous retrouvez devant une porte."
    n "En l’ouvrant vous retrouver le même lieu que le début."
    dav "Impossible."
    dav "Mais est-ce vraiment impossible ?"
    n "Vous répétez ce processus plusieurs fois."
    n "En vain."
    n "Quelles sont les limites du possible dans ce lieu."
    dav "Des animaux qui parlent, des entités surnaturelles, des cauchemars vivants."
    n "Une légère tape sur l’épaule vous fait sursauter."
    n "Vous vous retournez pour faire face à une personne."
    show x standby
    X "Salutations."
    n "Vous faites un pas en arrière."
    dav "..."
    X "Qui es-tu ?"
    n "Vous hésitez avant de parler et ravalez votre salive."
    dav "David"
    X "David..."
    X "Tu veux sortir d’ici ?"
    n "Vous hocher la tête."
    X "Suis-moi alors."
    n "Vous suivez l’individu."
    n "Après quelques temps il s’arrête sur un banc."
    X "Assieds-toi donc."
    n "Vous vous exécutez."
    X "Dis moi, qu’est ce qui amène des gens tel que toi, dans un endroit comme celui-ci ?"
    X "Je ne sais pas."
    n "La personne vous regarde d’un air inquisiteur."
    dav "Quoi ?"
    X "Non, Rien."
    n "Silence..."
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
        $sanite = 100

    n "Vous parlez de la nuit avec [X]."
    n "[X] lève la tête."
    show x etoile
    X "..."
    X "Ah oui."
    X "Il n’y a que ça ici, avec le temps on s’y fait."
    X "J’attend impatiemment l’instant où le jour reviendra."
    X "..."
    X "Mais..."
    X "Je commence à douter qu’il arrive un jour."
    n "Vous regardez X qui observe le ciel d’un air mélancolique."
    X "A une époque j'étais fasciné par les étoiles, l’univers, les galaxies."
    X "A force de les côtoyées quotidiennement ce sont devenues des confidentes."
    X "Elles ne me posent pas de questions incessantes, pas de remarques qui blessent, seulement une écoute attentive."
    X "..."
    X "J’imagine que toi aussi tu es une oreille attentive."
    n "Vous vous relevez avec [X]."

    jump chapitre_4_1_5

label chapitre_4_1_3:
    #Vêtements
    $ sanite -= 10
    if sanite < 0:
        $sanite = 0

    n "Vous demandez à [X] pourquoi ce choix de vêtements."
    n "[X] vous regarde d'un air jugeur."
    show x regret
    n "La conversation tourne vite à l’impasse."
    X "C’est silencieux généralement ici."
    X "Je ne me rappelle pas la dernière fois où il y avait du bruit dans le coin."
    X "Je ne me rappelle même pas depuis quand je suis la."
    n "[X] laisse un soupir."
    X "Mieux vaut ne pas prendre racine ici."
    n "Vous vous relevez avec [X]."

    jump chapitre_4_1_6

label chapitre_4_1_4:
    #Seul
    n "Vous demandez à X pourquoi il est seul."
    show x etoile
    n "[X] vous observe, son regard ne vous fixe pas, comme si il était dans la lune."
    X "Je ne me suis jamais poser la question."
    X "C’est devenu si habituel que cela ne m’a jamais effleuré l’esprit."
    X "Je suppose qu’avec le temps on s’habitue à tout."
    X "Je sais que cela ne fait pas si longtemps que tu es arrivé."
    X "Et bien que tu compte repartir aussi vite, avoir de la compagnie, aussi peu de temps cela change beaucoup de chose."
    n "Vous regardez [X], vous ne savez pas où vous mettre."
    show x standby
    X "Pardon, tu dois être mal à l’aise."
    X "Hâtons le pas, si tu le veux bien."
    n "Vous vous relevez avec [X]."

    jump chapitre_4_1_6

label chapitre_4_1_5:
    #Discussion +
    n "Vous lui demandez ce que lui fait ici."
    X "Moi ?"
    X "Je sais plus trop, comment je suis arrivé là, cela fait bien longtemps maintenant."
    show x etoile
    X "Je crois que j’était venu avec un objectif en tête mais j’ai oublié."
    n "Vous vous sentez distant de l’homme."
    n "Vous lui poser alors la question qui vous taraude de demander."
    dav "Si tu sais où se situe la sortie pourquoi ne pas partir."
    n "[X] s’arrête."
    X "..."
    X "Je ne sais pas."
    X "Je suis bien ici, pas de stress, pas de demande, moi et rien que moi."
    X "Parfois je me sens seul,..., mais seulement parfois."
    X "Prendre une telle décision, ce n'est pas quelque chose à faire à la légère."
    X "Choisir c’est renoncer."
    X "Je me le répète sans cesse."
    X "Avec le temps, même le monstre qui tape à ta porte devient peu à peu plus docile."
    X "Je sais que je parle beaucoup du temps, mais c’est un peu la seule chose que j’ai."
    X "Je me complais dedans, il guérit tous les maux, soigne tous les traumatismes."
    X "..."
    X "Je divague."
    show x standby
    X "Depuis aussi longtemps que je puisse me souvenir, je ne me rappelle pas de ma dernière interaction."
    X "Désolée..."
    X "..."

    jump chapitre_4_1_7

label chapitre_4_1_6:
    #Discussion
    n "Vous lui demandez ce que lui fait ici."
    X "Moi ?"
    X "Je sais plus trop, comment je suis arrivé là, cela fait bien longtemps maintenant."
    show x etoile
    X "Je crois que j’était venu avec un objectif en tête mais j’ai oublié."
    n "Vous vous sentez distant de l’homme."
    n "Vous lui poser alors la question qui vous taraude de demander."
    dav "Si tu sais où se situe la sortie pourquoi ne pas partir."
    n "[X] s’arrête."
    X "..."
    X "Je ne sais pas."
    X "Je suis bien ici, pas de stress, pas de demande, moi et rien que moi."
    X "Parfois je me sens seul,..., mais seulement parfois."
    X "Prendre une telle décision, ce n'est pas quelque chose à faire à la légère."
    X "Choisir c’est renoncer."
    X "Je me le répète sans cesse."
    X "Avec le temps, même le monstre qui tape à ta porte devient peu à peu plus docile."
    X "Je sais que je parle beaucoup du temps, mais c’est un peu la seule chose que j’ai."
    X "Je me complais dedans, il guérit tous les maux, soigne tous les traumatismes."
    X "..."
    X "Je divague."
    show x standby
    X "Depuis aussi longtemps que je puisse me souvenir, je ne me rappelle pas de ma dernière interaction."
    X "Désolée.."
    X "..."
    jump chapitre_4_3_0

label chapitre_4_1_7:
    #Coin
    show x standby
    X "Tien regarde, c’est l’endroit où je vien me reposer."
    X "C’est calme par ici."
    X "Je suis content de marcher avec toi."
    X "Continuons."
    n "[X] à l'air heureux."

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
    show x standby
    X "Bon, eh bien voilà, c’est la sortie."
    n "Devant vous il y a une fenêtre."
    X "Oui ça paraît bizarre mais c’est bien la sortie de ce lieu."
    n "Vous êtes septiques."
    dav "Pourquoi tu ne sors pas, toi ?"
    X "J’ai appris à accepter cet endroit."
    X "Mais ne t’inquiète pas pour moi."
    X "Focalise toi sur ton périple, tu es le protagoniste de ton histoire ne l’oublie pas."
    dav "Mais, et toi ?"
    n "[X] marque une longue pause."
    n "Il vous regarde en souriant."
    X "Tu sais."
    X "Je suis doué pour donner des conseils, mais pas pour les suivres."
    X "En tout cas j'espère que tu trouveras le réconfort que tu cherches."
    X "Continue vers l’avant."
    X "Quelque soit les obstacles sur ton chemin,continue d'avancer."
    X "Cours vers l'avenir, et si tu ne peux pas courir marche."
    X "Si tu ne peut pas marcher rampe, mais continue toujours vers ce destin qui est le tien."
    X "Car n’oublie jamais que personne ne le fera pour toi."
    hide x standby
    n "[X] se tourne et continue de marcher."
    n "Le silence de la nuit résonne à nouveau."
    n "Vous passez par la fenêtre."

    jump chapitre_4_3_2

label chapitre_4_2_0:
    #P/Vien
    n "Vous entendez des bruits de pas qui se rapprochent."
    n "Ils se rapprochent."
    n "Encore plus près."
    n "Ils sont juste ici..."
    n "Les bruits s'arrêtent."
    show x wakeup at left
    X "Ça va ?"
    n "Vous ouvrez les yeux pour voir un homme se pencher sur vous."
    jump chapitre_4_2_1

label chapitre_4_2_1:
    #Discussion -
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
    #Non
    $sanite += 10
    if sanite > 100:
        $sanite = 100
    dav "Non"
    X "Ah"
    X "Eh bien commençons par t'enlever le sol, c’est un bon début je pense."
    "L’homme vous aide à vous relever."
    show x standby
    jump chapitre_4_3_0

label chapitre_4_2_3:
    #Ça va
    dav "Ça va."
    X "Mouais j'en doute fort."
    X "Tien prend ma main."
    n "Vous attrapez la main de l’homme."
    show x standby
    X "Voilà."
    X "Alors dis moi qu’est ce que tu fait dans le coin ?"
    dav "Je m'échappait d’un monstre quand j’ai atterri là."
    X "Tu cherche la sortie je présume ?"
    dav "Ça serait bien oui."
    X "Suis-moi."
    jump chapitre_4_3_0

label chapitre_4_2_4:
    #Oui oui
    $ sanite -=10
    if sanite < 0:
        $sanite = 0
    dav "Oui oui."
    X "Ça ne t’avance à rien de mentir tu sais."
    X "Allez prend ma main on va te sortir de là."
    n "Vous attrapez la main de l’homme."
    show x standby
    X "C’est déjà mieux."
    X "Alors dit moi qu’est ce que tu fait dans le coin."
    dav "Je cherche a sortir de cet endroit."
    X "Je vois."
    X "Je veux bien t’y amener à condition que tu vienne faire une ballade avec moi."

    jump chapitre_4_2_8

label chapitre_4_2_8:
    #Discours
    X "Tu m’as l’air sacrément mal en point, ça va aller ?"
    X "Quoi que, vu ta réponse de tout à l'heure, pas sûr que tu sois honnête avec moi."
    X "En te voyant j’ai l’impression que tu as vécu une sacrée épopée par là-bas."
    n "Vous lui demandez ce que lui fait ici."
    X "Moi ?"
    X "Je sais plus trop, comment je suis arrivé là, cela fait bien longtemps maintenant."
    X "Je crois que j’était venu avec un objectif en tête mais j’ai oublié."
    n "Vous vous sentez distant de l’homme."
    n "Vous lui poser alors la question qui vous taraude de demander."
    dav "Si tu sais où se situe la sortie pourquoi ne pas partir."
    n "[X] s’arrête."
    show x etoile
    X "..."
    X "Je ne sais pas."
    X "Je suis bien ici, pas de stress, pas de demande, moi et rien que moi."
    X "Parfois je me sens seul,..., mais seulement parfois."
    X "Prendre une telle décision, ce n'est pas quelque chose à faire à la légère."
    X "Choisir c’est renoncer."
    X "Je me le répète sans cesse."
    X "Avec le temps, même le monstre qui tape à ta porte devient peu à peu plus docile."
    X "Je sais que je parle beaucoup du temps, mais c’est un peu la seule chose que j’ai."
    X "Je me complais dedans, il guérit tous les maux, soigne tous les traumatismes."
    X "..."
    X "Je divague."
    show x standby
    X "Depuis aussi longtemps que je puisse me souvenir, je ne me rappelle pas de ma dernière interaction."
    X "Désolée..."
    X "..."
    X "On arrive à l’endroit en question."
    X "Nos chemins vont devoirs se séparés."
    n "Vous arrivez à une ancienne cabane."
    jump chapitre_4_2_9

label chapitre_4_2_9:
    #Avert+Encouragement
    show x pensif
    X "Bon, eh bien voilà, c’est la sortie."
    n "Devant vous il y a une fenêtre."
    X "Oui ça paraît bizarre mais c’est bien la sortie de ce lieu."
    n "Vous êtes septique."
    dav "Pourquoi tu ne sors pas, toi ?"
    X "J’ai appris à accepter cet endroit."
    X "Mais ne t’inquiète pas pour moi."
    X "Focalise toi sur ton périple, tu es le protagoniste de ton histoire ne l’oublie pas."
    dav "Mais, et toi ?"
    n "[X] marque une longue pause."
    n "Il vous regarde en souriant."
    X "Tu sais."
    X "Je suis doué pour donner des conseils, mais pas pour les suivres."
    X "En tout cas j'espère que tu trouveras le réconfort que tu cherches."
    X "Et n’oublie jamais,tu es le maître de ton destin, continue vers l’avant."
    X "Quelque soit les obstacles sur ton chemin,continue d'avancer."
    X "Cours vers ton destin, et si tu ne peux pas courir marche."
    X "Si tu ne peut pas marcher rampe, mais continue toujours vers ce destin qui est tien."
    X "Car n’oublie jamais que personne ne le fera pour toi."
    hide x pensif
    n "X se tourne et continue de marcher."
    n "Le silence de la nuit résonne à nouveau."
    n "Vous passez par la fenêtre."

    jump chapitre_4_3_1

label chapitre_4_3_0:
    #Vien
    show x pensif
    X "T’es tu déjà demandé le but de la vie ?"
    X "Nous avons beau exister, le temps est inexorable et finit toujours par nous rattraper."
    X "Et pour remédier à cela, en tant qu’humains nous avons créé ces buts, ces désirs, ces espérances."
    X "Cette course à vouloir obtenir les objets de ses désirs, quand on l’achève, qu’est-ce qu’il nous reste ?"
    X "Je me pose la question parfois."
    X "..."
    X "Désolé, vu que je n’ai que du temps sur les bras j’essaye d’analyser notre mentalité d’homme."
    X "Enfin, assez parler de moi, tu dois être dans toutes tes émotions je me trompe ?"
    n "Vous acquiescer."
    X "Dit moi tout, comment tu es arrivé là, et pourquoi ?"
    n "Vous commencez à raconter votre périple à [X]."
    n "Il vous regarde d’un air perplexe."
    n "Au fur et à mesure que vous racontez l’histoire il devient de plus en plus compréhensif."
    X "Perte de mémoire, épopée surnaturelle, on croirait entendre un livre de chair de poule."
    X "Je pense que dans le monde tout est dû à une logique."
    X "Depuis le début tu as rencontré un chat obsédé par un monstre qu’il n’a jamais vu, une créature colérique, une succession de porte qui ont établi un monstre en fonction de tes choix puis tu es arrivé ici."
    X "Une logique devrait lié ces lieux mais j’ai du mal à voir laquelle."
    X "Je ne peux pas vraiment t’aider vu que tu repars si tôt, j’aurais bien voulu mais le temps me manque."
    X "Tien en parlant du loup voici la sortie."
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

    n "Vous donnez la photo à [X]."
    X "Oh....."
    show x trespensif
    n "....."
    n "....."
    n "[X] contemple la photo."
    X "Ça me rappelle des jours heureux."
    X "Tu as déjà eu des amis avec lesquelles tu pouvais avoir des conversations profondes ?"
    X "Être compris, se sentir écouté et apprécié je ne m’y habitue pas."
    
    jump chapitre_4_1_8
 
label chapitre_4_3_2:
    "Fin"

    return


