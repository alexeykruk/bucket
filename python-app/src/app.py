from flask import Flask
import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Hello"}), 200

@app.route("/api/v1/healthz")
def status():
    return jsonify({"status": "OK"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
