# Frontend — `src/frontend/`

## Raison d'être

Ce module contient l'interface utilisateur de la calculatrice. Il est entièrement statique (pas de JavaScript côté serveur, pas de framework frontend) et s'appuie sur le moteur de templates Jinja2 de Flask pour recevoir et afficher le résultat calculé par le backend.

---

## Fichiers

### `templates/index.html`

Template Jinja2 constituant la page unique de l'application. Il remplit deux rôles :

- **Affichage** : Rend l'interface de la calculatrice (boutons, écran) dans le navigateur.
- **Communication avec le backend** : Soumet l'expression via un formulaire HTML `POST` et affiche la variable `{{ result }}` injectée par Flask en retour.

La logique de saisie (concaténation des chiffres et opérateurs sur l'écran) est gérée par quelques fonctions JavaScript vanilla directement dans la page.

### `static/style.css`

Feuille de style de l'interface. Définit :
- La mise en page centrée de la calculatrice (flexbox).
- L'apparence des boutons (grille 4 colonnes, distinction visuelle entre chiffres et opérateurs).
- Les effets interactifs (`:hover`, `:active`).

Aucun framework CSS n'est utilisé — le fichier est entièrement en CSS natif.

---

## Dépendances et hypothèses

- Ce module n'a aucune dépendance npm ou externe : tout est du HTML/CSS/JS natif.
- Les fichiers sont servis par Flask, qui est configuré pour pointer vers ce dossier depuis `src/backend/app.py`. Ce module ne peut pas fonctionner indépendamment sans le serveur Flask.
- Le template s'attend à recevoir une variable `result` depuis Flask (chaîne vide par défaut, résultat ou message d'erreur après un POST).
- Le formulaire doit contenir un champ `name="display"` pour que le backend puisse lire l'expression soumise.

---
