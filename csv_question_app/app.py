import gradio as gr
import pandas as pd
from query_processor import process_query
from graph_plotter import plot_graph
from pydantic_ai import Agent
import ollama

csv_data = None  # Global variable to store uploaded CSV data

# Function to handle CSV upload
def upload_csv(file):
    global csv_data
    if file is None:
        return "No file uploaded."
    
    try:
        csv_data = pd.read_csv(file)  # Read CSV using filepath
        return f"CSV loaded successfully with {csv_data.shape[0]} rows and {csv_data.shape[1]} columns."
    except Exception as e:
        return f"Error loading CSV: {str(e)}"

# Function to answer user queries
def answer_query(query):
    if csv_data is None:
        return "Please upload a CSV file first."
    return process_query(csv_data, query)

# Function to plot graphs
def visualize_graph(column):
    if csv_data is None:
        return "Please upload a CSV file first."
    print("Plotting graph for column")
    return plot_graph(csv_data, column)

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# CSV Question Answering and Visualization App")

    with gr.Row():
        file_upload = gr.File(label="Upload CSV File", type="filepath")
        upload_button = gr.Button("Upload")

    upload_output = gr.Textbox(label="Upload Status")

    with gr.Row():
        query_input = gr.Textbox(label="Enter your query")
        query_button = gr.Button("Ask")

    query_output = gr.Textbox(label="Answer")

    with gr.Row():
        column_input = gr.Textbox(label="Enter column name for graph")
        graph_button = gr.Button("Plot Graph")
        
        graph_output = gr.Plot(label="Graph Output") 


    # Button actions
    upload_button.click(upload_csv, inputs=file_upload, outputs=upload_output)
    query_button.click(answer_query, inputs=query_input, outputs=query_output)
    graph_button.click(visualize_graph, inputs=column_input, outputs=graph_output)

if __name__ == "__main__":
    demo.launch()
