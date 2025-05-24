import streamlit as st
from PIL import Image
from components.image_uploader import upload_image
from components.chatbot import chatbot_popup

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
}

#perkiraan-kebutuhan-pasar {
  text-align: center;
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


col1, spacer, col2 = st.columns([1, 0.05, 1])

with col1:
    st.markdown("#### Deteksi Penyakit Tanaman Cabai")
    image = upload_image()

    if image:
        st.success("Gambar berhasil diunggah!")

with col2:
    with st.container(border=True):
        chatbot_popup()


st.markdown("<br>", unsafe_allow_html=True)
st.markdown("#### Perkiraan Kebutuhan Pasar")

st.markdown("<br>", unsafe_allow_html=True)
chart_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Value": [500, 350, 550, 400, 500, 450, 380, 580, 380, 450, 500, 550]
}

# Create a simple line chart
st.line_chart(chart_data, x="Month", y="Value")