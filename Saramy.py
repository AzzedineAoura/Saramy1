
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route principale pour renvoyer le fichier HTML de l'application React
@app.route('/')
def index():
    return render_template('index.html')

# Exemple de route pour g�rer une requ�te POST d'ajout de d�pense
@app.route('/api/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    # Ici, tu peux ajouter ton code pour traiter les donn�es de la d�pense envoy�es depuis le frontend
    # et effectuer les op�rations n�cessaires dans ta gestion de budget familial
    # Une fois les op�rations termin�es, tu peux renvoyer une r�ponse JSON appropri�e
    return jsonify({'message': 'Expense added successfully'})

# Exemple de route pour renvoyer les d�penses existantes
@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    # Ici, tu peux ajouter ton code pour r�cup�rer les d�penses existantes depuis ta base de donn�es ou autre source
    # et les renvoyer sous forme de r�ponse JSON
    expenses = [{'id': 1, 'amount': 50, 'description': 'Groceries'}, {'id': 2, 'amount': 20, 'description': 'Gas'}]
    return jsonify(expenses)

if __name__ == '__main__':
    app.run(debug=True)
  