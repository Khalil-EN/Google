from googleapiclient.discovery import build
from google.oauth2 import service_account
import io
from googleapiclient.http import MediaIoBaseDownload
import time
import subprocess

SCOPES=['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE="service_account.json"
PARENT_FOLDER_ID="19KD1YwYT5plTs9q1XuTJ8LO7lWIBHxrf"

def authentificate():
    creds=service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds


def monitor_changes():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    while True:
        # Get list of files in the specified folder
        results = service.files().list(q=f"'{FOLDER_ID}' in parents", fields="files(id, name)").execute()
        files = results.get('files', [])

        if files:
            # Check for new files
            for file in files:
                file_id = file['id']
                file_name = file['name']
                # Trigger script if a new file is detected
                subprocess.Popen(['python3', 'C:\TPs\Python\gtts_sample_espoir.py.py', file_id, file_name])

        # Wait for a certain period before checking again (e.g., every 5 minutes)
        time.sleep(300)
if __name__ == '__main__':
    monitor_changes()