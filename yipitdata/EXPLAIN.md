# Running the Code
This guide will walk you through the steps to create a Python virtual environment, activate it, install necessary packages, and run the Oscars Python Script.

## Step 1: Create a Virtual Environment

1. **Open a Terminal or Command Prompt:** Use your system’s terminal or command prompt.
2. **Navigate to Your Project Directory:** Use `cd` to change to the directory where you want to create the virtual environment.

   ```bash
   cd /path/to/your/project
   ```

3. **Create the Virtual Environment:**

   - **On Unix or MacOS:**

     ```bash
     python3 -m venv venv
     ```

   - **On Windows:**

     ```dos
     python -m venv venv
     ```

## Step 2: Activate the Virtual Environment

- **On Unix or MacOS:**

  ```bash
  source venv/bin/activate
  ```

- **On Windows (cmd.exe):**

  ```dos
  venv\Scripts\activate
  ```

- **On Windows (PowerShell):**

  ```powershell
  .\venv\Scripts\Activate
  ```

  After activation, you should see the virtual environment name in your command prompt (e.g., `(venv)`).

## Step 3: Install Requirements

1. **Ensure the Virtual Environment is Activated:** The prompt should show the environment name (e.g., `(venv)`).

2. **Install Packages Using `pip`:**

   ```bash
   pip install -r requirements.txt
   ```

   This command installs all the packages listed in the `requirements.txt` file into the virtual environment.

## Step 4: Run Python Code

1. **Navigate to Your Project Directory (if not already there):**

   ```bash
   cd /path/to/your/project
   ```

2. **Run Your Python Module:**

   ```bash
   python -m main
   ```

## Step 5: Open CSV

1. **A csv file was created in the same folder as the code, just open or load to a db and check the resulsts**

# Approach and Assumptions made

This document outlines the approach and assumptions for scraping and processing movie data from http://oscars.yipitdata.com/. Our objective was to extract comprehensive information about movies, including titles, release years, Wikipedia URLs, Oscar wins, and budget details. We utilized Python's requests library to fetch data from the endpoint, then parsed the JSON response to retrieve the necessary fields. For accurate budget information, we made additional requests using URLs provided in the 'Detail URL' field to fetch and standardize the budget data.

To clean the "Budget" column, we developed several functions to handle different scenarios. We extracted the monetary amount and currency, converting any non-USD amounts to USD using a fixed conversion rate for simplicity. NaN values were replaced with 0, and budget ranges were set to 0 to avoid inaccuracies. Regular expressions and conditional logic were employed to parse and format the budget data effectively, ensuring uniformity across the dataset.

For the "Year" column, we validated that entries were four-digit years, replacing any invalid or missing years with a default value. The final cleaned dataset was then exported to a CSV file using Pandas, making it ready for further analysis or reporting. In the main script, two distinct classes were implemented: DataFetcher for handling data retrieval and DataCleaner for processing and exporting the data. This modular approach enhances code maintainability by clearly separating the data fetching and cleaning responsibilities.
