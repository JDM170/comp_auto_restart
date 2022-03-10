#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import exit, argv
# from os import system
from subprocess import Popen
from filesio import FilesIO
from match_name import check_arm_name

file_name = ".\\computer_names.json"
default_values = {
    "1": [  # Пятидневка
        "IT01",
        "IT02"
    ],
    "2": [  # Цех
        "PIS09",
        "PIS10"
    ]
}
loaded_file = None


def main(prog_key):
    global loaded_file
    list_pc_names = loaded_file.get(prog_key)
    if list_pc_names is not None:
        for pc_name in list_pc_names:
            formatted_pc_name = check_arm_name(pc_name)
            if formatted_pc_name is not False:
                # print("pc_name:", formatted_pc_name)
                # system("shutdown /m \\{} /r /t 60 /c \"Плановая перезагрузка компьютера через 1 минуту!\"".format(formatted_pc_name))
                # Popen("shutdown /m \\{} /r /t 60 /c \"Плановая перезагрузка компьютера через 1 минуту!\"".format(formatted_pc_name)).wait()
                print("shutdown /m \\{} /r /t 60 /c \"Плановая перезагрузка компьютера через 1 минуту!\"".format(formatted_pc_name))
    else:
        print("Попробуйте еще раз выбрать область запуска скрипта!")


if __name__ == "__main__":
    if len(argv) < 2:
        print("Укажите номер запускаемой области!\n1 - Кабинеты; 2 - Цех")
        exit()
    try:
        filesio = FilesIO(file_name, default_values)
        loaded_file = filesio.get_data()
        main(argv[1])
    except KeyboardInterrupt:
        exit()
