import streamlit as st
import google.generativeai as genai
import os

# Konfigurasi Gemini API Key dari Hugging Face Secrets atau variabel lokal
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Inisialisasi model Gemini
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# Inisialisasi session state untuk chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def generate_response(user_input):
    system_prompt = (
        "Sicabai adalah penyuluh pertanian profesional yang ahli dalam budidaya, pengendalian hama, pemupukan, "
        "dan panen pada tanaman cabai. Jawablah setiap pertanyaan dengan akurat, singkat, dan mudah dipahami oleh petani.\n"
    )

    chat = st.session_state.chat_history

    # Ambil hingga 5 percakapan terakhir
    history_text = "\n".join([
        f"Farmer: {m['message']}" if m["role"] == "farmer" else f"Sicabai: {m['message']}"
        for m in chat[-5:] if m["message"] != system_prompt
    ])

    prompt = f"{system_prompt}\n{history_text}\nFarmer: {user_input}\nSicabai:"

    # Kirim prompt ke Gemini
    response = model.generate_content(prompt)
    bot_output = response.text.strip()

    # Tambahkan ke chat history
    st.session_state.chat_history.append({
        "role": "sicabai",
        "avatar": "https://raw.githubusercontent.com/daffamaul30/CabAI/main/assets/sicabai.png",
        "message": bot_output
    })

    return bot_output

# UI Streamlit
st.title("💬 Sicabai: Chatbot Cabai Pakai Gemini")

user_input = st.text_input("Masukkan pertanyaanmu di sini:")

if st.button("Tanya Sicabai"):
    if user_input:
        st.session_state.chat_history.append({"role": "farmer", "message": user_input})
        with st.spinner("Sicabai lagi mikir... 🌶️"):
            bot_reply = generate_response(user_input)
            st.success("✅ Sicabai menjawab:")
            st.markdown(bot_reply)
    else:
        st.warning("Tolong masukkan pertanyaan terlebih dahulu.")

# Menampilkan riwayat chat
if st.session_state.chat_history:
    st.subheader("Riwayat Obrolan:")
    for chat in reversed(st.session_state.chat_history):
        role_label = "👩‍🌾 Petani" if chat["role"] == "farmer" else "🌶️ Sicabai"
        st.markdown(f"**{role_label}:** {chat['message']}")