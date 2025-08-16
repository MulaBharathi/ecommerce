from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define a counter metric
REQUEST_COUNT = Counter('order_service_requests_total', 'Total number of requests to order service')

@app.route('/orders', methods=['GET'])
def get_orders():
    REQUEST_COUNT.inc()  # Increment the counter each time this route is called
    orders = [
        {"order_id": 1, "product_id": 101, "user_id": 1},
        {"order_id": 2, "product_id": 102, "user_id": 2}
    ]
    return jsonify(orders)

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

