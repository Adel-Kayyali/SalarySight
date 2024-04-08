from pymongo import MongoClient
from utils.model_predictions import load_model
from dotenv import load_dotenv
import os

load_dotenv()
mongo_uri = os.getenv('MONGO_URI')

if not mongo_uri:
    raise RuntimeError("MONGO_URI is not set in the environment variables.")

client = MongoClient(mongo_uri)
db = client.salary_data
model = load_model('model/xgboost_regressor_model.pkl')


def get_db():
    return db


def get_model():
    return model
