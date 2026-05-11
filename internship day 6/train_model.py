import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
df = pd.read_csv("titanic.csv")

# Drop Cabin
df = df.drop(columns=['Cabin'])

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Encode Sex
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])

# Encode Embarked
df['Embarked'] = df['Embarked'].map({
    'S': 0,
    'C': 1,
    'Q': 2
})

# Features and target
X = df[['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch', 'Embarked']]
y = df['Survived']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Scaling
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)

# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X_train_scaled, y_train)

# Save locally
joblib.dump(model, "titanic_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("MODEL CREATED SUCCESSFULLY")