from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load Models
churn_model = pickle.load(open("models/churn_model.pkl","rb"))
purchase_model = pickle.load(open("models/purchase_model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    required_fields = [
        "watch_hours",
        "active_days",
        "days_since_last_watch",
        "age",
        "customer_support_tickets",
        "completion_rate",
        "premium_interest",
        "platform_visits"
    ]

    # ---- BLOCK ONLY IF ANY FIELD EMPTY ----
    for f in required_fields:
        val = data.get(f, None)

        # if missing or blank ONLY
        if val is None or str(val).strip() == "":
            return jsonify({"error": f"{f} is required"}), 400


    df = pd.DataFrame([data])

    # ---- FORCE CREATE MODEL TRAINING COLUMNS ----
    df["last_week_watch"] = df.get("active_days", df.get("last_week_watch", 0))
    df["feedback_rating"] = df.get("customer_support_tickets", df.get("feedback_rating", 0))
    df["total_shows_watched"] = df.get("completion_rate", df.get("total_shows_watched", 0))
    df["subscription_type"] = df.get("platform_visits", df.get("subscription_type", 0))

    churn_features = [
        "watch_hours",
        "last_week_watch",
        "days_since_last_watch",
        "age",
        "feedback_rating",
        "total_shows_watched",
        "premium_interest",
        "subscription_type"
    ]

    purchase_features = churn_features  # same structure for now

    # Ensure exact feature order as model was trained
    try:
        churn_df = df[churn_model.feature_names_in_]
        purchase_df = df[purchase_model.feature_names_in_]
    except:
        # fallback if attribute missing
        churn_df = df[churn_features]
        purchase_df = df[purchase_features]


    churn_result = churn_model.predict(churn_df)[0]
    churn_prob = round(churn_model.predict_proba(churn_df)[0][1] * 100, 2)

    purchase_prob = round(purchase_model.predict_proba(purchase_df)[0][1] * 100, 2)

    return jsonify({
        "churn_risk": int(churn_result),
        "churn_probability": churn_prob,
        "purchase_probability": purchase_prob
    })



if __name__ == "__main__":
    app.run(debug=True)
