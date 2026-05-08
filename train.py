import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset/reviews.csv")

# Remove spaces
data.columns = data.columns.str.strip()

# Features
X = data["text_"]

# Labels
y = data["label"]

# IMPORTANT:
# OR = Genuine
# CG = Fake

print(data["label"].value_counts())

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Pipeline
model = Pipeline([

    ("tfidf", TfidfVectorizer(
        stop_words="english",
        lowercase=True,
        ngram_range=(1,2)
    )),

    ("classifier", LogisticRegression(
        max_iter=2000
    ))

])

# Train
model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy * 100:.2f}%")

# TEST CHECKS
print(model.predict([
    "This product changed my life completely buy now."
]))

print(model.predict([
    "The delivery was fast and packaging was excellent."
]))

# Save
joblib.dump(model, "model.pkl")

print("Model trained successfully!")