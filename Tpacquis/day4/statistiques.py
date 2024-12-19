# statistiques.py

def calculer_chiffre_affaire_total(clients):
    """Calcule le chiffre d'affaires total généré par tous les clients."""
    total = sum(client.calculer_chiffre_affaire() for client in clients)
    return total

def clients_par_categorie(clients):
    """Compte le nombre de clients dans chaque catégorie."""
    categories = {}
    for client in clients:
        if client.categorie in categories:
            categories[client.categorie] += 1
        else:
            categories[client.categorie] = 1
    return categories

def afficher_statistiques(clients):
    """Affiche des statistiques générales sur les clients."""
    print("\n--- Statistiques CRM ---")
    print(f"Nombre total de clients : {len(clients)}")
    
    chiffre_affaire = calculer_chiffre_affaire_total(clients)
    print(f"Chiffre d'affaires total : {chiffre_affaire:.2f} €")
    
    categories = clients_par_categorie(clients)
    print("Nombre de clients par catégorie :")
    for categorie, count in categories.items():
        print(f"{categorie} : {count} clients")

try:
    nom = form.getvalue('nom', 'Inconnu')
except Exception as e:
    print(f"<p>Erreur : {e}</p>")
import os

# Obtenir le répertoire de travail courant
repertoire_actuel = os.getcwd()
print(f"Répertoire actuel : {repertoire_actuel}")

import shutil
import os

# Créer une arborescence de dossiers pour l'exemple
os.mkdir('source_dossier')
with open('source_dossier/fichier.txt', 'w') as f:
    f.write("Contenu de fichier source.")

# Copier un répertoire et tout son contenu
source = 'source_dossier'
destination = 'backup_dossier'
try:
    shutil.copytree(source, destination)
    print(f"'{source}' copié vers '{destination}'.")
except FileExistsError:
    print(f"Erreur : Le dossier '{destination}' existe déjà.")

with open('exemple.txt', 'w') as fichier:
    fichier.write('Hello, world!')

import tkinter as tk

def on_click(event):
    print(f"Clic détecté à la position : {event.x}, {event.y}")

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.bind("<Button-1>", on_click)  # Lier l'événement clic gauche de la souris
canvas.pack()

root.mainloop()
