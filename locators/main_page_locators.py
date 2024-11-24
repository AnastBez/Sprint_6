from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_ACCEPT = By.XPATH, ".//button[text()='да все привыкли']"  # Соглашение с куками
    YANDEX_HEADER_BUTTON = By.XPATH, ".//img[@alt='Yandex']/parent::a"  # Лого Яндекс в хедере
    SCOOTER_HEADER_BUTTON = By.XPATH, ".//img[@alt='Scooter']/parent::a"  # Лого Самокат в хедере

    QUESTION = By.ID, 'accordion__heading-{}'  # Кнопка ракрытия вопроса
    ANSWER = By.ID, 'accordion__panel-{}'  # Строка расположение ответа
    QUESTION_8 = By.ID, 'accordion__heading-7'  # Кнопка расположения 8-го вопроса

    HEADER_ORDER_BUTTON = By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"
    # Кнопка Заказать в хедере
    MIDDLE_ORDER_BUTTON = By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"
    # Кнопка заказать в центре лендинга
