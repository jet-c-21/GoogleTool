# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/26/22
"""
from typing import Union

import pandas as pd
from googleapiclient.discovery import Resource


class FolderRetriever:
    def __init__(self, resource_service: Resource):
        self.resource_service = resource_service
        self.result = pd.DataFrame(columns=['level', 'path', 'name', 'parent', 'id', 'pid', 'kind'])

    def get_file_df_in_folder(self, folder_id: str) -> Union[pd.DataFrame, None]:
        query = f"parents = '{folder_id}'"

        file_ls = list()
        next_page_token = None
        flag = True
        while flag:
            resp = self.resource_service.files().list(q=query, pageToken=next_page_token).execute()
            file_ls.extend(resp.get('files'))

            next_page_token = resp.get('nextPageToken')
            if next_page_token is None:
                flag = False

        if len(file_ls) == 0:
            return

        df = pd.DataFrame(file_ls)
        return df

    def _find_folder_in_folder(self, searched_folder_id: str, level: int, parent: str) -> Union[pd.DataFrame, None]:
        file_df = self.get_file_df_in_folder(searched_folder_id)
        if file_df is None:
            return

        folder_df = file_df[file_df['mimeType'] == 'application/vnd.google-apps.folder']
        if len(folder_df) == 0:
            return

        folder_df = folder_df[['name', 'id', 'kind']]
        folder_df['level'] = level
        folder_df['parent'] = parent
        folder_df['path'] = folder_df.apply(
            lambda x: f"{x['parent']}{x['name']}" if parent == '/' else f"{x['parent']}/{x['name']}",
            axis=1)
        folder_df['pid'] = searched_folder_id

        return folder_df

    def _make_query(self, query_ls: list):
        record = list()
        for folder_id, level, parent in query_ls:
            folder_df = self._find_folder_in_folder(folder_id, level, parent)
            if folder_df is not None:
                record.append(folder_df)

        if len(record) == 0:
            return

        curr_lv_folder_df = pd.concat(record, ignore_index=True)

        # generate next level query list
        curr_level = curr_lv_folder_df.iloc[0]['level']
        next_level_query_ls = list()
        for i, row in curr_lv_folder_df.iterrows():
            q = (row['id'], curr_level + 1, row['path'])
            next_level_query_ls.append(q)

        # save current level folder df
        self.result = pd.concat([self.result, curr_lv_folder_df], ignore_index=True)

        # do next level query
        self._make_query(next_level_query_ls)

    def get_all_folder(self, root_folder_id: str) -> pd.DataFrame:
        self._make_query([(root_folder_id, 1, '/')])
        return self.result
