import pickle
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

from helpers import image_load_img_manual

MODEL_CNN_PENYAKIT = 'models/cnn_penyakit.h5'
MODEL_SURVEY = 'models/survey.pickle'

pengobatan = {
  "BEF": "Pengobatan dilakukan simtomatik dan pencegahan terhadap infeksi sekunder dengan antibiotik yang dilakukan oleh petugas yang berwenang.",
  "Brucellosi": "Dilakukan vaksinasi terhadap ternak yang terjangkit brucellosis Dilakukan uji Red Bengal Test (RBT) dan uji Complement Fixation Test (CFT). Apabila kedua tes mendapatkan hasil positif, maka dilakukan Test and Slaughter.",
  "Cacingan": "Obat yang biasanya digunakan oleh dokter hewan adalah dalam jenis benzimidazol, Imida-thiazol dan Avermectin (konsultasi dengan dokter hewan sebelum menggunakan).",
  "Masitis": "Menjaga kandang untuk tetap bersih. Memakai antiseptik guna pencelupan puting susu saat sebelum dan setelah pemerahan. Memberikan antibiotik berspek trum misalnya peniciline - streptomicine atau Suanovil (spiramycine).",
  "Pneumonia": "Pencegahan yang dapat dilakukan dengan melakukan sanitasi kandang yang benar, dan pisahkan sapi yang sakit pada kandang karantina. Pengobatan dilakukan dengan memberikan vaksin antibiotik untuk memutus siklus pertumbuhan penyebab pneumonia seperti vaksin Ca boroglukonat dan vitamin C, sulfonamid.",
  "Hipocalcemi": "Pengobatan dilakukan dengan cara menyuntikkan garam berkalsium lengkap seperti larutan kalsium klorida 10%, larutan kalsium boroglukonat 20-30%, dan campuran berbagai sediaan kalsium seperti Calphon Forte, Calfosal atau Calcitad-50.",
  "Skabies/LSD": "Memberikan minyak kelapa dicampur dengan kapur barus kemudian digosokkan pada kulit yang terkena skabies.",
  "Diare": "Untuk menggantikan cairan tubuh yang hilang akibat diare pada ternak dapat diberikan cairan elektrolit terutama air, bikarbonat, sodium, dan potassium atau larutan garam agar tidak terjadi dehidrasi yang lebih lanjut.",
  "Paratubercolosis": "Hewan-hewan yang positif MAP harus diafkir sesegera mungkin dan seluruh hewan harus dilakukan pengujian kembali dengan kombinasi uji yang berbeda.",
  "Kembung": "Memberikan anti bloat yang mengandung dimethicone serta minyak nabati yang berasal dari kacang tanah. Minyak nabati bisa disuntikkan pada sapi yang terkena bloat. Atau dapat di konsultasikan pada dokter hewan untuk pemakaian obat yang cocok.",
  "PMK": "masih ksg"
}

urutan_kelas = ['BEF', 'Brucellosis', 'Cacingan', 'Diare', 'Hipocalcemi',
                'Kembung', 'Masitis', 'PMK', 'Paratubercolosis', 'Pneumonia', 'Skabies/LSD']

penyakit_gambar = ["Scabise/LSD", "Masitis", "Normal", "PMK"]


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


def predict_with_model(model, image_bytes):
  # processed_image = preprocess_image(file_path)
  processed_image = preprocess_image(image_bytes)
  normalized_image = normalize_image(processed_image)
  predictions = model.predict(normalized_image)
  predicted_class = np.argmax(predictions, axis=1)
  return predicted_class


def predict(image_bytes, gejala_pengguna):
  penyakit = []
  penanganan = []

  # Load Model Survey
  with open(MODEL_SURVEY, 'rb') as file:
    loaded_data = pickle.load(file)

  # Hasil
  hasil_prediksi = loaded_data.predict([gejala_pengguna])

  # Misalkan probabilitas_prediksi adalah hasil dari clf.predict_proba([gejala_pengguna])
  n = 0
  for i in gejala_pengguna:
    n += i

  if n > 2:
    probabilitas_prediksi = loaded_data.predict_proba([gejala_pengguna])
    threshold = 0.2 # Tentukan threshold yang diinginkan

    # Ambil indeks kelas yang memiliki nilai probabilitas > threshold
    kelas_lebih_dari_threshold = [i for i, prob in enumerate(
      probabilitas_prediksi[0]) if prob > threshold]

  else:
    # kalo gejala kurang dari 2
    kelas_lebih_dari_threshold = []
    print("Maaf gejala tidak menunjukkan adanya penyakit pada sapi anda")

  for i in kelas_lebih_dari_threshold:
    if loaded_data.classes_[i] in penyakit_gambar:

      # Load Model CNN
      model = load_model(MODEL_CNN_PENYAKIT)

      f = image_bytes
      predicted_class = predict_with_model(model, f)
      common_elements = urutan_kelas[i] in penyakit_gambar[predicted_class[0]]

      if common_elements:
        # kalo prediksi gambar sesuai dengan penyakit dari survey
        a = loaded_data.classes_[i]
        b = pengobatan[loaded_data.classes_[i]]
        penyakit.append(a)
        penanganan.append(b)

      else:
        # kalo prediksi gambar tidak sesuai dengan penyakit dari survey
        a = loaded_data.classes_[i]
        b = pengobatan[loaded_data.classes_[i]]
        penyakit.append(a)
        penanganan.append(b)

    else:
      a = loaded_data.classes_[i]
      b = pengobatan[loaded_data.classes_[i]]
      penyakit.append(a)
      penanganan.append(b)

  return {
    "penyakit": penyakit,
    "penanganan": penanganan,
  }
