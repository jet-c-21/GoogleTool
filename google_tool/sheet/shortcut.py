# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/26/22
"""
from ..resourse_service import init_resource_service


def init_google_sheet_rs(oauth_cred_file: str, api_name='sheets', api_version='v4', scopes=None):
    if scopes is None:
        scopes = ['https://www.googleapis.com/auth/spreadsheets']

    return init_resource_service(oauth_cred_file, api_name, api_version, scopes)
