from flask import request

def create_input_vector(request_form, feature_names):
    size_mapping = {
        '1 to 50 employees': 0,
        '51 to 200 employees': 1,
        '201 to 500 employees': 2,
        '501 to 1000 employees': 3,
        '1001 to 5000 employees': 4,
        '5001 to 10000 employees': 5,
        '10000+ employees': 6
    }

    input_vector = {column: 0 for column in feature_names}

    input_vector['Job Title_' + request_form['job_title']] = 1
    input_vector['Type of ownership_' + request_form['type_of_ownership']] = 1
    input_vector['Industry_' + request_form['industry']] = 1

    selected_size = request_form['size']
    input_vector['Size'] = size_mapping[selected_size]

    input_vector['Rating'] = float(request_form['rating']) if request_form['rating'] else 0
    input_vector['Founded'] = int(request_form['founded_year']) if 'founded_year' in request_form and request_form['founded_year'] else 0

    return input_vector
