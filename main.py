#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import exit, argv
from os import system, getcwd
from subprocess import Popen
from filesio import FilesIO
from m_match_name.main import MatchIO
from time import sleep


default_values = {
    "restart_time": 60,
    "restart_message": "Плановая перезагрузка компьютера через 1 минуту!",
    "pc": {
        "1": [  # Пятидневка
            "IT01",
            "IT02"
        ],
        "2": [  # Цех
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
                    sleep(2)
                else:
                    print("shutdown /m \\\{} /r /f /t {} /c {}".format(formatted_pc_name, restart_time, restart_message))
    else:
        print("Попробуйте еще раз выбрать область запуска скрипта!")


if __name__ == "__main__":
    print(argv)
    if len(argv) < 2:
        print("Укажите номер запускаемой области!\n1 - Кабинеты; 2 - Цех")
        exit()
    try:
        filesio = FilesIO(default_values=default_values)
        loaded_file, err_msg = filesio.get_data()
        if loaded_file is False:
            raise Exception(err_msg)
        matchio = MatchIO()
        main(argv[1], argv[2].strip() == "debug")
    except Exception as exc:
        print(exc)
        exit()
    except KeyboardInterrupt:
        exit()
