from flask import Flask, render_template, request
import pickle
import numpy as np
import os

# Load the trained model
model = pickle.load(open("iris_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]
        prediction = model.predict([features])
        class_names = ['Setosa', 'Versicolor', 'Virginica']
        predicted_class = class_names[prediction[0]]
        return render_template("index.html", prediction=f"Predicted Iris Class: {predicted_class}")
    except Exception as e:
        return render_template("index.html", prediction=f"Error: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port, debug=True)
