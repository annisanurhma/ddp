import streamlit as st

st.title('aplikasi Data Diri')
st.header('Biodata Pribadi') 

nama = st.text_input('nama', max_chars=16)
st.write(f'nama saya adalah {nama}')

with st.form("biodata"):
        st.write("Masukan biodata anda")
        nama = st.text_input("Nama")
        email = st.text_input("Email")
        usia = st.number_input("Usia",min_value=0, max_value=100, step=1)
        
    
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(f'Nama saya adalah {nama}, Email saya {email} dan usia saya adalah {usia}') 