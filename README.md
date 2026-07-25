# 🛒 Amazon Product Review Sentiment Analysis

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
  ![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?logo=streamlit&logoColor=white)
  ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-0.24%2B-F7931E?logo=scikit-learn&logoColor=white)
  ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-FF6F00?logo=tensorflow&logoColor=white)
  ![License](https://img.shields.io/badge/License-MIT-green.svg)

  **An End-to-End NLP Pipeline for classifying customer feedback into positive and negative sentiments.**
</div>

---

## 📖 Table of Contents
- [Project Overview](#-project-overview)
- [Dataset Details](#-dataset-details)
- [Project Workflow](#-project-workflow)
- [Model Performance](#-model-performance)
- [Technologies Used](#-technologies-used)
- [Installation & Usage](#-installation--usage)
- [Project Structure](#-project-structure)
- [Future Roadmap](#-future-roadmap)

---

## 🚀 Project Overview

Customer reviews are a goldmine of information. This project leverages **Natural Language Processing (NLP)**, **Machine Learning**, and **Deep Learning** to automatically classify Amazon product reviews into **Positive** or **Negative** sentiments. 

It encompasses the entire machine learning lifecycle—from raw data preprocessing and exploratory data analysis (EDA) to model training, evaluation, and an interactive web deployment using Streamlit.

---

## 📊 Dataset Details

The project utilizes the **Amazon Fine Food Reviews Dataset**, comprising over 500,000 customer reviews.

### Sentiment Mapping Strategy
To frame this as a binary classification problem, neutral 3-star reviews were discarded. The remaining ratings were mapped as follows:

| Rating (Stars) | Sentiment Classification | Target Value |
| :--- | :--- | :--- |
| ⭐ / ⭐⭐ | **Negative** | `0` |
| ⭐⭐⭐⭐ / ⭐⭐⭐⭐⭐ | **Positive** | `1` |

> **Final Processed Dataset Size:** 525,814 Reviews

---

## ⚙️ Project Workflow

1. **Exploratory Data Analysis (EDA):** Analyzed review length distributions, class imbalances, and generated Word Clouds to discover frequent textual patterns.
2. **Text Preprocessing:** Cleaned the raw text by lowercasing, stripping HTML tags/punctuation, removing stopwords, tokenizing, and lemmatizing.
3. **Feature Engineering:**
   - *Classical ML:* Transformed text to numerical vectors using **TF-IDF Vectorization**.
   - *Deep Learning:* Prepared sequences via **Tokenization and Padding**.
4. **Model Training:** Experimented with multiple architectures to find the optimal balance of accuracy and computational efficiency.

---

## 🧠 Model Performance

We tested a variety of algorithms. Here is how they stacked up:

| Model | Architecture Type | Accuracy |
| :--- | :--- | ---: |
| 🏆 **Logistic Regression** | Linear / Classical ML | **91.24%** |
| **XGBoost** | Tree Ensemble | 89.60% |
| **Random Forest** | Tree Ensemble | 89.00% |
| **Naive Bayes** | Probabilistic | 86.67% |
| **LSTM** | Deep Learning (RNN) | 84.34% |

**Winning Model:** The **Logistic Regression + TF-IDF** combination provided the best performance (91.24%) and fastest inference time, making it the perfect candidate for production deployment.

---

## 💻 Technologies Used

* **Language:** Python
* **Data Handling:** Pandas, NumPy
* **Visualization:** Matplotlib, WordCloud
* **Machine Learning:** Scikit-Learn, XGBoost
* **Deep Learning:** TensorFlow, Keras
* **NLP:** NLTK
* **Deployment:** Streamlit, Joblib

---

## 🛠️ Installation & Usage

Want to run this project locally? Follow these steps:

### 1. Clone the repository
```bash
git clone [https://github.com/yourusername/AmazonSentimentAnalysis.git](https://github.com/yourusername/AmazonSentimentAnalysis.git)
cd AmazonSentimentAnalysis

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### 3.Install dependencies
```bash
pip install -r requirements.txt

### 4.Run the Streamlit App
```bash
streamlit run app/streamlit_app.py

## 📁 Project Structure

AmazonSentimentAnalysis/
│
├── app/
│   └── streamlit_app.py          # Interactive web UI
│
├── models/
│   ├── logistic_model.pkl        # Best performing ML model
│   ├── tfidf_vectorizer.pkl      # Saved text vectorizer
│   ├── tokenizer.pkl             # Deep learning tokenizer
│   └── lstm_sentiment.keras      # Saved LSTM model
│
├── notebooks/
│   └── sentiment_analysis.ipynb  # Full EDA, preprocessing, and training pipeline
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
