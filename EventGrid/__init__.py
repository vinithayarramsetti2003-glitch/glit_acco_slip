import logging
import json
import azure.functions as func
from azure.storage.blob import BlobClient

def main(event: func.EventGridEvent):

    data = event.get_json()
    blob_url = data["url"]

    logging.info(f"New blob created: {blob_url}")

    # Determine file type
    if "/atm/" in blob_url:
        file_type = "ATM"
    elif "/upi/" in blob_url:
        file_type = "UPI"
    else:
        file_type = "UNKNOWN"

    # Download blob
    blob = BlobClient.from_blob_url(blob_url)
    content = blob.download_blob().readall().decode("utf-8")

    logging.info(f"File content length: {len(content)}")
    
    # TODO: process content here
    # Validate → clean → insert into DB

    logging.info("Processing complete.")