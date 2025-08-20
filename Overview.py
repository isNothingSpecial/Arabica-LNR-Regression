import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# variabel X dan y

df = pd.read_csv('arabica_data_cleaned.csv')

X = df[["Aroma","Flavor","Aftertaste","Acidity","Body","Balance","Uniformity","Clean.Cup","Sweetness","Cupper.Points"]] # Variabel independen (prediktor)
y = df["Total.Cup.Points"] # Variabel dependen (target)

model = LinearRegression()
model.fit(X, y)

# Fungsi untuk mengklasifikasikan hasil
def classify_quality(score):
    """Mengklasifikasikan skor kopi ke dalam kategori kualitas."""
    if 90 <= score <= 100:
        return "Kopi Spesialti Luar Biasa (Outstanding Specialty Coffee)"
    elif 85 <= score < 90:
        return "Kopi Spesialti Sangat Baik (Excellent Specialty Coffee)"
    elif 80 <= score < 85:
        return "Kopi Spesialti (Specialty Coffee)"
    else:
        return "Kopi Non-Spesialti"

# --- Tampilan Streamlit ---

st.title("Aplikasi Prediksi Kualitas Kopi ☕")
st.write("Masukkan skor atribut sensorik untuk memprediksi Total Cup Points dan klasifikasi kualitas kopi.")

# Input dari pengguna
st.subheader("Skor Atribut Sensorik (Skala 0-10)")

# Gunakan kolom untuk inputan yang lebih rapi
col1, col2 = st.columns(2)

with col1:
    aroma = st.number_input("Aroma", min_value=0.0, max_value=10.0, value=8.5, step=0.1)
    flavor = st.number_input("Flavor", min_value=0.0, max_value=10.0, value=8.5, step=0.1)
    aftertaste = st.number_input("Aftertaste", min_value=0.0, max_value=10.0, value=8.0, step=0.1)
    acidity = st.number_input("Acidity", min_value=0.0, max_value=10.0, value=8.5, step=0.1)
    body = st.number_input("Body", min_value=0.0, max_value=10.0, value=8.3, step=0.1)

with col2:
    balance = st.number_input("Balance", min_value=0.0, max_value=10.0, value=8.4, step=0.1)
    uniformity = st.number_input("Uniformity", min_value=0.0, max_value=10.0, value=10.0, step=0.1)
    clean_cup = st.number_input("Clean Cup", min_value=0.0, max_value=10.0, value=10.0, step=0.1)
    sweetness = st.number_input("Sweetness", min_value=0.0, max_value=10.0, value=10.0, step=0.1)
    cupper_points = st.number_input("Cupper Points", min_value=0.0, max_value=10.0, value=8.5, step=0.1)

# Tombol untuk prediksi
if st.button("Prediksi Kualitas Kopi"):
    # Buat DataFrame dari input pengguna
    input_data = pd.DataFrame([[aroma, flavor, aftertaste, acidity, body, balance, uniformity, clean_cup, sweetness, cupper_points]],
                              columns=['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body', 'Balance', 'Uniformity', 'Clean.Cup', 'Sweetness', 'Cupper.Points'])

    # Lakukan prediksi
    predicted_score = model.predict(input_data)[0]

    # Klasifikasi hasil
    classification = classify_quality(predicted_score)
    
    st.markdown("---")
    st.subheader("Hasil Prediksi")
    st.write(f"**Total Cup Points yang diprediksi:** **:green[{predicted_score:.2f}]**")
    st.write(f"**Klasifikasi Kualitas:** **:blue[{classification}]**")

# Petunjuk penggunaan
st.markdown("---")
st.info("💡 **Petunjuk:** Ubah nilai di atas sesuai dengan data kopi Anda, lalu klik 'Prediksi Kualitas Kopi' untuk melihat hasilnya.")

