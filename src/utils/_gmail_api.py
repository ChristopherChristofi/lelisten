import os, sys, pickle
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

def create_service(client_secret_file, api_name, api_version, *scopes):
    # print(client_secret_files, api_name, api_version, scopes, sep='-')
    CLIENT_SECRECT_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    cred = None
    
    if not os.path.exists(f'.tokens'):
        os.makedirs('.tokens')

    token_pickle_file = f'.tokens/token_{API_SERVICE_NAME}_{API_VERSION}.pickle'

    if os.path.exists(token_pickle_file):
        with open(token_pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRECT_FILE, SCOPES)
            cred = flow.run_local_server()

        with open(token_pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print('Unable to connect.', file=sys.stderr)
        exit(1)
