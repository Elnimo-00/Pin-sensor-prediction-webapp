from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib, os

MODEL_DIR = "models"
MODEL_FILE = f"{MODEL_DIR}/model.joblib"
SCALER_FILE = f"{MODEL_DIR}/scaler.joblib"

os.makedirs(MODEL_DIR, exist_ok=True)

def train_model(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    Xtr, Xte, ytr, yte = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(Xtr, ytr)

    acc = accuracy_score(yte, clf.predict(Xte))

    joblib.dump(clf, MODEL_FILE)
    joblib.dump(scaler, SCALER_FILE)

    return acc

def predict_digit(features):
    clf = joblib.load(MODEL_FILE)
    scaler = joblib.load(SCALER_FILE)

    X = scaler.transform([features])
    probs = clf.predict_proba(X)[0]

    return int(probs.argmax()), float(probs.max())
