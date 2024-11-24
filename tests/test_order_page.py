import allure
import pytest
from pages.order_page import OrderPageForm
from pages.main_page import MainPageQuestion
from locators.main_page_locators import MainPageLocators
from data import *


class TestOrderPage:

    @pytest.mark.parametrize(
        'locator, data_set',
        [
            (MainPageLocators.HEADER_ORDER_BUTTON, DataOrder.DATA_SET_1),
            (MainPageLocators.MIDDLE_ORDER_BUTTON, DataOrder.DATA_SET_2)
        ]
    )
    @allure.title("Проверка создания заказа")
    @allure.description('Нажатие по кнопке "Заказать" - Заполнение "Для кого самокат" - Заполнение "Про аренду" - '
                        'Проверка номера заказа')
    def test_make_order(self, driver, locator, data_set):
        driver.get(URLs.url)
        main_page = MainPageQuestion(driver)
        order_page = OrderPageForm(driver)
        main_page.scroll_to_element(locator)
        main_page.click_element(locator)
        order_page.set_order(data_set)
        assert order_page.check_order()
