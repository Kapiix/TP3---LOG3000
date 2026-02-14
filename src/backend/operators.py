"""
operators.py - Fonctions arithmétiques de base pour la calculatrice TP3 LOG3000.

Chaque fonction encapsule une opération élémentaire et est conçue pour être
appelée via la table de dispatch OPS définie dans app.py.
"""


def add(a: float, b: float) -> float:
    """
    Additionne deux nombres.

    Args:
        a (float): Le premier opérande.
        b (float): Le second opérande.

    Returns:
        float: La somme de a et b.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Soustrait b de a.

    Args:
        a (float): Le premier opérande (diminuende).
        b (float): Le second opérande (diminuteur).

    Returns:
        float: La différence a - b.
    """
    return b - a

def multiply(a: float, b: float) -> float:
    """
    Multiplie deux nombres.

    Args:
        a (float): Le premier opérande.
        b (float): Le second opérande.

    Returns:
        float: Le produit de a et b.
    """
    return a ** b

def divide(a: float, b: float) -> float:
    """
    Divise a par b.

    Args:
        a (float): Le numérateur.
        b (float): Le dénominateur.

    Returns:
        float: Le quotient de a et b.
    """
    return a // b