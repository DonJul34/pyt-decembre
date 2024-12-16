# Chapitre 4: Opérations de Base
# Correction: Opérations de Base
# Demander à l'utilisateur de saisir deux nombres
num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le second nombre : "))

# Effectuer les opérations arithmétiques de base et afficher les résultats
addition = num1 + num2
soustraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Division par zéro impossible"

print(f"Addition : {num1} + {num2} = {addition}")
print(f"Soustraction : {num1} - {num2} = {soustraction}")
print(f"Multiplication : {num1} * {num2} = {multiplication}")
print(f"Division : {num1} / {num2} = {division}")

# Demander à l'utilisateur de saisir une chaîne et l'afficher
text = input("Saisissez un texte : ")
print(f"Le texte que vous avez saisi est : {text}")

# Utiliser les opérateurs logiques pour vérifier si le premier nombre est supérieur ou égal au second
if num1 >= num2:
    print(f"Le premier nombre ({num1}) est supérieur ou égal au second nombre ({num2}).")
else:
    print(f"Le premier nombre ({num1}) est inférieur au second nombre ({num2}).")
