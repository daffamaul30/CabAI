import streamlit as st
from PIL import Image
from components.image_uploader import upload_image

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
</style>
""",
    unsafe_allow_html=True,
)

# --- Header ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/logo.png", width=300)


st.markdown("#### Deteksi Penyakit Tanaman Cabai")
image = upload_image()

if image:
    st.success("Gambar berhasil diunggah!")

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("#### Perkiraan Kebutuhan Pasar")

st.markdown("<br>", unsafe_allow_html=True)
chart_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Value": [500, 350, 550, 400, 500, 450, 380, 580, 380, 450, 500, 550]
}

# Create a simple line chart
st.line_chart(chart_data, x="Month", y="Value")


# --- Chatbox (Placeholder) ---
