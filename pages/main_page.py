from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from time import sleep


class MainPageQuestion(BasePage):
    def get_relevant_answer_text(self, num):
        locator_question = self.format_locators(MainPageLocators.QUESTION, num)
        locator_answer = self.format_locators(MainPageLocators.ANSWER, num)
        self.scroll_to_element(MainPageLocators.QUESTION_8)
        self.click_element(locator_question)
        sleep(3)
        return self.get_text_element(locator_answer)
