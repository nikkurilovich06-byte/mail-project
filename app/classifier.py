
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
    def __init__(self, name: str, features: list[Feature], maxScore: int):
        self.categoryName=name
        self.categoryFeatures=features
        self.maxScore=maxScore
    
    def get_total_score_normalized(self, data: str)->int:
        totalScore=0
        for feature in self.categoryFeatures:
            totalScore += feature.get_score(data)
        return totalScore/self.maxScore


class MailClassifier:
    def __init__(self, categories: list[Category], minScore: float):
        self.categories = categories
        self.minScore=0.1
    
    def classify(self, data: str)-> str:
        scoresOfCategories={}
        for category in self.categories:
            scoresOfCategpries[category.name] = category.get_score(data)
        
        bestCategory = max(scoresOfCategory, key=scoresOfCategory.get(0))
        bestScore = scoresOfCategory[bestCategory]

        if bestScore<minScore:
            return "needs_review"
        
        return bestCategory










        




    