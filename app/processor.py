from pathlib import Path
import shutil

class MailProcessor:
    def __init__(self, reader, classifier, inbox_dir, processed_dir, stats):
        self.reader = reader
        self.classifier = classifier
        self.inbox_dir = Path(inbox_dir)
        self.processed_dir = Path(processed_dir)
        self.stats = stats

    def process_mail(self):
        for file_path in self.inbox_dir.iterdir():
            if file_path.is_file():
                self.process_one(file_path)
        return self.stats
    
    def process_one(self, file_path):
        try:
            message = self.reader.read(file_path)
            category = self.classifier.classify(message.content)
            self.move_to_category(file_path, category)
            self.stats.add_category(category)

        except Exception:
            self.move_to_broken(file_path)
            self.stats.add_broken()

