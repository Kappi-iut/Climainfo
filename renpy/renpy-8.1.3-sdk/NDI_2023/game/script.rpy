# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define n = Character('Noé', color="#c8ffc8")
define d = Character('Dimitri', color="#ffc8c8")
define v = Character('Vivien', color="#c8c8ff")


# Le jeu commence ici
label start:

    scene ecole

    show noe at left with moveinleft
    n "Salut ca va ?"

    show dim at right with moveinright
    d "Oui et toi ?"
    d "Ah tiens voila Vivien !"

    show viv at center with moveinright
    v "Salut les gars !"

    return
