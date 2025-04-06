
# Aadhaar-Linked Health Card Portal with Federated Learning

This is a demo-ready mock health application designed for showcasing Aadhaar-linked patient data access and Federated Learning (FL)-powered risk prediction for healthcare scenarios in India. The project combines secure login, record management, and real-time AI risk prediction using a previously trained FL model.

---

## 🚀 Project Structure
```
HealthCardApp/
├── aadhaar_health_flapp.py           # Main Streamlit app
├── patients_data.json                # Mock patient records
├── fl_model.pkl                      # FL-trained risk prediction model
├── requirements.txt                  # Python dependencies
```

---

## 🧰 1. Setup Instructions (Local Machine)

### ✅ Requirements:
- Python 3.8–3.11 (avoid 3.13+ for now)
- Virtual environment recommended

### 🧪 Create and activate virtual environment:
```bash
python3 -m venv health_env
source health_env/bin/activate  # On Mac/Linux
# .\health_env\Scripts\activate  # On Windows
```

### 📦 Install dependencies:
```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt`, manually run:
```bash
pip install streamlit joblib scikit-learn numpy
```

---

## 🏥 2. Prepare Patient Data (patients_data.json)

Here's a sample structure:
```json
{
  "123456789012": {
    "name": "Ravi Kumar",
    "records": [
      {"date": "2025-04-05", "diagnosis": "Flu", "prescription": "Zeepack"},
      {"date": "2025-02-14", "diagnosis": "Hypertension", "prescription": "Amlodipine"}
    ]
  }
}
```
You can add more users manually to simulate multiple logins.

> OTP for all users is hardcoded as `1234` for demo purposes.

---

## 🧠 3. Add FL Model File

Export your trained model (from Colab FL notebook) like this:
```python
import joblib
joblib.dump(clients[0].model, "fl_model.pkl")
```

Then download it from Colab:
```python
from google.colab import files
files.download("fl_model.pkl")
```

Place `fl_model.pkl` in the same folder as the app.

---

## 💻 4. Run the App
```bash
streamlit run aadhaar_health_flapp.py
```

Open your browser and go to:
```
http://localhost:8501/
```

You’ll see:
- Patient login panel
- Medical records display
- Doctor-only panel for **Federated Learning risk prediction**

---

## 🔄 (Optional) Re-Train FL Model in Colab

Use the Colab FL notebook:
- Load `Adhaar_hospital_A.csv`, `B`, and `C`
- Run 3–10 FL rounds
- Export trained model with `joblib`

You can repeat this to simulate continuous improvement.

---

## 🎯 Use Cases
- Research demo for healthcare FL
- Prototype for Aadhaar-linked apps
- Grant or funding submission

---

## 📬 Questions / Next Steps
Let us know if you'd like to:
- Enable doctor-specific logins
- Connect to an actual API backend
- Simulate privacy attacks / defenses in FL

---

*Built with ❤️ using Streamlit + Federated Learning (Flower + sklearn)*
