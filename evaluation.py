from classification import evaluate_classification
from regression import evaluate_regression
import pandas as pd

# 🔐 Reference event code used to find the API CSV file
API_EVENT_CODE = "EVT123"

def evaluate_submission(file_obj, event_type):
    # ✅ Check file extension
    if not file_obj.filename.lower().endswith('.csv'):
        return {"error": "File type error: Only CSV files are accepted."}

    try:
        user_df = pd.read_csv(file_obj)
    except Exception as e:
        return {"error": f"Failed to read CSV: {str(e)}"}

    # ✅ Route based on event type
    if event_type.lower() == "classification":
        score = evaluate_classification(user_df, API_EVENT_CODE)
        return {"score": score}
    elif event_type.lower() == "regression":
        score = evaluate_regression(user_df, API_EVENT_CODE)
        return {"score": score}
    else:
        return {"error": "Event type error"}
