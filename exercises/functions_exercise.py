# Chapitre 6: Création de Fonctions
# Correction: Exercice de Fonctions

# Fonction calculer_facture
def calculer_facture(prix, quantite, taux_tva=1.20):
    """Calcule le montant total TTC."""
    montant_ttc = prix * quantite * taux_tva
    return montant_ttc

# Exemple d'utilisation
facture = calculer_facture(100, 5)
print(f"Montant total TTC : {facture} €")

# Fonction rechercher_client
def rechercher_client(**client):
    """Affiche les informations du client."""
    print("\n--- Informations du client ---")
    for cle, valeur in client.items():
        print(f"{cle.capitalize()} : {valeur}")

# Exemple d'utilisation
rechercher_client(nom="Alice", email="alice@example.com", telephone="123456789")

# Fonction anonyme lambda
produit = lambda x, y: x * y

# Exemple d'utilisation
resultat = produit(4, 5)
print(f"Le produit des deux nombres est : {resultat}")
