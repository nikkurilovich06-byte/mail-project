from .classifier import Feature, Category

spam_features = [
    Feature("запрос_учетных_данных", ["логин и пароль", "введите пароль", "укажите пароль", "пароль от аккаунта", "учетные данные", "credentials"], confidence=0.9, is_penalty=False),
    Feature("банковские_данные", ["банковская карта", "данные карты", "номер карты", "cvv", "платежные данные", "bank card"], confidence=0.9, is_penalty=False),
    Feature("подозрительная_верификация", ["подтвердите личность", "подтвердите аккаунт", "верификация аккаунта", "аккаунт будет заблокирован", "подозрительный вход", "verify account"], confidence=0.75, is_penalty=False),
    Feature("подозрительные_ссылки", ["totally-not-spam", "secure-login", "password-reset", "cdn-service", "company-ru", "кликните по ссылке", "перейдите по ссылке"], confidence=0.8, is_penalty=False),
    Feature("выигрыш_акция", ["вы выиграли", "розыгрыш", "приз", "подарок", "iphone", "скидка 90", "только сегодня", "exclusive offer"], confidence=0.8, is_penalty=False),
    Feature("давление_срочностью", ["срочн", "urgent", "немедленно", "до конца дня", "последнее предупреждение"], confidence=0.2, is_penalty=False),
    Feature("penalty_реальный_инцидент", ["ошибка 500", "не работает", "сервис недоступен", "затронуты сотрудники", "весь отдел", "работа остановлена"], confidence=0.3, is_penalty=True),
]

spam_category = Category("spam_phishing", spam_features, min_confidence=0.5)


critical_incident_features = [
    Feature("остановка_работы", ["работа остановлена", "работа полностью остановлена", "блокирует работу", "невозможно работать", "business stopped"], confidence=0.9, is_penalty=False),
    Feature("недоступность_сервиса", ["сервис недоступен", "не отвечает", "недоступн", "лежит сервис", "service down", "unavailable", "не проходит healthcheck"], confidence=0.85, is_penalty=False),
    Feature("критическая_ошибка", ["ошибка 500", "критический инцидент", "критичн", "массовый сбой", "critical incident", "major outage"], confidence=0.85, is_penalty=False),
    Feature("массовое_влияние", ["у всего отдела", "у всех отдела", "затронуты сотрудники", "несколько коллег", "массово", "affected users"], confidence=0.7, is_penalty=False),
    Feature("эскалация", ["повторно", "без ответа", "второй запрос", "не устранена", "нужен статус", "escalation"], confidence=0.55, is_penalty=False),
    Feature("срочность", ["срочн", "urgent", "asap", "немедленно"], confidence=0.25, is_penalty=False),
    Feature("penalty_фишинг", ["вы выиграли", "банковская карта", "введите пароль", "подтвердите аккаунт", "приз", "розыгрыш"], confidence=0.35, is_penalty=True),
]

critical_incident_category = Category("critical_incidents", critical_incident_features, min_confidence=0.45)

categories=[
    spam_category,
    critical_incident_category
]



