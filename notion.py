# Notion Application
import json
import requests
import pandas as pd

file = open('secrets.json')  # Opens the files
problems = pd.read_excel("blind75.xlsx")  # Reads the excel file

data = json.load(file)  # loads the data then stores in variable called data

# Secret here:
secret = data['id']

# Database information here:
database = data['database_tasks']

file.close()  # close file

url = 'https://api.notion.com/v1/pages'

# Headers
headers = {
    'Authorization': f'Bearer {secret}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-08-16'
}

for i in range(len(problems)):
    data_input = {
        "parent": {"database_id": f"{database}"},
        "properties": {
            "Title": {
                "title": [
                    {
                        "text": {
                            "content": problems.iloc[i]['Name']
                        }
                    }
                ]
            },
            "Category": {
                "select": {
                    "name": problems.iloc[i]['Category']
                }
            },
            "Link": {
                "url": problems.iloc[i]['Link']
            },
            "Status": {
                "status": {
                    "name": "To do"
                }
            }
        }
    }
    requests.post(url, headers=headers, json=data_input)
