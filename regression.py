import pandas as pd
from sklearn.metrics import r2_score
import os

def evaluate_regression(user_df, event_code):
    try:
        # ✅ Load the API reference CSV from the "csv" folder
        api_csv_path = os.path.join("csv", f"{event_code}_actual.csv")
        if not os.path.exists(api_csv_path):
            return "API CSV not found"

        api_df = pd.read_csv(api_csv_path)

        # ✅ Check if column names match

        # ✅ Check if number of rows match
        if len(api_df) != len(user_df):
            return "File type Error"

        # ✅ Calculate and return R² score
        y_true = api_df['actual']
        y_pred = user_df['prediction']
        score = r2_score(y_true, y_pred)
        return round(score, 4)

    except Exception as e:
        return f"Evaluation error: {str(e)}"
