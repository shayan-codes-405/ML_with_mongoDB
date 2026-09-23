from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Database
db = client["predctive_ai"]

# Collection
customers = db["students"]

data = list(customers.find())

df = pd.DataFrame(data)


print(df.head())

# Feature(x)
X = df[["attendance","cgpa","studyHours","internships"]]

# Target(y)
y = df["placement"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Create the model using random forest classifier
model = RandomForestClassifier(n_estimators=100,random_state=42)

# Train the model
model.fit(X_train, y_train)


# Prediction
y_pred = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy Score: ",accuracy)
