
class Feature:
    def __init__(self, name: str, keywords: list[str], weight: int):
        self.name = name
        self.keywords = keywords
        self.weight = weight
    
    def word_found(self, data:str) -> bool:

        for keyword in self.keywords:
            if keyword in text:
                return True
        return False


    def get_score(self, data: str) -> float:
        if self.word_found(data):
            return self.weight
        return 0


    