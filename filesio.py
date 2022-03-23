#!/usr/bin/python3
# -*- coding: utf-8 -*-

from json import load, dump
from os.path import exists
from os import remove


class FilesIO:
    def __init__(self, file_name=".\\settings.json", default_values=None):
        self.file_name = file_name
        self.default_values = default_values

    def create_default_file(self):
        if self.default_values is not None:
            if exists(self.file_name):
                remove(self.file_name)
            with open(self.file_name, encoding="utf-8", mode="w") as f:
                dump(self.default_values, f, indent=4, separators=(",", " : "))

    def get_data(self):
        try:
            with open(self.file_name, encoding="utf-8", mode="r") as f:
                ret_data = load(f)
            return ret_data
        except FileNotFoundError:
            self.create_default_file()
            # ret_data = self.default_values
            return False
