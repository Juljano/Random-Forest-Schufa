import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def read_training_data():
    try:
        df = pd.read_csv("Training/Cleaned-german-Credit-Data.csv")
        x = df.drop("score", axis=1)
        y = df["score"]
        return x, y

    except FileNotFoundError:
        print("Trainingsdaten konnten nicht gefunden werden")
        return None, None


def train_random_forest(x,y, customer_credit_information):
    try:
        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=400, class_weight="balanced", max_depth=None)
        model.fit(x_train, y_train)

        print(metrics.classification_report(y_test,model.predict(x_test)))

        convert_list_to_2d_array = np.array(customer_credit_information).reshape(1, -1)

        prediction = model.predict(convert_list_to_2d_array)
        print("Gerne bieten wir dir ein Kredit an" if prediction[0] == 1 else "Tut mir leid, dein Antrag wird abgelehnt")

    except IOError as e:
        print(F"Es ist ein Problem enstanden: {e}")

