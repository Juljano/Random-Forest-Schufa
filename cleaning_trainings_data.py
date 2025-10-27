import pandas as pd
from streamlit import columns

# I got the Training data of University of Stuttgart
#Source https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data
# Last Update: 1994 😫

def cleaning_trainings_data():
    df = pd.read_csv('Training/german.data-numeric', delim_whitespace=True, header=None)

    # Added correct Columns to the dataset - For more Information see "German.doc"
    df.columns = ["status_checking_account",
                  "duration_month",
                  "credit_history",
                  "purpose",
                  "credit_amount",
                  "savings_account",
                  "employment_since",
                  "Installment_rate",
                  "person_status_sex",
                  "other_debtors",
                  "present_residence_since",
                  "property",
                  "age",
                  "other_installment_plans",
                  "housing",
                  "existing_credits",
                  "job",
                  "liable_maintenance_people",
                  "telephone",
                  "foreign_worker",
                  "unknown",
                  "unknown",
                  "unknown",
                  "unknown",
                  "score"
                  ]

    df["score"] = df["score"].replace({1: 1, 2: 0})  #replace 2 with 0

    #delete the "Unknown" and "other_debtors" -Columns
    df = df.drop(columns=["unknown"])
    df = df.drop(columns=["other_debtors"])

    # saving cleaned dataset as csv-file
    df.to_csv("Training/Cleaned-german-Credit-Data.csv", index=False)

