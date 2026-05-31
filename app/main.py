from pathlib import Path
from mail_reader import MailReader
from processor import MailProcessor


def main():
    inbox_dir = Path("inbox/")
    processed_dir = Path("processed/")

    reader = MailReader()
    stats = {} # ProcessingStats() когда будет готов

    processor = MailProcessor(
        reader=reader,
        inbox_dir=inbox_dir,
        processed_dir=processed_dir,
        stats=stats
    )

    processor.process_all()


if __name__ == "__main__":
    main()