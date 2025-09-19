# preprocess.py
import os
import pandas as pd

# ---------------------------
# Symptom & Disease Data
# ---------------------------
def load_symptom_data(path=None):
    """
    Load the symptoms dataset.
    Returns a DataFrame with columns: ['all_symptoms', 'Disease']
    """
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "data", "DiseaseAndSymptoms.csv")
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Symptom CSV file not found: {path}")
    
    df = pd.read_csv(path)
    
    # Normalize text
    df = df.applymap(lambda x: str(x).strip().lower() if isinstance(x, str) else x)
    
    # Combine all symptom columns into a single string
    symptom_cols = df.columns.drop("Disease")
    df["all_symptoms"] = df[symptom_cols].apply(lambda row: " ".join(row.dropna().astype(str)), axis=1)
    
    return df[["all_symptoms", "Disease"]]

def load_precaution_data(path=None):
    """
    Load the precautions dataset.
    Returns a dictionary: {Disease: {Description, Precaution1, Precaution2, ...}}
    """
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "data", "Disease_precautions.csv")
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Precautions CSV file not found: {path}")
    
    df = pd.read_csv(path)
    
    # Normalize text
    df = df.applymap(lambda x: str(x).strip().capitalize() if isinstance(x, str) else x)
    
    return df.set_index("Disease").to_dict(orient="index")

# ---------------------------
# Chatbot Data
# ---------------------------
def load_chatbot_data(paths=None):
    """
    Load chatbot CSV(s) and return a dictionary: {input: response}
    """
    if paths is None:
        paths = [
            os.path.join(os.path.dirname(__file__), "data", "chatbot_data.csv")
        ]

    chatbot_dict = {}
    for path in paths:
        if os.path.exists(path):
            df = pd.read_csv(path)
            # Normalize
            df = df.applymap(lambda x: str(x).strip().lower() if isinstance(x, str) else x)
            chatbot_dict.update(dict(zip(df['Input'], df['Response'])))
        else:
            print(f"⚠️ Chatbot CSV not found: {path}")

    return chatbot_dict

# ---------------------------
# Quick test
# ---------------------------
if __name__ == "__main__":
    try:
        df_symptoms = load_symptom_data()
        print("✅ Symptoms CSV loaded successfully")
        print(df_symptoms.head())
    except Exception as e:
        print("❌ Error loading symptoms CSV:", e)
    
    try:
        precautions = load_precaution_data()
        print("✅ Precautions CSV loaded successfully")
        print(list(precautions.items())[:3])
    except Exception as e:
        print("❌ Error loading precautions CSV:", e)
    
    try:
        chatbot_dict = load_chatbot_data()
        print("✅ Chatbot CSV loaded successfully")
        print(list(chatbot_dict.items())[:5])
    except Exception as e:
        print("❌ Error loading chatbot CSV:", e)
