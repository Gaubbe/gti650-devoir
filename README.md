# Devoir - GTI650
## Installer les dépendances
Pour rouler le script, il faut avoir toutes les dépendences installées. Il
est fortement recommandé d'utiliser un Virtual Environment pour y parvenir.

Pour créer l'environnement:
```bash
python -m venv .venv
```

Pour activer l'environnement:
- Windows
```powershell
.venv/scripts/activate
```

- Linux
```bash
source .venv/bin/activate
```

Vous pouvez ensuite installer les dépendances ainsi:
```bash
pip install -r requirements.txt
```

## Rouler le script
Une fois les dépendances installées, rouler le script revient à lancer cette
commande dans le dossier contenant ce script:

```bash
python ./sudoku.py
```

Le script roulera les circuits pour les version 2x2 et 3x3 du problème. Il
affichera ensuite toutes les portes réelles utilisées dans le circuit avec
le nombre de chaque porte utilisé. Le script affichera aussi la
probabilité de succès de l'algorithme de Grover, encore une fois pour les
deux version du problème. Finalement, un fichier PNG sera créé avec la
distribution de probabilité pour chaque entrée possible, seulement pour le
sudoku 2x2.
