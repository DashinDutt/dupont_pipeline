import pandas as pd
import os
import logging

# Set up basic logging (better than just print statements)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def count_rows(csv_path, output_path):
    """Counts rows in a CSV and appends the count to a file."""
    try:
        df = pd.read_csv(csv_path)
        row_count = len(df)

        # More robust file writing (using 'with' and handling potential errors)
        with open(output_path, 'a') as f:
            f.write(str(row_count) + '\n')

        logging.info(f"Counted {row_count} rows in {csv_path} and appended to {output_path}")

    except FileNotFoundError:
        logging.error(f"Error: CSV file not found at {csv_path}")
    except pd.errors.EmptyDataError:  # Catch empty CSV files
        logging.warning(f"Warning: CSV file is empty: {csv_path}")
        with open(output_path, 'a') as f: # Write 0 if file is empty
            f.write("0\n")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")  # Log the full traceback

if __name__ == "__main__":
    csv_file_path = os.environ.get("CSV_FILE_PATH") #To be determined by dockerfile
    output_file_path = os.environ.get("OUTPUT_FILE_PATH") #To be determined by dockerfile

    if not csv_file_path or not output_file_path:
        logging.error("CSV_FILE_PATH and OUTPUT_FILE_PATH environment variables are required.")
    else:
        count_rows(csv_file_path, output_file_path)