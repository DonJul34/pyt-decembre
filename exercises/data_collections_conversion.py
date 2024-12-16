# Chapitre 3: Gestion des Collections et Conversion
# Exercice: Gestion des Collections et Conversion
# Correction:
# Étape 1: Créer une liste de nombres
numbers = [1, 2, 2, 4, 5]

# Étape 2: Ajouter un nouvel élément à la liste
numbers.append(6)

# Étape 3: Convertir la liste en un tuple
nombre_set = set(numbers)
print(nombre_set)
# Étape 4: Créer un dictionnaire contenant des informations sur une personne
persons_info = [{
    "nom": "Alice",
    "âge": 30,
    "profession": "Développeur",
    "HasPayedScolarship" : True
},
{
    "nom": "Jean",
    "âge": 30,
    "profession": "Développeur",
    "HasPayedScolarship" : True
},
]
x = 0
for person in persons_info:
    print("Nous sommes actuellement dans le dictionnaire utilisateur n°"+ str(x))
    x+=1
    print(person["nom"])



# Étape 5: Ajouter un set pour les compétences de cette personne
skills_set = {"Python", "JavaScript", "SQL"}