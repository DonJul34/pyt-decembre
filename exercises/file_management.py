# Chapitre 7: Gestion des Fichiers
# Correction: Exercice de Gestion des Fichiers

# Créer un fichier et écrire dans 'journal.txt'
with open('journal.txt', 'a', encoding='utf-8') as fichier:
    entree = input("Saisissez une entrée pour le journal : ")
    fichier.write(entree + '\n')

# Lire et afficher le contenu du fichier
try:
    with open('journal.txt', 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
        print("\n--- Contenu du journal ---")
        print(contenu)
except FileNotFoundError:
    print("Le fichier 'journal.txt' n'existe pas.")
