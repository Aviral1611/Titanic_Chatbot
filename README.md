# Titanic Chatbot

This project is a chatbot that answers questions about the Titanic dataset using natural language. It is powered by Gemini and built with FastAPI and Streamlit.

## Project Structure


## Setup Instructions

### Backend

1. **Navigate to the backend directory:**
    ```sh
    cd backend
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Create a `.env` file and add your Gemini API key:**
    ```env
    GEMINI_API_KEY=your_gemini_api_key
    ```

5. **Run the FastAPI server:**
    ```sh
    uvicorn main:app --reload
    ```

### Frontend

1. **Navigate to the frontend directory:**
    ```sh
    cd frontend
    ```

2. **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```

## Usage

- Open your browser and go to `http://localhost:8501` to access the Streamlit frontend.
- Enter your questions about the Titanic dataset in the input field and click "Ask" to get answers.

## Example Questions

- What percentage of passengers were male?
- What was the average ticket fare?
- How many passengers embarked from each port?

## Project Details

### Backend

- **FastAPI**: Used to create the API endpoints.
- **LangChain**: Utilized for natural language processing with the Gemini model.
- **Pandas**: Used for data manipulation and analysis.
- **Matplotlib**: Included for potential future visualizations.

### Frontend

- **Streamlit**: Used to create an interactive web interface for the chatbot.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

## Author

Made by Aviral Bansal | [GitHub](https://github.com/Aviral1611)