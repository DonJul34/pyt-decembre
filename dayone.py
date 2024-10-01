import csv

# CRM - Gestion des clients avec stockage dans un fichier CSV

def bienvenue():
    """Affiche un message de bienvenue"""
    print("Bienvenue dans le CRM (Customer Relationship Manager)")

def creer_client():
    """Fonction pour ajouter un nouveau client et calculer le revenu potentiel"""
    # Saisie des informations d'un client
    nom = input("Entrez le nom du client : ")
    email = input("Entrez l'email du client : ")
    telephone = input("Entrez le numéro de téléphone du client : ")

    # Saisie du nombre d'employés du client
    try:
        nombre_employes = int(input("Entrez le nombre d'employés du client : "))
    except ValueError:
        print("Veuillez entrer un nombre entier pour le nombre d'employés.")
        nombre_employes = int(input("Entrez le nombre d'employés du client : "))

    # Calcul du coût du CRM
    cout_ht = 20 + 5 * nombre_employes  # Montant Hors Taxe
    tva = 0.20  # TVA de 20%
    montant_tva = cout_ht * tva  # Montant de la TVA
    cout_ttc = cout_ht + montant_tva  # Montant Toutes Taxes Comprises

    # Retourner un dictionnaire avec les informations du client
    return {
        "nom": nom,
        "email": email,
        "telephone": telephone,
        "nombre_employes": nombre_employes,
        "cout_ht": cout_ht,
        "cout_ttc": cout_ttc
    }

def sauvegarder_client_csv(client, fichier="clients.csv"):
    """Sauvegarde un client dans un fichier CSV"""
    with open(fichier, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Écrire les informations du client dans le fichier CSV
        writer.writerow([client['nom'], client['email'], client['telephone'], client['nombre_employes'], client['cout_ht'], client['cout_ttc']])
    print(f"Client {client['nom']} sauvegardé avec succès dans le fichier CSV.")

def afficher_clients_csv(fichier="clients.csv"):
    """Affiche les clients à partir d'un fichier CSV"""
    try:
        with open(fichier, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            print("\n--- Liste des clients (CSV) ---")
            for row in reader:
                print(f"Nom: {row[0]}, Email: {row[1]}, Téléphone: {row[2]}, Nombre d'employés: {row[3]}, Coût HT: {row[4]} $, Coût TTC: {row[5]} $")
    except FileNotFoundError:
        print("Aucun fichier CSV trouvé. Veuillez ajouter des clients d'abord.")

# Point d'entrée
if __name__ == "__main__":
    bienvenue()
    clients = []  # Liste pour stocker les clients temporairement (optionnel)

    while True:
        print("\n--- Menu ---")
        print("1. Ajouter un client")
        print("2. Afficher les clients")
        print("3. Quitter")

        choix = input("Sélectionnez une option : ")

        if choix == "1":
            # Ajouter un client et sauvegarder dans CSV
            client = creer_client()
            sauvegarder_client_csv(client)
            clients.append(client)  # Optionnel, permet de garder les clients en mémoire
        elif choix == "2":
            # Afficher les clients depuis le fichier CSV
            afficher_clients_csv()
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Option non valide, veuillez réessayer.")
