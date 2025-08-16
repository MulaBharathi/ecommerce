from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('product_service_requests_total', 'Total requests to product service')

@app.route('/products', methods=['GET'])
def get_products():
    REQUEST_COUNT.inc()
    products = [
        {"product_id": 101, "name": "Product 1"},
        {"product_id": 102, "name": "Product 2"}
    ]
    return jsonify(products)

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)

