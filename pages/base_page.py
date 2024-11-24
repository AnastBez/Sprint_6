from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def add_text_in_element(self, locator, text):
        self.find_element(locator).send_keys(text)

    def get_text_element(self, locator):
        return self.find_element(locator).text

    @staticmethod
    def format_locators(locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator

    def current_url(self):
        return self.driver.current_url

    def switch_to(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
