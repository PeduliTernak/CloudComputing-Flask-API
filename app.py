from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def perform_prediction(image_bytes):
    return "not implemented"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return jsonify({"status": "OK"})

    file = request.files.get("file")

    if file is None:
        return jsonify({"error": "no file"})

    image_bytes = file.read()
    result = perform_prediction(image_bytes)
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
