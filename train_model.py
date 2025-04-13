import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import joblib

# Load the dataset
df = pd.read_csv('/home/nerd/seymour/capston/phishdataset.csv')  # Update with the actual path to your dataset

# Preprocess the data
df = pd.get_dummies(df, columns=['sender', 'subject', 'keywords'])
X = df.drop('label', axis=1)  # features
y = df['label']  # labels

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

# Train the SVM model
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

# Save the trained model
joblib.dump(clf, 'phishing_model.joblib')

print("Model trained and saved successfully.")
