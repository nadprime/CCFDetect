import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('fraud_detection_model.pkl')

# Define the interface for the Streamlit app
st.title('Fraud Detection App')

transaction_amount = st.text_input('Transaction Amount')
merchant_category = st.selectbox('Merchant Category', ['Grocery', 'Entertainment', 'Travel', 'Other'])
card_type = st.selectbox('Card Type', ['Visa', 'Mastercard', 'American Express'])

features = pd.DataFrame({
    'Transaction Amount': [transaction_amount],
    'Merchant Category': [merchant_category],
    'Card Type': [card_type]
})

if st.button('Detect Fraud'):
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.error('This transaction is fraudulent')
    else:
        st.success('This transaction is not fraudulent')
