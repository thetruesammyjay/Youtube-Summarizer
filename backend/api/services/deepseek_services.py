import requests
import os

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
DEEPSEEK_API_URL = 'https.//api.deepseek.com/v1/summarize'

def summarize_text(text):
    headers = {
        'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'text': text,
        'max_length': 1500,
    }
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('summary')
    else:
        print(f"Error summarizing text: {response.status_code}")
        return None