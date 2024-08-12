from machine import Pin
import network
import socket
import time
from network import WLAN

ssid = 'IoT IMT Nord Europe'
password = '72Hin@R*'

# Configuration du réseau Wi-Fi
def configurer_reseau():
    # Initialise l'interface Wi-Fi en mode station
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(ssid, auth=(WLAN.WPA2, password))

    # Attendez la connexion
    while not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        time.sleep(1)

    print('Connected to Wi-Fi')
    print('IP Address:', wlan.ifconfig()[0])

# Fonction pour gérer les connexions TCP et recevoir des messages
def serveur_tcp():
    wlan = WLAN(mode=WLAN.STA)
    addr = wlan.ifconfig()[0]  # Utilisez l'adresse IP configurée pour le serveur
    port = 1234  # Le même port que celui utilisé par le client TCP

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((addr, port))
    s.listen(1)

    print('Serveur TCP en écoute sur {addr}:{port}')

    while True:
        conn, _ = s.accept()
        print('Connexion acceptée')

        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break
                print('Message reçu:', data)

                # Répondre au message reçu
                conn.send('Message reçu\n'.encode())

            except OSError as e:
                print('Erreur de connexion:', e)
                break

        conn.close()
        print('Connexion fermée')

# Exécution des fonctions
configurer_reseau()
serveur_tcp()
