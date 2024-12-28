
from flask import Flask, request, jsonify

app = Flask(__name__)

def suite_syracuse(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequence.extend([4, 2, 1])
    return sequence

@app.route('/syracuse', methods=['POST'])
def calculate_syracuse():
    data = request.json
    number = data.get('number')

    if not isinstance(number, int) or number <= 0:
        return jsonify({"error": "Nombre invalide, veuillez entrer un entier positif."}), 400

    results = {
        "pair": number % 2 == 0,
        "syracuse": suite_syracuse(number)
    }
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
        