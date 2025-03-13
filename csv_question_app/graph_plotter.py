import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(data: pd.DataFrame, column: str):
    """Plots a graph for the given column and returns a Matplotlib figure."""
    if column not in data.columns:
        return f"Column '{column}' not found in CSV."

    try:
        fig, ax = plt.subplots(figsize=(8, 5))
        data[column].value_counts().plot(kind="bar", color="skyblue", edgecolor="black", ax=ax)
        ax.set_xlabel(column)
        ax.set_ylabel("Count")
        ax.set_title(f"Distribution of {column}")
        return fig 
    except Exception as e:
        return f"Error generating graph: {e}"
