from pathlib import Path

class MailMessage:
    def __init__(self, filename: str, path: Path, content: str, subject: str, sender: str, recipient: str):
        self.filename = filename
        self.path = path
        self.content = content
        self.subject = subject
        self.sender = sender
        self.recipient = recipient

class ProcessingStats:
    def __init__(self):
        self.total = 0
        self.processed = 0
        self.broken = 0
        self.categories = {}

    def addTotal(self):
        self.total += 1
    
    def addProcessed(self):
        self.processed += 1
    
    def addBroken(self):
        self.broken += 1

    def addToCategory(self, category: str):
        if category in self.categories:
            self.categories[category] += 1
        else:
            self.categories[category] = 1
