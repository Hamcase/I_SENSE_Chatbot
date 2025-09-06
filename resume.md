---
# Documentation ISENSE pour Chatbot RAG

## Présentation Générale
I-SENSE est une plateforme IoT développée par OCP Maintenance Solutions (OCP MS), spécialisée dans la maintenance prédictive des machines industrielles.

**Objectifs principaux :**
- Surveiller l’état de santé des machines en temps réel
- Prédire l’apparition des défauts grâce à l’intelligence artificielle
- Optimiser la planification de la maintenance pour éviter d’impacter la production

La plateforme s’appuie sur la norme ISO 10816 (seuils vibratoires selon la classe des machines).  
Sources de données : VIBOX et MobiVib.

---
## Accès et Authentification
- Connexion par email et mot de passe
- Réinitialisation via « Mot de passe oublié »

---
## Modules et Fonctionnalités Principales

### Tableau de Bord
- Vue synthétique de l’état global des actifs
- Statuts des actifs :
  - **Normal** : aucune anomalie, valeurs vibratoires normales
  - **Moyen** : défauts précoces, pas de seuil critique dépassé
  - **Modéré** : dépassement du seuil d’avertissement
  - **Critique** : dépassement du seuil d’alarme, intervention rapide
  - **Indéfini** : données incomplètes
  - **Arrêt** : actif à l’arrêt
  - **Déconnecté** : Vibox non connectée
- Bouton pour détail des défauts (moyen, modéré, critique)
- Indicateurs généraux :
  - Nombre total d’actifs
  - Nombre d’utilisateurs
  - Mesures manuelles/en ligne/sans fil
  - Points de mesure créés
  - Nombre de Vibox connectés

### Vue Cartographique
- Carte de l’usine vue de haut
- Position des actifs sur le site
- Codes couleurs/indicateurs visuels pour état des actifs

### Module Actifs
- Visualisation de toutes les machines surveillées
- Recherche rapide (nom, référence)
- Filtres : entité, date, statut, classe

#### Informations par actif
- Nom
- Diagramme cinématique
- État des sous-actifs
- Historique de santé
- Défauts détectés/prédits (I-PREDICT)
- Caractéristiques techniques des sous-actifs

#### Page détaillée d’un actif
- **Machine Health Index** : calculé par IA
- **Asset Health History** : historique des états
- **Diagramme cinématique** : structure mécanique, points de mesure cliquables
- **Tendance des mesures** : graphique, code couleur (rouge, jaune, gris)
- **Recommandations** : liste des défauts, date, points, % énergie
- **Instruments** : état des capteurs/systèmes (Vibox)
- **Sous-actifs** : historique spécifique
- **Predicted Faults** : défauts prédits par IA

---
## Points de Mesure
- Directions d’analyse des vibrations :
  - RV : radiale verticale
  - RH : radiale horizontale
  - RO : radiale oblique
  - AX : axiale

---
## Critères de Criticité et Paramètres
- **Classe** : criticité pour la production
  - AA : très critique
  - A : critique
  - B : moins critique
  - C : le moins critique
- **Groupe** : selon ISO 10816
- **Valeurs aberrantes** : seuil par défaut 20
- **Coupling** : accouplement mécanique
- **Bearing** : palier mécanique

---
## Module Analysis
- Examen approfondi des données vibratoires
- Visualisation du diagramme cinématique
- Matrice de santé des actifs
- Filtrage par type de mesure, date, caractéristiques
- Analyse des tendances et signaux vibratoires (harmoniques, énergie, pics, bande latérale)
- Accès rapide à Analytics

---
## Module Analytics
- Vision synthétique des performances et alertes prédictives
- Indicateurs de performance (KPI) : heures de marche, temps d’arrêt, MTBF, MFT, MUT
- Indice de santé global
- Chronologie des alarmes
- Niveau de sévérité, recommandations
- Évolution de l’amplitude vibratoire
- Onglet Predict : défauts prédits, validation/rejet par expert
- Auto-diagnostic : 5 problèmes les plus fréquents

