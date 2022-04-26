# coding: utf-8
"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 4/26/22
"""
from typing import Union

import pandas as pd
from googleapiclient.discovery import Resource


class SheetEditor:
    def __init__(self, resource_service: Resource):
        self.resource_service = resource_service

    def get_sheet_metadata(self, sheet_id: str):
        pass
