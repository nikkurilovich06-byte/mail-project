import logging               #подключаем библиотеку для логирования
import os                     #подключаем библиотеку для работы с папками

def setup_logger():

    os.makedirs("logs", exist_ok=True)       #создается папка logs, если её нет

    logging.basicConfig(                                       #настройка логирования
        filename = "logs/event.log",                            #указываем, где будем хранить логи
        level = logging.INFO,                                    #записываем сообщения уровня INFO и выше (INFO, WARNING, ERROR, CRITICAL)
        format = "%(asctime)s | %(levelname)s | %(message)s",     #шаблон для сообщений (дата | уровень | сообщение)
        encoding = "utf-8"                                         #файл должен поодерживать русский текст
    )

