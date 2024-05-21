# irisclassifier

This is a Flask application that implements a Suport Vector Classifier (SVC) model to classify iris flowers based on their sepal and petal characteristics (sepal length, sepal width, petal length, petal width). The model is trained on the Iris flower dataset from the UCI Machine Learning Repository.

**Deployment**
This application is deployed on Heroku (or your preferred hosting platform).

**Usage**

*1. Accessing the Application:*

The deployed application is accessible through the following URL:

https://dashboard.heroku.com/apps/irisclassifier/deploy/github

*2. User Interface:*

The application currently provides a basic user interface. You can interact with the model by making a GET request to the root path (/). This will trigger the model to predict the flower species based on the default iris flower data.

**Dependencies**
This application uses the following Python libraries:

Flask
scikit-learn
Jinja2 (for templating, if applicable)

*Note:* The specific versions of these libraries should be listed in a requirements.txt file for easy deployment.

