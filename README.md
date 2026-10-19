# Procedural Generation — One Algorithm at a Time

Languages: [English](#english-side) · [Français](#french-side)

# English Side

Hey! I'm a dev who loves procedural gen, and I'm currently challenging myself to implement one procedural gen algorithm per day, or at least per week if it's a complicated one.

## Content

- [voronoi-diagrams](#16102026-first-day-voronoi-diagrams)
- [Random](<README#19/10/2026 Day 2 — Random>)

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

## 19/10/2026 Day 2 — Random

Even today, a simple algorithm generates random noise. Although it isn't particularly useful on its own, it can be used to add texture to other algorithms.

Its implementation is simple: we fill our grid with random numbers in our case, a number between 0 and 1. This allows us to create noise textures like this.

![BG_Random](Images/BG_Random.png)

And as I mentioned earlier, it is possible to use this noise texture to introduce variation into our textures. The following examples use the same random seed and vary only the degree of variation that the randomization applies to the Voronoi texture, ranging from 0 to 1.

![BG_VoronoiRandomV0](Images/BG_VoronoiRandomV0.png)

![BG_VoronoiRandomV0_15](Images/BG_VoronoiRandomV0_15.png)

![BG_VoronoiRandomV0_5](Images/BG_VoronoiRandomV0_5.png)

![BG_VoronoiRandomV1](Images/BG_VoronoiRandomV1.png)

The code, if you want to test it: [Test Code](TestCodes/MiniRandom.py)

Command to execute it from this folder

```bash
python3 TestCodes/MiniRandom.py
```

# French Side

[Retour à la version anglaise](#english-side)

Salut ! Je suis développeur et j'adore la génération procédurale. Je me suis lancé un défi : implémenter un algorithme de génération procédurale par jour, ou au moins par semaine si l'algorithme est compliqué.

## Sommaire

- [Diagrammes de Voronoï](#16102026-premier-jour--diagrammes-de-voronoï)
- [Random](<README#19/10/2026 Jour 2 — Random>)

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

## 19/10/2026 Jour 2 — Bruit

Aujourd'hui encore, un algorithme simple le bruit aléatoire. Bien qu'il ne soit pas vraiment utile par lui-même, il peut être utilisé pour ajouter de la texture à d'autres algorythmes.

Son implémentation est simple : on remplit notre grille de nombres aléatoires, un chiffre entre 0 et 1 dans notre cas. Ce qui nous permet de créer des textures de bruit comme ceci.

![BG_Random](Images/BG_Random.png)

Et comme je l'ai mentionné précédemment, il est possible d'utiliser cette texture de bruit pour apporter de la variance dans nos textures. Les exemples suivants utilisent la même graine d'aléatoire et varient seulement le degré de variance que l'aléatoire applique sur la texture de Voronoi, allant de 0 à 1.

![BG_VoronoiRandomV0](Images/BG_VoronoiRandomV0.png)

![BG_VoronoiRandomV0_15](Images/BG_VoronoiRandomV0_15.png)

![BG_VoronoiRandomV0_5](Images/BG_VoronoiRandomV0_5.png)

![BG_VoronoiRandomV1](Images/BG_VoronoiRandomV1.png)

Le code, si vous voulez le tester : [Code de test](TestCodes/MiniRandom.py)

Commande pour l'executer depuis ce dossier

```bash
python3 TestCodes/MiniRandom.py
```
