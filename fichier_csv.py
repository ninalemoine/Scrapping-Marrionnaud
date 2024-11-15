import json
import csv

# Charger le fichier JSON
with open('products_info.json', 'r') as f:
    data = json.load(f)

# Ouvrir un fichier CSV pour écrire les données
with open('parfums_info_marketplace.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Extraire les en-têtes
    headers = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    
    # Écrire les en-têtes et les données
    writer.writeheader()
    writer.writerows(data)

print("Les données ont été exportées avec succès vers un fichier CSV.")
