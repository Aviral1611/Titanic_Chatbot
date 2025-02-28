from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os
from data import titanic_df

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.1,
    max_tokens=500
)

# Define the prompt template (no visualization instruction)
prompt_template = """
You are a data analyst working with the Titanic dataset. The dataset has these columns:
PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked.

Here’s a sample of the data:
{data_sample}

Answer this question as accurately as possible:
{question}

Provide a concise, clear answer in plain English.
"""

prompt = PromptTemplate(
    input_variables=["data_sample", "question"],
    template=prompt_template
)

# Create the LangChain chain
chain = LLMChain(llm=llm, prompt=prompt)

def process_query(question):
    data_sample = titanic_df.head(5).to_string()
    try:
        response = chain.invoke({"data_sample": data_sample, "question": question})["text"]
    except Exception as e:
        response = f"Error processing query: {str(e)}. Try a simpler question."
    
    return response