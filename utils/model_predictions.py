import pickle
import pandas as pd

def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def make_prediction(model, input_vector, feature_names):
    input_df = pd.DataFrame([input_vector])
    input_df = input_df[feature_names]
    return model.predict(input_df)[0]
