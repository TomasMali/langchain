import requests
import csv

def perform_get_request():
    url = "http://localhost:3303/files/allCompleted/"
    params = {
        "library": "PRO90DAT",
        "as": "10.200.100.160",
        "tablename": "MGLIS00F"
    }

    try:
        # First GET request to get data
        response = requests.get(url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("First GET Request successful.")
            data = response.json()

            # Second GET request to get column descriptions
            column_descriptions = get_column_descriptions()

            # Modify only the header of the data with column descriptions
            data_with_column_names = modify_header(data[0], column_descriptions)

            # Save the result to a CSV file
            save_to_csv(data, data_with_column_names)

        else:
            print(f"First GET Request failed with status code: {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"An error occurred: {e}")

def get_column_descriptions():
    column_url = "http://localhost:3303/files/columsDescription/"
    column_params = {
        "library": "PRO90DAT",
        "tablename": "MGLIS00F",
        "as": "10.200.100.160",
        "userLib": "WRKTOMMAL",
        "userDb": "WRKTOMMAL"
    }

    try:
        # Make the second GET request to get column descriptions
        column_response = requests.get(column_url, params=column_params)

        # Check if the request was successful (status code 200)
        if column_response.status_code == 200:
            print("Second GET Request successful.")
            return column_response.json()
        else:
            print(f"Second GET Request failed with status code: {column_response.status_code}")
            print(column_response.text)
            return []

    except Exception as e:
        print(f"An error occurred in the second GET request: {e}")
        return []

def modify_header(sample_row, column_descriptions):
    modified_header = []

    for key in sample_row.keys():
        matching_column = next((col for col in column_descriptions if col["COLUMN_NAME"].upper() == key), None)
        if matching_column:
            column_text = matching_column["COLUMN_TEXT"]
            modified_header.append(f"{column_text} ({key})")
        else:
            modified_header.append(key)

    return modified_header

def save_to_csv(data, modified_header):
    try:
        with open("data.csv", mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)

            # Write modified header
            writer.writerow(modified_header)

            # Write data
            writer.writerows([row.values() for row in data])

        print("Data saved to data.csv.")

    except Exception as e:
        print(f"An error occurred while saving to CSV: {e}")

# if __name__ == "__main__":
#     perform_get_request()



# import csv

# def listino(file_path='data.csv'):
#     with open(file_path, 'r', newline='') as csvfile:
#         csv_reader = csv.reader(csvfile)
#         header = next(csv_reader)  # Assuming the first row is the header

#         # Create a list to store rows as dictionaries
#         rows = []
#         for row in csv_reader:
#             rows.append(row)

#         # Format the data into a string
#         formatted_data = ','.join(header) + '\n'
#         for row in rows:
#             formatted_data += ','.join(row) + '\n'

#     return formatted_data