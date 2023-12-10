from flask import Flask, request, jsonify
from flask_cors import CORS

from predict import predict_with_model

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    file = request.files.get('file')

    if file is None:
      return jsonify({'status': False, 'error': 'no file'}), 400

    try:
      image_bytes = file.read()
      result = predict_with_model(image_bytes)
      return jsonify({'status': True, 'prediction': result})
    except Exception as e:
      print(e)
      return jsonify({'status': False, 'error': str(e)}), 500

  return jsonify({'status': True, 'message': 'OK'})


if __name__ == '__main__':
  app.run(debug=True)
