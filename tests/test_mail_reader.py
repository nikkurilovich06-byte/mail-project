from pathlib import Path
import pytest
from app.mail_reader import MailReader
from app.models import MailMessage


@pytest.fixture
def reader():
    return MailReader()

@pytest.fixture
def tmp_file(tmp_path):
    def _make_file(filename: str, content: str, encoding: str = 'utf-8'):
        file = tmp_path / filename
        file.write_bytes(content.encode(encoding))
        return file
    return _make_file

def test_read_valid_file_returns_mail_message(reader, tmp_file):
    file = tmp_file("mail.txt", "From: user@edu.hse.ru\nSubject: Тест\n\nПривет!")
    assert isinstance(reader.read(file), MailMessage)

def test_read_parses_subject(reader, tmp_file):
    file = tmp_file("mail.txt", "From: user@edu.hse.ru\nSubject: Важное письмо\n\nТекст")
    assert reader.read(file).subject == "Важное письмо"

def test_read_parses_sender(reader, tmp_file):
    file = tmp_file("mail.txt", "From: user@edu.hse.ru\nSubject: Тест\n\nТекст")
    assert reader.read(file).sender == "user@edu.hse.ru"

def test_read_parses_recipient(reader, tmp_file):
    file = tmp_file("mail.txt", "From: user@edu.hse.ru\nTo: it-support@company.ru\nSubject: Тест\n\nТекст")
    assert reader.read(file).recipient == "it-support@company.ru"

def test_read_content_contains_subject_and_body(reader, tmp_file):
    file = tmp_file("mail.txt", "From: user@edu.hse.ru\nSubject: Срочно\n\nСервер упал")
    message = reader.read(file)
    assert "Срочно" in message.content
    assert "Сервер упал" in message.content