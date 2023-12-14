from load_survey import prediksi_penyakit_berdasarkan_gejala
from cnn import predict

with open('.ignore/masitis images (13).jpg', 'rb') as f:
  file = f.read()

gejala_list = prediksi_penyakit_berdasarkan_gejala()
dummy_list = [1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]

HASIL = predict(file, gejala_list)

print(HASIL)
