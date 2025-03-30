import pandas as pd
from sklearn.metrics import accuracy_score
import os

def evaluate_classification(user_df, event_code):
    try:
        # ✅ Step 1: Load the API CSV from the "csv" folder
        api_csv_path = os.path.join("csv", f"{event_code}_actual.csv")
        if not os.path.exists(api_csv_path):
            return "API CSV not found"

        api_df = pd.read_csv(api_csv_path)

        # ✅ Step 2: Compare column names
        '''if list(api_df.columns) != list(user_df.columns):
            return "File type Error"
'''
        # ✅ Step 3: Compare row count
        if len(api_df) != len(user_df):
            return "File type Error"

        # ✅ Step 4: Calculate accuracy score
        y_true = api_df['actual']
        y_pred = user_df['prediction']
        score = accuracy_score(y_true, y_pred)
        return round(score, 4)

    except Exception as e:
        return f"Evaluation error: {str(e)}"
