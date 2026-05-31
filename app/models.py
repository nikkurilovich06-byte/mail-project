from pathlib import Path          # подключаем библиотеку для работы с путями к файлам

class MailMessage:
    def __init__(self, filename: str, path: Path, content: str, subject: str, sender: str, recipient: str):
        self.filename = filename       # имя файла
        self.path = path               # путь к файлу
        self.content = content         # содержимое письма
        self.subject = subject         # тема письма
        self.sender = sender           # отправитель письма
        self.recipient = recipient     # получатель письма

class ProcessingStats:
    def __init__(self):
        self.total = 0                 # общее количество обработанных писем
        self.processed = 0             # количество успешно обработанных писем
        self.broken = 0                # количество сломанных писем
        self.categories = {}           # словарь для хранения количества писем в каждой категории

    def addProcessed(self):
        self.processed += 1
        self.total += 1
    
    def addBroken(self):
        self.broken += 1
        

    def addToCategory(self, category: str):
        if category in self.categories:        # если категория уже есть в словаре, то увеличиваем значение на 1
            self.categories[category] += 1
        else:                                  #если категории нет в словаре, то добавляем ее и присваиваем значение 1
            self.categories[category] = 1
 gi