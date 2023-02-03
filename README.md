# Projet horloge binaire
Notre équipe est composée de Théa Blachon et Julien Grenouilleau.
***
> Nous avons réalisé une horloge binaire, composée d'une Raspberry Pi Pico w qui permet la connexion à notre serveur node et traduit l'information qu'elle reçoit du serveur grâce à des fils reliés à des leds.

### Fonctionnement

- La Raspberry envoie une requête toutes les demi-secondes au serveur node sur une route / .
- Quand le serveur reçoit la requête, il renvoie les données d'une API qui permet de lire l'heure.
- La raspberry reçoit l'information qu'il convertit en binaire et affiche l'heure avec ses leds.