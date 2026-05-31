from pathlib import Path
from .processor import MailProcessor
from .mail_reader import MailReader
from .models import ProcessingStats

def main():
    inbox = Path("inbox/")
    processed = Path("processed/")
    stats=ProcessingStats()
    reader=MailReader()
    
    processor = MailProcessor(reader=reader,classifier=None,inbox_dir=inbox, processed_dir=processed,stats=stats)

    processor.process_all()

    '''
    files = list(inbox.iterdir())

    for file in files:
        if file.is_file():
            processor.process(file)
'''

if __name__ == "__main__":
    main()