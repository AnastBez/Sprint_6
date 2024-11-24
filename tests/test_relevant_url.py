import allure
import pytest
from pages.order_page import *
from pages.main_page import MainPageQuestion
from locators.main_page_locators import MainPageLocators
from data import *
from time import sleep


class TestOrderPage:
    @allure.title("Нажатие на логотип «Яндекс")
    @allure.description('Оформить заказ - Нажать "Проверить статус" - Клик по лого "Яндекс"')
    @pytest.mark.parametrize(
        'locator, data_set, locator_link, url_link',
        [
            (MainPageLocators.HEADER_ORDER_BUTTON, DataOrder.DATA_SET_1, MainPageLocators.YANDEX_HEADER_BUTTON,
             URLs.url_Dzen)
        ]
    )
    def test_check_ya_click_logo(self, driver, locator, locator_link, url_link, data_set):
        driver.get(URLs.url)
        main_page = MainPageQuestion(driver)
        order_page = OrderPageForm(driver)
        main_page.click_element(locator)
        order_page.set_order(data_set)
        current_url = order_page.check_url(locator_link)

        assert url_link in current_url


class TestOrderPage2:
    @pytest.mark.parametrize(
        'locator, data_set, check, locator_link, url_scooter',
        [
            (MainPageLocators.HEADER_ORDER_BUTTON, DataOrder.DATA_SET_2, OrderPageLocators.CHECK_STATUS,
             MainPageLocators.SCOOTER_HEADER_BUTTON, URLs.url_scooter)
        ]
    )
    @allure.title("Нажатие на логотип «Самоката")
    @allure.description('Оформить заказ - Нажать "Проверить статус" - Клик по лого "Самоката"')
    def test_check_scooter_click_logo(self, driver, locator, data_set, check, locator_link, url_scooter):
        driver.get(URLs.url)
        main_page = MainPageQuestion(driver)
        order_page = OrderPageForm(driver)
        main_page.click_element(locator)
        order_page.set_order(data_set)
        main_page.click_element(check)
        sleep(10)
        main_page.click_element(locator_link)

        assert url_scooter == driver.current_url
