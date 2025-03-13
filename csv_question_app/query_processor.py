import ollama
import pandas as pd

MODEL_NAME = "llama2"

def process_query(data: pd.DataFrame, query: str):
    """Handles user queries using a local LLM."""
    try:
        data_dict = data.to_dict()
        print("Getting response from LLM")
        response = ollama.chat(MODEL_NAME, messages=[
            {"role": "system", "content": "You are an AI that answers questions based on CSV data."},
            {"role": "user", "content": f"Given this data: {data_dict}, answer this query: {query}"}
        ])
        return response["message"]["content"]
    except Exception as e:
        return f"Error processing query: {e}"
