# Backend — `src/backend/`

## Raison d'être

Ce module contient l'intégralité de la logique serveur de la calculatrice. Il est responsable de :
- Recevoir les requêtes HTTP envoyées depuis le formulaire HTML.
- Parser et valider les expressions arithmétiques saisies par l'utilisateur.
- Calculer le résultat en déléguant à des fonctions arithmétiques dédiées.
- Retourner le résultat (ou un message d'erreur) au frontend via un template Jinja2.

---

## Fichiers

### `app.py`

Point d'entrée de l'application Flask. Contient deux responsabilités principales :

- `calculate(expr)` : Fonction de parsing qui extrait les deux opérandes et l'opérateur d'une expression textuelle, puis appelle la fonction arithmétique correspondante.
- `index()` : Route Flask unique (`/`) gérant les requêtes GET (affichage initial) et POST (traitement du formulaire).

Flask est configuré avec des chemins explicites vers les dossiers `templates/` et `static/` du frontend, car ils ne se trouvent pas à l'emplacement par défaut.

### `operators.py`

Bibliothèque de fonctions arithmétiques pures, sans dépendance externe :

| Fonction | Description |
|---|---|
| `add(a, b)` | Retourne `a + b` |
| `subtract(a, b)` | Retourne `a - b` |
| `multiply(a, b)` | Retourne `a * b` |
| `divide(a, b)` | Retourne `a / b` |

Ces fonctions sont intentionnellement isolées de Flask pour faciliter les tests unitaires indépendants.

---

## Dépendances

| Dépendance | Usage |
|---|---|
| Python | Langage d'exécution |
| Flask | Serveur HTTP et rendu de templates |

---

## Hypothèses

- Le frontend soumet toujours l'expression via un champ nommé `display` dans le formulaire POST.
- Une expression valide contient exactement un opérateur (`+`, `-`, `*`, `/`) entouré de deux opérandes numériques.
- Le module est lancé depuis son propre répertoire (`src/backend/`) pour que les chemins relatifs vers le frontend soient résolus correctement.

---