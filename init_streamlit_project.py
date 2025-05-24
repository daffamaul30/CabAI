import os

folders = [
    "pages",
    "components",
    "utils",
    "assets",
    "data"
]

files = {
    "main.py": '''import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="🧠")

st.title("Beranda Aplikasi Streamlit")
st.write("Selamat datang di aplikasi Streamlit kamu 🎉")
''',
    "README.md": "# Streamlit App\nDeskripsi aplikasi Streamlit kamu.",
    "requirements.txt": "streamlit",
    "components/sidebar.py": "# Fungsi sidebar akan dibuat di sini",
    "utils/data_loader.py": "# Fungsi untuk load data",
    "utils/formatter.py": "# Fungsi untuk formatting data",
    "config.py": "# Konfigurasi umum bisa didefinisikan di sini",
    "assets/favicon.png": "",  # placeholder, bisa ganti manual nanti
    "pages/1_dashboard.py": "# Halaman Dashboard",
    "pages/2_data_upload.py": "# Halaman Upload Data"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Struktur Streamlit project berhasil dibuat!")
