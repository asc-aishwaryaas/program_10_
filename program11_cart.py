
from flask import Flask, request, jsonify

app = Flask(__name__)
orders = []

@app.route('/addOrders', methods=['POST'])
def addOrders():
    data = request.get_json()
    orders.append(data)
    return jsonify({"message": "Order added", "order": data}), 201

@app.route('/showOrders', methods=['GET'])
def showOrders():
    return jsonify(orders[-5:][::-1])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
