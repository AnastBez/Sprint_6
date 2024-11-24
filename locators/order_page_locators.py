from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = By.XPATH, '//input[@placeholder="* Имя"]'  # Поле Имя
    LAST_NAME_INPUT = By.XPATH, '//input[@placeholder="* Фамилия"]'  # Поле Фамилия
    ADDRESS_INPUT = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'  # Поле Адрес
    STATION_INPUT = By.XPATH, '//input[@placeholder="* Станция метро"]'  # Поле Метро
    STATION_TAP = By.XPATH, '/html/body/div/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[5]/button'  # Кнопка станции
    # "Комсомольская"
    TEL_NUM_INPUT = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'  # Поле Телефон
    NEXT_STEP_BUTTON = By.XPATH, './/button[text()="Далее"]'  # Кнопка Далее для перехода к след стр.

    DATA_DELIVERY = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'  # Поле выьорка даты
    RENT_INPUT = By.XPATH, ".//span[@class='Dropdown-arrow']"  # Поле открытия списка с выбором срока аренды
    DAYS_RENT = By.XPATH, ".//div[text()='сутки']"  # выбор срока "сутки"
    BLACK_COLOR = By.ID, 'black'  # цвет самоката - черный
    COMMENT_INPUT = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'  # Поле Комментарий
    ORDER_BUTTON = By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"  # Кнопка Заказать
    CONFIRM_ORDER = By.XPATH, ".//button[text()='Да']"  # Кнопка подтвержленияя создания заказа
    NUM_ORDER = By.XPATH, ".//div[contains(text(),'Номер заказа')]"  # Текст с номером заказа

    CHECK_STATUS = By.XPATH, ".//button[text()='Посмотреть статус']"  # Кнопка проверки статуса заказа в поп-апе
