# LOG3000 - TP3 du groupe 42

## Objectif
Ce repo contient une calculatrice web simple développée avec Flask (Python) permettant d'effectuer les quatre opérations arithmétiques de base (addition, soustraction, multiplication et division).
L'application reçoit une expression arithmétique via un formulaire HTML, la parse et la calcule côté serveur, puis retourne le résultat à l'utilisateur.

## Prérequis d'installation

- python
- pip
- git

---

## Structure du dépôt

```
TP3---LOG3000/
├── src/
│   ├── backend/         # Serveur Flask et logique de calcul
│   │   ├── app.py
│   │   ├── operators.py
│   │   └── README.md
│   └── frontend/        # Interface utilisateur
│       ├── templates/
│       │   └── index.html
│       ├── static/
│       │   └── style.css
│       └── README.md
├── .gitignore
└── README.md
```

---

## Installation

**1. Cloner le dépôt**
```
git clone https://github.com/Kapiix/TP3---LOG3000.git
```

**2. Installer les dépendances**
```
pip install flask
```

---

## Instructions d'installation

**Lancer l'application**
```
python app.py
```

Ouvrir ensuite [http://127.0.0.1:5000](http://127.0.0.1:5000) dans un navigateur.

---

## Utilisation

1. Cliquer sur les boutons numériques pour entrer le premier opérande.
2. Cliquer sur un opérateur (`+`, `−`, `×`, `÷`).
3. Entrer le second opérande.
4. Appuyer sur `=` pour afficher le résultat.
5. Appuyer sur `C` pour réinitialiser l'affichage.

**Contraintes actuelles :**
- Un seul opérateur par expression.
- Les deux opérandes doivent être des nombres (entiers ou décimaux).
- La division par zéro retourne un message d'erreur.

---

## Tests

A AJOUTER PLUS TARD

---

## Contribuer

### Branches

| Branche | Utilisation |
|---|---|
| `main` | Code stable et testé uniquement |
| `dev` | Branche d'intégration |
| `feature/<nom>` | Développement d'une fonctionnalité |
| `fix/<nom>` | Correction d'un bug |

### Flux de travail

1. Créer une branche depuis `dev` :
   ```
   git checkout dev
   git pull
   git checkout -b feature/ma-fonctionnalite
   ```
2. Faire ses modifications et commiter :
   ```
   git add .
   git commit -m "feat: description courte de la modification"
   ```
3. Pousser la branche et ouvrir une Pull Request vers `dev`.
4. La PR doit être approuvée par au moins un autre membre avant d'être fusionnée.
5. Les fusions vers `main` se font uniquement depuis `dev`, après validation complète.

### Issues

Utiliser les GitHub Issues pour signaler un bug ou proposer une amélioration.
Inclure : une description claire, les étapes pour reproduire (si bug), et le comportement attendu.
