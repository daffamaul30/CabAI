import streamlit as st
from PIL import Image
import time
import streamlit.components.v1 as components

def deteksi_penyakit():
    st.success("Fungsi deteksi dijalankan!")

def upload_image():

    # components.html(
    #     """
    #     <style>
          
    #     #fileInput {
    #         display: none !important;
    #     }

    #     .labelInput {
    #         display: flex;
    #         flex-direction: column;
    #         align-items: center;
    #         width: 100%;
    #         height: 500px !important;
    #         background-color: #F4F4F4;
    #         color: #008000;
    #         text-align: center;
    #         border-radius: 5px;
    #         font-size: 80px;
    #         font-weight: 600 !important;
    #         cursor: pointer;
    #     }
    #     </style>
    #     """,
    #     height=100
    # )
    col1, col2 = st.columns([1, 1])
    with col1:
      uploaded_file = st.file_uploader("", label_visibility="collapsed", type=["jpg", "jpeg", "png"])
    with col2:
      if uploaded_file is not None:
          image = Image.open(uploaded_file)

          st.image(image, use_container_width=True)
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
    }
    button[kind="primary"]:hover {
        background-color: #fff !important;
        color: #008000 !important;
        border: 2px solid #008000 !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5) !important;
    }
    .detect-button {
        background-color: #008000;
        color: white;
        margin: 20px;
        padding: 10px 20px;
        border-radius: 5px;
        border: 2px solid #008000;
        cursor: pointer;
        transition: background-color 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Define the hover state for the button */
    .detect-button:hover {
        background-color: #fff;
        color: #008000;
        border: 2px solid #008000;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
    left, middle, right = st.columns(3)
    if middle.button('Deteksi Penyakit', type="primary", use_container_width=True):
      deteksi_penyakit()

    # return uploaded_file if detect and uploaded_file is not None else None