---
## Module Administratrice
- Gestion des zones : liste, création, cartographie
- Gestion des familles d’actifs : création, défauts, champs, diagrammes cinématiques
- Organisation visuelle par drag & drop

---
## Asset Manager Monitoring

### 1. Création d’un nouvel actif
- Bouton « Créer un nouvel actif »
- Choix du type : industriel 

### 2. Paramètres à renseigner pour la création d'un nouvel actif
- Famille : ex. groupe turboalternateur, motopompe, agitateur, motoventilateur
- Nom de l’actif
- Référence : identifiant unique de l’actif
- Entité : entreprise ou pôle qui ajoute l’actif
- Classe : AA/A/B/C (niveau de criticité)
- Structure : rigide ou flexible
- Groupe : selon ISO 10816
- Puissance : en Watt (W)
- Valeur aberrante : seuil de mesure fausse (défaut 20)
- Type de point de mesure : manuel (Mobivib) ou en ligne (Vibox)
- Image de l’actif
- Sauvegarde et choix du diagramme

### 3. Diagrammes
- Choix ou création de diagramme
- Drag & drop des sous-actifs et accouplements
- Zoom, rotation, upload de formes
- Sauvegarde et passage aux sous-actifs

### 4. Liste des sous-actifs disponibles
- Agitator  
- Alternator (plain/rolling bearings)  
- Compressor (plain/rolling bearings)  
- Crusher  
- Cylinder  
- DC motor  
- Drum conveyor  
- Elevateur  
- Fan  
- Gearbox (plain/rolling bearings)  
- Malaxeur  
- Pignon attaque  
- Pump (plain/rolling bearings)  
- Redler  
- Soufflante (plain/rolling bearings)  
- Turbine  
- AC Motor  
- Granulateur-sub asset

### 5. Définir les points de mesure
- Ajout via pop-up, choix direction (RV, RH, RO, AX)
- Numérotation automatique, modifiable

### 6. Configuration des bearings
- Modification via pop-up
- Points associés, étiquette, type (plain/rolling)
- Paramètres plain bearing : température, pression, fréquence instabilité, débit
- Paramètres rolling bearing : fabricant, référence, type, fréquences, modifiables
- Sauvegarde

### 7. Suppression d’un point
- Désélectionner toutes les directions, confirmer

### 8. Ajout d’un Coupling (Accouplement)
- Nom, points associés, type : Belt Pulley, Pinion-Crown, Chain Drive
- Paramètres spécifiques selon type : puissance, dimensions, références, fréquences, etc.

### 9. Ajout d’une configuration
- Appareil de mesure, points associés

### 10. Informations complémentaires
- **Pales d’agitateur** : éléments rotatifs pour brasser/mélanger
- **Types de compresseur** :
  - Vis rotatif : compression continue, débits élevés
  - Piston : mouvement alternatif, capacité moyenne
  - Palettes : fonctionnement silencieux, sans pulsation
- **Types de concasseur** :
  - Marteau, Chaîne, Cylindres, Boulets, Barres, Pendulaire
- **Types de pompe** :
  - Volumétrique : déplacement mécanique, hautes pressions
  - Centrifuge : roue tournante, grands débits
  - À vide : création de vide, applications industrielles

---

## Détails des sous-actifs et leurs paramètres

Cette section détaille les paramètres à renseigner pour chaque sous-actif dans la plateforme I-SENSE. Pour chaque sous-actif, les paramètres communs sont listés en premier, suivis des paramètres spécifiques. Les paramètres communs obligatoires sont : **Nom du sous-actif**, **Référence**, et **Nombre de roulements**. Les autres paramètres communs (**Marque**, **Puissance**, **Vitesse**) et tous les paramètres spécifiques sont facultatifs.


