# Procedural Generation — One Algorithm at a Time

Languages: [English](#english-side) · [Français](#french-side)

# English Side

Hey! I'm a dev who loves procedural gen, and I'm currently challenging myself to implement one procedural gen algorithm per day, or at least per week if it's a complicated one.

## Content

- [voronoi-diagrams](#16102026-first-day-voronoi-diagrams)

## 16/10/2026 First day Voronoï diagrams

![Voronoi Example](BG_Voronoi.png)

A Voronoi texture or diagram is a segmentation of a space into cells, where each cell represents the points that are closest to one randomly placed point among all the points placed in that space.

Today, I did the simplest implementation, which can be explained in three simple steps:

1. Place cell points randomly on a grid.
2. Go through each point of the grid and find the distance to the closest cell point.
3. Use the distances you calculated to make a grayscale gradient.

The code, if you want to test it: [Test Code](TestCodes/MiniVoronoi.py)

Command to execute it from this folder

```bash
python3 TestCodes/MiniVoronoi.py
```

[Voronoi Diagram — Wikipedia](https://en.wikipedia.org/wiki/Voronoi_diagram)

# French Side

[Retour à la version anglaise](#english-side)

Salut ! Je suis développeur et j'adore la génération procédurale. Je me suis lancé un défi : implémenter un algorithme de génération procédurale par jour, ou au moins par semaine si l'algorithme est compliqué.

## Sommaire

- [Diagrammes de Voronoï](#16102026-premier-jour--diagrammes-de-voronoï)

## 16/10/2026 Premier jour — Diagrammes de Voronoï

Une texture ou un diagramme de Voronoï est un découpage de l'espace en cellules, où chaque cellule représente les points les plus proches d'un point placé aléatoirement parmi tous les points disposés dans cet espace.

Aujourd'hui, j'ai réalisé l'implémentation la plus simple, qui peut s'expliquer en trois étapes :

1. Placer des points de cellule aléatoirement sur une grille.
2. Parcourir chaque point de la grille et trouver la distance jusqu'au point de cellule le plus proche.
3. Utiliser les distances calculées pour créer un dégradé en niveaux de gris.

Le code, si vous voulez le tester : [Code de test](TestCodes/MiniVoronoi.py)

Commande pour l'executer depuis ce dossier

```bash
python3 TestCodes/MiniVoronoi.py
```

[Diagramme de Voronoï — Wikipédia](https://fr.wikipedia.org/wiki/Diagramme_de_Vorono%C3%AF)
