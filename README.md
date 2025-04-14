# Iris Flower Classifier 🌸 (Flask Deployment)

This is a simple web-based machine learning app that classifies Iris flowers based on their sepal and petal measurements. It uses a Logistic Regression model trained on the popular Iris dataset, and the app is built using Flask.

---

## 🔧 Technologies Used

- Python
- Flask
- scikit-learn
- HTML (Jinja templates)
- Render (for free deployment)

---

## 💡 How it Works

1. The user enters sepal and petal measurements into a web form.
2. The data is sent to a Flask backend.
3. A trained Logistic Regression model (`iris_model.pkl`) predicts the flower type.
4. The result is shown back on the web page.

---

## 🧠 Model Details

- Dataset: Iris dataset from `sklearn.datasets`
- Model: Logistic Regression
- Accuracy: Trained with ~80% test accuracy

---

## 🚀 Live Demo

🔗 [Click here to open the deployed app](https://iris-classifier-d0a0.onrender.com)

---

## 📂 Project Structure

Any_Of_Your_Folder/
  ├── app.py
  ├── iris_model.pkl    #it will create automatically when you run the train_model.py
  ├── train_model.py
  ├── requirements.txt
  └── template/
      └── index.html
