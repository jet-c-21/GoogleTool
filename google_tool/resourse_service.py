# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/26/22
"""
import pickle
import os
from typing import Union
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build, Resource
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request


def init_resource_service(client_secret_file, api_service_name, api_version, *scope_ls) -> Union[Resource, None]:
    print(client_secret_file, api_service_name, api_version, scope_ls, sep='-')

    scopes = [scp for scp in scope_ls[0]]
    print(scopes)

    cred = None

    pickle_file = f"token_{api_service_name}_{api_version}.pickle"
    # print(pickle_file)

    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes)
            cred = flow.run_local_server()

        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    try:
        service = build(api_service_name, api_version, credentials=cred)
        print(api_service_name, 'service created successfully')
        return service

    except Exception as e:
        print('Unable to connect.')
        print(e)
        return
