from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

from helpers import image_load_img_manual

model = load_model('cnn_penyakit.h5')
penyakit = ['lumpy', 'masitis', 'normal', 'pmk']


def preprocess_image(image_bytes):
  # Set your desired image size
  # img = image.load_img(file_path, target_size=(150, 150))
  img = image_load_img_manual(image_bytes, target_size=(150, 150))

  img_array = image.img_to_array(img)
  img_array = np.expand_dims(img_array, axis=0)
  return img_array


def normalize_image(img_array):
  # Normalize pixel values to the range [0, 1]
  normalized_img = img_array / 255.0
  return normalized_img


def predict_with_model(image_bytes):
  processed_image = preprocess_image(image_bytes)
  normalized_image = normalize_image(processed_image)
  predictions = model.predict(normalized_image)
  # Assuming it's a classification task
  predicted_class = np.argmax(predictions, axis=1)
  result = penyakit[predicted_class[0]]
  return result
