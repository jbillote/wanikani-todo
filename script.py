from dotenv import load_dotenv
import json
import os
import requests

load_dotenv()
api_key = os.getenv('API_TOKEN')

url = 'https://api.wanikani.com/v2/summary'
headers = { 'Authorization': f'Bearer {api_key}' }

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    raw_reviews = response.json()['data']['reviews']
    reviews = []
    for review in raw_reviews:
        if review['subject_ids']:
            reviews.append(review['available_at'])
    print(json.dumps(reviews, indent=2))
except requests.exceptions.RequestException as e:
    print(e)
