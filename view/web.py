# impor streamlit sebagai kerangka ujung depan
import streamlit as st

# impor fungsi yang diperlukan
from controller.open_file import open_file
from controller.raw_conversion import raw_to_cfg
from controller.cyk_algorithm.cyk_parse import parse

# siapkan tampilan web
def run_streamlit():
    # konfigurasi halaman web
    st.set_page_config(layout='wide')
    # mempersiapkan aturan cnf
    raw_cfg = open_file('model/cnf.txt')
    # konversi format raw aturan cnf agar dapat terbaca oleh python
    cnf = raw_to_cfg(raw_cfg)
    # membuat Heading judul pada halaman web
    st.title('Cek Kalimat Baku dengan Algoritma CYK - Kelompok 1 (E)')
    # split web menjadi dua kolom, kolom kanan menampilkan aturan cnf, kolom kiri menampilkan tabel pengisian
    col1, col2 = st.columns(2, gap='small')

    # bagian kolom kiri
    with col1:
        # menampilkan form input kalimat
        string_input = st.text_input('Masukan kalimat bahasa Indonesia', placeholder="Masukan kalimat bahasa Indonesia")
        # konversi kalimat menjadi list kata yang dipisahkan oleh spasi
        list_string = string_input.split(' ')
        # menampilkan button
        button_click = st.button('Cek Kalimat', type='primary')
        # jika button di klik
        if button_click:
            if button_click:
                # menampilkan error ketika tidak ada string atau hanya memasukan 1 string
                if len(list_string) <= 1:
                    st.error("Kalimat tidak boleh kosong ataupun satu kata")
                # jika yang kalimat yang dimasukan lebih dari satu kata
                elif string_input != '':
                    st.write('<br><p>Filling Table:</p>', unsafe_allow_html=True)
                    parse(cnf, string_input.split(' '))

    # bagian kolom kanan
    with col2:
        # menampilkan Aturan CNF
        st.write("Aturan CNF:")
        st.write(raw_cfg)