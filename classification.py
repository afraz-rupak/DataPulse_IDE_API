import os
import pandas as pd
from sklearn.metrics import accuracy_score



BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Path to project folder

def evaluate_classification(user_df, event_code):
    try:
        api_csv_path = os.path.join(BASE_DIR, "csv", f"{event_code}_actual.csv")

        print(f"🔍 Looking for file: {api_csv_path}")

        if not os.path.exists(api_csv_path):
            return "API CSV not found"

        api_df = pd.read_csv(api_csv_path)

        if len(api_df) != len(user_df):
            return "File type Error"

        y_true = api_df['actual']
        y_pred = user_df['prediction']
        score = accuracy_score(y_true, y_pred)
        return round(score, 4)

    except Exception as e:
        return f"Evaluation error: {str(e)}"

