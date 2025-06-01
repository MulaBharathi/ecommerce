from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    products = [{"product_id": 101, "name": "Laptop", "price": 800}, {"product_id": 102, "name": "Mobile", "price": 500}]
    return jsonify(products)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
