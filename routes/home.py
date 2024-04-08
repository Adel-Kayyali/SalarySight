from flask import Blueprint, request, render_template

from db_setup import get_db, get_model
from static.constants import feature_names
from utils.data_processing import create_input_vector
from utils.database_operations import insert_prediction
from utils.model_predictions import make_prediction

home_blueprint = Blueprint('home', __name__, template_folder='templates')


@home_blueprint.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        db = get_db()
        model = get_model()

        input_vector = create_input_vector(request.form, feature_names)

        predicted_salary = make_prediction(model, input_vector, feature_names)

        # Format the predicted salary into a range
        def format_salary(salary):
            rounded_salary = round(salary / 1000) * 1000
            lower_bound = rounded_salary - 5000
            upper_bound = rounded_salary + 5000
            return f"{lower_bound // 1000}K-{upper_bound // 1000}K"

        formatted_salary = format_salary(predicted_salary)

        # Prepare the document to insert into MongoDB
        document_to_insert = {
            'job_title': request.form['job_title'],
            'type_of_ownership': request.form['type_of_ownership'],
            'industry': request.form['industry'],
            'company_size': request.form['size'],
            'rating': input_vector['Rating'],
            'founded_year': input_vector['Founded'],
            'predicted_salary': predicted_salary,
            'predicted_salary_range': formatted_salary
        }

        # Insert the document into MongoDB
        predictions_collection = db.predictions
        insert_prediction(document_to_insert, predictions_collection)

        return render_template('result.html', prediction=formatted_salary)

    return render_template('index.html')
