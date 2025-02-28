from fastapi import FastAPI
from data import titanic_df
from agent import process_query

app = FastAPI(title="Titanic Chatbot API")

@app.get("/query")
async def query_titanic(question: str):
    question_lower = question.lower()

    # Handle common queries directly for speed
    if "percentage of passengers were male" in question_lower:
        male_percentage = (titanic_df["Sex"] == "male").mean() * 100
        return {"text": f"{male_percentage:.2f}% of passengers were male."}
    
    elif "histogram of passenger ages" in question_lower:
        return {"text": "The average age was approximately {titanic_df['Age'].mean():.2f}, but I can’t generate histograms."}
    
    elif "average ticket fare" in question_lower:
        avg_fare = titanic_df["Fare"].mean()
        return {"text": f"The average ticket fare was {avg_fare:.2f}."}
    
    elif "passengers embarked from each port" in question_lower:
        embarked_counts = titanic_df["Embarked"].value_counts()
        text = f"Passengers embarked: {', '.join([f'{port}: {count}' for port, count in embarked_counts.items()])}."
        return {"text": text}
    
    # Fallback to Gemini for other queries
    text_response = process_query(question)
    return {"text": text_response}

@app.get("/")
async def root():
    return {"message": "Titanic Chatbot API is running with Gemini (Text Only)!"}