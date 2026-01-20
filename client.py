# FILE: client.py
import streamlit as st
import requests

URL = "http://127.0.0.1:8000/mahasiswa"

st.title("Aplikasi Kampus")

menu = st.sidebar.selectbox("Menu", ["Lihat Data", "Tambah Data"])

if menu == "Lihat Data":
    st.header("Data Mahasiswa")
    if st.button("Refresh"):
        try:
            r = requests.get(URL)
            st.table(r.json())
        except:
            st.error("Server belum nyala!")

elif menu == "Tambah Data":
    st.header("Tambah Mahasiswa")
    with st.form("form"):
        nama = st.text_input("Nama")
        nim = st.text_input("NIM")
        jurusan = st.text_input("Jurusan")
        if st.form_submit_button("Simpan"):
            data = {"nama": nama, "nim": nim, "jurusan": jurusan}
            try:
                requests.post(URL, json=data)
                st.success("Berhasil!")
            except:
                st.error("Gagal koneksi server")