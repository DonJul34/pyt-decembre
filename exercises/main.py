# main.py

from mon_calculateur import operations

# Utilisation des fonctions du module
a, b = 10, 5
print(f"Addition : {operations.addition(a, b)}")        # Affiche 15
print(f"Soustraction : {operations.soustraction(a, b)}")  # Affiche 5
print(f"Multiplication : {operations.multiplication(a, b)}")  # Affiche 50
print(f"Division : {operations.division(a, b)}")          # Affiche 2.0
