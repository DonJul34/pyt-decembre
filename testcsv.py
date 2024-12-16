import csv
#Retourne un objet qui itère sur les lignes du fichier.

with open('fichier.csv', mode='r') as fichier:
    lecteur = csv.reader(fichier)
    for ligne in lecteur:
        print(ligne)
        
#Utilisé pour écrire des lignes dans un fichier.
    
with open('fichier.csv', mode='w', newline='') as fichier:
    ecrivain = csv.writer(fichier)
    ecrivain.writerow(['Nom', 'Âge', 'Profession'])
    ecrivain.writerow(['Alice', '30', 'Ingénieur'])
    
    
with open('fichier.csv', mode='a', newline='') as fichier:
    ecrivain.writerow({'Nom': 'Alice', 'Âge': 30, 'Profession': 'Ingénieur'})
