#!/usr/bin/python3
# -*- coding: utf-8 -*-

from json import load, dump, JSONDecodeError
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

    def check_file_structure(self, file_data):
        if self.default_values is not None:
            return file_data.keys() == self.default_values.keys()

    def get_data(self):
        ret_data, err_msg = False, ""
        try:
            with open(self.file_name, encoding="utf-8", mode="r") as f:
                ret_data = load(f)
            if not self.check_file_structure(ret_data):
                err_msg = "В файле настроек не хватает данных. Пересоздайте файл с настройками."
                ret_data = False
        except FileNotFoundError:
            err_msg = "Файл не найден. Создан новый шаблонный файл."
            self.create_default_file()
        except JSONDecodeError:
            err_msg = "Ошибка загрузки файла, проверьте на наличие ошибок."
        finally:
            return ret_data, err_msg
