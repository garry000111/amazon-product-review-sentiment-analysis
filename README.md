# Amazon Product Review Sentiment Analysis

## Project Overview

This project focuses on classifying Amazon product reviews into **Positive** and **Negative** sentiments using Natural Language Processing (NLP), Machine Learning, and Deep Learning techniques.

The project includes a complete NLP pipeline starting from data preprocessing and exploratory data analysis to model training, evaluation, and deployment using Streamlit.

---

## Dataset

Dataset: Amazon Fine Food Reviews Dataset

The dataset contains over **500,000 customer reviews** collected from Amazon products.

### Features Used

* **Text** – Customer review text
* **Score** – Rating provided by the customer

### Sentiment Mapping

| Score | Sentiment         |
| ----- | ----------------- |
| 1, 2  | Negative (0)      |
| 4, 5  | Positive (1)      |
| 3     | Removed (Neutral) |

Final Dataset Size: **525,814 Reviews**

---

## Project Workflow

### 1. Data Understanding

* Dataset inspection
* Missing value analysis
* Class distribution analysis

### 2. Exploratory Data Analysis (EDA)

* Review length distribution
* Score distribution
* Word frequency analysis
* Word Cloud visualization

### 3. Text Preprocessing

* Lowercasing
* HTML tag removal
* Punctuation removal
* Stopword removal
* Tokenization
* Lemmatization

### 4. Feature Engineering

#### Classical Machine Learning

* TF-IDF Vectorization

#### Deep Learning

* Tokenization
* Sequence Generation
* Padding

---

## Models Implemented

### Machine Learning Models

* Logistic Regression
* Naive Bayes
* Random Forest
* XGBoost

### Deep Learning Models

* LSTM (Long Short-Term Memory)

---

## Model Performance

| Model               | Accuracy |
| ------------------- | -------: |
| Logistic Regression |   91.24% |
| XGBoost             |   89.60% |
| Random Forest       |   89.00% |
| Naive Bayes         |   86.67% |
| LSTM                |   84.34% |

### Best Model

**Logistic Regression + TF-IDF** achieved the highest accuracy of **91.24%** and was selected for deployment.

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* NLTK
* TensorFlow / Keras
* XGBoost
* Streamlit
* Joblib

---

## Project Structure

```text
AmazonSentimentAnalysis/
│
├── app/
│   └── streamlit_app.py
│
├── models/
│   ├── logistic_model.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── tokenizer.pkl
│   └── lstm_sentiment.keras
│
├── notebooks/
│   └── sentiment_analysis.ipynb
│
├── requirements.txt
└── README.md
```

---

## Streamlit Deployment

The trained Logistic Regression model was deployed using Streamlit.

### Features

* Enter Amazon review text
* Predict sentiment
* Display Positive/Negative prediction
* Show confidence score

---

## Key Learnings

* Natural Language Processing (NLP)
* Text Preprocessing
* TF-IDF Vectorization
* Machine Learning Model Comparison
* Deep Learning with LSTM
* Model Evaluation
* Streamlit Deployment

---

## Future Improvements

* BERT-based sentiment analysis
* Hyperparameter tuning
* Docker deployment
* Cloud deployment
* Real-time review monitoring

---

## Author

**Gaurav Khambat**

Computer Science Student | Machine Learning Enthusiast
