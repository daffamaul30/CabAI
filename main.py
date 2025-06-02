# "c:\Users\daffa\AppData\Local\Programs\Python\Python312\python.exe"

import streamlit as st
from PIL import Image
from image_uploader import upload_image
from chatbot import chatbot_popup
from demand_forecast import forecast


# --- Page Configuration ---
st.set_page_config(
    page_title="CabAI",
    page_icon="https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/icon.png", # Replace with your CabAI favicon URL
    layout="centered"
)

st.markdown(
    """
<style>
.stAppHeader {
    display: none;
}
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}
#deteksi-penyakit-tanaman-cabai {
  text-align: center;
  margin-bottom: 20px;
}

#perkiraan-kebutuhan-pasar {
  text-align: center;
  margin-top: 20px;
}
.stMainBlockContainer {
  max-width: 1280px !important;
}
</style>
""",
    unsafe_allow_html=True,
)

# --- Header ---
left, middle, right = st.columns(3)
middle.image("https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/logo.png", width=100, use_container_width=True)


st.markdown("<br>", unsafe_allow_html=True)
st.markdown("#### Deteksi Penyakit Tanaman Cabai")
col1, spacer, col2 = st.columns([1, 0.05, 1])

with col1:
    upload_image()

with col2:
    with st.container(border=True):
        chatbot_popup()


st.markdown("<br>", unsafe_allow_html=True)
st.markdown("#### Perkiraan Kebutuhan Pasar")

model, scaler, kebutuhan_asli, kebutuhan_scaled = prepare_forecast_data()

# Inisialisasi session_state hanya sekali
if 'prediksi_scaled' not in st.session_state:
    st.session_state.prediksi_scaled = []
    st.session_state.input_scaled = kebutuhan_scaled[-12:].tolist()
    st.session_state.tanggal_terakhir = kebutuhan_asli.index[-1]

# Penjelasan
st.write("Prediksi dilakukan per bulan berdasarkan 12 bulan terakhir.")

with st.spinner("Sedang Menghitung Kebutuhan Pasar..."):
    forecast()
