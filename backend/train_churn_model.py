import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv(r"C:\Users\devap\Documents\ott_ai_platform\dataset\ott_dataset.csv")

# Encode categorical
le = LabelEncoder()
df['subscription_type'] = le.fit_transform(df['subscription_type'])

# Features and Target
X = df[['watch_hours','last_week_watch','subscription_type','age',
        'days_since_last_watch','total_shows_watched','premium_interest','feedback_rating']]
y = df['churned']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save Model
pickle.dump(model, open("churn_model.pkl","wb"))

print("Churn Model Trained & Saved Successfully!")
