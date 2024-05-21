# irisclassifier

This is a Flask application that implements a Suport Vector Classifier (SVC) model to classify iris flowers based on their sepal and petal characteristics (sepal length, sepal width, petal length, petal width). The model is trained on the Iris flower dataset from the UCI Machine Learning Repository.

**Data**

The dataset contains 150 data points, with 50 samples from each Iris species.
Each data point has four features:
Sepal length (cm)
Sepal width (cm)
Petal length (cm)
Petal width (cm)
Target Variable:

The target variable is the Iris species (setosa, versicolor, or virginica).

*Popularity:*

Due to its simplicity, clear structure, and availability in many machine learning libraries, the Iris flower dataset is a popular choice for:

- Introducing machine learning concepts like classification and supervised learning.
- Evaluating and comparing the performance of different classification algorithms.
- Teaching the basics of data exploration and visualization.

*Limitations:*

The dataset is very small compared to modern datasets used in machine learning.
It has a low number of features (only four) and is not very high-dimensional.
Because the dataset is so well-known, some algorithms might overfit to it, leading to poor performance on unseen data.

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

