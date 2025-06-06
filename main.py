from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# ✅ Allow requests from your exact landing page URL
CORS(app, origins=["https://16959149-f846-400c-9924-b961fb3c50fc-00-1mfkirmx9lr8w.picard.replit.dev"])

# ✅ Dummy transaction IDs just for testing
valid_tx_ids = {
    "btc": ["txid123", "txid456"],
    "sol": ["soltxabc", "soltxdef"]
}

@app.route('/verify', methods=['POST'])
def verify_transaction():
    data = request.get_json()
    txid = data.get("tx_id")
    coin = data.get("coin", "").lower()

    if coin in valid_tx_ids and txid in valid_tx_ids[coin]:
        return jsonify({"status": "success", "message": "Payment verified."})
    else:
        return jsonify({"status": "failed", "message": "Could not verify payment."})

@app.route('/')
def home():
    return "✅ TX verification server running..."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


