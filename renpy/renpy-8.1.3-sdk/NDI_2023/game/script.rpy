define p = Character('Professeur Olivier', color="#c8f3ff")
define n = Character('Nico Naïf', color="#a77f2e")

screen barre_carbone():
    zorder 100
    vbar value AnimatedValue(carbone, max_carbone, delay=1.0):
        xalign 0.970 yalign 0.008
        xmaximum 47
        ymaximum 327
        left_bar Frame("images/empty.png", 100, 10)
        right_bar Frame("images/full.png", 100, 10)
        thumb "images/thumb.png"
        thumb_offset 30
    imagebutton idle "images/text.png" xalign 0.988 yalign 0.01 xmaximum 47 ymaximum 327 action NullAction()

default carbone = 1
default max_carbone = 100


label start:

    scene tsunami with fade

    "7 décembre 2023, la ville de Kappi est touchée par des phénomènes climatiques extrêmes."
    "Des inondations et des tempêtes fréquentes ont poussé la municipalité à organiser une réunion publique pour discuter des mesures à prendre."

    scene meeting_room with fade

    show olivier1 at left with moveinleft

    "Le Professeur Olivier est invité pour mener les débats et fournir des informations sur le sujet."

    show nico3 at right with moveinright

    "Nico Naif, un habitant de Kappi, assiste à la réunion par curiosité."

    show screen barre_carbone

    show olivier6 at left 
    hide olivier1 

    p "Mesdames et Messieurs, l’heure est grave."
    p "Notre pays a été touché par des phénomènes climatiques graves."
    p "Nous devons prendre des mesures sérieuses pour faire face à ces changements climatiques."
    p "Nous sommes ici pour trouver des solutions efficaces et sur le long terme, pour réduire les émissions de gaz à effet de serre, principale cause du réchauffement climatique."
    p "Si nous n’agissons pas aujourd’hui, il sera trop tard pour limiter le réchauffement de la planète à 1,5°C."
    p "Nous allons commencer par un temps d’échange d’idées, afin de recueillir des potentielles solutions au problème, et ce, à toutes les échelles."
    p "Car vous savez, chaque geste compte dans la lutte contre le changement climatique. Chacun de nous peut faire la différence."

    show olivier1 at left 
    hide olivier6

    show nico7 at right
    hide nico3

    n "Oh, je ne sais pas. C'est pas plutôt aux grandes entreprises et aux gouvernements de faire quelque chose ? On est juste des individus, après tout."

    show nico3 at right
    hide nico7

    show olivier6 at left
    hide olivier1

    p "Certes, les grandes entreprises et les gouvernements ont un rôle majeur à jouer."
    p "Mais n'oublions pas que nos choix individuels en tant que consommateurs et citoyens contribuent aussi à façonner le monde qui nous entoure."

    show olivier1 at left
    hide olivier6

    show nico7 at right
    hide nico3

    n "Hmm, je ne suis pas convaincu. C'est pas à nous d'agir, c'est trop compliqué."

    show nico3 at right
    hide nico7

    menu:
        "Peut-être qu'on ne peut rien changer...":

            $ carbone += 8
            show olivier2 at left
            hide olivier1

            p "Cependant, penser que 'ce n’est pas à nous d’agir' pourrait nous laisser dans l'inaction."
            p "Nous avons un rôle à jouer, même en tant qu'individus."
            p "Changer nos habitudes et encourager les autres à faire de même peut déclencher des réactions en chaîne positives."

        "Chacun de nous a un rôle à jouer.":

            show olivier2 at left
            hide olivier1

            p "Chacun de nous a une part de responsabilité dans la préservation de notre planète."
            p "En faisant des choix conscients au quotidien, nous pouvons influencer positivement notre entourage et contribuer à un changement plus vaste."
            p "Ne sous-estimons pas l'impact que nous pouvons avoir en tant qu'individus engagés."

    show olivier1 at left
    hide olivier2

    show nico5 at right
    hide nico3

    n "Très bien, alors on a qu’a tous planter des arbres. Ils absorbent le CO2 non ?"     

    show nico4 at right
    hide nico5

    menu:
        "Oui, plantons tous des arbres, c'est une solution naturelle !":

            $ carbone += 8
            show olivier5 at left
            hide olivier1

            p "Planter des arbres est une excellente initiative, mais nous ne devrions pas compter uniquement sur cette solution."
            p "Selon le GIEC, l'élimination du carbone ne devrait pas remplacer la réduction des émissions."
            p "Certaines technologies peuvent avoir des conséquences négatives, et il est essentiel de se concentrer sur la conservation des écosystèmes et la réduction des émissions pour une solution plus durable."

        "Plantons des arbres, mais cela ne suffit pas.":
            
            show olivier5 at left
            hide olivier1

            p "Planter des arbres est une excellente initiative, mais nous ne devrions pas compter uniquement sur cette solution."
            p "Selon le GIEC, l'élimination du carbone ne devrait pas remplacer la réduction des émissions."
            p "Certaines technologies peuvent avoir des conséquences négatives, et il est essentiel de se concentrer sur la conservation des écosystèmes et la réduction des émissions pour une solution plus durable."



    show olivier4 at left
    hide olivier5

    show nico6 at right
    hide nico4

    n "Mais comment conserver les écosystèmes ? A-t-on le pouvoir de changer quelque chose ?"

    show nico4 at right
    hide nico6

    show olivier5 at left
    hide olivier4

    p "Bien sûr. L’objectif est d’atteindre la neutralité carbone d’ici 2050."
    p "Pour ce faire le moyen le plus efficace est de se liberer des energies fosilles."
    p "Elles altèrent les écosystèmes et réprésentent une part majeur des émissions de gaz à effet de serre."

    show olivier4 at left
    hide olivier5

    show nico6 at right
    hide nico4

    n "Mais quelles alternatives a-t-on aux énergies fossiles ? Les energies renouvelables, c’est pas assez efficace."

    show nico4 at right
    hide nico6

    menu:
        "Peut-être que ce n’est pas la meilleure solution.":

            $ carbone += 8
            show olivier3 at left
            hide olivier4

            p "Je comprends que cela puisse sembler douteux."
            p "Cependant, les énergies renouvelables ont fait d'énormes progrès."

            show olivier5 at left
            hide olivier3

            p "Selon le GIEC, les énergies solaire et éolienne sont désormais compétitives par rapport à la production d'énergie fossile."
            p "Leur coût a même baissé considérablement ces dernières années, ce qui les rend très attractives sur le plan économique."

        "Il me semble que les énergies renouvelables sont devenues compétitives et efficaces.": 

            $ carbone += 8
            show olivier3 at left
            hide olivier4

            p "C'est une excellente question. En fait, les énergies renouvelables, en particulier le solaire et l'éolien, sont devenues extrêmement compétitives et efficaces."

            show olivier5 at left
            hide olivier3

            p "Le GIEC souligne que leurs progrès techniques ont été bien plus rapides que prévu, et leurs coûts ont chuté de manière significative."
            p "Pour lutter contre le changement climatique, nous devons accélérer le déploiement de ces sources d'énergie à faible émission de carbone."

    show olivier4 at left
    hide olivier5

    show nico5 at right
    hide nico4

    n "De toute façon, moi je ne m'inquiète pas trop."
    n "Avec les progrès qu’on fait de nos jours, je pense que la technologie nous sauvera."   

    show nico4 at right
    hide nico5

    menu:
        "Oui, je pense que la technologie résoudra tout.":

            $ carbone += 8
            show olivier3 at left
            hide olivier4

            p "C'est compréhensible. La technologie peut certainement contribuer, mais elle ne peut pas être la seule solution."
            p "Nous devons également changer nos comportements et adopter des modes de vie plus durables pour réduire notre empreinte carbone."
            p "La combinaison de la technologie et de l'action individuelle est essentielle."

        "La technologie seule ne suffira pas.":    

            show olivier3 at left
            hide olivier4

            p "Il est vrai que la technologie peut apporter des solutions, mais elle ne peut pas résoudre le problème à elle seule."
            p "Le rapport du GIEC souligne l'importance de réduire nos émissions de gaz à effet de serre et de changer nos modes de vie."
            p "La technologie doit être utilisée de manière complémentaire à des actions concrètes de notre part pour garantir un avenir durable."

    p "Je vais vous donner une piste : la sobriété énergétique est essentielle. Nous devons revoir nos habitudes. Des suggestions ?"   

    show olivier1 at left
    hide olivier4

    menu:
        "Eviter la voiture individuelle, privilégier les transports en commun, et réduire notre consommation de viande.":

            show olivier3 at left
            hide olivier1

            p "Excellent choix !"

            show olivier5 at left
            hide olivier3

            p "Le GIEC souligne l'importance de ces actions pour réduire notre empreinte carbone."
            p "En optant pour les transports en commun et en limitant la consommation de viande, nous contribuons à la réduction des émissions de gaz à effet de serre."
            p "Ces actions sont non seulement bonnes pour l'environnement, mais elles contribuent également à une transition écologique socialement juste en évitant de renforcer les inégalités."

        "Acheter de la nourriture bio, un véhicule électrique et rénover son appartement pour limiter sa consommation.":

            $ carbone += 8
            show olivier3 at left
            hide olivier1

            p "C'est certainement une intention louable, mais il est essentiel de considérer la dimension sociale de la transition écologique."
            p "Tout le monde ne peut pas se permettre ces choix d'un point de vue économique."

            show olivier5 at left
            hide olivier3

            p "Le GIEC met en avant l'importance de ne pas laisser de côté les plus précaires."
            p "Plutôt que des actions individuelles coûteuses, nous devons privilégier des mesures collectives qui favorisent des solutions accessibles à tous."   

    show olivier1 at left
    hide olivier5

    show nico7 at right
    hide nico4

    n "Mais ça va être difficile de changer faire changer leurs habitudes à des millions de gens."
    n "Et pour les transports, les voitures électriques, c'est la solution, non ?"     

    show nico8 at right
    hide nico7    

    show olivier2 at left
    hide olivier1

    p "Changer les habitudes à grande échelle est un défi, mais les voitures électriques peuvent effectivement jouer un rôle crucial dans la réduction des émissions de gaz à effet de serre."
    p "On ne peut pas obliger les gens à en acheter, en revanche on peut améliorer l'efficacité des batteries des véhicules électriques."
    p "C’est essentiel pour rendre cette transition encore plus bénéfique sur le plan environnemental."
    p "C'est une combinaison d'actions individuelles et de progrès technologiques qui nous rapprochera de nos objectifs climatiques."  

    show olivier3 at left
    hide olivier2

    p "D’autres suggestions ?"

    show olivier1 at left
    hide olivier3

    menu:
        "Le nucléaire.":

            $ carbone += 8
            show olivier3 at left
            hide olivier1
            p "Tu soulèves une perspective intéressante."

            show olivier2 at left
            hide olivier3

            p "Le nucléaire a été considéré comme une option, mais selon les données du GIEC, son déploiement a été plus lent que prévu."
            p "Il présente également des risques pour les Objectifs de Développement Durable."
            p "Nous devons évaluer attentivement cette option tout en accélérant le déploiement des énergies renouvelables, qui sont déjà compétitives et offrent un potentiel d'atténuation plus fort."

        "Le captage du CO2.":

            $ carbone += 8
            show olivier3 at left
            hide olivier1

            p "C'est une perspective valable."

            show olivier2 at left
            hide olivier3

            p "Cependant, selon les données du GIEC, le captage du CO2 a progressé plus lentement que prévu."
            p "De plus, il présente des risques pour les Objectifs de Développement Durable."
            p "Le rapport met en évidence que les énergies renouvelables, telles que le solaire et l'éolien, ont un potentiel d'atténuation beaucoup plus fort à un coût bien plus faible."
            p "Il est donc crucial de privilégier ces alternatives pour accélérer notre transition vers une énergie plus propre."  

    show olivier1 at left
    hide olivier2

    show nico6 at right
    hide nico8

    n "De toute façon, c’est l'industrie le plus gros pollueur. Pas sûr que ça puisse vraiment changer..."    

    show nico8 at right
    hide nico6

    menu:
        "L'industrie ne peut pas vraiment décarboner, c'est trop compliqué.":

            $ carbone += 8
            show olivier2 at left
            hide olivier1
            p "C'est compréhensible de penser cela."
            p "Cependant, selon les données du GIEC, les progrès technologiques récents rendent la décarbonation de l'industrie tout à fait possible."
            p "Nous avons des technologies émergentes qui peuvent réduire les émissions de manière significative, mais cela nécessite des choix politiques et des investissements pour transformer vraiment le secteur industriel."

        "Si, l'industrie peut changer avec les nouvelles technologies.":

            show olivier2 at left
            hide olivier1
            p "C'est exact, il y a de l'espoir pour la décarbonation de l'industrie."
            p "De nouvelles technologies émergent, comme des procédés de production à faibles émissions de GES, et des approches circulaires telles que la réutilisation et le recyclage sont en développement."
            p "Cependant, cela nécessite des choix politiques audacieux pour transformer réellement le secteur industriel et atteindre ces objectifs de décarbonation."

    show olivier1 at left
    hide olivier2

    show nico7 at right
    hide nico8

    n "Mais est-ce que ça ne va pas coûter trop cher aux entreprises ?"       

    show nico8 at right
    hide nico7

    menu:
        "Oui, ça va être cher. On devrait laisser les entreprises décider.":

            $ carbone += 8
            show olivier2 at left
            hide olivier1

            p "C'est une préoccupation légitime."
            p "Cependant, le GIEC souligne que la décarbonation de l'industrie nécessite des investissements significatifs."
            p "Il est crucial que les gouvernements prennent des mesures et établissent des incitations pour encourager les entreprises à adopter des pratiques plus durables."

        "Les investissements sont nécessaires, mais les avantages à long terme en valent la peine.":

            show olivier2 at left
            hide olivier1
            p "C'est vrai, les investissements seront nécessaires, mais les avantages à long terme pour notre planète et notre économie en valent la peine."
            p "Les gouvernements peuvent jouer un rôle essentiel en fournissant des incitations et en mettant en place des politiques qui encouragent les entreprises à adopter des pratiques plus respectueuses du climat."     

    p "Nous n’avons pas beaucoup parlé d’alimentation jusqu'à présent."
    p "Savez-vous que la production de viande est responsable d’une grande partie des émissions de gaz à effet de serre ?"      

    show olivier1 at left
    hide olivier2

    show nico6 at right
    hide nico8  

    n "La réduction de viande, sérieusement ? On va tous devenir végétariens ?"

    show nico4 at right
    hide nico6

    menu:

        "Oui, réduire notre consommation de viande est importante pour l'environnement.":

            show olivier2 at left
            hide olivier1

            p "C'est une option, en effet."
            p "Le GIEC confirme que le passage à des régimes alimentaires riches en protéines végétales permet une forte réduction des émissions de gaz à effet de serre."
            p "Cela pourrait contribuer de manière significative à nos efforts pour lutter contre le changement climatique et apporter d'autres avantages tels que la préservation de la biodiversité et la sécurité alimentaire."

        "Non, je ne pense pas que réduire la consomation de viande soit nécessaire.":    

            $ carbone += 8
            show olivier2 at left
            hide olivier1
            p "C'est une perspective compréhensible, mais selon les données du GIEC, la réduction de la consommation de viande est l'une des mesures les plus efficaces pour réduire les émissions de gaz à effet de serre dans le secteur de l'agriculture."
            p "Il est important de considérer des alternatives alimentaires plus durables pour soutenir notre planète."

    show olivier1 at left
    hide olivier2

    show nico5 at right
    hide nico4

    n "J’ai entendu parler de l'agroécologie, c'est quoi ça ?"       

    show nico4 at right
    hide nico5

    menu:
        "C'est une pratique agricole durable qui utilise moins d'engrais chimiques.":

            show olivier3 at left
            hide olivier1

            p "Bonne réponse !"

            show olivier6 at left
            hide olivier3

            p "L'agroécologie est une approche agricole durable qui implique des pratiques comme la réduction de l'utilisation d'engrais chimiques, la diversification des cultures et une meilleure gestion des déjections animales."
            p "Cela aide à réduire les émissions de gaz à effet de serre tout en préservant la biodiversité et en assurant la sécurité alimentaire."

        "Je ne sais pas vraiment, ça doit être compliqué.":

            $ carbone += 8
            show olivier3 at left
            hide olivier1
            p "Pas de problème."

            show olivier6 at left
            hide olivier3
            p "L'agroécologie peut sembler complexe, mais en réalité, c'est une pratique agricole durable qui vise à minimiser les impacts environnementaux tout en assurant la production alimentaire."
            p "Elle utilise des méthodes plus respectueuses de l'environnement, contribuant ainsi à atténuer le changement climatique."

    p "Ces idées de transition sont très nobles, mais les industries vont avoir besoin d’aides, notamment financières."

    show olivier1 at left
    hide olivier6

    show nico7 at right
    hide nico4

    n "Pourquoi avons-nous besoin d'aides financières ? Chacun peut bien faire sa part sans cela, non ?"

    show nico8 at right
    hide nico7       

    menu:
        "Oui, les aides financières sont nécessaires pour rendre les solutions accessibles à tous.":

            show olivier2 at left
            hide olivier1
            p "C'est une excellente question."
            p "Le GIEC souligne que pour garantir une transition équitable, des aides financières sont nécessaires."
            p "Tout le monde n'a pas les mêmes moyens, et ces aides permettent d'assurer que personne n'est laissé pour compte dans cette transition cruciale."

        "Non, les gens devraient pouvoir supporter les coûts eux-mêmes.":

            $ carbone += 8
            show olivier2 at left
            hide olivier1
            p "Il est compréhensible de penser ainsi, mais le GIEC met en avant la nécessité d'aides financières pour garantir une transition juste et équitable."
            p "Cela ne concerne pas seulement les coûts individuels, mais aussi la création d'un système qui favorise des choix écologiques pour tous."    

    show olivier1 at left
    hide olivier2

    show nico6 at right
    hide nico8

    n "Mais cela ne va-t-il pas créer des inégalités si certaines personnes reçoivent des aides et d'autres non ?"

    show nico8 at right
    hide nico6

    menu:
        "Oui, mais c'est nécessaire pour assurer une transition équitable.":

            show olivier5 at left
            hide olivier1
            p "Une observation pertinente."
            p "C'est pour éviter ces inégalités que le GIEC recommande des mesures qui réduisent les écarts économiques, garantissant ainsi que la transition écologique profite à tous, indépendamment de leurs moyens financiers."        

        "Non, tout le monde devrait se débrouiller par lui-même.":

            $ carbone += 8
            show olivier5 at left
            hide olivier1
            p "Cependant, le GIEC souligne que sans certaines aides financières, certaines personnes pourraient être exclues de la transition écologique."
            p "L'objectif est de créer un système où tout le monde peut participer et bénéficier des solutions durables, quel que soit son niveau financier."

    show olivier6 at left
    hide olivier5

    p "Mesdames et Messieurs, nos échanges ont été riches et variés."
    p "Il est clair que chacun de nous a un rôle à jouer dans la lutte contre le changement climatique."
    p "Les solutions existent, mais elles nécessitent des choix courageux et des actions concrètes."        


    return
