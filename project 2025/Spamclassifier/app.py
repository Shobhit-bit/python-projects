import string
import streamlit as st
import pandas as pd
import pickle
from nltk.corpus import stopwords
import nltk
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# Download the stopwords corpus if it's not already downloaded
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

X_tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
bern_model = pickle.load(open('bern_model.pkl', 'rb'))
Gausnb_model = pickle.load(open('Gausnb_model.pkl', 'rb'))
knn_model = pickle.load(open('knn_model.pkl', 'rb'))
LR_model = pickle.load(open('LR_model.pkl', 'rb'))
Multinb_model = pickle.load(open('Multinb.pkl', 'rb'))
RF_model = pickle.load(open('RF_model.pkl', 'rb'))
svm_model = pickle.load(open('svm_model.pkl', 'rb'))

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


st.title('Sms spam classifier')
input_text = st.text_area('Enter a message to classify')


if st.button('Predict'):
    if input_text:
        # 1. Preprocess the input text
        transformed_sms = transform_text(input_text)

        # 2. Vectorize the preprocessed text
        vector_text = X_tfidf.transform([transformed_sms])

        # 3. Make the prediction for different model
        # The vectorizer's sparse output needs to be converted to a dense array for BernoulliNB
        prediction_bern = bern_model.predict(vector_text.toarray())[0]
        if prediction_bern==1:
            prediction_bern = 'Spam'
        else:
            prediction_bern = 'Not Spam'

        # The vectorizer's sparse output needs to be converted to a dense array for GaussianNB
        prediction_gausnb = Gausnb_model.predict(vector_text.toarray())[0]
        if prediction_gausnb==1:
            prediction_gausnb = 'Spam'
        else:
            prediction_gausnb = 'Not Spam'

        prediction_knn = knn_model.predict(vector_text)[0]
        if prediction_knn==1:
            prediction_knn = 'Spam'
        else:
            prediction_knn = 'Not Spam'

        prediction_LR = LR_model.predict(vector_text)[0]
        if prediction_LR==1:
            prediction_LR = 'Spam'
        else:
            prediction_LR = 'Not Spam'

        prediction_Multinb = Multinb_model.predict(vector_text)[0]
        if prediction_Multinb==1:
            prediction_Multinb = 'Spam'
        else:
            prediction_Multinb = 'Not Spam'

        prediction_RF = RF_model.predict(vector_text)[0]
        if prediction_RF==1:
            prediction_RF = 'Spam'
        else:
            prediction_RF = 'Not Spam'

        prediction_SVM = svm_model.predict(vector_text)[0]
        if prediction_SVM==1:
            prediction_SVM = 'Spam'
        else:
            prediction_SVM = 'Not Spam'

        # 4. Display the result
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