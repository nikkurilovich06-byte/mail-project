from pathlib import Path       # подключаем библиотеку для рботы с путями к файлам

class MailMessage:
    def __init__(self, filename: str, path: Path, content: str, subject: str, sender: str, recipient: str):
        self.filename = filename          # имя файла
        self.path = path                  # путь к файлу
        self.content = content            # содержание сообщения
        self.subject = subject            # тема сообщения
        self.sender =  sender             # отправитель
        self.recipient = recipient        # получатель

class ProcessingStats:
    def __init__(self):
        self.total = 0                    # общее количество обработанных писем
        self.processed = 0                # количество удачно обработанных писем
        self.broken = 0                   # количество сломаных писем
        self.categories = {}              # сколько писем попало в каждую категорию

    def addTotal(self):
        self.total += 1
    
    def addProcessed(self):
        self.processed += 1
    
    def addBroken(self):
        self.broken += 1

    def addToCategory(self, category: str):
        if category in self.categories:         
            self.categories[category] += 1      #если категория уже есть, то увеличиваем её счетчик на 1
        else:
            self.categories[category] = 1       #ели категории нет, то создаем её и присваиваем значение 1
