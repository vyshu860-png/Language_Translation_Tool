import streamlit as st
from deep_translator import GoogleTranslator
st.title("Language Translation Tool")
st.caption("SAM AI TECHNOLOGIES | Created by kunchala Naga vaishnavi")
st.write("Translate text from one language to another easily")
text = st.text_area("enter your text:",placeholder="example: Hoe are you?")
language = {"English" : "en",
"Telugu" : "te",
"Hindi" : "hi",
"Tamil" : "ta",
"Malayam" : "ml",
"Bengali" : "bn",
"Kannada" : "kn",
"Marathi" : "mr",
"Gujarati" : "gu",
"Punjabi" : "pa",
"French" : "fr",
"German" : "de",
"Spanish" : "es",
"Japanese" : "ja",
"Korean" : "ko",
"Chinese" : "zh-CN"

}
target_language = st.selectbox("Select target language:",list(language.keys()))
if st.button("Translate"):
    if text.strip():
        try:
            translated_text = GoogleTranslator(Source = "auto",target = language[target_language]).translate(text)
            st.subheader("Translated_text:")
            st.success(translated_text)
        except Exception as e:
            st.error("Translation failed.Please check your internet connection")
    else:
            st.warning("Please enter some text first.")

