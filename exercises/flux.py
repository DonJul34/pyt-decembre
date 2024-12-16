# Demander à l'utilisateur de saisir un nombre
number = float(input("Saisissez un nombre : "))

# Utiliser if, elif, et else pour déterminer si le nombre est négatif, zéro, ou positif
if number < 0:
    print("Le nombre est négatif.")
elif number == 0:
    print("Le nombre est zéro.")
else:
    print("Le nombre est positif.")

# Boucles
# Boucle for pour afficher tous les nombres pairs entre 1 et 20
listenombre = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
print("Nombres pairs entre 1 et 20 :")
for nombre in listenombre:
    if nombre % 2 == 0:
        print(nombre)

# Boucle while qui demande à l'utilisateur un mot de passe jusqu'à ce qu'il saisisse le bon
correct_password = "python123"
password = ""
while password != correct_password:
    password = input("Saisissez le mot de passe : ")
    if password != correct_password:
        print("Mot de passe incorrect, essayez de nouveau.")

print("Mot de passe correct, accès autorisé.")

# Exceptions
# Demander à l'utilisateur de saisir un nombre pour diviser 100
try:
    divisor = float(input("Saisissez un nombre pour diviser 100 : "))
    result = 100 / divisor
    print(f"100 divisé par {divisor} est égal à {result}.")
except ValueError:
    print("Erreur : Veuillez entrer un nombre valide.")
except ZeroDivisionError:
    print("Erreur : Division par zéro impossible.")
except Exception as e:
    print(e)
