# import library dan framework yang diperlukan
import streamlit as st
from pandas import DataFrame
# import proses tabel segitiga bawah
from controller.cyk_algorithm.triangular_table import *
# mengurai kalimat menggunakan algoritma CYK
def parse(cnf, list_of_string):
    # mempersiapkan table filling
    table = create_table(list_of_string)
    # menampilkan kedalam web
    st.table(DataFrame(table, columns=list_of_string))
    # isi iterasi pertama (baris paling bawah di tabel pengisian)
    filling_bottom(table, cnf, list_of_string)
    # menampilkan kedalam web
    st.table(DataFrame(table, columns=list_of_string))
    # isi semua tabel pengisian dan tunjukkan status penerimaan
    filling_all(cnf, table, list_of_string)