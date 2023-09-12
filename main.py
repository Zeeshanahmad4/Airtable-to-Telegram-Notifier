# main.py

import logging
from modules.airtable.airtable_api import fetch_changed_entries, prepare_data_for_telegram
from modules.telegram.telegram_api import send_message_to_telegram

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    try:
        logging.info("Fetching changed entries from Airtable...")
        records = fetch_changed_entries()

        if records:
            logging.info(f"Found {len(records)} changed entries.")
            text = prepare_data_for_telegram(records)
            logging.info("Sending data to Telegram...")
            response = send_message_to_telegram(text)
            if response.get("ok"):
                logging.info("Data successfully sent to Telegram!")
            else:
                logging.error(f"Failed to send data to Telegram. Error: {response.get('description')}")
        else:
            logging.info("No changed entries found.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
 
