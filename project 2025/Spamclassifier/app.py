import string
import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import stopwords
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

X_tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
bern_model = pickle.load(open('bern_model.pkl', 'rb'))
Gausnb_model = pickle.load(open('Gausnb_model.pkl', 'rb'))
knn_model = pickle.load(open('knn_model.pkl', 'rb'))
LR_model = pickle.load(open('LR_model.pkl', 'rb'))
Multinb_model = pickle.load(open('Multinb.pkl', 'rb'))
RF_model = pickle.load(open('RF_model.pkl', 'rb'))
svm_model = pickle.load(open('svm_model.pkl', 'rb'))

performance_metrics = {
        'Multinomial NB': {'accuracy': 0.9739, 'precision': 1.0000},
        'SVM': {'accuracy': 0.9797, 'precision': 0.9844},
        'Bernoulli NB': {'accuracy': 0.9787, 'precision': 0.9920},
        'Gaussian NB': {'accuracy': 0.8830, 'precision': 0.5536},
        'Logistic Regression': {'accuracy': 0.9497, 'precision': 0.9346},
        'KNN': {'accuracy': 0.9072, 'precision': 1.0000},
        'Random Forest': {'accuracy': 0.9778, 'precision': 1.0000},
    }

def transform_text(text):
    text = text.lower()

    # 1. Tokenize the text and remove non-alphanumeric characters
    y = []
    for char in text:
        if char.isalnum() or char.isspace():  # Keep spaces to split words later
            y.append(char)
    text = "".join(y)

    # 2. Tokenize into words and remove stopwords and punctuation
    y = []
    for word in text.split():
        if word not in stopwords.words('english') and word not in string.punctuation:
            y.append(word)

    return " ".join(y)

def pred(text):
    if text == 1:
        text = 'Spam'
    else:
        text = 'Not Spam'
    return text

st.set_page_config(page_title="SMS Spam Classifier", layout="wide")

st.sidebar.title("Navigation")

page = st.sidebar.radio("Go to", ["Classifier", "About the Project", "Model Performance"])

if page == "Classifier":
    st.title("Sms Spam Classifier")
    input_text = st.text_area("Enter a message to classify")
    if st.button('Predict'):
        if input_text:
            transformed_sms = transform_text(input_text)

            vector_text = X_tfidf.transform([transformed_sms])

            prediction_bern = bern_model.predict(vector_text.toarray())[0]
            pred(prediction_bern)

            prediction_gausnb = Gausnb_model.predict(vector_text.toarray())[0]
            pred(prediction_gausnb)

            prediction_knn = knn_model.predict(vector_text)[0]
            pred(prediction_knn)

            prediction_LR = LR_model.predict(vector_text)[0]
            pred(prediction_LR)

            prediction_Multinb = Multinb_model.predict(vector_text)[0]
            pred(prediction_Multinb)

            prediction_RF = RF_model.predict(vector_text)[0]
            pred(prediction_RF)

            prediction_SVM = svm_model.predict(vector_text)[0]
            pred(prediction_SVM)

            df = pd.DataFrame(
                [
                    {"Model": "Bernoulli Naive bayes Prediction", "Prediction" :prediction_bern},
                    {"Model": "Gaussian Naive bayes Prediction", "Prediction": prediction_gausnb},
                    {"Model": "Multinomial Naive bayes Prediction","Prediction" : prediction_Multinb},
                    {"Model": "Logistic Regression Prediction", "Prediction": prediction_LR},
                    {"Model": "SVM Prediction", "Prediction": prediction_SVM},
                    {"Model": "KNN Prediction", "Prediction": prediction_knn},
                    {"Model": "Random Forest Prediction", "Prediction": prediction_RF}

                ])
            st.dataframe(df, use_container_width=True)

        else:
            st.warning('Please enter a message to classify.')

elif page == "Model Performance":
    st.title("Model Performance Metrics")
    st.markdown("This section presents the performance metrics of the trained models on the test set.")

    # Create DataFrame for bar chart
    performance_df = pd.DataFrame(performance_metrics).T.reset_index().rename(columns={'index': 'Algorithm'})
    melted_df = pd.melt(performance_df, id_vars=['Algorithm'], var_name='Metric', value_name='Score')
    st.subheader("Algorithm vs. Accuracy and Precision")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=melted_df, x='Algorithm', y='Score', hue='Metric', ax=ax)
    ax.set_ylim(0.5, 1.1)
    ax.set_title("Algorithm vs Accuracy and Precision")
    plt.xticks(rotation=20, ha='right')
    plt.tight_layout()
    st.pyplot(fig)


elif page == "About the Project":
    st.title("About the SMS Spam Classifier")
    st.markdown("""
    ### Project Overview
    * **Project Name:** SMS Spam Classifier
    * **Goal:** To classify a given SMS message as either "Spam" or "Not Spam". This is a supervised machine learning problem.

    ### How It Works
    The project follows a standard Natural Language Processing (NLP) pipeline to achieve the classification:
    1.  **Data Preprocessing:** Incoming text messages are first cleaned to prepare them for the models.
        * **Lowercasing:** All text is converted to lowercase for consistency.
        * **Punctuation and URL Removal:** Unwanted characters like punctuation and URLs are removed to reduce noise.
        * **Chat Word Expansion:** Common chat abbreviations (e.g., 'u' to 'you') are expanded to improve model understanding.
        * **Stop Word Removal:** Common English words that do not add significant meaning (e.g., "the", "is") are filtered out.
    2.  **Feature Extraction:** The cleaned text is then transformed into a numerical format that machine learning models can understand. We use a **TF-IDF (Term Frequency-Inverse Document Frequency)** vectorizer to weigh the importance of each word in a message.
    3.  **Machine Learning Models:** The vectorized data is used to train and test several classification models. The web app showcases predictions from a diverse set of classifiers, including:
        * Naive Bayes (Multinomial, Gaussian, Bernoulli)
        * Support Vector Machine (SVM)
        * Logistic Regression
        * K-Nearest Neighbors (KNN)
        * Random Forest

    ### Technology Stack
    * **Programming Language:** Python
    * **Web Framework:** Streamlit
    * **Key Libraries:** `scikit-learn` for machine learning, `pandas` for data manipulation, `nltk` for NLP tasks, `matplotlib` and `seaborn` for data visualization.
    """)