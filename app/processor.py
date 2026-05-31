from pathlib import Path
from .classifier import MailClassifier
from .features import categories
import shutil
import logging


class MailProcessor:
    def __init__(self, reader, classifier, inbox_dir, processed_dir, stats):
        self.reader = reader
        self.classifier = MailClassifier(categories, 0.1)
        self.inbox_dir = Path(inbox_dir)
        self.processed_dir = Path(processed_dir)
        self.stats = stats


    def process_all(self): #обрабатывает все письма в папке входящих
        logging.info("Starting mail processing")

        if not self.inbox_dir.exists():
            logging.error("Inbox folder not found")

            print("Inbox folder not found")
            return self.stats
        for file_path in self.inbox_dir.iterdir():
            if file_path.is_file():
                self.process_one(file_path)

        logging.info("Mail processing completed")
        return self.stats
    
    
    def process_one(self, file_path): #обрабатываем одно письмо, условно решаем что делать с ним
        try:
            message = self.reader.read(file_path)
            category = self.classifier.classify(message.content)
            self.move_to_category(file_path, category)
            self.stats.addToCategory(category)
            self.stats.addProcessed()

            logging.info(f"File {file_path.name} was moved to folder {category}")

        except Exception as e:
            print("Ошибка при обработке файла:", file_path)
            print(type(e).__name__, e)
            self.move_to_broken(file_path)
            self.stats.addBroken()

            logging.warning(f"File {file_path.name} was moved to folder broken")

        self.stats.addTotal()



    def move_to_category(self, file_path, category): #перемещаем письмо в папку своей категории
        processed_folder = self.processed_dir
        category_folder = processed_folder / category   
        category_folder.mkdir(parents=True, exist_ok=True)
        new_file_path = category_folder / file_path.name
        shutil.move(str(file_path), str(new_file_path))


    def move_to_broken(self, file_path): #перемещвем сломанное письмо в папку broken
        processed_folder = self.processed_dir
        broken_folder = processed_folder / 'broken'
        broken_folder.mkdir(parents=True, exist_ok=True)
        new_file_path = broken_folder / file_path.name
        shutil.move(str(file_path), str(new_file_path))
