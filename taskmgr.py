import os

# Nom du fichier pour stocker les tâches
fichier_taches = "taches.txt"

# Liste pour stocker les tâches
taches = []

# Fonction pour charger les tâches depuis le fichier
def charger_taches():
    if os.path.exists(fichier_taches):
        with open(fichier_taches, "r") as fichier:
            for ligne in fichier:
                taches.append(ligne.strip())

# Fonction pour sauvegarder les tâches dans le fichier
def sauvegarder_taches():
    with open(fichier_taches, "w") as fichier:
        for tache in taches:
            fichier.write(tache + "\n")

# Fonction pour ajouter une tâche
def ajouter_tache(tache):
    taches.append(tache)
    sauvegarder_taches()
    print(f"Tâche '{tache}' ajoutée.")

# Fonction pour supprimer une tâche
def supprimer_tache(tache):
    if tache in taches:
        taches.remove(tache)
        sauvegarder_taches()
        print(f"Tâche '{tache}' supprimée.")
    else:
        print(f"Tâche '{tache}' non trouvée.")

# Fonction pour afficher les tâches
def afficher_taches():
    if taches:
        print("Liste des tâches :")
        for i, tache in enumerate(taches, 1):
            print(f"{i}. {tache}")
    else:
        print("Aucune tâche à afficher.")

# Charger les tâches au démarrage du programme
charger_taches()

# Interface utilisateur simple
while True:
    print("\nGestionnaire de tâches")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Afficher les tâches")
    print("4. Quitter")
    
    choix = input("Choisissez une option : ")
    
    if choix == '1':
        tache = input("Entrez la tâche à ajouter : ")
        ajouter_tache(tache)
    elif choix == '2':
        tache = input("Entrez la tâche à supprimer : ")
        supprimer_tache(tache)
    elif choix == '3':
        afficher_taches()
    elif choix == '4':
        print("Au revoir !")
        break
    else:
        print("Option invalide, veuillez réessayer.")