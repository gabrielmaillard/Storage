# Gestionnaire d'Articles et d'Emplacements
## Présentation

À l'âge de 9 ans, j'ai entrepris un projet ambitieux de développement logiciel, motivé par ma passion naissante pour l'informatique. Mon objectif était de créer un système de gestion d'articles et d'emplacements, offrant une interface utilisateur conviviale.

Ce projet illustre mon intérêt profond pour les modèles de données : organiser et stocker efficacement des informations est crucial en informatique, notamment à l'ère de l'intelligence artificielle.

## Contexte et Objectifs

En utilisant le langage Python et la bibliothèque PyQt5 pour les interfaces graphiques utilisateur (GUI), j'ai cherché à développer mes compétences en informatique tout en créant un outil fonctionnel et esthétiquement plaisant.

Toutefois, la plupart des fonctionnalités nécessaires à mon application n'étaient pas nativement présentes dans PyQT5. C'est pourquoi j'ai modifié les composants. Ces modifications sont visibles dans le dossier components et en particulier pour le Tree et Root.

## Fonctionnalités Clés

1. Interface Utilisateur Intuitive : J'ai développé une interface utilisateur conviviale, basée sur une architecture de fenêtres et d'onglets pour une navigation fluide et une organisation efficace des données.

2. Gestion Hiérarchique des Données : Le système permet la gestion hiérarchique d'articles et d'emplacements, avec des fonctionnalités avancées telles que l'ajout, la suppression et la modification d'éléments.

3. Recherche et Filtrage Dynamiques : J'ai implémenté une fonctionnalité de recherche permettant aux utilisateurs de rechercher des articles spécifiques en temps réel, améliorant ainsi l'efficacité de la gestion des données.

4. Interaction avec une Base de Données : Le projet intègre des opérations de lecture, d'écriture et de mise à jour de données dans une base de données SQLite, démontrant ma compréhension des principes fondamentaux de la gestion de données.

5. Réutilisation de Composants : J'ai utilisé des concepts de réutilisation de composants, tels que la création de widgets personnalisés pour la gestion de l'arborescence des données et des onglets dynamiques pour une expérience utilisateur optimale.

## Technique

### Utilisation de PyQt5 pour les Interfaces Graphiques.
J'ai exploité les fonctionnalités avancées de la bibliothèque PyQt5 pour la création de fenêtres, de widgets et de mises en page personnalisées, démontrant ma maîtrise des outils de développement GUI.

### Programmation Orientée Objet
J'ai adopté une approche orientée objet pour organiser le code en classes et en modules réutilisables, favorisant la modularité et la maintenabilité du projet.

### Manipulation de Données avec Python
J'ai utilisé les fonctionnalités de manipulation de données de Python pour interagir avec la base de données SQLite, en mettant en œuvre des opérations CRUD (Create, Read, Update, Delete) pour gérer les données d'articles et d'emplacements.

### Récursivité et algorithmes de parcours
Pour la gestion hiérarchique des emplacements, j'ai mis en œuvre des algorithmes récursifs pour parcourir et afficher les données de manière efficace, démontrant ma compréhension des concepts avancés d'algorithmique.

## Organisation du code :

* main.py : Le fichier principal pour exécuter le programme. Il charge les configurations à partir d'un fichier JSON, initialise la base de données et lance l'interface utilisateur.

* data.py : Ce module contient la classe DatabaseManager qui gère les opérations de base de données telles que la création de tables, l'ajout, la suppression et la modification d'entrées, ainsi que la récupération de données.

* components/ : Ce répertoire contient les différentes composantes de l'interface utilisateur, telles que les fenêtres de dialogue pour ajouter des articles ou des emplacements, ainsi que la classe Root qui agit comme le point d'entrée principal pour l'interface utilisateur.