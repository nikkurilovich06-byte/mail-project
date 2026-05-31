from pathlib import Path
from .processor import MailProcessor
from .mail_reader import MailReader
from .models import ProcessingStats
from .logger_config import setup_logger
import logging

def main():
    setup_logger()
    logging.info("Program started")
    inbox = Path("inbox/")
    processed = Path("processed/")
    stats=ProcessingStats()
    reader=MailReader()
    
    processor = MailProcessor(reader=reader,classifier=None,inbox_dir=inbox, processed_dir=processed,stats=stats)

    processor.process_all()
    logging.info("Program finished")

if __name__ == "__main__":
    main()