## Agitator
Voici les paramètres à renseigner pour l'agitateur :
- **Nom du sous-actif** (obligatoire) : Nom de l'agitateur
- **Référence** (obligatoire) : Référence unique de l'agitateur
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans l'agitateur
- **Marque** : Marque de l'agitateur
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Current (A)** : Courant nécessaire pour faire tourner le moteur à la vitesse désirée (ampère)
- **Diamètre des pales** : Diamètre des pales de l’agitateur
- **Matériau de pales** : Matériau des pales de l'agitateur
- **Nombre de pales** : Nombre de pales de l'agitateur
- **Voltage (V)** : Tension nécessaire pour alimenter l'agitateur (Volt)

## Alternator with rolling bearings (paliers de roulement)
Voici les paramètres à renseigner pour l'alternateur à paliers de roulement :
- **Nom du sous-actif** (obligatoire) : Nom de l'alternateur
- **Référence** (obligatoire) : Référence unique de l'alternateur
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans l'alternateur
- **Marque** : Marque de l'alternateur
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Number of blades** : Nombre de pales de l'alternateur
- **Capacité en kVa** : Capacité de l'alternateur (kVa)
- **Current (A)** : Courant maximal fourni en continu (A)
- **Facteur de puissance** : Indicateur d'efficacité de l'alternateur
- **Rendement (%)** : Rendement de l'alternateur (%)
- **Voltage (V)** : Tension générée (V)

## Alternator with plain bearings (paliers lisses)
Voici les paramètres à renseigner pour l'alternateur à paliers lisses :
- **Nom du sous-actif** (obligatoire) : Nom de l'alternateur
- **Référence** (obligatoire) : Référence unique de l'alternateur
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans l'alternateur
- **Marque** : Marque de l'alternateur
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Number of blades** : Nombre de pales de l'alternateur
- **Capacité en kVa** : Capacité de l'alternateur (kVa)
- **Current (A)** : Courant maximal fourni en continu (A)
- **Facteur de puissance** : Indicateur d'efficacité de l'alternateur
- **Rendement (%)** : Rendement de l'alternateur (%)
- **Voltage (V)** : Tension générée (V)

## Compressor with plain bearings (paliers lisses)
Voici les paramètres à renseigner pour le compresseur à paliers lisses :
- **Nom du sous-actif** (obligatoire) : Nom du compresseur
- **Référence** (obligatoire) : Référence unique du compresseur
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le compresseur
- **Marque** : Marque du compresseur
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Compressor type** : Type de compresseur (vis rotatif, piston, palettes)
- **Flow rate (m³/s)** : Débit volumétrique (m³/s)
- **Pressure (bar)** : Pression du compresseur (bar)

## Compressor with rolling bearings (paliers de roulement)
Voici les paramètres à renseigner pour le compresseur à paliers de roulement :
- **Nom du sous-actif** (obligatoire) : Nom du compresseur
- **Référence** (obligatoire) : Référence unique du compresseur
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le compresseur
- **Marque** : Marque du compresseur
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Compressor type** : Type de compresseur (vis rotatif, piston, palettes)
- **Flow rate (m³/s)** : Débit volumétrique (m³/s)
- **Pressure (bar)** : Pression du compresseur (bar)

## Crusher
Voici les paramètres à renseigner pour le concasseur :
- **Nom du sous-actif** (obligatoire) : Nom du concasseur
- **Référence** (obligatoire) : Référence unique du concasseur
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le concasseur
- **Marque** : Marque du concasseur
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Crusher type** : Type de concasseur (marteau, chaîne, cylindres, boulets, barres, pendulaire)
- **Disposition** : Orientation du concasseur (vertical ou horizontal)

## Cylinder
Voici les paramètres à renseigner pour le cylindre :
- **Nom du sous-actif** (obligatoire) : Nom du cylindre
- **Référence** (obligatoire) : Référence unique du cylindre
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le cylindre
- **Marque** : Marque du cylindre
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Current (A)** : Courant électrique absorbé (A)
- **Voltage (V)** : Tension d'alimentation (V)
- **Power (W)** : Puissance électrique (W)
- **Type d'excitation** : Type d'excitation du cylindre

