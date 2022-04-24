import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        # enumurate local files recursively
        for root, dirs, files in os.walk(file_from):
            for file in files:
                # construct the full local path
                local_path = os.path.join(root, file)
                #print("local: " + local_path)

                # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, file_from)
                #print("Relative path: " + relative_path)
                dropbox_path = os.path.join(file_to, relative_path)
                #print("Dropbox path: " + dropbox_path)

                # upload the file
                with open(local_path, 'rb') as f:
                   dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'sl.BGQdkfuo48ssJVaRh2ayXwrFRg8sNeuvxY872S69sKUwPW83oPa6jW1Hb2Pzlf7lclKydCRJsav2ednFepMNB4mgdPmZyQ3qgUjsje-ZePSeD0-m7tR56eOufsh6bOltdWqvxjo'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path you want to move: "))
    file_to = input("Enter the path to upload to Dropbox: ") # This is the full path to upload the file to, including the name you wish the file to be called once uploaded

    transferData.upload_file(file_from, file_to)
    print("The file or folder has been moved!")

main()