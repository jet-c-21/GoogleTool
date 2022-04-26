# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/26/22
"""
from ..resourse_service import init_resource_service


def init_google_drive_rs(oauth_cred_file: str, api_name='drive', api_version='v3', scopes=None):
    if scopes is None:
        scopes = ['https://www.googleapis.com/auth/drive']

    return init_resource_service(oauth_cred_file, api_name, api_version, scopes)
