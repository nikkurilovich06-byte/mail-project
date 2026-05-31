from pathlib import Path
from app.models import MailMessage, ProcessingStats

def test_MailMessage_filename():
    mail = MailMessage("mail_04.txt", Path("inbox/mail_04.txt"), "Let's go to the party today!", "Invitation", "alex34@gmail.ru", "era78@gmail.ru")
    
    assert mail.filename == "mail_04.txt"
    assert mail.path == Path("inbox/mail_04.txt")
    assert mail.content == "Let's go to the party today!"
    assert mail.subject == "Invitation"
    assert mail.sender == "alex34@gmail.ru"
    assert mail.recipient == "era78@gmail.ru"

def test_ProcessingStats_initialization():
    stats = ProcessingStats()
    
    assert stats.total == 0
    assert stats.processed == 0
    assert stats.broken == 0
    assert stats.categories == {}

def test_ProcessingStats_addProcessed():
    stats = ProcessingStats()
    stats.addProcessed()
    
    assert stats.processed == 1
    assert stats.total == 1
    assert stats.broken == 0

def test_ProcessingStats_addBroken():
    stats = ProcessingStats()
    stats.addBroken()
    
    assert stats.broken == 1
    assert stats.total == 1
    assert stats.processed == 0

def test_ProcessingStats_mix_addBroken_addProcessed():
    stats = ProcessingStats()
    stats.addBroken()
    stats.addProcessed()
    stats.addProcessed()

    assert stats.broken == 1
    assert stats.processed == 2
    assert stats.total == 3

def test_ProcessingStats_addToCategory():
    stats = ProcessingStats()
    stats.addToCategory("spam")
    
    assert stats.categories["spam"] == 1

def test_ProcessingStats_mix_addToCategory():
    stats = ProcessingStats()
    stats.addToCategory("spam")
    stats.addToCategory("ham")
    stats.addToCategory("spam")

    assert stats.categories["spam"] == 2
    assert stats.categories["ham"] == 1

