import streamlit as st

def chatbot_popup():
    
    st.markdown(
    """
    <style>
      button[data-testid="stChatInputSubmitButton"] {
          color: green !important;
      }

      div[data-testid="stChatInput"] {
        border: 3px solid #008000 !important;
        border-radius: 20px !important;
      }

      div[data-testid="stVerticalBlockBorderWrapper"] div[height="400"] {
        border: 3px solid #008000 !important;
        border-radius: 10px !important;
      }

      div[data-testid="stVerticalBlockBorderWrapper"] {
        padding-top: 0 !important;
      }
    </style>
    """,
    unsafe_allow_html=True
)
    col1, col2 = st.columns([4, 1])  # col2 lebih sempit di kanan
    with col2:
      st.image("https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/logo.png", width=100, use_container_width=True)
    
    messages = st.container(height=400)
    messages.chat_message("assistant").write("Hi! Ada yang bisa saya bantu?")
    if prompt := st.chat_input("Tuliskan pertanyaanmu..."):
        messages.chat_message("user").write(prompt)
