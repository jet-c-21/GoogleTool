# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/26/22
"""
from pprint import pp
import pandas as pd
from google_tool import init_resource_service
from google_tool.drive import init_google_drive_rs, FolderRetriever
from google_tool.spreadsheets import init_google_sheet_rs, SpreadsheetEditor
import json

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

CLIENT_SECRET_FILE = 'jcv_oauth.json'

if __name__ == '__main__':
    # drive_rs = init_google_drive_rs(CLIENT_SECRET_FILE)
    # fr = FolderRetriever(drive_rs)
    #
    # folder_id = '1uR5XCZ3zSnbiuTHCB9uez9JHXUdndm-I'  # PrettyPaper/data
    # x = fr.get_all_folder(folder_id)
    # print(x)

    s_sheet_id = '19VtTXhTf_y5gOp8DkMVh7sPnVNAV7gAndxmD_jNmwR4'  # PrettyPaper-Member
    sheet_rs = init_google_sheet_rs(CLIENT_SECRET_FILE)
    sse = SpreadsheetEditor(sheet_rs)
    x = sse.get_spreadsheet_sdf_ls_by_default_parse(s_sheet_id)
    pp(x)

    # json_str = json.dumps(x)
    # print(json_str)

    # resp = sheet_rs.spreadsheets().values().get(
    #     spreadsheetId=sheet_id,
    #     majorDimension='ROWS',
    #     range='PrettyPaper-Member!A1:E24',
    # ).execute()
    #
    # pp(resp)


