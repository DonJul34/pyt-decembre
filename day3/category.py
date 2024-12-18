class Categorie:
    """Classe représentant une catégorie avec un prix par employé."""
    
    def __init__(self, nom, prix_par_employe):
        self.nom = nom
        self.prix_par_employe = prix_par_employe
    
    def __str__(self):
        return f"Catégorie: {self.nom}, Prix par employé: {self.prix_par_employe} €"
