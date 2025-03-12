import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def plot_graph(data: pd.DataFrame, column: str):
    """Plots a graph for the given column and returns an image."""
    if column not in data.columns:
        return f"Column '{column}' not found in CSV."

    try:
        plt.figure(figsize=(8, 5))
        data[column].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.title(f"Distribution of {column}")

        # Convert plot to base64 image for Gradio
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format="png")
        img_buf.seek(0)
        encoded_img = base64.b64encode(img_buf.getvalue()).decode("utf-8")
        return f"<img src='data:image/png;base64,{encoded_img}'/>"
    except Exception as e:
        return f"Error generating graph: {e}"
