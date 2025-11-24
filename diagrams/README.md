# Génération de diagrammes
La génération des diagrammes dépend de:
- LaTeX, avec les paquets:
  - amsmath
  - tikz
  - quantikz
  - braket
- imagemagick

Optionellement, la dépendance à `make` permet d'accélérer le processus de build.

Il est recommandé d'utiliser [l'environnement Docker](#environnement-docker).

## Générer manuellement les diagrammes
Pour générer un diagramme manuellement, il y a deux options:

- ** Pour un diagramme de math **:
```bash
pdflatex -halt-on-error -interaction=nonstopmode -jobname=<nom du fichier sans .tex> main_math.tex
```

- ** Pour un diagramme de circuit **:
```bash
pdflatex -halt-on-error -interaction=nonstopmode -jobname=<nom du fichier sans .tex> main_circuit.tex
```

Ensuite, pour le convertir en PNG, utiliser la commande:
```bash
convert -density 600 -units PixelsPerInch <nom du PDF obtenu à l'étape précédente> -quality 90 <nom du PNG>
```

## Makefile
On peut aussi utiliser `make`, ce qui fera en sorte de compiler tout les diagrammes.
>[!CAUTION]
> Si vous voulez ajouter un diagramme de math, il est absolument nécessaire de
> nommer le fichier selon le *pattern* `math_*.tex`.

Pour compiler tout les diagrammes, il suffit de rouler:
```bash
make all
```

Il existe aussi une commande pour nettoyer tout les fichiers de build:
```bash
make clean
```

## Environnement Docker
Pour utiliser l'environnement Docker il faut d'abord *build* l'image:
```bash
docker build -t alpine-latex .
```

Ensuite, pour l'utiliser avec `make`, on peut rouler cette commande:
```bash
docker run --rm -v .:/root/diagrams alpine-latex make all
```
