#!/usr/bin/python3
# -*- coding: utf-8 -*-

from json import load, dump, JSONDecodeError
from os.path import isfile
from os import remove


class FilesIO:
    def __init__(self, file_name=".\\settings.json", default_values=None):
        self.file_name = file_name
        self.default_values = default_values

    def create_default_file(self):
        if self.default_values is None:
            return
        if isfile(self.file_name):
            remove(self.file_name)
        with open(self.file_name, encoding="utf-8", mode="w") as f:
            dump(self.default_values, f, indent=4, separators=(",", " : "))

    def check_file_structure(self, file_data):
        if self.default_values is None:
            return False
        return file_data.keys() == self.default_values.keys()

    def get_data(self):
        ret_data, err_msg = False, ""
        if isfile(self.file_name) is False:
            self.create_default_file()
        try:
            with open(self.file_name, encoding="utf-8", mode="r") as f:
                ret_data = load(f)
        except JSONDecodeError:
            return False, "Ошибка загрузки файла, проверьте файл на наличие ошибок."
        if not self.check_file_structure(ret_data):
            ret_data = False
            err_msg = "В файле настроек не хватает данных. Удалите или пересоздайте файл с настройками."
        return ret_data, err_msg
