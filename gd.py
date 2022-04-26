# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/25/22
"""
from pprint import pp
import pandas as pd
from Google import create_service
from googleapiclient.discovery import Resource

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

CLIENT_SECRET_FILE = 'jcv_oauth.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']


def get_folder_file_df(api_service: Resource, folder_id: str) -> pd.DataFrame:
    query = f"parents = '{folder_id}'"

    file_ls = list()
    next_page_token = None
    flag = True
    while flag:
        resp = api_service.files().list(q=query, pageToken=next_page_token).execute()
        file_ls.extend(resp.get('files'))

        next_page_token = resp.get('nextPageToken')
        if next_page_token is None:
            flag = False

    df = pd.DataFrame(file_ls)
    return df


def zzz_get_all_folders(api_service: Resource, folder_id: str):
    result = pd.DataFrame(columns=['level', 'path', 'name', 'parent', 'id', 'pid'])
    folder_ls = list()

    flag = True
    while flag:
        parent = '/'
        level = 1
        pid = folder_id
        fid_ls = [folder_id]

        for fid in fid_ls:
            ff_df = get_folder_file_df(api_service, fid)
            folder_df = ff_df[ff_df['mimeType'] == 'application/vnd.google-apps.folder']
            folder_df = folder_df[['name', 'id', 'kind']]
            folder_df['level'] = level
            folder_df['parent'] = parent
            folder_df['path'] = folder_df.apply(
                lambda x: f"{x['parent']}{x['name']}" if parent == '/' else f"{x['parent']}/{x['name']}",
                axis=1)
            folder_df['pid'] = pid

            result = pd.concat([result, folder_df])
            print(result)

        flag = False


def find_folder(api_service: Resource, level: int, parent: str, pid: str):
    ff_df = get_folder_file_df(api_service, pid)
    folder_df = ff_df[ff_df['mimeType'] == 'application/vnd.google-apps.folder']
    if len(folder_df) == 0:
        return

    folder_df = folder_df[['name', 'id', 'kind']]
    folder_df['level'] = level
    folder_df['parent'] = parent
    folder_df['path'] = folder_df.apply(
        lambda x: f"{x['parent']}{x['name']}" if parent == '/' else f"{x['parent']}/{x['name']}",
        axis=1)
    folder_df['pid'] = pid

    return folder_df

def xxx()

def get_all_folders(api_service: Resource, folder_id: str):
    result = pd.DataFrame(columns=['level', 'rel_path', 'name', 'id', 'pid'])
    folder_df = find_folder(api_service, 1, '/', folder_id)
    print(folder_df)



if __name__ == '__main__':
    service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    pp(dir(service))

    # folder_id = '16Voqk1_hndZCJFONFI3Dj8md-WrjlI_Y'  # PrettyPaper
    # folder_id = '1uR5XCZ3zSnbiuTHCB9uez9JHXUdndm-I'  # PrettyPaper/data

    # folder_df = get_folder_file_df(service, folder_id)
    # print(folder_df)

    # get_all_folders(service, folder_id)
