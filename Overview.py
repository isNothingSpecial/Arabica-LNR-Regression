import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import importlib

## data

st.set_page_config(page_title="Homepage",layout="wide")
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
    st.markdown(''' **Sejarah Singkat Sribu** :
- **2011** : Sribu diluncurkan sebagai platform kontes desain yang berfokus pada pasar Indonesia, menawarkan berbagai kategori seperti desain logo, desain kemasan, dan desain interior.
- **2012** : Menerima pendanaan awal dari East Ventures, yang memungkinkan ekspansi layanan.
- **2014** : Mendapat investasi tambahan dari Asteria Japan dan memperluas kategori layanan untuk mencakup lebih dari sekadar desain grafis.
- **2018** : Menerima pendanaan dari Crowdworks, pasar freelance terbesar di Jepang.
- **2022** : Diakuisisi oleh Mynavi Japan dan menjadi anak perusahaan mereka.
''')

with col2:
    st.markdown('''**Pencapaian Sribu** :
- Hingga tahun 2022, Sribu telah melayani lebih dari 30.000 klien dengan komunitas freelancer yang dikurasi secara ketat untuk memastikan kualitas dalam komunikasi, ketepatan waktu, dan hasil kerja.
- Sribu juga telah menerima beberapa penghargaan, termasuk Indonesia ICT Awards 2013 dan SparxUp Award 2011
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
