
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route principale pour renvoyer le fichier HTML de l'application React
@app.route('/')
def index():
    return render_template('index.html')

# Exemple de route pour gérer une requête POST d'ajout de dépense
@app.route('/api/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    # Ici, tu peux ajouter ton code pour traiter les données de la dépense envoyées depuis le frontend
    # et effectuer les opérations nécessaires dans ta gestion de budget familial
    # Une fois les opérations terminées, tu peux renvoyer une réponse JSON appropriée
    return jsonify({'message': 'Expense added successfully'})

# Exemple de route pour renvoyer les dépenses existantes
@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    # Ici, tu peux ajouter ton code pour récupérer les dépenses existantes depuis ta base de données ou autre source
    # et les renvoyer sous forme de réponse JSON
    expenses = [{'id': 1, 'amount': 50, 'description': 'Groceries'}, {'id': 2, 'amount': 20, 'description': 'Gas'}]
    return jsonify(expenses)

if __name__ == '__main__':
    app.run(debug=True)
  