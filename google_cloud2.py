from googleapiclient.discovery import build
from google.oauth2 import service_account
import io
from googleapiclient.http import MediaIoBaseDownload


SCOPES=['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE="service_account.json"
PARENT_FOLDER_ID="19KD1YwYT5plTs9q1XuTJ8LO7lWIBHxrf"

def authentificate():
    creds=service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_photo(file_path):
    creds=authentificate()
    service=build('drive', 'v3', credentials=creds)
    file_metadata={
        'name' : "Hello",
        'parents' : [PARENT_FOLDER_ID]
    }
    file=service.files().create(body=file_metadata, media_body=file_path).execute()

def download_photo(file_id, dest_path):
    creds = authentificate()
    service = build('drive', 'v3', credentials=creds)
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(dest_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))


def get_file_id(file_name, parent_folder_id):
    creds = authentificate()
    service = build('drive', 'v3', credentials=creds)
    query = f"name='{file_name}' and '{parent_folder_id}' in parents"
    response = service.files().list(q=query, fields='files(id)').execute()
    files = response.get('files', [])
    if files:
        return files[0]['id']
    else:
        print(f"File '{file_name}' not found in folder with ID '{parent_folder_id}'")
        return None

def delete_file(file_id):
    service = authenticate()
    try:
        service.files().delete(fileId=file_id).execute()
        print(f"File with ID {file_id} deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
file_id = get_file_id('lamp.png', PARENT_FOLDER_ID)


download_photo(file_id, 'downloaded_file.png')
upload_photo("C:\TPs\Ateliers\ATELIER_DEV_WEB\Images\lightv1.png")