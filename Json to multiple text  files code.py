import json
import os

# Function to load JSON data from a file
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to write specific columns to a text file with tab-separated values
def write_columns(data, file_path, columns):
    with open(file_path, 'w') as file:
        # Write headers
        file.write('\t'.join(columns) + '\n')
        for item in data:
            row = [str(item[col]) if col in item else '' for col in columns]
            file.write('\t'.join(row) + '\n')
    print(f"Data written to {file_path}")

# Path to the source JSON file
json_file = '/Users/harishwarbageli.r/Desktop/pythonfiles/new.json'

# Output directory
output_dir = '/Users/harishwarbageli.r/Desktop/pythonfiles'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load data from the source JSON file
data = load_json(json_file)

# Check if the data is a list of dictionaries
if isinstance(data, list) and all(isinstance(item, dict) for item in data):
    # Get all keys (columns) from the first dictionary
    columns = list(data[0].keys())
    
    # Define columns for each output file
    columns_file1 = columns[:10]
    columns_file2 = columns[10:20]
    
    # Define output files
    output_file1 = os.path.join(output_dir, 'output1.txt')
    output_file2 = os.path.join(output_dir, 'output2.txt')
    
    # Write the columns to the respective text files
    write_columns(data, output_file1, columns_file1)
    write_columns(data, output_file2, columns_file2)
else:
    print("The JSON data is not a list of dictionaries or contains fewer than 20 columns.")
