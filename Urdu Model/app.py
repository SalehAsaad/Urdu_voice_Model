import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/RichardErkhov/traversaal-llm-regional-languages_-_Unsloth_Urdu_Llama3_1_FP16_PF100-gguf"
HF_TOKEN = "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"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("🇵🇰 Urdu Chatbot – Hugging Face API")

prompt = st.text_area("💬 اپنا سوال لکھیں:")

if st.button("جواب حاصل کریں"):
    with st.spinner("ماڈل سے رابطہ کیا جا رہا ہے..."):
        output = query({
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 256
            }
        })
        if "error" in output:
            st.error(f"❌ Error: {output['error']}")
        else:
            st.markdown("### 🤖 جواب:")
            st.write(output[0]["generated_text"])
