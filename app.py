from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from cnn import predict

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    file = request.files.get('file')
    gejala_matrix = request.form.get('gejala_matrix')
    gejala_matrix = json.loads(gejala_matrix)

    if file is None:
      return jsonify({'status': False, 'error': 'no file'}), 400

    if gejala_matrix is None or gejala_matrix == '':
      return jsonify({'status': False, 'error': 'no gejala matrix'}), 400

    try:
      image_bytes = file.read()
      result = predict(image_bytes, gejala_matrix)
      return jsonify({'status': True, 'prediction': result})
    except Exception as e:
      print(e)
      return jsonify({'status': False, 'error': str(e)}), 500

  return jsonify({'status': True, 'message': 'OK'})


if __name__ == '__main__':
  app.run(debug=True)
