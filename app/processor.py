from pathlib import Path
import shutil

class MailProcessor:
    def __init__(self, reader, classifier, inbox_dir, processed_dir, stats):
        self.reader = reader
        self.classifier = classifier
        self.inbox_dir = Path(inbox_dir)
        self.processed_dir = Path(processed_dir)
        self.stats = stats


        