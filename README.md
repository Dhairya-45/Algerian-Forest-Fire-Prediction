# 🔥 Algerian Forest Fire Prediction

An end-to-end Machine Learning web application to predict the **Fire Weather Index (FWI)** using meteorological data from the Algerian Forest Fires dataset.

🌐 **Live Demo:** [Click Here](https://algerian-forest-fire-prediction-kxmc.onrender.com)

> ⚠️ Hosted on Render's free tier — first load may take 50+ seconds to wake up.

---

## 📌 Problem Statement
Forest fires cause massive environmental and economic damage.  
This project predicts the **Fire Weather Index (FWI)** based on weather and fire-related features to estimate fire risk levels.

---

## 🚀 Features
- Real-time Fire Weather Index (FWI) prediction
- Fire risk classification (Low, Moderate, High, Extreme)
- User-friendly Flask web interface
- Scalable ML pipeline

---

## 🧠 Machine Learning Pipeline
1. Data preprocessing & cleaning  
2. Feature selection  
3. Feature scaling using **StandardScaler**  
4. Model training using **Ridge Regression**  
5. Model serialization using **Pickle**  

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Machine Learning:** Scikit-learn  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS  
- **Deployment:** Render  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure
```
Algerian-Forest-Fire-Prediction/
│
├── model/                  # Jupyter notebooks for EDA & model training
├── pkl/                    # Serialized model and scaler files
│   ├── ridge.pkl
│   └── scaler.pkl
├── templates/              # HTML templates
│   └── home.html
├── application.py          # Flask application
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 📊 Dataset
- **Source:** [UCI Machine Learning Repository - Algerian Forest Fires Dataset](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++)
- **Regions:** Bejaia (northeast Algeria) and Sidi Bel-abbes (northwest Algeria)
- **Period:** June to September 2012

### Input Features
| Feature | Description |
|---|---|
| Temperature | Temperature at noon (°C) |
| RH | Relative Humidity (%) |
| Ws | Wind Speed (km/h) |
| Rain | Total rainfall (mm) |
| FFMC | Fine Fuel Moisture Code |
| DMC | Duff Moisture Code |
| ISI | Initial Spread Index |
| Classes | Fire / Not Fire |
| Region | 0 = Bejaia, 1 = Sidi Bel-abbes |

### Target Variable
- **FWI** — Fire Weather Index (continuous value indicating fire danger)

---

## ⚙️ How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Dhairya-45/Algerian-Forest-Fire-Prediction.git
cd Algerian-Forest-Fire-Prediction
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Flask app**
```bash
python application.py
```

**4. Open in browser**
```
http://localhost:5000
```

---

## 📦 Requirements
```
flask
numpy
scikit-learn
gunicorn
```

---

## 📸 Screenshots
<!-- Add screenshots of your web app here --><img width="945" height="915" alt="image" src="https://github.com/user-attachments/assets/43cfaecb-2415-4e84-8e4e-2a5778d0592b" />

> Home Page / Prediction Form

---

## 🌐 Deployment
This app is deployed on **Render**.  
👉 [Live Demo](https://algerian-forest-fire-prediction-kxmc.onrender.com)

---

## 🙋‍♂️ Author
**Dhairya**  
[GitHub](https://github.com/Dhairya-45)
