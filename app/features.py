from .classifier import Feature, Category

spam_features = [
        Feature("срочность", ["срочно", "urgent"], 1),
        Feature("фишинг", ["логин", "пароль", "банковская карта"], 2),
        Feature("выигрыш", ["вы выиграли", "приз", "подарок"], 1),
        Feature("штрафные слова", ["не работает", "уже второй день", "затронуты", "коллег"], -1)
    ]

important_features = [
        Feature("срочность", ["срочно", "urgent"], 1),
        Feature("важность", ["важно", "important"], 3),
        Feature("массовость", ["не работает", "уже второй день", "затронуты", "коллег"], 2),
    ]

spam_category = Category("spam_phishing", spam_features)
important_category = Category("important_category", important_features)



