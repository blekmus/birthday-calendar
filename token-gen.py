# for debugging purposes
# this script can be used to generate a token.json file
# which can be used in script.py to authenticate with google contacts API

from google_auth_oauthlib.flow import InstalledAppFlow
import httplib2
import logging

httplib2.debuglevel = 4

SCOPES = ["https://www.googleapis.com/auth/contacts.readonly"]

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


# get google token.json file
def get_token():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials


creds = get_token()

with open("token.json", "w") as token:
    token.write(creds.to_json())
