# **User Documentation** 

---

```markdown
# 📘 User Documentation – CSV Evaluation API

Welcome to the CSV Evaluation API! This service allows you to upload a CSV file to either:

- ✅ Save it as a reference dataset (if authorized)
- 📊 Evaluate it based on a **classification** or **regression** task

---

## 🔗 API Endpoint

```
POST http://<your-server-url>/submit
```

> Replace `<your-server-url>` with your actual domain or server IP (e.g., `https://your-api.onrender.com/submit`)

---

## 📝 Required Parameters (Form Data)

| Field           | Type   | Required | Description                                                  |
|------------------|--------|----------|--------------------------------------------------------------|
| `file`          | File   | ✅        | CSV file with columns: `actual`, `prediction`                |
| `event_code`    | String | ✅        | The event code provided by the API owner (`EVT123`)          |
| `security_code` | String | ✅        | The security code provided by the API owner (`SEC456`)       |
| `event_type`    | String | ✅        | Must be either `classification` or `regression`              |

---

## 📂 CSV Format Requirements

### Required Columns:
```
id, prediction
```

### ✅ Sample Content:
```csv
id,prediction
1,1
2,1
3,1
4,0
```

- Column names **must match exactly**
- Column order must be `id`, `prediction`
- Row count must match the API reference CSV

---

## ✅ Example Request (Using `curl`)

```bash
curl -X POST http://<your-server-url>/submit \
  -F "file=@submission.csv" \
  -F "event_code=EVT123" \
  -F "security_code=SEC456" \
  -F "event_type=classification"
```

---

## ⚙️ Logic & Behavior

### ✅ If `event_code` **and** `security_code` match:
- The uploaded CSV file will be **saved as** `/csv/EVT123_actual.csv`
- If a file with the same name exists, it will be **overwritten**

### ⚠️ If codes do **not match**:
- The uploaded file will be **evaluated** against the API reference file (`EVT123_actual.csv`)
  - If `event_type = classification` → returns **accuracy score**
  - If `event_type = regression` → returns **R² score**

---

## 📈 Example Responses

### ✅ File Saved:
```json
{
  "message": "CSV saved successfully"
}
```

### ✅ Score Returned:
```json
{
  "score": 0.875
}
```

### ❌ Errors:
```json
{ "error": "Missing data" }

{ "error": "File type error: Only CSV files are accepted." }

{ "error": "File type Error" }

{ "error": "API CSV not found" }

{ "error": "Event type error" }
```

---

