# admin.py

from client import Client
from category import Categorie


def creer_client(categories):
    """Crée un nouveau client avec gestion dynamique des catégories."""
    nom = input("Nom du client : ")
    email = input("Email du client : ")
    telephone = input("Téléphone du client : ")
    
    categorie_nom = input("Catégorie (SEO/Web/Autre ou une nouvelle) : ").capitalize()
    
    # Vérifier si la catégorie existe
    if categorie_nom not in categories:
        print(f"La catégorie '{categorie_nom}' n'existe pas encore.")
        try:
            prix_par_employe = float(input(f"Entrez le coût par employé pour la catégorie '{categorie_nom}' : "))
        except ValueError:
            print("Valeur invalide. Utilisation du coût par défaut (5 €).")
            prix_par_employe = 5
        
        # Ajouter la nouvelle catégorie
        nouvelle_categorie = Categorie(categorie_nom, prix_par_employe)
        categories[categorie_nom] = nouvelle_categorie
        print(f"Nouvelle catégorie '{categorie_nom}' ajoutée avec un coût par employé de {prix_par_employe} €.")
    else:
        # Récupérer le prix par employé de la catégorie existante
        prix_par_employe = categories[categorie_nom].prix_par_employe
    
    while True:
        try:
            nombre_employes = int(input("Nombre d'employés : "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    return Client(nom, email, telephone, categorie_nom, nombre_employes, prix_par_employe)

def modifier_client(client):
    """Permet de modifier les informations d'un client existant."""
    client.nom = input(f"Nouveau nom (actuel: {client.nom}) : ") or client.nom
    client.email = input(f"Nouvel email (actuel: {client.email}) : ") or client.email
    client.telephone = input(f"Nouveau téléphone (actuel: {client.telephone}) : ") or client.telephone
    client.categorie = input(f"Nouvelle catégorie (actuelle: {client.categorie}) : ").capitalize() or client.categorie
    return client

def supprimer_client(clients, nom_client):
    """Supprime un client de la liste."""
    clients = [client for client in clients if client.nom != nom_client]
    print(f"Le client {nom_client} a été supprimé.")
    return clients
