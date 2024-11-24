import allure
import pytest
import data
from pages.main_page import MainPageQuestion
from data import *


class TestMainPage:
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, data.Answers.A_1),
            (1, data.Answers.A_2),
            (2, data.Answers.A_3),
            (3, data.Answers.A_4),
            (4, data.Answers.A_5),
            (5, data.Answers.A_6),
            (6, data.Answers.A_7),
            (7, data.Answers.A_8)
        ]
    )
    @allure.title("Проверка ответов в 'Вопросы о важном'")
    @allure.description("Открыть главную страницу - Прокрутить до блока 'Вопросы о важном' - Проверить ответ")
    def test_answer_is_relevant(self, driver, num, result):

        main_page = MainPageQuestion(driver)
        driver.get(URLs.url)
        result_page = main_page.get_relevant_answer_text(num)
        assert result_page == result
