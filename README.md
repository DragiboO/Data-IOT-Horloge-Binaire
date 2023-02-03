# Projet horloge binaire
Notre équipe est composée de Théa Blachon et Julien Grenouilleau.
***
> Nous avons réalisé une horloge binaire, composée d'une Raspberry Pi Pico w qui permet la connexion à notre serveur node et traduit l'information qu'elle reçoit du serveur grâce à des fils reliés à des leds.

### Fonctionnement

- La Raspberry envoie une requête toutes les demi-secondes au serveur node sur une route / .
- Quand le serveur reçoit la requête, il renvoie les données d'une API qui permet de lire l'heure.
- La raspberry reçoit l'information qu'il convertit en binaire et affiche l'heure avec ses leds.

### Lecture de l'heure

Colonne bleue :

- Heures

Colonne verte :

- Minutes

Colonne rouge :

- Secondes

Pour chaque couleur :

- première colonne : dizaine
- deuxième colonne : unité

Exemple :

Dans la vidéo, on peut voir qu'il est 16h24 et les secondes passent de 23 à 27.

Pour les différentes colonnes, lorsque plusieurs leds s'allument, nous pouvons les additionner afin d'obtenir l'heure finale : la première led vaut 1, la deuxième vaut 2, la troisième vaut 4 et la quatrième vaut 8. Si on regarde la partie bleue (les heures), on additionne 2 et 4 et cela fait 6 il est donc bien 16h.