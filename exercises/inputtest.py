import logging


"""
Ceci est un programme pour afficher le nom dutilsateur
Utilisant lAPI:
- OpenAI (Envirlnement variable clé)
"""

try:
    name = (input("Entrez votre nom d'utilisateur")) # Demande à l'utilisateur d'input depuis le CMDs
except:
    print("Ceci nest pas un nombre entier")

print("Bonjour, "+ name)