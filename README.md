# 🎥 OTT AI Personalisation & Churn Intelligence Platform

An AI-powered OTT Analytics & Intelligence platform that predicts **user churn**, estimates **purchase probability**, evaluates **business impact**, and recommends **real-time retention strategies** with insights, charts, persona classification, and exportable business reports.

---

## 🌍 Live Demo
🔗 **Deployed Platform:** https://ott-ai-platform.onrender.com

---

## 🚀 Key Features

### ✅ AI Prediction & Intelligence
- 🔥 Churn Risk Prediction  
- 🎯 Purchase Probability
- ⚠️ Risk Level Badging (High / Medium / Safe)
- 📊 Engagement Score
- 🔐 Retention Priority
- 💼 Business Impact Evaluation
- 👤 Smart User Persona Detection
- 🧠 AI Reasoning Explanation
- 🧠 AI Recommended Business Actions

---

## 📈 Visual Intelligence Dashboard
- Doughnut Chart → Churn Probability
- Bar Chart → Purchase Probability
- Real-time AI Insights Panel
- Prediction History Log

---

## 📥 Business Reporting
- 📄 Export AI Report (CSV)
- 📊 Export Business Report (.xlsx)

---

## ✨ UI & Experience
- Premium Admin Dashboard Interface  
- Dark Themed Professional Design  
- Smooth UX with Real-time Updates  

---

## 🧠 Tech Stack

### Backend
- Python
- Flask
- Scikit-Learn
- Pandas

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript
- Chart.js

### Deployment
- Render (Cloud Hosting)

---

## 🏗️ Project Structure
ott_ai_platform
│── app.py
│── models/
│ ├── churn_model.pkl
│ ├── purchase_model.pkl
│── templates/
│ ├── index.html
│── static/
│ ├── (optional future assets)
│── requirements.txt
│── README.md

## 🛠️ Run Locally

### 1️⃣ Clone the Project
git clone https://github.com/devaprasathk28-dot/ott-ai-platform.git
cd ott-ai-platform

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run Flask Server
python app.py

### 4️⃣ Open in Browser
http://127.0.0.1:5000

## 🔌 API Endpoint

### `POST /predict`

#### Request Body
{
"watch_hours": 10,
"active_days": 5,
"days_since_last_watch": 3,
"age": 22,
"customer_support_tickets": 1,
"completion_rate": 80,
"premium_interest": 1,
"platform_visits": 10
}


#### Response
{
"churn_risk": 0,
"churn_probability": 23,
"purchase_probability": 65
}


## 🏆 Real-World Use Cases
Ideal for:
- OTT Platforms (Netflix, Hotstar, Prime)
- Streaming Providers
- Telecom OTT Bundles
- Product Analytics Teams
- AI Research & Academic Projects


## 👨‍💻 Developed By
**Team Prime Cortex – ByteQuest Hackathon**
Built with ❤️ Intelligence & Innovation
DEVAPRASATH K