## DC motor
Voici les paramètres à renseigner pour le moteur DC :
- **Nom du sous-actif** (obligatoire) : Nom du moteur DC
- **Référence** (obligatoire) : Référence unique du moteur DC
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le moteur DC
- **Marque** : Marque du moteur DC
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)

## Drum conveyor
Voici les paramètres à renseigner pour le drum conveyor :
- **Nom du sous-actif** (obligatoire) : Nom du drum conveyor
- **Référence** (obligatoire) : Référence unique du drum conveyor
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le drum conveyor
- **Marque** : Marque du drum conveyor
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Diameter (mm)** : Diamètre du drum conveyor (mm)

## Elevateur
Voici les paramètres à renseigner pour l'elevateur :
- **Nom du sous-actif** (obligatoire) : Nom de l'elevateur
- **Référence** (obligatoire) : Référence unique de l'elevateur
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans l'elevateur
- **Marque** : Marque de l'elevateur
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Current (A)** : Courant électrique absorbé par l'elevateur (A)
- **Voltage (V)** : Tension électrique d'alimentation (V)
- **Yield (%)** : Rendement de l'elevateur (%)
- **Input rotation speed (tr/min)** : Vitesse de rotation en entrée (tr/min)
- **Output rotation speed (tr/min)** : Vitesse de rotation en sortie (tr/min)
- **Reference** : Référence de l'elevateur

## Fan
Voici les paramètres à renseigner pour le ventilateur :
- **Nom du sous-actif** (obligatoire) : Nom du ventilateur
- **Référence** (obligatoire) : Référence unique du ventilateur
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le ventilateur
- **Marque** : Marque du ventilateur
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Yield (%)** : Rendement du ventilateur (%)
- **Number of blades** : Nombre de pales du ventilateur
- **Bearing carrier** : Support des roulements (entre paliers ou porte à faux)
- **Flow rate (m³/s)** : Débit volumétrique d'air ou de gaz déplacé (m³/s)
- **Static pressure (bar/pa)** : Pression statique générée (bar/pa)
- **Nominal pressure (m/bar)** : Pression nominale (m/bar)
- **Discharge / suction type** : Direction du flux d'air (axial or helical / radial or centrifugal / tengential)

## Gearbox with plain bearings (paliers lisses)
Voici les paramètres à renseigner pour la boîte à vitesses à paliers lisses :
- **Nom du sous-actif** (obligatoire) : Nom de la boîte à vitesses
- **Référence** (obligatoire) : Référence unique de la boîte à vitesses
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans la boîte à vitesses
- **Marque** : Marque de la boîte à vitesses
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Yield (%)** : Rendement de la boîte à vitesses (%)
- **Number of floors** : Nombre d’étages d’engrenage
- **Reducer type** : Type de réducteur
- **Gear type** : Type d'engrenage
- **Input rotation speed (tr/min)** : Vitesse de rotation de l'arbre d'entrée (tr/min)
- **Output rotation speed (tr/min)** : Vitesse de rotation de l'arbre de sortie (tr/min)

## Gearbox with rolling bearings (paliers de roulement)
Voici les paramètres à renseigner pour la boîte à vitesses à paliers de roulement :
- **Nom du sous-actif** (obligatoire) : Nom de la boîte à vitesses
- **Référence** (obligatoire) : Référence unique de la boîte à vitesses
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans la boîte à vitesses
- **Marque** : Marque de la boîte à vitesses
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Yield (%)** : Rendement de la boîte à vitesses (%)
- **Number of floors** : Nombre d’étages d’engrenage
- **Reducer type** : Type de réducteur
- **Gear type** : Type d'engrenage
- **Input rotation speed (tr/min)** : Vitesse de rotation de l'arbre d'entrée (tr/min)
- **Output rotation speed (tr/min)** : Vitesse de rotation de l'arbre de sortie (tr/min)

