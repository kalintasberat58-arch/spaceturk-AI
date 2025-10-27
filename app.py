import streamlit as st
from openai import OpenAI
import os

# OpenAI API anahtarını ortam değişkeninden al
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="🚀 SpaceTurk AI", page_icon="🤖", layout="centered")

st.title("🚀 SpaceTurk AI 2.0")
st.markdown("Komutan, ben buradayım! Her türlü soruna cevap vermeye hazırım. 💬")

# Kullanıcıdan girdi al
user_input = st.text_input("Sen:", placeholder="Bana bir şey sor Komutan...")

if user_input:
    with st.spinner("Yanıt hazırlanıyor..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Sen Spaceturk AI adlı, kullanıcıya 'Komutan' diye hitap eden akıllı bir yardımcı botsun."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.success("Spaceturk AI:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Hata oluştu: {e}")
