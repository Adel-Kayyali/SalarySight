def insert_prediction(document, predictions_collection):
    # Convert numpy.float32 to native Python float for predicted_salary
    document['predicted_salary'] = float(document['predicted_salary'])
    document['predicted_salary_range'] = document['predicted_salary_range']

    predictions_collection.insert_one(document)
