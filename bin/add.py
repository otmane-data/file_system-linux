#!/bin/python3
import os
import hashlib
import getpass

def create_user():
    # Demander le nom d'utilisateur
    username = input("Entrez le nom d'utilisateur: ")

    # Demander le mot de passe (le mot de passe ne sera pas affiché pendant la saisie)
    password = getpass.getpass("Entrez le mot de passe: ")

    # Utiliser hashlib pour hacher le mot de passe avec SHA-512
    hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()

    # Demander le commentaire (description)
    comment = input("Entrez le commentaire (optionnel): ")

    # Construire la commande pour créer l'utilisateur avec le commentaire
    useradd_command = f"sudo useradd -m -c '{comment}' {username}"

    # Exécuter la commande pour créer l'utilisateur
    os.system(useradd_command)

    # Écrire les informations dans le fichier hache.txt
    with open('/home/mouad/ID1FS/managers/hache.txt', 'a') as hache_file:
        hache_file.write(f"{username}:{hashed_password}\n")

    print(f"L'utilisateur {username} a été créé avec succès.")

if __name__ == "__main__":
    create_user()
