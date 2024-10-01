import csv
import os

# CRM - Gestion des clients avec stockage dans un fichier CSV et tarification par catégorie

def bienvenue():
    """Affiche un message de bienvenue"""
    print("Bienvenue dans le CRM (Customer Relationship Manager)")

def creer_client(nombre_employes=1):
    """Fonction pour ajouter un nouveau client avec un paramètre par défaut pour le nombre d'employés"""
    # Saisie des informations d'un client
    nom = input("Entrez le nom du client : ")
    email = input("Entrez l'email du client : ")
    telephone = input("Entrez le numéro de téléphone du client : ")
    
    # Saisie de la catégorie du client
    print("\nCatégories disponibles : SEO, Web, Autre")
    categorie = input("Entrez la catégorie du client (SEO/Web/Autre) : ").strip().lower()
    
    # Tarification dynamique selon la catégorie
    if categorie == "seo" or categorie == "web":
        prix_par_employe = 7
    else:
        prix_par_employe = 5
    
    # Saisie du nombre d'employés du client avec gestion des erreurs
    while True:
        try:
            nombre_employes = int(input("Entrez le nombre d'employés du client : "))
            if nombre_employes < 0:
                raise ValueError("Le nombre d'employés ne peut pas être négatif.")
            break
        except ValueError as e:
            print(f"Erreur : {e}. Veuillez entrer un nombre valide.")

    # Calcul du coût du CRM
    cout_ht = 20 + prix_par_employe * nombre_employes  # Montant Hors Taxe
    tva = 0.20  # TVA de 20%
    montant_tva = cout_ht * tva  # Montant de la TVA
    cout_ttc = cout_ht + montant_tva  # Montant Toutes Taxes Comprises

    # Retourner un dictionnaire avec les informations du client
    return {
        "nom": nom,
        "email": email,
        "telephone": telephone,
        "categorie": categorie.capitalize(),
        "nombre_employes": nombre_employes,
        "prix_par_employe": prix_par_employe,
        "cout_ht": cout_ht,
        "cout_ttc": cout_ttc
    }

def sauvegarder_client_csv(client, fichier="clients.csv"):
    """Sauvegarde un client dans un fichier CSV avec gestion des erreurs"""
    try:
        with open(fichier, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Écrire les informations du client dans le fichier CSV
            writer.writerow([client['nom'], client['email'], client['telephone'], client['categorie'], client['nombre_employes'], client['prix_par_employe'], client['cout_ht'], client['cout_ttc']])
        print(f"Client {client['nom']} sauvegardé avec succès dans le fichier CSV.")
    except IOError as e:
        print(f"Erreur lors de la sauvegarde du client : {e}")

def afficher_clients_csv(fichier="clients.csv"):
    """Affiche les clients à partir d'un fichier CSV avec gestion des exceptions"""
    if not os.path.exists(fichier):
        print("Le fichier CSV n'existe pas. Veuillez ajouter des clients.")
        return
    
    try:
        with open(fichier, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            print("\n--- Liste des clients (CSV) ---")
            for row in reader:
                print(f"Nom: {row[0]}, Email: {row[1]}, Téléphone: {row[2]}, Catégorie: {row[3]}, Nombre d'employés: {row[4]}, Prix par employé: {row[5]} €, Coût HT: {row[6]} $, Coût TTC: {row[7]} $")
    except FileNotFoundError:
        print("Aucun fichier CSV trouvé. Veuillez ajouter des clients d'abord.")
    except csv.Error as e:
        print(f"Erreur lors de la lecture du fichier CSV : {e}")

def modifier_client(fichier="clients.csv"):
    """Permet de modifier les informations d'un client dans le fichier CSV"""
    afficher_clients_csv(fichier)
    client_index = int(input("Entrez le numéro du client à modifier : ")) - 1
    clients = lire_clients_csv(fichier)
    
    if 0 <= client_index < len(clients):
        nom = input(f"Entrez le nouveau nom (actuel: {clients[client_index]['nom']}) : ") or clients[client_index]['nom']
        email = input(f"Entrez le nouvel email (actuel: {clients[client_index]['email']}) : ") or clients[client_index]['email']
        telephone = input(f"Entrez le nouveau téléphone (actuel: {clients[client_index]['telephone']}) : ") or clients[client_index]['telephone']
        categorie = input(f"Entrez la nouvelle catégorie (actuelle: {clients[client_index]['categorie']}) : ") or clients[client_index]['categorie']
        
        # Ajuster le prix par employé si la catégorie a changé
        prix_par_employe = 7 if categorie.lower() in ["seo", "web"] else 5
        
        # Modifier le client dans la liste
        clients[client_index] = {
            "nom": nom,
            "email": email,
            "telephone": telephone,
            "categorie": categorie.capitalize(),
            "nombre_employes": clients[client_index]["nombre_employes"],
            "prix_par_employe": prix_par_employe,
            "cout_ht": clients[client_index]["cout_ht"],
            "cout_ttc": clients[client_index]["cout_ttc"]
        }

        # Sauvegarder la liste mise à jour
        sauvegarder_clients_csv(clients, fichier)

def sauvegarder_clients_csv(clients, fichier="clients.csv"):
    """Sauvegarde la liste des clients dans un fichier CSV"""
    try:
        with open(fichier, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for client in clients:
                writer.writerow([client['nom'], client['email'], client['telephone'], client['categorie'], client['nombre_employes'], client['prix_par_employe'], client['cout_ht'], client['cout_ttc']])
        print("Clients sauvegardés avec succès.")
    except IOError as e:
        print(f"Erreur lors de la sauvegarde des clients : {e}")

def lire_clients_csv(fichier="clients.csv"):
    """Lit la liste des clients depuis un fichier CSV"""
    clients = []
    if os.path.exists(fichier):
        with open(fichier, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file, fieldnames=["nom", "email", "telephone", "categorie", "nombre_employes", "prix_par_employe", "cout_ht", "cout_ttc"])
            clients = list(reader)
    return clients

# Point d'entrée
if __name__ == "__main__":
    bienvenue()
    
    while True:
        print("\n--- Menu ---")
        print("1. Ajouter un client")
        print("2. Afficher les clients")
        print("3. Modifier un client")
        print("4. Quitter")

        choix = input("Sélectionnez une option : ")

        if choix == "1":
            client = creer_client()
            sauvegarder_client_csv(client)
        elif choix == "2":
            afficher_clients_csv()
        elif choix == "3":
            modifier_client()
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Option non valide, veuillez réessayer.")
