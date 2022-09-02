#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import exit, argv
from os import system
from subprocess import Popen
from filesio import FilesIO
from m_match_name.main import MatchIO


default_values = {
    "restart_time": 60,
    "restart_message": "Плановая перезагрузка компьютера через 1 минуту!",
    "pc": {
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


def main(comp_key, is_debug):
    global loaded_file
    list_pc_names = loaded_file.get("pc").get(comp_key)
    if list_pc_names is not None:
        restart_time = loaded_file.get("restart_time")
        restart_message = loaded_file.get("restart_message")
        for pc_name in list_pc_names:
            formatted_pc_name = matchio.check_pc_name(pc_name)
            if formatted_pc_name is not False:
                if is_debug is False:
                    # system("shutdown /m \\\{} /r /f /t 60 /c \"Плановая перезагрузка компьютера через 1 минуту!\"".format(formatted_pc_name))
                    Popen("shutdown /m \\\{} /r /f /t {} /c {}".format(formatted_pc_name, restart_time, restart_message)).wait()
                else:
                    print("shutdown /m \\\{} /r /f /t {} /c {}".format(formatted_pc_name, restart_time, restart_message))
    else:
        print("Попробуйте еще раз выбрать область запуска скрипта!")


if __name__ == "__main__":
    if len(argv) < 3:
        print("Укажите номер запускаемой области!\n2 - Кабинеты; 7 - Цех")
        exit()
    try:
        filesio = FilesIO(default_values=default_values)
        loaded_file = filesio.get_data()
        if loaded_file is False:
            raise OSError
        matchio = MatchIO()
        main(argv[1], argv[2].strip() == "debug")
    except OSError:
        print("Файл с настройками не найден. Создан файл со стандартными настройками.")
        exit()
    except KeyboardInterrupt:
        exit()
