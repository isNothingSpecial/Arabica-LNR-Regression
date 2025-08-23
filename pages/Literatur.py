import streamlit as st

def show_literatur_page():
    st.header("📚 Literatur & Informasi")
    st.write("Jelajahi informasi mendalam tentang kopi dan cara kerja aplikasi ini.")

    # --- Bagian 1: Tentang Aplikasi Ini ---
    st.markdown("---")
    st.subheader("💡 Tentang Aplikasi Ini")
    st.write(
        "Aplikasi ini adalah sebuah inisiatif data science yang didukung oleh AI untuk membantu Anda memahami dan memprediksi kualitas kopi. "
        "Menggunakan model regresi linier yang dilatih dengan data dari **Specialty Coffee Association (SCA)**, aplikasi ini dapat memprediksi total skor "
        "kualitas kopi (Total Cup Points) berdasarkan atribut sensoriknya."
    )

    # --- Bagian 2: Memahami Penilaian Kopi ---
    st.markdown("---")
    st.subheader("☕ Memahami Sistem Penilaian Kopi")
    
    # Gunakan expander untuk menyembunyikan/menampilkan detail
    with st.expander("Apa itu Cupping dan Total Cup Points?"):
        st.write(
            "**Cupping** adalah metode standar untuk mengevaluasi kualitas kopi. Seorang juru cicip (cupper) akan menilai kopi berdasarkan 10 atribut "
            "yang berbeda, seperti aroma, rasa, dan keasaman. **Total Cup Points** adalah skor total dari semua penilaian tersebut, "
            "yang menjadi indikator utama kualitas kopi."
        )

    with st.expander("Kategori Kualitas Kopi"):
        st.write(
            "Berikut adalah klasifikasi standar yang digunakan dalam aplikasi ini:"
        )
        st.markdown(
            """
            * **90-100 poin**: **Kopi Spesialti Luar Biasa**. Kualitas istimewa, kompleks, dan unik.
            * **85-89.99 poin**: **Kopi Spesialti Sangat Baik**. Karakteristik yang menonjol dan seimbang.
            * **80-84.99 poin**: **Kopi Spesialti**. Ambang batas minimum untuk disebut kopi spesialti.
            * **Di bawah 80 poin**: **Kopi Non-Spesialti**. Tidak memenuhi standar kualitas spesialti.
            """
        )

    # --- Bagian 3: Fakta Menarik tentang Kopi ---
    st.markdown("---")
    st.subheader("🌍 Fakta dan Atribut Utama Kopi Arabika")
    
    # Gunakan columns untuk tata letak yang lebih rapi
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Perbedaan Arabika & Robusta**")
        st.write(
            "Arabika cenderung memiliki rasa yang lebih kompleks dan keasaman yang cerah, sementara Robusta memiliki rasa yang lebih kuat, pahit, dan kadar kafein lebih tinggi."
        )

    with col2:
        st.markdown("**Pengaruh Ketinggian (Altitude)**")
        st.write(
            "Kopi yang ditanam di dataran tinggi (high-altitude) biasanya memiliki biji yang lebih padat dan matang lebih lambat, menghasilkan rasa yang lebih kompleks dan keasaman yang lebih baik."
        )

    st.markdown("---")
    
    # Opsi untuk kembali atau lanjut ke halaman lain
    if st.button("Kembali ke Halaman Utama"):
        st.session_state.page = "main"

# Contoh penggunaan di app.py
# if 'page' not in st.session_state:
#     st.session_state.page = "main"
# if st.session_state.page == "main":
#     # Kode untuk halaman utama
#     if st.button("Jelajahi Literatur"):
#         st.session_state.page = "literatur"
# elif st.session_state.page == "literatur":
#     show_literatur_page()
