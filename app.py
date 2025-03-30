from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from evaluation import evaluate_submission
from waitress import serve
app = Flask(__name__)
UPLOAD_FOLDER = 'csv'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load secrets from environment variables
API_EVENT_CODE = os.getenv("API_EVENT_CODE")
API_SECURITY_CODE = os.getenv("API_SECURITY_CODE")

@app.route('/submit', methods=['POST'])
def submit_csv():
    file = request.files.get('file')
    event_code = request.form.get('event_code')
    security_code = request.form.get('security_code')
    event_type = request.form.get('event_type')

    if not all([file, event_code, security_code, event_type]):
        return jsonify({"error": "Missing data"}), 400

    filename = secure_filename(f"{event_code}_actual.csv")
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Check for valid event and security codes
    if event_code == API_EVENT_CODE and security_code == API_SECURITY_CODE:
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        if os.path.exists(filepath):
            os.remove(filepath)
        file.save(filepath)
        return jsonify({"message": "CSV saved successfully"}), 200
    else:
        result = evaluate_submission(file, event_type)
        return jsonify(result)

mode = ''
if __name__ == '__main__':
    if mode == 'dev':
        app.run(debug=True)
    else:
        serve(app, host='0.0.0.0', port=5000, threads=2)
