#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import exit, argv
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
is_debug = False


def main(comp_key):
    global loaded_file, is_debug
    list_pc_names = loaded_file.get("pc").get(comp_key)
    if list_pc_names is None:
        print("Попробуйте еще раз выбрать область запуска скрипта!")
        exit()
    restart_time = loaded_file.get("restart_time")
    restart_message = loaded_file.get("restart_message")
    for pc_name in list_pc_names:
        formatted_pc_name = matchio.check_pc_name(pc_name)
        if formatted_pc_name is False:
            continue
        if is_debug is False:
            Popen("shutdown /m \\\{} /r /f /t {} /c {}".format(formatted_pc_name, restart_time, restart_message)).wait()
            sleep(2)
        else:
            print("shutdown /m \\\{} /r /f /t {} /c {}".format(formatted_pc_name, restart_time, restart_message))


if __name__ == "__main__":
    if len(argv) < 2:
        print("Укажите номер запускаемой области!\n1 - Кабинеты; 2 - Цех")
        exit()
    if len(argv) == 3:
        is_debug = argv[2].strip() == "debug"
    try:
        filesio = FilesIO(default_values=default_values)
        loaded_file, err_msg = filesio.get_data()
        if loaded_file is False:
            print(err_msg)
            exit()
        matchio = MatchIO()
        main(argv[1])
    except KeyboardInterrupt:
        exit()
