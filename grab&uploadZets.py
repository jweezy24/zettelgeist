from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/script.projects']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1gcHzsXx6Vmhg5lxTeDKFFQL6WZveI3AvAr_dBW43FJI'
SAMPLE_RANGE_NAME = 'A2:H85'

#google script code
create_doc = '''
function createDoc() {
  doc = DocumentApp.create('Document Name');
}
'''.strip()

get_range_of_doc = '''
function createDoc() {
  var doc = SpreadsheetApp.openById('1gcHzsXx6Vmhg5lxTeDKFFQL6WZveI3AvAr_dBW43FJI');
  var namedRanges = doc.getNamedRanges()
  if (namedRanges.length > 1) {
  Logger.log(namedRanges[0].getName());
}
}
'''.strip()

SAMPLE_MANIFEST = '''
{
  "timeZone": "America/New_York",
  "exceptionLogging": "CLOUD"
}
'''.strip()

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

    #service = build('sheets', 'v4', credentials=creds)
    service2 = build('script', 'v1', credentials=creds)

    # Call the Sheets API
    #sheet = service.spreadsheets()
    #result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
    #                            range=SAMPLE_RANGE_NAME).execute()
    #values = result.get('values', [])


    #try:
    request = { # A request to run the function in a script. The script is identified by the
      # specified `script_id`. Executing a function on a script returns results
      # based on the implementation of the script.
    "function": "createDoc", # The name of the function to execute in the given script. The name does not
        # include parentheses or parameters.
    "devMode": True, # If `true` and the user is an owner of the script, the script runs at the
        # most recently saved version rather than the version deployed for use with
        # the Apps Script API. Optional; default is `false`.
    "parameters": [ # The parameters to be passed to the function being executed. The object type
        # for each parameter should match the expected type in Apps Script.
        # Parameters cannot be Apps Script-specific object types (such as a
        # `Document` or a `Calendar`); they can only be primitive types such as
        # `string`, `number`, `array`, `object`, or `boolean`. Optional.
      "",
    ]
  }
    response = service2.scripts().run(scriptId='AKfycbxrE7z65fIIxxxmtXoV8tcZu3v5GTu4Hc053BnL0rKVrJ4fHoE', body=request).execute()
    folderSet = response['response'].get('result')
    print(folderSet)
    #except:
        # The API encountered a problem.
        #print("There was a problem homie.")

main()
