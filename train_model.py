{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "a433a7c5-9df0-431d-ae12-b1f27a482c8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.97\n",
      "Model and scaler saved successfully.\n"
     ]
    }
   ],
   "source": [
    "# train_model.py (Replace with your actual training script path)\n",
    "\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.svm import SVC\n",
    "from sklearn.metrics import accuracy_score\n",
    "import pickle\n",
    "\n",
    "# Load the dataset (adjust URL if needed)\n",
    "url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'\n",
    "col_name = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']\n",
    "df = pd.read_csv(url, names=col_name)\n",
    "\n",
    "# Split into features and target\n",
    "X = df.drop(['class'], axis=1)\n",
    "y = df['class']\n",
    "\n",
    "# Split the dataset into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)\n",
    "\n",
    "# Scale the features\n",
    "scaler = StandardScaler()\n",
    "X_train_scaled = scaler.fit_transform(X_train)\n",
    "X_test_scaled = scaler.transform(X_test)\n",
    "\n",
    "# Train the SVM model\n",
    "model = SVC(kernel='linear', random_state=42)\n",
    "model.fit(X_train_scaled, y_train)\n",
    "\n",
    "# Predict the labels of the test data\n",
    "y_pred = model.predict(X_test_scaled)\n",
    "\n",
    "# Calculate the accuracy score\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(f\"Accuracy: {accuracy:.2f}\")\n",
    "\n",
    "# Save the model and scaler to a file using pickle\n",
    "try:\n",
    "    with open('model_scaler_iris.pkl', 'wb') as file:\n",
    "        pickle.dump((model, scaler), file)\n",
    "    print(\"Model and scaler saved successfully.\")\n",
    "except Exception as e:\n",
    "    print(\"Error occurred while saving the model and scaler:\", e)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13058cee-ba05-4074-bf1e-30827c4d5ba6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
