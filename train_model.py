import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
import joblib

# Load the dataset
df = pd.read_csv('phishdataset.csv')

# Convert timestamp to numerical features
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.dayofweek
df['month'] = df['timestamp'].dt.month

# Encode categorical variables
label_encoder = LabelEncoder()
df['sender'] = label_encoder.fit_transform(df['sender'])
df['subject'] = label_encoder.fit_transform(df['subject'])
df['keywords'] = label_encoder.fit_transform(df['keywords'])
df['label'] = label_encoder.fit_transform(df['label'])

# Select features
features = ['sender', 'subject', 'keywords', 'has_url', 'has_attachment', 'sender_length', 'hour', 'day_of_week', 'month']
X = df[features]
y = df['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Train the SVM model
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

# Save the trained model
joblib.dump(clf, 'phishing_model.joblib')
joblib.dump(label_encoder, 'label_encoder.joblib')

print("Model trained and saved successfully.")
print(f"Training accuracy: {clf.score(X_train, y_train):.2f}")
print(f"Testing accuracy: {clf.score(X_test, y_test):.2f}")
