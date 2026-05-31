

class Feature:
    def __init__ (self, name: str, keywords: list[str], weight: int):
        self.name = name
        self.keywords = [keyword.lower() for keyword in keywords]
        self.weight = weight
    
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

    def get_score(self, data: str) -> float:
        #print(self.name, self.count_found_words(data)) - для проверки оставил
        return self.count_found_words(data)/len(self.keywords)*self.weight
    


class Category:
    def __init__(self, name: str, features: list[Feature]):
        self.categoryName=name
        self.category_features=features
    
    def get_total_score_normalized(self, data: str)->float:
        total_score=0
        sum_weights=sum(abs(feature.weight) for feature in self.category_features)
        for feature in self.category_features:
            total_score += feature.get_score(data)
        
        return total_score/sum_weights


class MailClassifier:
    def __init__(self,categories: list[Category], minScore: float):
        self.categories = categories
        self.minScore=minScore
    
    def classify(self, data: str):
        scoresOfCategories={}
        for category in self.categories:
            scoresOfCategories[category.categoryName] = category.get_total_score_normalized(data)
        
        bestCategory = max(scoresOfCategories, key=scoresOfCategories.get)
        bestScore = scoresOfCategories[bestCategory]

        if bestScore<self.minScore:
            return "needs_review"
        print(bestCategory, scoresOfCategories)
        return bestCategory 








        




    