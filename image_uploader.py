import streamlit as st
from PIL import Image
import time
import streamlit.components.v1 as components

from io import BytesIO
from classify import classify_image_with_gemini

def deteksi_penyakit(image_bytes):
    GOOGLE_API_KEY = "AIzaSyCNQi8CXPlLeeu3j1vVu0-t2NfZf2uHLco"

    with st.spinner("Sedang menganalisis gambar..."):
        try:
            hasil = classify_image_with_gemini(image_bytes, GOOGLE_API_KEY)
            st.session_state.hasil_klasifikasi = hasil  # Simpan ke session_state

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")


def upload_image():

    col1, col2 = st.columns([1, 1], vertical_alignment="center")
    with col1:
        uploaded_file = st.file_uploader("", label_visibility="collapsed", type=["jpg", "jpeg"])
    with col2:
      if uploaded_file is not None:
          image = Image.open(uploaded_file)

          st.image(image, use_container_width=True)

          img_bytes = BytesIO()
          image.save(img_bytes, format="JPEG")
          image_bytes = img_bytes.getvalue()
      else:
          st.image("https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/stock.jpg", use_container_width=True)

    # Tombol deteksi
    st.markdown(
    """
    <style>
    .st-emotion-cache-1gulkj5 {
        display: flex;
        flex-direction: column;
        height: 350px;
        justify-content: center !important;
    }
    div[data-testid="stFileUploaderDropzoneInstructions"] {
        text-align: center !important;
        justify-content: center !important;
        width: 100% !important;
        margin-bottom: 20px !important;
    }
    .st-emotion-cache-nwtri {
        display: none !important;
    }

    .e16xj5sw5 {
      margin-top: -65px;
      margin-bottom: 12px;
    }

    /* Define a class for your button */
    button[kind="secondary"] {
        width: 100% !important;
    }
    button[kind="primary"] {
        background-color: #008000 !important;
        color: white !important;
        padding: 10px 20px !important;
        border-radius: 5px !important;
        border: 2px solid #008000 !important;
        cursor: pointer !important;
        transition: background-color 0.3s ease !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2) !important;
        height: 40px !important;
    }
    button[kind="primary"]:hover {
        background-color: #fff !important;
        color: #008000 !important;
        border: 2px solid #008000 !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    left, middle, right = st.columns(3)
    if middle.button('Deteksi Penyakit', type="primary", use_container_width=True):
      if uploaded_file is not None:
          deteksi_penyakit(image_bytes)
      else:
          st.warning("⚠️ Silakan unggah gambar terlebih dahulu sebelum melakukan deteksi.")

    if "hasil_klasifikasi" in st.session_state:
        hasil = st.session_state.hasil_klasifikasi
        st.markdown(f"**Kategori:** `{hasil.get('klasifikasi', 'Tidak diketahui')}`")
        st.markdown(f"**Alasan:** {hasil.get('alasan', '-')}")
        if hasil.get('klasifikasi', 'Tidak diketahui') != "Penyakit Tidak Dapat Diidentifikasi":
          if st.button('Tanyakan Solusi', use_container_width=True):
              # Simpan prompt ke session state
              st.session_state.user_input = f"Tanaman cabai saya terdeteksi kategori '{hasil.get('klasifikasi', 'Tidak diketahui')}'. Apa solusi yang bisa saya lakukan?"
