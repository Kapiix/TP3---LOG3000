# Frontend — `src/tests/`

## Raison d'être

Ce module contient les tests unitaires du projet. Les tests peuvent être exécutés avec la commande `python -m unittest` depuis le dossier `src/`.

---

## Fichiers


### `__init__.py`
Sert à identifier le dossier `src/tests/` en tant que module.

### `test_operators.py`

Tests unitaires des opérateurs définis dans `src/backend/operators.py`.

Comporte les tests suivants :

- **test_subtract** : Vérifie que l'opérateur de soustraction fonctionne comme prévu.
- **test_multiply** : Vérifie que l'opérateur de multiplication fonctionne comme prévu.
- **test_divide** : Vérifie que l'opérateur de division fonctionne comme prévu.

---

## Dépendances

| Dépendance | Usage |
|---|---|
| Python | Langage d'exécution |

Note : `unittest` n'est pas une dépendance externe, puisque c'est un module par défaut de Python.

## Hypothèses

- Le module est exécuté depuis le répertoire `src/` par la commande `python -m unittest` afin de bien trouver tous les modules nécessaires.

---
