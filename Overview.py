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
    st.markdown(''' **Awal Mula Penilaian: Dari Tampilan Fisik ke Rasa** :
Pada awalnya, penilaian kopi didasarkan pada tampilan fisik biji. Kopi dinilai berdasarkan ukuran, bentuk, dan warna biji,
serta jumlah cacat fisik yang terlihat. Sistem ini, yang masih digunakan di beberapa pasar komersial hingga kini (seperti standar SNI yang berbasis cacat),
seringkali tidak mencerminkan kualitas rasa kopi saat diseduh.

Seiring waktu, para pedagang dan penilai kopi menyadari bahwa tampilan fisik tidak selalu berkorelasi dengan rasa.
Kopi yang terlihat bagus bisa saja memiliki rasa yang hambar atau tidak enak. Demikian pula, kopi dengan biji yang kurang sempurna secara visual
terkadang menghasilkan rasa yang luar biasa. Oleh karena itu, muncullah kebutuhan untuk menilai kopi berdasarkan aspek sensoriknya.
''')

with col2:
    st.markdown('''**Era "Spesialti Kopi" dan "Third Wave"** :
Istilah "Specialty Coffee" pertama kali diperkenalkan oleh Erna Knutsen dari Knutsen Coffee Ltd. dalam sebuah artikel pada tahun 1974.
Ia mendefinisikan kopi spesialti sebagai kopi yang memiliki profil rasa khusus dan berasal dari biji yang ditanam di iklim mikro tertentu.

Konsep ini kemudian berkembang pesat, sejalan dengan munculnya gerakan "Third Wave of Coffee" pada akhir abad ke-20.
Gerakan ini mendorong para konsumen untuk melihat kopi seperti halnya anggur—sebagai produk pertanian yang memiliki karakteristik unik berdasarkan :
- Varietas
- Asal
- Cara Pemrosesan
''')

st.markdown(''' Tujuan melakukan Clustering ini adalah untuk mengidentifikasi karakteristik pelanggan dimana dalam kasus ini adalah menggunakan Karakteristik-karakteristik,seperti :
- Recency
- Frequency
- Monetary
- Category

Dimana setelah setelah mengetahui karakteristik karakteristik diatas lalu data tersebut diolah untuk melakukan pemetaan cluster dari data yang diperoleh tersebut,lalu setelah dimasukkan mesin akan mengolah data tersebut guna memahami dengan karakteristik sebagai berikut termasuk kedalam cluster yang mana.

Dalam Project ini algoritma yang digunakan adalah menggunakan algoritma K-Means,dimana Algoritma K-Means sendiri sering digunakan dalam project-project berbasis unsupervised learning,dimana algoritma ini memiliki keuntungan yang diantaranya adalah :
- Cepat dan efisien, terutama pada dataset yang besar.
- Mudah dipahami dan diimplementasikan.''')



