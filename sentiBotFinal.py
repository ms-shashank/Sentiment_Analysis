import streamlit as st
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def sentiBotAnalyzer(input):
    sentiment = SentimentIntensityAnalyzer()
    statement = sentiment.polarity_scores(input)

    return  statement['pos'], statement['neg'], statement['neu'], statement['compound']

def analyzeCompound(comp):
    if comp < 0:
        return "Negative"
    elif 0 <= comp <= 0.4:
        return "Neutral"
    elif 0.4 < comp:
        return "Postive"


st.header("Sentiment Analysis Bot ")
st.subheader("I will analyze the customer review of the products ")

text = st.text_input("Enter a sentence to analyze ")
if st.button("Submit"):
    w, x, y, z  = sentiBotAnalyzer(text)
    review = analyzeCompound(z)
    st.write(review)
    #st.write(w, x, y, z)
else:
    print("Nothing is printing right now")
