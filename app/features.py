from .classifier import Feature, Category

spam_features = [
        Feature("срочность", ["срочн", "urgent"], confidence = 0.2),
        Feature("фишинг", ["логин", "пароль", "банковская карта", "подвердите"], confidence = 0.6),
        Feature("выигрыш", ["вы выиграли", "приз", "подарок"], confidence = 0.8),
        Feature("штрафные слова", ["не работает", "уже второй день", "затронуты", "коллег"], confidence = 0.3)
    ]

important_features = [
        Feature("срочность", ["срочно", "urgent"], 1),
        Feature("важность", ["важно", "important"], 3),
        Feature("массовость", ["не работает", "уже второй день", "затронуты", "коллег"], 2),
    ]

spam_category = Category("spam_phishing", spam_features, min_confidence)
important_category = Category("important_category", important_features)

categories = [spam_category, important_category]

