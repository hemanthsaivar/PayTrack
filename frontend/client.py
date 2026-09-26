import os
import httpx

BASE_URL = os.environ.get('PAYTRACK_API_URL', 'http://127.0.0.1:8000')

def call(method, path, **kwargs):
    with httpx.Client(base_url=BASE_URL, timeout=5) as client:
        response = client.request(method, path, **kwargs)
        response.raise_for_status()
        if path.endswith('.csv'):
            return response.text
        return response.json()
