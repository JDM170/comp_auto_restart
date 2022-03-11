#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import exit, argv
# from os import system
from subprocess import Popen
from filesio import FilesIO
from match_name import MatchIO

file_name = ".\\computer_names.json"
default_values = {
    "expr_list": [
        [r"^[a-zA-Z]+\d+$", "R54-630300"],  # THE01
        [r"^\d+[a-zA-Z]+\d+$", "R54-"],  # 630300THE01
        [r"^[rR]\d*[-]\d+[a-zA-Z]+\d+$", ""]  # R54-630300THE01
    ],
    "comp": {
        "2": [  # Пятидневка
            "IT01",
            "IT02"
        ],
        "7": [  # Цех
            "PIS09",
            "PIS10"
        ]
    }
}
loaded_file = None


def main(comp_key):
    global loaded_file
    list_pc_names = loaded_file.get("comp").get(comp_key)
    if list_pc_names is not None:
        for pc_name in list_pc_names:
            formatted_pc_name = matchio.check_arm_name(pc_name)
            if formatted_pc_name is not False:
                # print("pc_name:", formatted_pc_name)
                # system("shutdown /m \\{} /r /f /t 60 /c \"Плановая перезагрузка компьютера через 1 минуту!\"".format(formatted_pc_name))
                # Popen("shutdown /m \\{} /r /f /t 60 /c \"Плановая перезагрузка компьютера через 1 минуту!\"".format(formatted_pc_name)).wait()
                print("shutdown /m \\\{} /r /f /t 60 /c \"Плановая перезагрузка компьютера через 1 минуту!\"".format(formatted_pc_name))
    else:
        print("Попробуйте еще раз выбрать область запуска скрипта!")


if __name__ == "__main__":
    if len(argv) < 2:
        print("Укажите номер запускаемой области!\n2 - Кабинеты; 7 - Цех")
        exit()
    try:
        filesio = FilesIO(file_name, default_values)
        loaded_file = filesio.get_data()
        if loaded_file is False:
            return
        matchio = MatchIO(loaded_file.get("expr_list"))
        main(argv[1])
    except KeyboardInterrupt:
        exit()
