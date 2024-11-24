from pages.base_page import BasePage
from locators.order_page_locators import *
from time import sleep


class OrderPageForm(BasePage):

    def set_order(self, data_set):
        self.add_text_in_element(OrderPageLocators.NAME_INPUT, data_set['name'])
        self.add_text_in_element(OrderPageLocators.LAST_NAME_INPUT, data_set['last_name'])
        self.add_text_in_element(OrderPageLocators.ADDRESS_INPUT, data_set['address'])
        self.click_element(OrderPageLocators.STATION_INPUT)
        sleep(3)
        self.click_element(OrderPageLocators.STATION_TAP)
        self.add_text_in_element(OrderPageLocators.TEL_NUM_INPUT, data_set['tel_num'])
        self.click_element(OrderPageLocators.NEXT_STEP_BUTTON)
        self.add_text_in_element(OrderPageLocators.DATA_DELIVERY, data_set['order_data'])
        sleep(1)
        self.click_element(OrderPageLocators.RENT_INPUT)
        self.click_element(OrderPageLocators.DAYS_RENT)
        self.click_element(OrderPageLocators.BLACK_COLOR)
        self.add_text_in_element(OrderPageLocators.COMMENT_INPUT, data_set['comment'])
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_ORDER)
        sleep(3)

    def check_order(self):
        locator = OrderPageLocators.NUM_ORDER
        return self.get_text_element(locator)

    def check_url(self, locator):
        self.click_element(OrderPageLocators.CHECK_STATUS)
        self.click_element(locator)
        sleep(20)
        self.switch_to()
        sleep(5)
        return self.current_url()
