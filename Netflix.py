import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Load the CSV dataset
def load_data(file_path):
    try:
        # Use read_csv() to load CSV files
        data = pd.read_csv(file_path)
        print("Dataset Loaded Successfully")  # Debugging message
        print(data.head())  # Display first few rows to confirm loading
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Could not load dataset: {str(e)}")
        return None

# Function to search and display movies/shows
def search_content():
    query = entry.get().lower()  # Get the search query from user input
    try:
        print(f"Searching for: {query}")  # Debugging message
        
        # Search in the 'title' column (note the lowercase 'title')
        results = data[data['title'].str.lower().str.contains(query, na=False)]  # Use na=False to avoid issues with missing values

        if not results.empty:
            result_text = ""
            for index, row in results.iterrows():
                result_text += f"Title: {row['title']}\nType: {row['type']}\nGenre: {row['listed_in']}\nRelease Year: {row['release_year']}\n\n"
            result_label.config(text=result_text)
        else:
            messagebox.showinfo("No Results", "No matches found!")
    
    except KeyError as e:
        messagebox.showerror("Error", f"Dataset is missing column: {str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create GUI
def create_app():
    global entry, result_label
    
    # Set up the main window
    root = tk.Tk()
    root.title("Netflix-like App")
    root.geometry("500x400")
    
    # Add search label and entry
    tk.Label(root, text="Search Movies/Shows").pack(pady=10)
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)
    
    # Search button
    search_button = tk.Button(root, text="Search", command=search_content)
    search_button.pack(pady=10)
    
    # Result label to display search results
    result_label = tk.Label(root, text="", justify="left", anchor="w", wraplength=400)
    result_label.pack(pady=20)
    
    # Start the application
    root.mainloop()

# Main part of the code
if __name__ == "__main__":
    file_path = "E:/21HM1A3030/Netflix/netflix_titles.csv"  # Path to the uploaded CSV file
    data = load_data(file_path)
    
    if data is not None:
        create_app()
