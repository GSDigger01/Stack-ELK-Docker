import requests
import json
import time

LOGSTASH_URL = 'http://localhost:5044'
API_URL = 'https://real-time-amazon-data.p.rapidapi.com/search?query=Phone&page=1&country=US'
HEADERS = {
    'X-RapidAPI-Key': 'ce1d992fbemshe8ae9f9bdcb5db2p15bd9cjsnd87f82cf72c7',
    'X-RapidAPI-Host': 'real-time-amazon-data.p.rapidapi.com'
}

def fetch_amazon_data():
    try:
        response = requests.get(API_URL, headers=HEADERS)
        response.raise_for_status()  
        data = response.json()
        return data
    except requests.exceptions.HTTPError as err:
        if response.status_code == 429:
            print("Received 429 Too Many Requests. Waiting before retrying...")
            time.sleep(60)  
            return fetch_amazon_data()
        else:
            raise err

def send_to_logstash(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(LOGSTASH_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print('Data sent to Logstash successfully')
    else:
        response.raise_for_status()

if __name__ == "__main__":
    try:
        amazon_data = fetch_amazon_data()
        for item in amazon_data['data']['products']:
            send_to_logstash(item)
    except Exception as e:
        print(f"Error: {e}")
