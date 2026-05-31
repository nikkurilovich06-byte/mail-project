

class Feature:
    def __init__ (self, name: str, keywords: list[str], confidence: int, is_penalty: bool):
        self.name = name
        self.keywords = [keyword.lower() for keyword in keywords]
        self.feature_confidence = confidence
        self.is_penalty=is_penalty
    
    def word_found(self, data:str) -> bool:
        for keyword in self.keywords:
            if keyword in data:
                return True
        return False

    def count_found_words(self,data)->int:
        data=data.lower()
        count=0
        for keyword in self.keywords:
            if keyword in data:
                print(keyword, self.name)
                count += 1
        return count

    def get_feature_confidence(self, data: str) -> float:
        if self.word_found(data):
            return self.feature_confidence
        return 0
    


class Category:
    def __init__(self, name: str, features: list[Feature], min_confidence: int):
        self.category_name=name
        self.category_features=features
        self.min_confidence= min_confidence
    
    def get_category_confidence(self, data: str)->float:
        multiplication=1
        for feature in self.category_features:
            if not feature.is_penalty:
                multiplication *= (1-feature.get_feature_confidence(data))
        total_confidence=1-multiplication

        for feature in self.category_features:
            if feature.is_penalty:
                total_confidence*=(1-feature.get_feature_confidence(data))

        if total_confidence>= self.min_confidence:
            return total_confidence
        return 0


class MailClassifier:
    def __init__(self, categories: list[Category], minScore: float):
        self.categories = categories
        self.min_score=minScore
    
    def classify(self, data: str):
        scoresOfCategories={}
        for category in self.categories:
            scoresOfCategories[category.category_name] = category.get_category_confidence(data)
        
        bestCategory = max(scoresOfCategories, key=scoresOfCategories.get)
        bestScore = scoresOfCategories[bestCategory]

        if bestScore<self.min_score:
            return "needs_review"
        print(bestCategory, scoresOfCategories)
        return bestCategory 








        




    