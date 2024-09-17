## Netflix Search App

A simple Python application that allows users to search for Netflix titles using a Tkinter-based graphical user interface (GUI). This app leverages the power of `pandas` to load and search through a CSV dataset of Netflix titles.

## Features

- **Search by Title**: Input a movie or show title to find relevant matches.
- **View Results**: Shows the title, type, genre, and release year of the matched entries.
- **Error Handling**: Displays error messages if the dataset fails to load or if there are search issues.

## Requirements

- Python 3.x
- `pandas`
- `tkinter` (typically included with Python)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/Netflix-Search-App.git
   cd Netflix-Search-App
   ```

2. **Install Required Packages**:
   If `pandas` is not already installed, you can do so with:
   ```bash
   pip install pandas
   ```

3. **Prepare the Dataset**:
   Make sure you have the `netflix_titles.csv` dataset. Place it in the same directory as `app.py` or adjust the file path in the script as needed.

## Usage

1. **Run the Application**:
   ```bash
   python app.py
   ```

2. **Search for Titles**:
   - Type your search query in the text box and click "Search."
   - The results will appear below the search button.

## File Structure

- `app.py`: The main Python script that operates the application.
- `netflix_titles.csv`: The dataset with Netflix titles (if included).
- `README.md`: This document, which provides project information.

## Contributing

You're welcome to submit issues or pull requests if you have suggestions or bug fixes. Contributions are appreciated!

## Contact

For any questions or feedback, please contact [sophiasad1421@gmail.com]. 
