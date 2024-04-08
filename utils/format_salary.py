def format_salary(salary):
    # Round the salary to the nearest thousand and then create the range
    rounded_salary = round(salary / 1000) * 1000
    lower_bound = rounded_salary - 5000
    upper_bound = rounded_salary + 5000
    return f"{lower_bound // 1000}K-{upper_bound // 1000}K"
