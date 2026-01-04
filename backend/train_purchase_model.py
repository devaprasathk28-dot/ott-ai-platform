import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv(r"C:\Users\devap\Documents\ott_ai_platform\dataset\ott_dataset.csv")

le = LabelEncoder()
df['subscription_type'] = le.fit_transform(df['subscription_type'])

# purchase target = premium_interest
X = df[['watch_hours','last_week_watch','subscription_type',
        'total_shows_watched','feedback_rating']]
y = df['premium_interest']

X_train, X_test, Y_train, Y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestClassifier()
model.fit(X_train,Y_train)

pickle.dump(model, open("purchase_model.pkl","wb"))

print("Purchase Model Trained & Saved Successfully!")
