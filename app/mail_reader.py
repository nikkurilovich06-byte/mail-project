from pathlib import Path
from dataclasses import dataclass
import chardet


@dataclass
class MailMessage:
    filename: str
    subject: str
    sender: str
    body: str


class MailReader:

    def __init__(self):
        pass

    def read(self, file_path: Path) -> MailMessage | None:

        if file_path.suffix not in ['.eml', '.txt']:
            # Неизвестный формат
            return None

        if file_path.stat().st_size == 0:
            # Пустой файл
            return None

        raw_file = file_path.read_bytes()
        encoding = chardet.detect(raw_file)['encoding'] or 'utf-8'
        content = raw_file.decode(encoding, errors='replace')

        return self._parse(file_path.name, content)

    def _parse(self, filename: str, content: str) -> MailMessage:
        lines = content.splitlines()
        subject = ""
        sender = ""
        body = []
        in_body = False

        subject_keys = ["Subject:", "Тема:"]
        sender_keys = ["From:", "От кого:"]

        for line in lines:
            if in_body:
                body.append(line)
            elif any(line.startswith(key) for key in subject_keys):
                subject = line.split(":", 1)[1].strip()
            elif any(line.startswith(key) for key in sender_keys):
                sender = line.split(":", 1)[1].strip()
            elif line == "":
                in_body = True

        return MailMessage(
            filename=filename,
            subject=subject,
            sender=sender,
            body="\n".join(body)
        )