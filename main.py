import os.path
import cleaning_trainings_data
from random_forest import read_training_data, train_random_forest

credit_info = [
    "Existing account status 1: < 0€, 2: < 200€, 3: >= 200€, 4: no checking account",
    "Credit duration in months?",
    "Previous credit history reliable (y/n)?",
    "Purpose: 0: new Car, 1: used Car, 2: furniture/equipment, 3: radio/television, 5: domestic appliances, 10: others ",
    "Credit amount?",
    "Savings account: 1: < 100€, 2: < 500€, 3: < 1.000€, 4: >= 1.000€, 5: no saving account",
    "Employment duration (y/n)?", #1
    "Installment rate reasonable (y/n)?",
    "Personal status & sex? Choose between 1 and 4:  1: Male, divorced/separated/married, 2: Female, divorced/separated/married, 3: Male Single, 4: Female Single",
    "Residence duration?", #2
    "Property ownership (y/n)?",
    "Your Age",
    "Other installment plans: 1: Bank, 2: stores, 3: none",
    "Housing: 1: rent, 2: own, 3: for free",
    "Existing credits (y/n)?",
    "Job:  1: unemployed/unskilled, 2: unskilled, 3: skilled employee, 4: highly qualified employee/ officer",
    "Number of dependents (y/n)?",
    "Telephone (y/n)?",
    "Foreign worker (y/n)?"
]

if __name__ == "__main__":
    if not os.path.exists("Training/Cleaned-german-Credit-Data.csv"):
        print("Please wait we are training the Random Forest-Model")
        cleaning_trainings_data.cleaning_trainings_data()
    else:

        try:
            print("Please wait....")
            x, y = read_training_data()
            print("Hello and welcome to Sparkasse Eilsener-Hause.")
            print("Please enter your information to rating your credit score:")
            print("y: Yes , n: No")
            customer_credit_information = []
            for i in credit_info:
                customer_answer = input(F"{i}: ")
                if customer_answer == "y" or customer_answer == "yes":
                    customer_credit_information.append(1) #True
                elif customer_answer == "n" or customer_answer == "no":
                    customer_credit_information.append(0) #False
                else:
                    customer_credit_information.append(customer_answer)
            train_random_forest(x, y, customer_credit_information)
        except IOError as error:
            print(f"Something went wrong {error}")




