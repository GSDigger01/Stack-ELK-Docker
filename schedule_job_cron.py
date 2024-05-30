import schedule
import time
from amazon_data_collector import fetch_amazon_data, send_to_logstash

def job():
    try:
        amazon_data = fetch_amazon_data()
        for item in amazon_data['results']:
            send_to_logstash(item)
    except Exception as e:
        print(f"Error: {e}")

schedule.every(1).hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
