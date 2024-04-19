import streamlit as st
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

st.title("Text Generation App")
st.write("Enter a starting prompt and let the AI continue the story!")

prompt = st.text_input("Prompt:", "")
max_length = st.slider("Max Generated Length", 50, 200, 100)

if st.button("Generate"):
  generated_text = generator(prompt, max_length=max_length, num_return_sequences=1)[0]['generated_text']
  st.write("Generated Text:")
  st.success(generated_text)
