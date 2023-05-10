from flask import Flask, request
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return 'Hello, world!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Use the data to make a prediction with the model
    prediction = model.predict(data)
    return str(prediction)

if __name__ == '__main__':
    app.run(debug=True)
