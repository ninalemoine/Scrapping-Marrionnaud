# Scrapping-Marrionnaud
Scrapping du site Marrionnaud pour une analyse des parfums pour femmes 

# Projet Python Scraping : Marionnaud

## Introduction

Ce projet vise à extraire des informations pertinentes sur les parfums pour femmes disponibles sur le site de **Marionnaud**. Il s'agit d'un projet éducatif dans lequel nous utilisons le scraping web et l'analyse de données pour comprendre la structure des données produits, automatiser leur extraction, et les organiser de manière structurée.
Les données exploitées sont sous format JSON et CSV.

---

## Objectif

L'objectif principal est d'extraire et d'analyser principalement les informations des parfums dans les catégories suivantes :  
- **Eaux de parfum**  
- **Eaux de toilette**  
- **Eaux de cologne**

### Données collectées par produit :
- **Catégorie** : eau de parfum, eau de toilette, eau de cologne  
- **Marque** : exemple "Chanel"  
- **Nom du parfum** : exemple "Coco Mademoiselle"  
- **Quantité** : exemple "50 ml"  
- **Prix** : exemple "99,00 €"*
- **Stock** : exemple "Instock"

---

## Étapes principales

### Étape 1 : Récupération des liens de pages
- Parcourir les pages de la catégorie principale et générer une liste comprenant les informations de chaque page contenant les produits sous format JSON.

### Étape 2 : Extraction des données des parfums
- Filtrer et récupérer uniquement les données des produits correspondant aux catégories d'intérêt.

### Étape 3 : Collecte des informations
- Extraire les informations détaillées des produits et les structurer dans un format CSV pour analyse.

---

## Fichiers générés

- **`resultats.json`** : Contient les informations de chaque page de produits.  
- **`products_info.json`** : Contient les informations détaillées des parfums sous format JSON.  
- **`parfums_info_marketplace.csv`** : Une version CSV des données JSON, utilisable pour une analyse dans Excel ou Google Sheets.

---

## Fonctionnement

### Installation des dépendances
Assurez-vous que Python est installé, puis installez les bibliothèques nécessaires :  
```bash
pip install requests beautifulsoup4
