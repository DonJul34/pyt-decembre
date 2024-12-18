from flask import Flask, request, jsonify
import logging
import sqlite3
from flask_cors import CORS


# Initialisation de l'application Flask
app = Flask(__name__)
CORS(app)  # Autorise les requêtes CORS pour toutes les routes

# Configuration du module logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='app.log',
                    filemode='a')

# Configuration de la base de données CRM
DATABASE = 'crm.db'

def init_db():
    """Initialise la base de données CRM."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nom TEXT NOT NULL,
                        email TEXT NOT NULL,
                        telephone TEXT NOT NULL,
                        categorie TEXT NOT NULL,
                        nb_employes INTEGER NOT NULL
                      )''')
    conn.commit()
    conn.close()

# Initialisation de la base de données
init_db()

@app.route('/ajouter_client', methods=['POST'])
def ajouter_client():
    """Ajoute un client à la base de données."""
    try:
        # Récupérer les données du formulaire envoyées via JS
        data = request.json
        nom = data.get('nom')
        email = data.get('email')
        telephone = data.get('telephone')
        categorie = data.get('categorie')
        nb_employes = data.get('nb_employes')

        # Validation des données
        if not all([nom, email, telephone, categorie, nb_employes]):
            logging.warning("Données manquantes dans la requête.")
            return jsonify({"message": "Tous les champs sont obligatoires."}), 400

        # Ajout du client dans la base de données
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        try:
            cursor.execute('''INSERT INTO clients (nom, email, telephone, categorie, nb_employes)
                            VALUES (?, ?, ?, ?, ?)''',
                        (nom, email, telephone, categorie, nb_employes))
            conn.commit()

        except Exception as e:
            logging.critical("Critical error while SQL request insert client " + e)
        finally:
            conn.close()

        logging.info(f"Client ajouté : {nom}, {email}")
        return jsonify({"message": "Client ajouté avec succès."}), 201

    except Exception as e:
        logging.error(f"Erreur lors de l'ajout du client : {e}")
        return jsonify({"message": "Erreur interne du serveur."}), 500


@app.route('/clients', methods=['GET'])
def lister_clients():
    """Liste tous les clients dans la base de données."""
    try:
        logging.info("Appel de la route /clients")
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM clients''')
        clients = cursor.fetchall()
        conn.close()

        # Transformer les résultats en une liste de dictionnaires
        clients_list = [
            {
                "id": client[0],
                "nom": client[1],
                "email": client[2],
                "telephone": client[3],
                "categorie": client[4],
                "nb_employes": client[5]
            } for client in clients
        ]

        logging.info("Liste des clients récupérée avec succès.")
        return jsonify(clients_list), 200

    except Exception as e:
        logging.error(f"Erreur lors de la récupération des clients : {e}")
        return jsonify({"message": "Erreur interne du serveur."}), 500

if __name__ == '__main__':
    app.run(debug=True)