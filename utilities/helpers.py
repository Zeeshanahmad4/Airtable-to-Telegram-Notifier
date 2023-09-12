# helpers.py

def format_record_for_telegram(record):
    """
    Convert a single Airtable record into a string formatted for Telegram.
    """
    # Extracting the fields from the record
    fields = record.get('fields', {})

    # For this example, let's assume the Airtable has columns 'Title', 'Description', and 'Status'
    title = fields.get('Title', 'N/A')
    description = fields.get('Description', 'N/A')
    status = fields.get('Status', 'N/A')
    
    # Creating a formatted message
    formatted_message = f"*Title:* {title}\n\n*Description:* {description}\n\n*Status:* {status}"
    
    return formatted_message

# Note: As the project evolves, more utility functions can be added to this file.
