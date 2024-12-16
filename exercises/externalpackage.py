import requests

# Effectuer une requête GET sur une API publique
response = requests.get('https://api.github.com')
if response.status_code == 200:
    print("Requête réussie !")
    print(response.json())
else:
    print(f"Échec de la requête. Statut : {response.status_code}")
