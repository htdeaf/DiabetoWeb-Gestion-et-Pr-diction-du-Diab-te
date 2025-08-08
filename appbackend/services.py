import joblib

model = joblib.load("model.pkl")

def predict_diabetes(glucose, bmi, age, pedigree):
    input_data = [[glucose, bmi, age, pedigree]]
    prediction = model.predict(input_data)[0]
    return prediction
