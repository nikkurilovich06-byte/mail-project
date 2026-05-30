
class Feature:
    def __init__(self, name: str, keywords: list[str], weight: int):
        self.name = name
        self.keywords = keywords
        self.weight = weight
    
    def word_found(self, data:str) -> bool:
        for keyword in self.keywords:
            if keyword in data:
                return True
        return False


    def get_score(self, data: str) -> float:
        if self.word_found(data):
            return self.weight
        return 0

class Category:
    def __init__(self, name: str, features: list[Feature]):
        self.categoryName=name
        self.categoryFeatures=features
    
    def get_total_score(self, data: str)->int:
        totalScore=0
        for feature in self.categoryFeatures:
            totalScore += feature.get_score(data)
        return totalScore





    