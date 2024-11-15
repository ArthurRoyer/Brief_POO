# Classe de base pour un animal
class Animal:
    def __init__(self, nom, espece, regime_alimentaire):
        self.nom = nom
        self.espece = espece
        self.regime_alimentaire = regime_alimentaire

    def __str__(self):
        return f"{self.espece} nommé {self.nom}"

    def est_predateur(self):
        """Retourne True si l'animal est un prédateur."""
        return False

    def proie_admissible(self, autre_animal):
        """Retourne True si cet animal peut être mangé par le prédateur (animal courant)."""
        return False

    def nourrir(self, nourriture):
        """Nourrit l'animal en fonction de son régime alimentaire."""
        if self.regime_alimentaire == "carnivore" and nourriture == "viande":
            print(f"{self.nom} ce régale de ce délicieux festin de viande.")
        elif self.regime_alimentaire == "herbivore" and nourriture == "légumes":
            print(f"{self.nom} ce régale de ce délicieux festin de légumes.")
        elif self.regime_alimentaire == "omnivore" and nourriture in ["viande", "légumes"]:
            print(f"{self.nom} ce régale de ce délicieux festin de {nourriture}.")
        else:
            print(f"{self.nom} n'aime pas ça du tout.")


# Sous-classes des espèces d'animaux
class Loup_arctique(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Loup arctique", "carnivore")

    def est_predateur(self):
        """Le loup arctique est un prédateur."""
        return True

    def proie_admissible(self, autre_animal):
        """Le loup arctique chasse uniquement le boeuf musqué."""
        return isinstance(autre_animal, Boeuf_musque)


class Boeuf_musque(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Boeuf musqué", "herbivore")


class Ours_polaire(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Ours polaire", "omnivore")

    def est_predateur(self):
        """L'ours polaire est un prédateur."""
        return True

    def proie_admissible(self, autre_animal):
        """L'ours polaire chasse uniquement le boeuf musqué."""
        return isinstance(autre_animal, Boeuf_musque)


class Lemming_arctique(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Lemming arctique", "herbivore")


class Renard_arctique(Animal):
    def __init__(self, nom):
        super().__init__(nom, "Renard arctique", "carnivore")

    def est_predateur(self):
        """Le renard arctique est un prédateur."""
        return True

    def proie_admissible(self, autre_animal):
        """Le renard arctique chasse uniquement le lemming arctique."""
        return isinstance(autre_animal, Lemming_arctique)


# Classe Territoire pour contenir des animaux
class Territoire:
    def __init__(self):
        self.animaux = []

    def ajouter_animal(self, animal):
        """Ajoute un animal sur le territoire."""
        self.animaux.append(animal)

    def lister_animaux(self):
        """Affiche la liste des animaux présents sur le territoire."""
        if self.animaux:
            print(f"\nLes animaux sur le territoire {numero_territoire} sont :")
            for animal in self.animaux:
                print(f"- {animal}")
        else:
            print("Le territoire est abandonné.")

    def chasser(self):
        """Gère les relations prédateur/proie dans le territoire."""
        for predator in self.animaux:
            if predator.est_predateur():
                for prey in self.animaux:
                    if predator != prey and not prey.est_predateur() and predator.proie_admissible(prey):
                        # Si le prédateur chasse la proie, la proie est supprimée du territoire
                        print(f"{predator} chasse et mange {prey}")
                        self.animaux.remove(prey)
                        break  # Le prédateur ne peut manger qu'une proie à la fois


# Classe Ecosysteme pour gérer les territoires
class Ecosysteme:
    def __init__(self):
        self.territoires = []

    def ajouter_territoire(self, territoire):
        """Ajoute un territoire dans l'écosystème."""
        self.territoires.append(territoire)

    def compter_territoires(self):
        """Retourne le nombre de territoires dans l'écosystème."""
        return len(self.territoires)

    def afficher_territoires(self):
        """Affiche le nombre de territoires dans l'écosystème."""
        print(f"L'écosystème contient {self.compter_territoires()} territoire(s).")


# Fonction pour ajouter des animaux à un territoire
def ajouter_animaux_au_territoire(territoire, numero_territoire):
    animaux_disponibles = [
        ("Loup arctique", Loup_arctique),
        ("Boeuf musqué", Boeuf_musque),
        ("Ours polaire", Ours_polaire),
        ("Lemming arctique", Lemming_arctique),
        ("Renard arctique", Renard_arctique)
    ]

    while True:
        print(f"\nLes animaux disponibles pour le territoire {numero_territoire} sont :")
        for idx, (nom, _) in enumerate(animaux_disponibles, 1):
            print(f"{idx}. {nom}")

        # Demander à l'utilisateur de choisir un animal ou de terminer
        while True:
            try:
                choix = int(input(
                    f"Choisissez un animal à ajouter en entrant son numéro (ou entrez 0 pour terminer le territoire {numero_territoire}) : "))
                if choix == 0:
                    return  # Sortir de la fonction si l'utilisateur entre 0
                if 1 <= choix <= len(animaux_disponibles):
                    animal_nom = input(f"Quel nom voulez-vous donner à votre {animaux_disponibles[choix - 1][0]} ? ")
                    animal_classe = animaux_disponibles[choix - 1][1]
                    animal = animal_classe(animal_nom)
                    territoire.ajouter_animal(animal)
                    print(f"{animal} ajouté au territoire {numero_territoire}.")
                    break  # Sortir de la boucle de choix d'animal
                else:
                    print("Choix invalide. Veuillez entrer un numéro entre 1 et 5.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier.")

    # Affichage du nombre d'animaux et de leurs noms après l'ajout
    #print(f"\nLe territoire {numero_territoire} contient {len(territoire.animaux)} animaux :")
    #territoire.lister_animaux()


# Fonction pour nourrir les animaux
def nourrir_animaux(territoire):
    for animal in territoire.animaux:
        while True:
            nourriture = input(f"Que voulez-vous donner à manger à {animal.nom} (viande ou légumes) ? ").lower()
            if nourriture in ["viande", "légumes"]:
                animal.nourrir(nourriture)
                break
            else:
                print("Veuillez choisir entre 'viande' ou 'légumes'.")



if __name__ == "__main__":
    # Création d'un écosystème
    mon_ecosysteme = Ecosysteme()

    # Ajouter des territoires
    numero_territoire = 1
    while True:
        # Création et ajout d'un territoire
        territoire = Territoire()
        mon_ecosysteme.ajouter_territoire(territoire)

        print("Bienvenue dans les steps arctiques !")

        # Ajouter des animaux dans le territoire
        print(f"Ajout des animaux dans le territoire {numero_territoire} :")
        ajouter_animaux_au_territoire(territoire, numero_territoire)

        # Demander à l'utilisateur s'il souhaite ajouter un nouveau territoire
        reponse = input("\nVoulez-vous ajouter un autre territoire ? (oui/non) : ").lower()
        if reponse != "oui":
            break
        numero_territoire += 1

    # Affichage du nombre d'animaux et de leurs noms sur chaques territoires
    print("\nLes différents térritoires contiennent :")
    for idx, territoire in enumerate(mon_ecosysteme.territoires, 1):
        print(f"\nTerritoire {idx}:")
        territoire.lister_animaux()

    # Nourrir les animaux dans chaque territoire
    print("\nOn nourrit les animaux :")
    for idx, territoire in enumerate(mon_ecosysteme.territoires, 1):
        print(f"\nTerritoire {idx}:")
        nourrir_animaux(territoire)

    # Chasser et afficher les résultats après la chasse
    print("\nC'est l'heure de la chasse !")
    for idx, territoire in enumerate(mon_ecosysteme.territoires, 1):
        territoire.chasser()
        print(f"\nAprès la chasse sur le territoire {idx}, il ne reste que :")
        territoire.lister_animaux()
