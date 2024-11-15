import json

# Charger le fichier JSON existant
with open('resultats.json', 'r', encoding='utf-8') as f:
    produits = json.load(f)

# Liste pour stocker les informations extraites
produits_info = []

# Parcourir chaque produit dans le fichier JSON
for produit in produits:
    # Extraire les informations de base
    product_code = produit.get('code', 'Non spécifié')
    product_name = produit.get('name', 'Non spécifié')
    in_stock = produit.get("stock", {}).get("stockLevelStatus")
    category_hierarchy = produit.get('categoryNameHierarchy', 'Non spécifiée')
    ean = produit.get('ean', 'Non spécifié')
    sku = produit.get('defaultSku', 'Non spécifié')
    
    # Extraire le prix
    price_value = produit.get('price', {}).get('value', 'Non spécifié')

    # Extraire la taille 
    size_value = produit.get("size")

    # Extraire la marque
    brand_name = produit.get('masterBrand', {}).get('name', 'Non spécifiée')
    

    # Ajouter les informations extraites à la liste
    produit_info = {
        "Product Code": product_code,
        "Name": product_name,
        "Brand": brand_name, 
        "Category Hierarchy": category_hierarchy,
        "Stock": in_stock,
        "Price": price_value,
        "Size":size_value,
        "EAN": ean, #code barre 
        "SKU": sku, #ID 
    }
   
    produits_info.append(produit_info)

# Sauvegarder les résultats dans un fichier JSON - encoding = encodage du site différent 
with open('products_info.json', 'w', encoding='utf-8') as f:
    json.dump(produits_info, f, ensure_ascii=False, indent=4)

print("Les informations des produits ont été enregistrées dans 'produits_info.json'.")