## Malaxeur
Voici les paramètres à renseigner pour le malaxeur :
- **Nom du sous-actif** (obligatoire) : Nom du malaxeur
- **Référence** (obligatoire) : Référence unique du malaxeur
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le malaxeur
- **Marque** : Marque du malaxeur
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Current (A)** : Courant électrique absorbé pour fonctionner (A)
- **Voltage (V)** : Tension d'alimentation (V)

## Pignon attaque
Voici les paramètres à renseigner pour le pignon attaque :
- **Nom du sous-actif** (obligatoire) : Nom du pignon attaque
- **Référence** (obligatoire) : Référence unique du pignon attaque
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le pignon attaque
- **Marque** : Marque du pignon attaque
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Current (A)** : Courant absorbé par le moteur connecté au pignon (A)
- **Module de denture** : Module de denture du pignon
- **Nombre de dents pignon** : Nombre de dents du pignon d’attaque
- **Nombre de dents roue** : Nombre de dents de la roue engrenée
- **Voltage (V)** : Tension du moteur qui entraîne le pignon (V)

## Pump with plain bearings (paliers lisses)
Voici les paramètres à renseigner pour la pompe à paliers lisses :
- **Nom du sous-actif** (obligatoire) : Nom de la pompe
- **Référence** (obligatoire) : Référence unique de la pompe
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans la pompe
- **Marque** : Marque de la pompe
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Yield (%)** : Rendement de la pompe (%)
- **Number of floors** : Nombre d’étages ou roues dans la pompe
- **Number of blades** : Nombre d’aubes dans la pompe
- **Disposition** : Orientation de la pompe (horizontal ou vertical)
- **Pump type** : Type de pompe (volumetric, centrifugal, vacuum)
- **Flow rate (m³/s)** : Débit volumétrique (m³/s)
- **HMT (m)** : Hauteur manométrique totale (m)

## Pump with rolling bearings (paliers de roulement)
Voici les paramètres à renseigner pour la pompe à paliers de roulement :
- **Nom du sous-actif** (obligatoire) : Nom de la pompe
- **Référence** (obligatoire) : Référence unique de la pompe
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans la pompe
- **Marque** : Marque de la pompe
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Yield (%)** : Rendement de la pompe (%)
- **Number of floors** : Nombre d’étages ou roues dans la pompe
- **Number of blades** : Nombre d’aubes dans la pompe
- **Disposition** : Orientation de la pompe (horizontal ou vertical)
- **Pump type** : Type de pompe (volumetric, centrifugal, vacuum)
- **Flow rate (m³/s)** : Débit volumétrique (m³/s)
- **HMT (m)** : Hauteur manométrique totale (m)

## Redler
Voici les paramètres à renseigner pour le Redler :
- **Nom du sous-actif** (obligatoire) : Nom du Redler
- **Référence** (obligatoire) : Référence unique du Redler
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le Redler
- **Marque** : Marque du Redler
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Bearing reference** : Référence des roulements utilisés (valeur possible : None)
- **Current (A)** : Courant absorbé par le moteur du Redler (A)
- **Number of floors** : Nombre d’étages
- **Gear type** : Type d'engrenage du réducteur (Helical toothing, Straight toothing, Chevron toothing)
- **Speed variator** : Indique si le moteur est équipé d'un variateur de vitesse (yes ou no)
- **Voltage (V)** : Tension d'alimentation du moteur (V)
- **Yield (%)** : Rendement du système d'entraînement (%)

## Soufflante with plain bearings (paliers lisses)
Voici les paramètres à renseigner pour la soufflante à paliers lisses :
- **Nom du sous-actif** (obligatoire) : Nom de la soufflante
- **Référence** (obligatoire) : Référence unique de la soufflante
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans la soufflante
- **Marque** : Marque de la soufflante
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Number of blades** : Nombre d’aubes ou lobes du rotor

## Soufflante with rolling bearings (paliers de roulement)
Voici les paramètres à renseigner pour la soufflante à paliers de roulement :
- **Nom du sous-actif** (obligatoire) : Nom de la soufflante
- **Référence** (obligatoire) : Référence unique de la soufflante
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans la soufflante
- **Marque** : Marque de la soufflante
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Number of blades** : Nombre d’aubes ou lobes du rotor

