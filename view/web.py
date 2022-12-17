import streamlit as st

from controller.open_file import open_file
from controller.raw_conversion import raw_to_cfg
from controller.cyk_algorithm.cyk_parse import parse

def run_streamlit():
    st.set_page_config(layout='wide')
    
    raw_cfg = open_file('model/cnf.txt')
    cnf = raw_to_cfg(raw_cfg)

    st.title('String Checker with CYK Algorithm')

    col1, col2 = st.columns(2, gap='small')

    with col1:
        string_input = st.text_input('Masukan kalimat bahasa Indonesia', placeholder="Masukan kalimat bahasa Indonesia")
        button_click = st.button('Cek Kalimat', type='primary')
        if button_click:
            st.write('<br><p>Filling Table:</p>', unsafe_allow_html=True)
            parse(cnf, string_input.split(' '))

    with col2:
        st.write("### CNF Rules:")
        st.write(raw_cfg)

    


    