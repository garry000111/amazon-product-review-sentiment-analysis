import streamlit as st
import joblib

# Load saved model and vectorizer
model = joblib.load("models/logistic_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# App title
st.title("Amazon Product Review Sentiment Analysis")

st.write(
    "Enter an Amazon product review and predict whether the sentiment is Positive or Negative."
)

# User input
review = st.text_area(
    "Enter Review",
    height=150
)

if st.button("Predict Sentiment"):

    review_vector = vectorizer.transform([review])

    prediction = model.predict(review_vector)[0]

    probability = model.predict_proba(review_vector)[0]

    confidence = max(probability) * 100

    if prediction == 1:
        st.success(
            f"Positive Review 😊 | Confidence: {confidence:.2f}%"
        )
    else:
        st.error(
            f"Negative Review 😞 | Confidence: {confidence:.2f}%"
        )