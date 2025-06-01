from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = [{"order_id": 1, "product_id": 101, "user_id": 1}, {"order_id": 2, "product_id": 102, "user_id": 2}]
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
