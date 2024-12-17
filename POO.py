# Classe Livre
class Livre:
    def __init__(self, titre, auteur, annee, genre):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre

    def __str__(self):
        return f"{self.titre} (Auteur: {self.auteur}, Année: {self.annee}, Genre: {self.genre})"


# Classe Bibliothèque
class Bibliotheque:
    def __init__(self, nom, adresse):
        self.livres = []  # Liste pour stocker les objets Livre
        self.nom = nom
        self.adresse = adresse
    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre ajouté : {livre}")

    def supprimer_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                self.livres.remove(livre)
                print(f"Livre supprimé : {titre}")
                return
        print(f"Livre non trouvé : {titre}")

    def lister_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            print("\nListe des livres dans la bibliothèque :")
            for livre in self.livres:
                print(livre)

    def rechercher_par_auteur(self, auteur):
        livres_auteur = [livre for livre in self.livres if livre.auteur == auteur]
        if livres_auteur:
            print(f"\nLivres de l'auteur '{auteur}' :")
            for livre in livres_auteur:
                print(livre)
        else:
            print(f"Aucun livre trouvé pour l'auteur '{auteur}'.")


# Fonction de test du programme
def test_bibliotheque():
    # Créer une instance de la bibliothèque
    ma_bibliotheque = Bibliotheque()

    # Ajouter des livres
    livre1 = Livre("1984", "George Orwell", 1949, "Dystopie")
    livre2 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954, "Fantasy")
    livre3 = Livre("Harry Potter à l'école des sorciers", "J.K. Rowling", 1997, "Fantasy")

    ma_bibliotheque.ajouter_livre(livre1)
    ma_bibliotheque.ajouter_livre(livre2)
    ma_bibliotheque.ajouter_livre(livre3)

    # Lister les livres
    ma_bibliotheque.lister_livres()

    # Rechercher des livres par auteur
    ma_bibliotheque.rechercher_par_auteur("J.R.R. Tolkien")
    ma_bibliotheque.rechercher_par_auteur("George Orwell")

    # Supprimer un livre
    ma_bibliotheque.supprimer_livre("1984")

    # Lister les livres après suppression
    ma_bibliotheque.lister_livres()

    # Essayer de supprimer un livre qui n'existe pas
    ma_bibliotheque.supprimer_livre("1984")

    # Rechercher par auteur sans résultat
    ma_bibliotheque.rechercher_par_auteur("Inconnu")


# Exécution du programme de test
test_bibliotheque()