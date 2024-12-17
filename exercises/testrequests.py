import requests

# Effectuer une requête GET sur une API publique
response = requests.get('https://api.github.com/EAZEAZEZAEAZ')
if response.status_code == 200:
    print("Requête réussie !")
    print(response.json())
    print(response.status_code)
else:
    print(f"Échec de la requête. Statut : {response.status_code}")
