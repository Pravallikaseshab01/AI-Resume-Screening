import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("resume_data.csv")

# Debugging step: Print column names
print("Columns in dataset:", df.columns)

# ✅ Use "Skills" instead of "Resume Text"
X = df["Skills"]
y = df["Job Title"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a text processing + classification pipeline
vectorizer = TfidfVectorizer(stop_words='english')
model = MultinomialNB()

pipeline = make_pipeline(vectorizer, model)

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate the model
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model
joblib.dump(pipeline, "model.pkl")

print("✅ Model training complete! Model saved as 'model.pkl'")
