# Projet de Communication TCP entre ROS 2 et un Microcontrôleur via Wi-Fi

Ce projet montre comment établir une communication entre un nœud ROS 2 et un microcontrôleur via un protocole TCP sur un réseau Wi-Fi. Le client ROS 2 envoie des messages au serveur TCP sur le microcontrôleur, qui répond en confirmant la réception du message.

## Aperçu

Le projet consiste à mettre en place une communication via le protocole TCP entre :

- Un nœud ROS 2 fonctionnant sur une machine qui envoie des messages au serveur via Wi-Fi.
- Un serveur TCP fonctionnant sur un microcontrôleur compatible Wi-Fi (par exemple, un FiPy ou un autre microcontrôleur similaire), qui reçoit les messages et répond.

## Prérequis

- Un ordinateur avec ROS 2 installé (la version utilisée dépend de votre configuration, par exemple, ROS 2 iron.).
- Un microcontrôleur avec un module Wi-Fi (par exemple, FiPy).
- Une connexion Wi-Fi stable pour que les deux appareils puissent communiquer.
- Python installé sur l'ordinateur.

## Installation et Configuration

### Pour le Client ROS 2 (sur l'ordinateur)

1. Installez les dépendances ROS 2 en suivant les instructions de votre distribution ROS 2.
2. Clonez ce dépôt dans votre espace de travail ROS 2 :

    ```bash
    git clone https://github.com/99332365/Projet-de-Communication-TCP-entre-ROS-2-et-un-Microcontr-leur-via-Wi-Fi.git
    cd Projet-de-Communication-TCP-entre-ROS-2-et-un-Microcontr-leur-via-Wi-Fi
    ```

3. Compilez le package :

    ```bash
    colcon build
    ```

4. Sourcez votre espace de travail :

    ```bash
    source install/setup.bash
    ```

### Pour le Serveur TCP (sur le microcontrôleur)

1. Configurez votre microcontrôleur pour se connecter au réseau Wi-Fi. Modifiez le SSID et le mot de passe dans le fichier `server.py` :

    ```python
    ssid = 'Votre_SSID'
    password = 'Votre_Mot_de_Passe'
    ```

2. Chargez le script sur votre microcontrôleur (via Pycom ou tout autre outil de flash pour votre carte).

## Démarrage

### Serveur TCP sur le microcontrôleur

1. Allumez votre microcontrôleur et assurez-vous qu'il se connecte au réseau Wi-Fi.
2. Le serveur TCP commencera à écouter sur l'adresse IP du microcontrôleur, sur le port **1234**.

### Client TCP ROS 2

1. Après avoir compilé le package, exécutez le nœud ROS 2 qui envoie des messages au serveur TCP :

    ```bash
    ros2 run my_workspace tcp_sender_node
    ```

2. Le nœud tentera de se connecter au serveur sur l'adresse IP et le port spécifiés :
    - Adresse IP : 10.89.2.196 (celle du microcontrôleur)
    - Port : 1234

3. Une fois connecté, le nœud enverra périodiquement des messages toutes les 5 secondes au serveur TCP, qui les affichera et répondra par une confirmation.

## Structure du Projet

tcp_sender_node.py (client ROS 2) :

Ce script initialise un nœud ROS 2 nommé tcp_sender_node.
Il configure un client TCP pour se connecter à un serveur distant (le microcontrôleur) et envoie un message toutes les 5 secondes.
server.py (serveur sur le microcontrôleur) :

Ce script configure un serveur TCP qui écoute sur l'adresse IP du microcontrôleur et un port spécifique (1234).
Il attend des connexions entrantes, affiche les messages reçus et répond par une confirmation.
Détails Techniques
Client TCP (ROS 2)
Le client TCP est implémenté comme un nœud ROS 2. Voici les points clés :

Bibliothèque utilisée : rclpy pour créer le nœud ROS 2 et socket pour établir une connexion TCP.
Périodicité : Le client envoie des messages toutes les 5 secondes grâce à un timer ROS 2.
Fonctionnement :
Le client tente de se connecter au serveur TCP avec l'adresse IP et le port spécifiés.
Si la connexion est réussie, un message est envoyé périodiquement au serveur.
Serveur TCP (microcontrôleur)
Le serveur TCP fonctionne sur le microcontrôleur et écoute les connexions des clients.

Connexion Wi-Fi : Le script connecte d'abord le microcontrôleur à un réseau Wi-Fi.
Écoute TCP : Une fois connecté au réseau, il attend les connexions sur un port (1234) et affiche les messages reçus.
Réponse : Après avoir reçu un message, il renvoie un accusé de réception au client.
Auteur
Samar Rezgui
GitHub : 99332365
