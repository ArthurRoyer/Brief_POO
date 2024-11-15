# Arctic Ecosystem Simulation

Bienvenue dans le simulateur d'écosystème arctique ! Ce programme permet de créer des territoires, d'y ajouter des animaux, de les nourrir et de simuler des interactions naturelles comme la chasse.

---

## **Description du projet**

Ce projet simule un écosystème arctique composé de plusieurs territoires. Chaque territoire peut contenir des animaux variés, chacun ayant des comportements spécifiques (régime alimentaire, relations prédateur-proie). 

L'utilisateur peut :
1. Ajouter des territoires et y placer des animaux.
2. Nourrir les animaux en fonction de leurs besoins alimentaires.
3. Simuler des interactions de chasse où les prédateurs chassent leurs proies.

---

## **Fonctionnalités**

### 1. **Gestion des territoires**
- Créez plusieurs territoires.
- Ajoutez autant d'animaux que souhaité à chaque territoire.
- Observez les interactions entre les animaux dans chaque territoire.

### 2. **Ajout d'animaux**
Les animaux disponibles sont :
- **Loup arctique** : Prédateur qui chasse les **Boeufs musqués**.
- **Boeuf musqué** : Herbivore.
- **Ours polaire** : Prédateur omnivore qui chasse les **Boeufs musqués**.
- **Lemming arctique** : Herbivore.
- **Renard arctique** : Prédateur qui chasse les **Lemmings arctiques**.

### 3. **Nourrissage**
Nourrissez les animaux selon leur régime alimentaire :
- `Carnivore` : Mange de la viande.
- `Herbivore` : Mange des légumes.
- `Omnivore` : Peut manger de la viande ou des légumes.

### 4. **Simulation de la chasse**
- Les prédateurs chassent leurs proies admissibles selon des règles définies.
- Observez quels animaux survivent après la chasse.

---

## **Installation**

### **Prérequis**
- Python 3.x installé sur votre machine.

### **Étapes**
1. Clonez ce dépôt ou téléchargez les fichiers.
2. Exécutez le fichier principal avec :
   ```bash
   python arctic_ecosystem.py

## **Structure du projet**

### **Fichier principal**
- `arctic_ecosystem.py` : Fichier contenant tout le code source.

---

### **Classes principales**

#### **Animal** : Classe de base pour les animaux.
- **Attributs** :
  - `nom`
  - `espece`
  - `regime_alimentaire`
- **Méthodes** :
  - `nourrir(nourriture)` : Permet de nourrir l’animal.
  - `est_predateur()` : Retourne si l’animal est un prédateur.
  - `proie_admissible(autre_animal)` : Vérifie si un animal peut être une proie.

#### **Sous-classes spécifiques**
- `Loup_arctique`
- `Boeuf_musqué`
- `Ours_polaire`
- `Lemming_arctique`
- `Renard_arctique`

---

#### **Territoire** : Gère les animaux présents dans un territoire.
- **Méthodes** :
  - `ajouter_animal(animal)` : Ajoute un animal au territoire.
  - `lister_animaux()` : Affiche les animaux présents.
  - `chasser()` : Simule les relations prédateur-proie.

---

#### **Ecosysteme** : Gère l'ensemble des territoires.
- **Méthodes** :
  - `ajouter_territoire(territoire)` : Ajoute un territoire.
  - `compter_territoires()` : Retourne le nombre de territoires.
  - `afficher_territoires()` : Affiche les territoires et leurs animaux.

---

## **Auteur**
Projet développé par **Arthur ROYER**.

---

## **Licence**
Ce projet est sous licence MIT. Vous êtes libre de l’utiliser, le modifier et le distribuer.

---

Bon amusement dans votre exploration de l’écosystème arctique ! 🐾❄️
