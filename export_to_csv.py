import csv
import requests
import json

def fetch_logs_from_elasticsearch():
    url = "http://localhost:9200/amazon_data/_search"
    query = {
        "query": {
            "match_all": {}
        },
        "size": 10000  
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers, data=json.dumps(query))
    response.raise_for_status()
    data = response.json()
    return data

def save_logs_to_csv(logs):
    hits = logs.get('hits', {}).get('hits', [])
    if hits:
        fieldnames = hits[0]['_source'].keys()
        with open('amazon_data.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for log in hits:
                writer.writerow(log['_source'])

if __name__ == "__main__":
    logs = fetch_logs_from_elasticsearch()    
    save_logs_to_csv(logs)
