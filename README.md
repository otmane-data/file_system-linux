
# 🗃️ ID1FS - Système de Fichiers Linux Simulé en Python

Un projet éducatif pour simuler le fonctionnement d’un système de fichiers Linux, entièrement implémenté en **Python** sous **Ubuntu**. Il permet de gérer des **utilisateurs**, **fichiers**, et **répertoires** avec des commandes en ligne de commande comme sous Linux.

---

## 🧰 Structure du Projet

```
📁 ID1FS/
 ┣ 📂 bin/         → Scripts et commandes exécutables
 ┣ 📂 home/        → Répertoires personnels des utilisateurs
 ┣ 📂 managers/    → Gestionnaires internes du système
 ┗ 📂 rapp/        → Documentation, rapports et logs
```

---

## ⚙️ Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/<votre-utilisateur>/ID1FS.git
   cd ID1FS
   ```

2. Assurez-vous que Python 3 est installé :
   ```bash
   python3 --version
   ```

3. Configurez le fichier `bin/config.ini` pour définir le chemin d’installation

4. Exécutez les scripts depuis le dossier `bin/` :
   ```bash
   cd bin
   python3 add.py
   ```

---

## 🔐 Fonctionnalités

### 👤 Gestion des Utilisateurs
- Création de comptes avec mot de passe (hashé en SHA-512)
- Authentification sécurisée
- Suivi des connexions (sessions actives)

### 📄 Gestion des Fichiers
- Création et suppression de fichiers
- Affichage du contenu (`open`)
- Modification de fichiers (`edit`)
- Listing des fichiers (`list`)

---

## 💻 Commandes Disponibles

| Commande     | Description                      | Exemple                             |
|--------------|----------------------------------|--------------------------------------|
| `add.py`     | Ajouter un nouvel utilisateur    | `python3 add.py`                     |
| `connect`    | Connexion à un compte utilisateur| `./connect -u alice`                 |
| `create`     | Créer un fichier                 | `./create -f note.txt`              |
| `delete`     | Supprimer un fichier             | `./create -d -f note.txt`           |
| `list`       | Lister les fichiers              | `./create -l`                        |
| `open`       | Ouvrir un fichier                | `./open note.txt`                   |
| `edit`       | Modifier un fichier              | `./edit note.txt`                   |
| `end`        | Déconnexion                      | `./end`                              |

---

## 🛡️ Sécurité

- Mots de passe stockés via **hashage SHA-512**
- Historique des actions via **système de journalisation**
- Isolation des utilisateurs dans des répertoires personnels

---

## 🧱 Architecture du Système

- **Gestionnaire d'utilisateurs** : Création, login, sessions
- **Gestionnaire de fichiers** : Opérations CRUD sur les fichiers
- **Sessions** : Suivi des connexions utilisateur
- **Logs** : Trace des opérations pour audit et sécurité

---

## 🎓 Objectif Pédagogique

Ce projet simule un environnement Linux de manière simplifiée pour :
- Comprendre le fonctionnement d’un système de fichiers
- S’exercer à la gestion d’utilisateurs et de droits
- Maîtriser les bases de la programmation système en Python

---

## 👥 Auteurs

- [Votre Nom / Équipe]

---

## 📄 Licence

Projet sous licence **MIT**.

---

