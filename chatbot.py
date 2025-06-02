import streamlit as st
from generate_chat import generate_response

def chatbot_popup():
    # ==== CSS Custom Styling ====
    st.markdown(
        """
        <style>
        button[data-testid="stChatInputSubmitButton"] {
            color: green !important;
        }
        div[data-testid="stChatInput"] {
            border: 4px solid #008000 !important;
            border-radius: 10px !important;
            overflow: hidden !important;
            margin-top: 15px !important;
        }
        div[data-testid="stChatInput"] div {
            border-radius: 0px !important;
            background-color: #ffffff !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] div[height="450"] {
            border: 3px solid #008000 !important;
            border-radius: 10px !important;
        }
        div[data-testid="stVerticalBlockBorderWrapper"] {
            padding-top: 0 !important;
        }
        div[data-testid="stChatMessage"]:has(img[alt="sicabai avatar"]) {
            flex-direction: row-reverse !important;
        }
        div[aria-label="Chat message from sicabai"] {
            border-radius: 10px !important;
            border: 2px solid #FF0000 !important;
            padding: 2px 10px !important;
            width: fit-content !important;
            max-width: 450px !important;
            margin: 0
        }
        div[aria-label="Chat message from farmer"] {
            border-radius: 10px !important;
            border: 2px solid #008000 !important;
            padding: 2px 10px !important;
            width: fit-content !important;
            max-width: 450px !important;
            margin: 0
        }
        div[data-testid="stChatMessage"] {
            padding: 10px 0px 0px !important;
        }
        div[data-testid="stVerticalBlock"]:has(div[data-testid="stChatMessage"] img) {
            gap: 0px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # ==== Logo Header ====
    col1, col2 = st.columns([4, 1])
    with col2:
        st.image("https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/logo.png", width=100, use_container_width=True)

    # Chat History
    if "chat_history" not in st.session_state:
      st.session_state.chat_history = [
        {
            "role": "sicabai",
            "avatar": "https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/sicabai.png",
            "message": "Halo! Saya Sicabai, penyuluh pertanian spesialis tanaman cabai. Apa yang bisa saya bantu hari ini?"
        }
    ]

    messages = st.container(height=450)

    # Render chat history
    for msg in st.session_state.chat_history:
        messages.chat_message(msg["role"], avatar=msg["avatar"]).markdown(msg["message"])

    # Chat input
    if prompt := st.chat_input("Tuliskan pertanyaanmu..."):
        # Append user message
        st.session_state.chat_history.append({
            "role": "farmer",
            "avatar": "https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/farmer.png",
            "message": prompt
        })
        messages.chat_message("farmer", avatar="https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/farmer.png").write(prompt)

        with st.spinner("SiCabAI sedang berpikir..."):
            generate_response(prompt)

        st.rerun()  # Refresh to render response

    if st.session_state.get("user_input"):
        st.session_state.chat_history.append({
            "role": "farmer",
            "avatar": "https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/farmer.png",
            "message": st.session_state.user_input
        })
        messages.chat_message("farmer", avatar="https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/farmer.png").write(st.session_state.user_input)
        with st.spinner("SiCabAI sedang berpikir..."):
            generate_response(st.session_state.user_input)
        st.session_state.user_input = None
        st.rerun()
