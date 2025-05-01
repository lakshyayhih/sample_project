import streamlit as st
from textblob import TextBlob

st.title("🧠 Text Sentiment Analyzer")

user_input = st.text_area("Enter your sentence here:")

if st.button("Analyze"):
    if user_input:
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity

        st.write(f"**Sentiment Score:** {sentiment:.2f}")

        if sentiment > 0:
            st.success("This is a Positive statement 😊")
        elif sentiment < 0:
            st.error("This is a Negative statement 😠")
        else:
            st.info("This is Neutral 😐")
    else:
        st.warning("Please enter some text.")
