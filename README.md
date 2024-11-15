# 🕵️‍♀️ Projet Python de Scraping - Marionnaud Parfums

### 📋 Description
Ce projet extrait des données sur les **parfums pour femmes** depuis le site de **Marionnaud** en utilisant Python et le scraping. Il est conçu pour collecter les informations essentielles (catégorie, marque, nom, quantité, et prix) des produits dans les catégories suivantes :
- Eau de Parfum
- Eau de Toilette
- Eau de Cologne

Les données collectées sont exportées dans des fichiers JSON et CSV, et un fichier Google Sheet est généré pour analyse.

---

## 🚀 Fonctionnalités

- **Extraction automatique des liens des pages produits**
- **Filtrage par catégories d'intérêt** pour ne garder que les parfums pertinents
- **Scraping détaillé des informations produits** : catégorie, marque, nom, quantité, prix
- **Stockage des données** dans des fichiers JSON et CSV pour faciliter les analyses
- **Exportation vers Google Sheet** pour analyser et visualiser les données

---

## 📁 Structure des Fichiers de Sortie

- **`resultats.json`** : Contient les informations de chaque page de la catégorie.
- **`products_info.json`** : Enregistre les informations complètes de chaque parfum.
- **`parfums_info_marketplace.csv`** : Fichier CSV final pour analyse sur un tableur ou importation en base de données.

---

## 🛠️ Utilisation

### Prérequis
Assurez-vous d'avoir les modules Python suivants installés :
```bash
pip install requests beautifulsoup4
