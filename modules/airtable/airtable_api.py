# airtable_api.py

import requests

API_KEY = "YOUR_AIRTABLE_API_KEY"
BASE_ID = "YOUR_BASE_ID"
TABLE_NAME = "YOUR_TABLE_NAME"

AIRTABLE_ENDPOINT = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def fetch_changed_entries(status="changed"):
    """
    Fetch entries from Airtable that have a specific status.
    """
    params = {"filterByFormula": f"status='{status}'"}  # Filtering by status
    response = requests.get(AIRTABLE_ENDPOINT, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json().get("records", [])
    return []

def prepare_data_for_telegram(records):
    """
    Prepare the data from Airtable records for sending to Telegram.
    """
    return "\n".join([str(record) for record in records])
 
