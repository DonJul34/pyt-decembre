# Classe Livre
class Livre:
    def __init__(self, titre, auteur, annee, genre):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre

    def __str__(self):
        return f"{self.titre} (Auteur: {self.auteur}, Année: {self.annee}, Genre: {self.genre})"

# Sous-classes pour différents types de livres
class Roman(Livre):
    def __init__(self, titre, auteur, annee, genre, nombre_pages):
        super().__init__(titre, auteur, annee, genre)
        self.nombre_pages = nombre_pages
    def __str__(self):
        return f"{self.titre} (Roman, Auteur: {self.auteur}, Année: {self.annee}, Pages: {self.nombre_pages})"

class Revue(Livre):
    def __init__(self, titre, auteur, annee, genre, numero_edition):
        super().__init__(titre, auteur, annee, genre)
        self.numero_edition = numero_edition
    def __str__(self):
        return f"{self.titre} (Revue, Auteur: {self.auteur}, Année: {self.annee}, Edition: {self.numero_edition})"

class Manga(Livre):
    def __init__(self, titre, auteur, annee, genre, volume, illustrator):
        super().__init__(titre, auteur, annee, genre)
        self.volume = volume
        self.illustrator = illustrator

    def __str__(self):
        return f"{self.titre} (Manga, Auteur: {self.auteur}, Année: {self.annee}, Volume: {self.volume}, Illustrateur : {self.illustrator})"

class Encyclopedie(Livre):
    def __init__(self, titre, auteur, annee, genre, domaine):
        super().__init__(titre, auteur, annee, genre)
        self.domaine = domaine

    def __str__(self):
        return f"{self.titre} (Encyclopédie, Auteur: {self.auteur}, Année: {self.annee}, Domaine: {self.domaine})"

class Biographie(Livre):
    def __init__(self, titre, auteur, annee, genre, sujet):
        super().__init__(titre, auteur, annee, genre)
        self.sujet = sujet

    def __str__(self):
        return f"{self.titre} (Biographie, Auteur: {self.auteur}, Année: {self.annee}, Sujet: {self.sujet})"

# Classe Bibliothèque
class Bibliotheque:
    def __init__(self, nom, adresse):
        self.livres = []  # Liste pour stocker les objets Livre
        self.nom = nom
        self.adresse = adresse
    
    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livres ajouté : {livre}")


    def ajouter_livres(self, livres):
        for livre in livres :
            self.livres.append(livre)
            print(f"Livres ajouté : {livre}")

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

# Créer une instance de la bibliothèque
ma_bibliotheque = Bibliotheque("Municipale Brest","6 rue des chats")

# Ajouter des livres
livre1 = Livre("1985", "George Orwell", 1949, "Dystopie")
roman1 = Roman("1984", "George Orwell", 1949, "Dystopie", 328)
roman2 = Roman("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954, "Fantasy", 1200)
manga1 = Manga("Naruto", "Masashi Kishimoto", 1999, "Shonen", 1,"Masashi Kishimoto")
revue1 = Revue("National Geographic", "Divers", 2023, "Science", 215)
encyclo1 = Encyclopedie("Encyclopédie de l'Univers", "Carl Sagan", 1980, "Science", "Astronomie")
biographie1 = Biographie("Steve Jobs", "Walter Isaacson", 2011, "Biographie", "Steve Jobs")
liste_livre = [livre1,roman1,roman2,manga1,revue1,encyclo1,biographie1]

ma_bibliotheque.ajouter_livres(liste_livre)
# Ajouter les livres à la bibliothèque

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