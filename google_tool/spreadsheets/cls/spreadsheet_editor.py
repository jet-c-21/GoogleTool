# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/26/22
"""
from typing import Union

import pandas as pd
from googleapiclient.discovery import Resource


class SpreadsheetEditor:
    def __init__(self, resource_service: Resource):
        self.resource_service = resource_service

    def get_spreadsheet_metadata(self, spreadsheet_id: str) -> dict:
        metadata = self.resource_service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()

        return metadata

    def get_whole_sheet(self, spreadsheet_id: str, sheet_title: str) -> dict:
        resp = self.resource_service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            majorDimension='ROWS',
            range=sheet_title,
        ).execute()

        return resp

    def get_whole_spreadsheet(self, spreadsheet_id: str) -> list:
        """
        :param spreadsheet_id:
        :return:
            [
                {
                    'title': sheet_title (str),
                    'data': sheet_data (dict),
                },

                {...},
                {...}
            ]
        """
        result = list()
        s_sheet_meta = self.get_spreadsheet_metadata(spreadsheet_id)
        sheet_title_ls = [s['properties']['title'] for s in s_sheet_meta['sheets']]

        for sheet_title in sheet_title_ls:
            sheet_data = self.get_whole_sheet(spreadsheet_id, sheet_title)
            result.append({'title': sheet_title, 'data': sheet_data})

        return result

    def get_spreadsheet_sdf_ls_by_default_parse(self, spreadsheet_id) -> list:
        result = list()
        spreadsheet_data = self.get_whole_spreadsheet(spreadsheet_id)

        for s_sheet_data in spreadsheet_data:
            s_sheet_title = s_sheet_data['title']
            s_sheet_data = s_sheet_data['data']['values']

            col = s_sheet_data[0]
            record = s_sheet_data[1:]
            df = pd.DataFrame(record, columns=col)

            result.append({'title': s_sheet_title, 'data': df})

        return result
