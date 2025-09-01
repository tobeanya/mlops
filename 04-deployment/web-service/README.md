## Deploying a ML model as a web service

* Create virtual env with pipenv
* Create script for prediction
* Put script in Flask app
* Run with Gunicornn
    * gunicorn --bind=0.0.0.0:9696 predict:app

* Package app in Docker
    * docker build -t ride-duration-prediction-service:v1 .
    * docker run -it --rm -p 9696:9696 ride-duration-prediction-service:v1