## Turbine
Voici les paramètres à renseigner pour la turbine :
- **Nom du sous-actif** (obligatoire) : Nom de la turbine
- **Référence** (obligatoire) : Référence unique de la turbine
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans la turbine
- **Marque** : Marque de la turbine
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Number of blades** : Nombre d’aubes dans le rotor de la turbine
- **Number of floors** : Nombre d’étages ou rangées dans la turbine
- **Bearing carrier** : Support de roulement (entre paliers ou porte à faux)
- **Steam pressure at the inlet (bar)** : Pression de la vapeur ou du gaz à l'entrée (bar)
- **Steam pressure at the outlet (bar)** : Pression de la vapeur ou du gaz à la sortie (bar)
- **Steam temperature (°C)** : Température de la vapeur ou du gaz à l'entrée (°C)
- **Yield (%)** : Rendement de la turbine (%)

## AC motor
Voici les paramètres à renseigner pour le moteur AC :
- **Nom du sous-actif** (obligatoire) : Nom du moteur AC
- **Référence** (obligatoire) : Référence unique du moteur AC
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le moteur AC
- **Marque** : Marque du moteur AC
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)
- **Current (A)** : Courant électrique absorbé par le moteur (A)
- **Speed variator** : Indique si le moteur est équipé d'un variateur de vitesse (yes ou no)
- **Voltage (V)** : Tension nominale d'alimentation (V)

## Granulateur sub asset
Voici les paramètres à renseigner pour le granulateur :
- **Nom du sous-actif** (obligatoire) : Nom du granulateur
- **Référence** (obligatoire) : Référence unique du granulateur
- **Nombre de roulements** (obligatoire) : Nombre de roulements contenus dans le granulateur
- **Marque** : Marque du granulateur
- **Puissance** : Énergie électrique consommée (Watt)
- **Vitesse** : Vitesse de rotation (préciser variable ou fixe, si variable : min et max, en RPM ou Hz)

---
## Rôle des Systèmes Externes

### MobiVib
- Outil portable (smartphone/tablette)
- Acquisition et analyse instantanée des données vibratoires
- Partage des données
- Intégré à I-SENSE

### VIBOX
- Station de surveillance en ligne
- Acquisition automatique des mesures
- Intégration avec I-SENSE

---
## FAQ

**Q : Que signifie RV ?**  
R : Radiale verticale

**Q : Que signifie RH ?**  
R : Radiale horizontale

**Q : Que signifie RO ?**  
R : Radiale oblique

**Q : Que signifie AX ?**  
R : Axiale

**Q : Quels sont les deux systèmes externes utilisés par I-SENSE ?**
R : MobiVib et Vibox

**Q : Que signifie le terme "Machine Health Index" dans I-SENSE ?**
R : Le terme "Machine Health Index" dans I-SENSE représente l'indice de santé des machines. Cet indice est calculé par l'IA de la plateforme.

**Q : Comment créer un nouvel actif ?**  
R : Voici les étapes pour créer un nouvel actif :  
1) Aller sur « Asset Manager Monitoring »  
2) Cliquer sur « Créer un nouvel actif »  
3) Entrer les informations relatives au nouvel actif (Famille, Nom de l’actif, Référence, Entité, Classe, Structure, Groupe, Puissance, Valeur aberrante, Type de point de mesure et image)

**Q : Quels sont les sous-actifs disponibles ?**
R : Les sous-actifs disponibles sont : Agitator, Alternator (plain/rolling bearings), Compressor (plain/rolling bearings), Crusher, Cylinder, DC motor, Drum conveyor, Elevateur, Fan, Gearbox (plain/rolling bearings), Malaxeur, Pignon attaque, Pump (plain/rolling bearings), Redler, Soufflante (plain/rolling bearings), Turbine, AC Motor, Granulateur-sub asset
---



