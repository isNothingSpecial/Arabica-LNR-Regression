import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import importlib

## data

st.set_page_config(page_title="Overview",layout="wide")
#side bar

##layout

# Menggunakan HTML dan CSS untuk membuat header dan subheader rata tengah
st.markdown(
    """
    <h1 style='text-align: center;'>Penilaian Kualitas Biji Kopi Dengan menggunakan Algoritma Linier Regression</h1>
    """, 
    unsafe_allow_html=True
)

st.write(''' Seperti namanya, kopi Specialty adalah sebuah penilaian atau pengklasifikasian terhadap kopi yang memiliki aroma dan rasa yang istimewa. Jika kita menilai berdasarkan penilaian SCAA (Specialty Coffee Association of America) maka sebuah kopi specialty wajib memiliki nilai minimum 80 dan maksimum 100 serta tidak memiliki cacat primer untuk green bean/biji hijau-nya.''')

col1,col2 = st.columns(2)
with col1:
    st.markdown(''' **Awal Mula Penilaian: Dari Tampilan Fisik ke Rasa** \n
Pada awalnya, penilaian kopi didasarkan pada tampilan fisik biji. Kopi dinilai berdasarkan ukuran, bentuk, dan warna biji,
serta jumlah cacat fisik yang terlihat. Sistem ini, yang masih digunakan di beberapa pasar komersial hingga kini (seperti standar SNI yang berbasis cacat),
seringkali tidak mencerminkan kualitas rasa kopi saat diseduh.

Seiring waktu, para pedagang dan penilai kopi menyadari bahwa tampilan fisik tidak selalu berkorelasi dengan rasa.
Kopi yang terlihat bagus bisa saja memiliki rasa yang hambar atau tidak enak. Demikian pula, kopi dengan biji yang kurang sempurna secara visual
terkadang menghasilkan rasa yang luar biasa. Oleh karena itu, muncullah kebutuhan untuk menilai kopi berdasarkan aspek sensoriknya.
''')

with col2:
    st.markdown('''**Era "Spesialti Kopi" dan "Third Wave"** \n
Istilah "Specialty Coffee" pertama kali diperkenalkan oleh Erna Knutsen dari Knutsen Coffee Ltd. dalam sebuah artikel pada tahun 1974.
Ia mendefinisikan kopi spesialti sebagai kopi yang memiliki profil rasa khusus dan berasal dari biji yang ditanam di iklim mikro tertentu.

st.Konsep ini kemudian berkembang pesat, sejalan dengan munculnya gerakan "Third Wave of Coffee" pada akhir abad ke-20.
Gerakan ini mendorong para konsumen untuk melihat kopi seperti halnya anggur—sebagai produk pertanian yang memiliki karakteristik unik berdasarkan :
- Varietas
- Asal
- Cara Pemrosesan
''')

col3,col4 = st.columns(2)
with col3:
    st.markdown(''' **Pembentukan SCA dan Standarisasi Penilaian** \n

Pada tahun 1982, didirikanlah Specialty Coffee Association of America (SCAA). Organisasi ini menjadi tonggak penting dalam standarisasi penilaian kopi spesialti.
SCAA, yang kemudian merger dengan Specialty Coffee Association of Europe (SCAE) pada tahun 2017 menjadi Specialty Coffee Association (SCA),
mengembangkan sistem penilaian yang dikenal sebagai SCA Cupping Protocol atau Q-Grading System.

Sistem ini, yang masih menjadi acuan global hingga kini, memiliki karakteristik utama sebagai berikut:
1. Sistem 100 Poin: Kopi dinilai pada skala 100 poin, di mana kopi dengan skor 80 atau lebih dianggap sebagai kopi spesialti.
2. Penilaian Sensorik: Penilaian tidak lagi hanya berdasarkan cacat fisik, tetapi berfokus pada atribut rasa dan aroma, seperti:
- Fragrance/Aroma (Aroma kering dan basah)
- Flavor (Rasa)
- Aftertaste (Sisa Rasa setelah ditelan)
- Acidity (Keasaman)
- Body (Kekentalan)
- Balance (Keseimbangan)
- Clean Cup (Kebersihan Rasa)
- Uniformity (Keseragaman Rasa)
- Sweetness (Rasa Manis)
- Overall (kesan keseluruhan)

3. Pelatihan Profesional: SCA memperkenalkan program sertifikasi untuk para penilai kopi, yang dikenal sebagai Q Grader.
Mereka dilatih untuk mencicipi dan menilai kopi secara objektif dan konsisten menggunakan standar yang sama di seluruh dunia.
''')

with col4:
    st.markdown('''**Era "Spesialti Kopi" dan "Third Wave"** \n
Istilah "Specialty Coffee" pertama kali diperkenalkan oleh Erna Knutsen dari Knutsen Coffee Ltd. dalam sebuah artikel pada tahun 1974.
Ia mendefinisikan kopi spesialti sebagai kopi yang memiliki profil rasa khusus dan berasal dari biji yang ditanam di iklim mikro tertentu.

st.Konsep ini kemudian berkembang pesat, sejalan dengan munculnya gerakan "Third Wave of Coffee" pada akhir abad ke-20.
Gerakan ini mendorong para konsumen untuk melihat kopi seperti halnya anggur—sebagai produk pertanian yang memiliki karakteristik unik berdasarkan :
- Varietas
- Asal
- Cara Pemrosesan
''')
