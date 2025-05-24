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

      div[data-testid="stChatMessage"]:has(img[alt="sicabai avatar"]) {
        flex-direction: row-reverse !important;
      }

      div[data-testid="stChatMessage"]:has(div[aria-label="Chat message from sicabai"]) {
        text-align: right !important;
      }

      div[data-testid="stChatMessage"]:has(div[aria-label="Chat message from sicabai"]) p {
        border-radius: 10px !important;
        border: 2px solid #008000 !important;
        padding: 2px 10px !important;
        width: fit-content !important;
      }

      div[data-testid="stMarkdownContainer"]:has(p)  {
        display: flex;
        justify-content: end;
      }

    </style>
    """,
    unsafe_allow_html=True
)
    col1, col2 = st.columns([4, 1])  # col2 lebih sempit di kanan
    with col2:
      st.image("https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/logo.png", width=100, use_container_width=True)
    
    messages = st.container(height=400)
    messages.chat_message("sicabai", avatar="https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/sicabai.png").write("Hi! Ada yang bisa saya bantu?")
    if prompt := st.chat_input("Tuliskan pertanyaanmu..."):
        messages.chat_message("user").write(prompt)
