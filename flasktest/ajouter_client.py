from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Client
import logging
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'votre_cle_secrete'  # Remplacez par une clé secrète réelle

db.init_app(app)

# Configurer le logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
)
logger = logging.getLogger(__name__)

# Créer les tables au démarrage de l'application
with app.app_context():
    db.create_all()
    logger.info("Base de données initialisée.")

@app.route('/')
def index():
    logger.info("Accès à la page d'ajout de client.")
    return render_template('ajouter_client.html')

@app.route('/ajouter', methods=['POST'])
def ajouter():
    try:
        nom = request.form['nom']
        email = request.form['email']
        telephone = request.form['telephone']
        categorie = request.form['categorie']
        nombre_employes = int(request.form['nombre_employes'])

        logger.info(f"Récupération des données du formulaire : {nom}, {email}, {telephone}, {categorie}, {nombre_employes}")

        # Vérifier si l'email existe déjà
        if Client.query.filter_by(email=email).first():
            logger.warning(f"Tentative d'ajout d'un client avec un email existant : {email}")
            flash('Un client avec cet email existe déjà.', 'error')
            return redirect(url_for('index'))

        # Créer un nouvel objet Client
        nouveau_client = Client(
            nom=nom,
            email=email,
            telephone=telephone,
            categorie=categorie,
            nombre_employes=nombre_employes
        )

        # Ajouter à la base de données
        db.session.add(nouveau_client)
        db.session.commit()

        logger.info(f"Client ajouté avec succès : {nouveau_client}")
        flash('Client ajouté avec succès !', 'success')
        return redirect(url_for('index'))

    except Exception as e:
        logger.error(f"Erreur lors de l'ajout du client : {e}")
        flash('Une erreur est survenue lors de l\'ajout du client.', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    # S'assurer que le fichier des logs existe
    if not os.path.exists('app.log'):
        open('app.log', 'a').close()
    app.run(debug=True)
