from pathlib import Path
from processor import MailProcessor


def main():
    inbox = Path("inbox/")
    
    processor = MailProcessor()

    files = list(inbox.iterdir())

    for file in files:
        if file.is_file():
            processor.process(file)


if __name__ == "__main__":
    main()