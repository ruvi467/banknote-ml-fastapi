


# 🏦 Banknote Authentication ML API

A machine learning project that predicts whether a banknote is **genuine or fake** using a Random Forest classifier and exposes the trained model through a FastAPI REST API.

## 🚀 Project Overview

This project demonstrates an end-to-end Machine Learning workflow:

**Dataset → Preprocessing → Model Training → Evaluation → FastAPI → Prediction**

## 🧠 Machine Learning

- **Algorithm:** Random Forest Classifier
- **Dataset:** Banknote Authentication Dataset
- **Features:** Variance, Skewness, Curtosis, Entropy
- **Train/Test Split:** 80/20
- **Framework:** Scikit-learn

## ⚡ FastAPI

The trained ML model is integrated with FastAPI to provide a prediction API.

### `POST /predict`

**Request:**

json
{
  "variance": 3.6216,
  "skewness": 8.6661,
  "curtosis": -2.8073,
  "entropy": -0.44699
}


**Response:**

json
{
  "prediction": "Its a Bank note"
}



FastAPI Swagger UI can be used to test the API directly.

## 🛠️ Tech Stack

**Python** • **Pandas** • **NumPy** • **Scikit-learn** • **FastAPI** • **Pydantic** • **Uvicorn** • **Postman** • **Git & GitHub**

## 📂 Project Structure


banknote-ml-fastapi/
│
├── app.py
├── Banknote.py
├── modelTraining.ipynb
├── data_banknote_authentication.csv
├── requirements.txt
├── pyproject.toml
├── uv.lock
└── README.md


 Train the model

Run the cells in `modelTraining.ipynb` to train the model and generate the trained model file.


## 🧪 Testing

The API has been tested using:

* FastAPI Swagger UI
* Postman

## 🔮 Future Improvements

* Add a web-based frontend
* Add detailed model evaluation metrics
* Add automated tests
* Dockerize the application
* Deploy the API to the cloud
* Add CI/CD with GitHub Actions

## 👨‍💻 Author

**Ruvina N**

Computer Science Engineering Student | Machine Learning • AI • Backend Development



