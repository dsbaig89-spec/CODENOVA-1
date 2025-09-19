import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from preprocess import load_symptom_data

def train_model():
    df = load_symptom_data()  # automatically uses backend/data/symptoms.csv
    X = df["all_symptoms"]
    y = df["Disease"]

    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", MultinomialNB())
    ])

    model.fit(X, y)

    # Save model
    model_dir = os.path.join(os.path.dirname(__file__), "model")
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "symptom_classifier.pkl")
    joblib.dump(model, model_path)
    print(f"✅ Model trained and saved at {model_path}")

if __name__ == "__main__":
    train_model()
