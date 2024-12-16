# Chapitre 3: Gestion des Collections et Conversion
# Exercice: Gestion des Collections et Conversion
# Correction:
# Étape 1: Créer une liste de nombres
numbers = [1, 2, 3, 4, 5]

# Étape 2: Ajouter un nouvel élément à la liste
numbers.append(6)

# Étape 3: Convertir la liste en un tuple
numbers_tuple = tuple(numbers)

# Étape 4: Créer un dictionnaire contenant des informations sur une personne
person_info = {
    "nom": "Alice",
    "âge": 30,
    "profession": "Développeur"
}

# Étape 5: Ajouter un set pour les compétences de cette personne
skills_set = {"Python", "JavaScript", "SQL"}
person_info["compétences"] = skills_set

# Étape 6: Imprimer toutes les informations de manière structurée
print("Liste des nombres :", numbers)
print("Tuple des nombres :", numbers_tuple)
print("\nInformations sur la personne :")
print("Nom : " + person_info['nom'] + ",  " + str(person_info['âge']) + ", " + person_info['compétences'])
print(f"Nom : {person_info['nom']} , {person_info['âge']} , {person_info['compétences']}")

print(f"Âge : {person_info['âge']}")
print(f"Profession : {person_info['profession']}")
print(f"Compétences : {', '.join(person_info['compétences'])}")
