import sqlite3

# Gestion de la base de données SQLite
def creer_table_clients():
    """Crée la table des clients dans la base de données."""
    connection = sqlite3.connect('crm.db')
    cursor = connection.cursor()
    
    # Création de la table si elle n'existe pas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            email TEXT,
            telephone TEXT,
            categorie TEXT,
            nombre_employes INTEGER,
            prix_par_employe REAL,
            cout_ht REAL,
            cout_ttc REAL
        )
    ''')
    connection.commit()
    connection.close()

def ajouter_client_bd(client):
    """Ajoute un client à la base de données."""
    connection = sqlite3.connect('crm.db')
    cursor = connection.cursor()
    
    cursor.execute('''
        INSERT INTO clients (nom, email, telephone, categorie, nombre_employes, prix_par_employe, cout_ht, cout_ttc)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (client.nom, client.email, client.telephone, client.categorie, client.nombre_employes, client.prix_par_employe, client.cout_ht, client.cout_ttc))
    
    connection.commit()
    connection.close()

def recuperer_clients_bd():
    """Récupère tous les clients depuis la base de données."""
    connection = sqlite3.connect('crm.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM clients')
    clients = cursor.fetchall()
    
    connection.close()
    return clients