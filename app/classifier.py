class Feature:
    def __init__ (self, name: str, keywords: list[str], weight: int):
        self.name = name
        self.keywords = keywords
        self.weight = weight
    
    def word_found(self, data:str) -> bool:
        for keyword in self.keywords:
            if keyword in data:
                return True
        return False

    def count_found_words(self,data)->int:
        count=0
        for keyword in self.keywords:
            if keyword in data:
                count += 1
        return count

    def get_score(self, data: str) -> float:
        #print(self.name, self.count_found_words(data)) - для проверки оставил
        return self.count_found_words(data)/len(self.keywords)*self.weight
    


class Category:
    def __init__(self, name: str, features: list[Feature]):
        self.categoryName=name
        self.categoryFeatures=features
    
    def get_total_score_normalized(self, data: str)->float:
        totalScore=0
        sum_weights=sum(abs(feature.weight) for feature in self.categoryFeatures)
        for feature in self.categoryFeatures:
            totalScore += feature.get_score(data)
        
        return totalScore/sum_weights


class MailClassifier:
    
    def __init__(self, categories: list[Category], minScore: float):
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
        
        return [bestCategory, scoresOfCategories] #потом поменять - оставить только bestCategory



#ниже пока что для примера - потом будет подгружаться из других файлов
if __name__ == "__main__":

    spam_features = [
        Feature("срочность", ["срочно", "urgent"], 1),
        Feature("фишинг", ["логин", "пароль", "банковская карта"], 2),
        Feature("выигрыш", ["вы выиграли", "приз", "подарок"], 1),
        Feature("штрафные слова", ["не работает", "уже второй день", "затронуты", "коллег"], -1)
    ]

    important_features = [
        Feature("важность", ["важно", "important"], 3),
        Feature("массовость", ["не работает", "уже второй день", "затронуты", "коллег"], 2),
    ]

    spam_category = Category("spam_phishing", spam_features)
    important_category = Category("important_category", important_features)

    classifier = MailClassifier([spam_category,important_category],0.1)

    text1 = "Здравствуйте! Срочно требуется ваш логин, это важно, ничего не работает"
    text2 = "Добрый день, как дела?"
    
    print()

    print(text1)
    print(classifier.classify(text1))
    print()

    print(text2)
    print(classifier.classify(text2))
    print()







        




    