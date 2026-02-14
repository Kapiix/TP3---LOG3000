"""
app.py - Serveur Flask pour la calculatrice web TP3 LOG3000.

Expose une route unique (/) qui accepte des expressions arithmétiques
simples soumises via un formulaire HTML et retourne le résultat calculé.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Dossiers séparés car le projet suit une architecture backend/frontend
app = Flask(__name__,
            template_folder='../frontend/templates',
            static_folder='../frontend/static')

# Table de dispatch : associe chaque symbole à sa fonction arithmétique
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str) -> float:
    """
    Évalue une expression arithmétique simple à deux opérandes.

    Accepte des expressions de la forme "a OP b" où OP est l'un des
    opérateurs +, -, *, /. Les espaces sont ignorés. Un seul opérateur
    est autorisé par expression.

    Args:
        expr (str): L'expression à évaluer (ex: "3 + 5", "10/2").

    Returns:
        float: Le résultat de l'opération.

    Raises:
        ValueError: Si l'expression est vide, mal formée, contient plus
                    d'un opérateur, ou si les opérandes ne sont pas des nombres.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de la calculatrice.

    GET  : Affiche la calculatrice avec un résultat vide.
    POST : Récupère l'expression saisie, la calcule et renvoie le résultat
           (ou un message d'erreur) à la vue.

    Returns:
        str: La page HTML rendue par le template index.html.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Mode debug activé uniquement en développement local
    app.run(debug=True)