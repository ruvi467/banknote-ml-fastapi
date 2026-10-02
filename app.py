import uvicorn
from fastapi import FastAPI
from Banknote import Banknote
import pickle
import pandas as pd

app = FastAPI()

# Load the trained ML model
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


# Home route
@app.get("/")
def home():
    return {"message": "Banknote Prediction API is running"}


# Prediction route
@app.post("/predict")
def predict_banknote(data: Banknote):

    # Convert Pydantic model to dictionary
    data = data.model_dump()

    # Get input values
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]

    # Create DataFrame using the same feature names
    # that were used during model training
    input_data = pd.DataFrame([{
        "variance": variance,
        "skewness": skewness,
        "curtosis": curtosis,
        "entropy": entropy
    }])

    # Make prediction
    prediction = classifier.predict(input_data)

    # Convert prediction into readable text
    if prediction[0] > 0.5:
        prediction = "Fake note"
    else:
        prediction = "Its a Bank note"

    return {
        "prediction": prediction
    }


# Start the server
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=5001
    )