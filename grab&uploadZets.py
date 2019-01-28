from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/script.projects']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1gcHzsXx6Vmhg5lxTeDKFFQL6WZveI3AvAr_dBW43FJI'
SAMPLE_RANGE_NAME = 'A2:H85'


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/home/jweezy/Downloads/creds.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)
    service2 = build('script', 'v1', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                               range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    info = []
    path = "/home/jweezy/Documents/Code/zettelgeist/docs/example/mlb"
    for (dirpath, dirnames, filenames) in os.walk(path):
        for f in filenames:
            if ".yaml" in f:
                info.append(parseFile(path + "/"+ f))

    request3 = {
    "function": "update",
    "devMode": True,
    "parameters": ["1cFPIXaPGawk1ULZj2NnSKCzOHmLatBMc04vSVZ-czJE"]
    }

    titles = []
    row = 2
    for i in info:
        for j in i.keys():
            if j == "title":
                request3.update({"parameters": request3.get("parameters") + ["A"+str(row)]})
                request3.update({"parameters": request3.get("parameters") + [i.get(j)]})
                response = service2.scripts().run(scriptId='AKfycbxrE7z65fIIxxxmtXoV8tcZu3v5GTu4Hc053BnL0rKVrJ4fHoE', body=request3).execute()

            if j == "url":
                request3.update({"parameters": request3.get("parameters")+ ["B"+str(row)]})
                request3.update({"parameters": request3.get("parameters")+ [i.get(j)]})
                response = service2.scripts().run(scriptId='AKfycbxrE7z65fIIxxxmtXoV8tcZu3v5GTu4Hc053BnL0rKVrJ4fHoE', body=request3).execute()

            if j == "summary":
                request3.update({"parameters": request3.get("parameters")+ ["C"+str(row)]})
                request3.update({"parameters": request3.get("parameters")+ [i.get(j)]})
                response = service2.scripts().run(scriptId='AKfycbxrE7z65fIIxxxmtXoV8tcZu3v5GTu4Hc053BnL0rKVrJ4fHoE', body=request3).execute()

            if j == "note":
                request3.update({"parameters": request3.get("parameters")+ ["D"+str(row)]})
                request3.update({"parameters": request3.get("parameters")+ [i.get(j)]})
                response = service2.scripts().run(scriptId='AKfycbxrE7z65fIIxxxmtXoV8tcZu3v5GTu4Hc053BnL0rKVrJ4fHoE', body=request3).execute()

            if j == "tags":
                request3.update({"parameters": request3.get("parameters")+ ["E"+str(row)]})
                request3.update({"parameters": request3.get("parameters")+ [i.get(j)]})
                response = service2.scripts().run(scriptId='AKfycbxrE7z65fIIxxxmtXoV8tcZu3v5GTu4Hc053BnL0rKVrJ4fHoE', body=request3).execute()

            request3 = {
            "function": "update",
            "devMode": True,
            "parameters": ["1cFPIXaPGawk1ULZj2NnSKCzOHmLatBMc04vSVZ-czJE"]
            }
        row += 1





    #try:
    request = {
    "function": "getRange",
    "devMode": True,
    "parameters": [
    "1rqFwTIINwswir1uCB7q21_m4reyyT76uUJOUbKaPwbE",
    ]
    }
    request2 = {
    "function": "createDoc",
    "devMode": True,
    "parameters": ["testZetel"]
    }

    folderSet = response['response'].get('result')
    print(folderSet)
    #except:
        # The API encountered a problem.
        #print("There was a problem homie.")
def parseFile(file):
    info = open(file, "r")
    files = {file: ''}
    dict = {"title":'', "summary": "", "url":'', "note":"", "tags":"" }
    for i in info:
        for j in dict.keys():
            if j+":" in i:
                currentTag = j
                if j == "url":
                    firstLine = i.split("url:")[1]
                    break
                firstLine = i.split(":")[1]
                break
        if firstLine != '':
            dict.update({currentTag: firstLine})
            firstLine = ''
        else:
            dict.update({currentTag: dict.get(currentTag)+ "\n" + i})
    info.close()
    return dict



main()
