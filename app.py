from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def perform_prediction(image_bytes):
  return 'not implemented'


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    file = request.files.get('file')

    if file is None:
      return jsonify({'status': False, 'error': 'no file'})

    try:
      image_bytes = file.read()
      result = perform_prediction(image_bytes)
      return jsonify({'status': True, 'prediction': result})
    except Exception as e:
      return jsonify({'status': False, 'error': str(e)})

  return jsonify({'status': True, 'message': 'OK'})


if __name__ == '__main__':
  app.run(debug=True)
