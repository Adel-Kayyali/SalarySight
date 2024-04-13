
# SalarySight - Salary Prediction App

SalarySight is a web application that provides salary estimates in the United States based on job titles, company size, industry, and other factors.

## Features

- Predict salary ranges for various job titles and industries
- User-friendly web interface
- Dark mode toggle for comfortable viewing

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or higher
- Flask
- MongoDB account and cluster
- Docker (optional for containerization)

### Installing

1. **Clone the repository:**

```bash
git clone https://github.com/your-github-username/salarysight.git
cd salarysight
```

2. **Set up a virtual environment:**

- Linux
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

- Windows
```bash
python -m venv venv
source `venv\Scripts\activate` 
```

3. **Install the required packages:**

```bash
pip install -r requirements.txt
```

4. **Set up the environment variables:**

Create a `.env` file in the project root directory and add the following:

```env
MONGO_URI=your_mongodb_connection_string
FLASK_APP=app.py
FLASK_ENV=development
```

Replace `your_mongodb_connection_string` with your actual MongoDB connection string.

5. **Run the application:**

```bash
flask run
```

### Using Docker

If you prefer to use Docker, make sure you have Docker installed and running on your machine.

1. **Build the Docker image:**

```bash
docker build -t salarysight .
```

2. **Run the Docker container:**

```bash
docker run -p 5000:5000 -e MONGO_URI="your_mongodb_connection_string" salarysight
```

### Deployment

For production environments, it's recommended to use a production-ready server such as Gunicorn and serve the application behind a web server like Nginx or Apache.

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [MongoDB](https://www.mongodb.com/) - Database platform used
- [XGBoost](https://xgboost.readthedocs.io/) - Machine learning library for the prediction model

## Authors

- **Adel Kayyali** - *Initial work* - [Adel Kayyali](https://www.linkedin.com/in/adel-kayyali-082051293/).

## License

This project is licensed under the MIT License.
