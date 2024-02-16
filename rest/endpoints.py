import requests
# import rest.rest_header as headers
from tabulate import tabulate


def json_to_table(json_data):
    # Extract the 'result' key from JSON data
    result = json_data.get('result', [])
    
    # If there's no data, return an empty string
    if not result:
        return ""
    
    # Extract headers from the first item in the 'result' list
    headers = list(result[0].keys())
    
    # Extract rows from the 'result' list
    rows = [list(row.values()) for row in result]
    
    # Use tabulate to format the data as a table
    table = tabulate(rows, headers, tablefmt="pipe")
    
    return table


def gruppi(input=""):

    print("###"*4 + "\n")
    print(input + "")
    print("###"*4)

    params = {
        'withStandardTranslations': 'true',
    }

    json_data = {
        'entity': {
            'filters': [
                {
                    'alias': 'Grp',
                    'column': 'LogDel',
                    'operation': 'eq',
                    'value': False,
                },
            ],
            'sorts': [],
            'limit': None,
        },
        'params': None,
    }

    response = requests.post(
        'http://localhost:8080/synergy2-ws/ws/spec/sys/qry/exec/44',
        params=params,
        # cookies=cookies,
        headers=headers.get_header(),
        json=json_data,
    )

    # Handle the response
    if response.status_code == 200:
        print("Request successful")
        try:
            return str(response.json())
        except ValueError:
            print("Response content is not in JSON format:", response.content)
    else:
        return str(response.content)







def risorse(input=""):
    params = {
        'withStandardTranslations': 'true',
    }

    json_data = {
        'entity': {
            'generateId': True,
            'filters': [
                {
                    'alias': 'Res',
                    'column': 'LogDel',
                    'operation': 'eq',
                    'value': False,
                },
            ],
            'sorts': [],
            'limit': None,
        },
        'params': None,
    }

    response = requests.post(
        'http://localhost:8080/synergy2-ws/ws/spec/sys/qry/exec/149',
        params=params,
        headers=headers.get_header(),
        json=json_data,
    )
        # Handle the response
    if response.status_code == 200:
        print("Request successful")
        try:
            return json_to_table(response.json())
        except ValueError:
            print("Response content is not in JSON format:", response.content)
    else:
        return str(response.content)
    



def permessi(input=""):
    params = {
        'withStandardTranslations': 'true',
    }

    json_data = {
        'entity': {
            'filters': [],
            'sorts': [],
            'limit': None,
        },
        'params': None,
    }

    response = requests.post(
        'http://localhost:8080/synergy2-ws/ws/spec/sys/qry/exec/141',
        params=params,
        headers=headers.get_header(),
        json=json_data,
    )
            # Handle the response
    if response.status_code == 200:
        print("Request successful")
        try:
            return json_to_table(response.json())
        except ValueError:
            print("Response content is not in JSON format:", response.content)
    else:
        return str(response.content)
    




def query(input=""):




    params = {
        'withStandardTranslations': 'true',
    }

    json_data = {
        'entity': {
            'filters': [
                {
                    'alias': 'Qry',
                    'column': 'LogDel',
                    'operation': 'eq',
                    'value': False,
                },
                {
                    'alias': 'Qry',
                    'column': 'QryTpl',
                    'operation': 'eq',
                    'value': True,
                },
            ],
            'sorts': [],
            'limit': None,
        },
        'params': None,
    }

    response = requests.post(
        'http://localhost:8080/synergy2-ws/ws/spec/sys/qry/exec/129',
        params=params,
        headers=headers.get_header(),
        json=json_data,
    )

    if response.status_code == 200:
        print("Request successful")
        try:
            return json_to_table(response.json())
        except ValueError:
            print("Response content is not in JSON format:", response.content)
    else:
        return str(response.content)
    



def eventi(input=""):

    params = {
        'withStandardTranslations': 'true',
    }

    json_data = {
        'entity': {
            'filters': [
                {
                    'alias': 'Evt',
                    'column': 'LogDel',
                    'operation': 'eq',
                    'value': False,
                },
            ],
            'sorts': [],
            'limit': None,
        },
        'params': None,
    }

    response = requests.post(
        'http://localhost:8080/synergy2-ws/ws/spec/sys/qry/exec/18',
        params=params,
        headers=headers.get_header(),
        json=json_data,
    )
    
    if response.status_code == 200:
        print("Request successful")
        try:
            return json_to_table(response.json())
        except ValueError:
            print("Response content is not in JSON format:", response.content)
    else:
        return str(response.content)
    




import csv
import json

def anagrafica(input=""):
    file_path='/Users/tomasmali/Desktop/LangGraph/rest/ana.csv'
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        # Read CSV data into a list of dictionaries
        data = list(csv_reader)
        
        # Convert the list of dictionaries to JSON format
        json_data = json.dumps(data, indent=4)

    return str(json_data)

# Example usage:
# json_string = listino('jercc.csv')
# print(json_string) 
# return json_string



# print(listino())
  