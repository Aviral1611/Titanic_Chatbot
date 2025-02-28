import pandas as pd

def load_titanic_data():
    # Load the dataset
    df = pd.read_csv("Titanic-Dataset.csv")
    
    # Basic preprocessing
    df["Age"] = df["Age"].fillna(df["Age"].mean())  # Fill missing ages with mean
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])  # Fill with mode
    df["Fare"] = df["Fare"].fillna(df["Fare"].mean())  # Fill missing fares
    
    return df

# Load data once when module is imported
titanic_df = load_titanic_data()