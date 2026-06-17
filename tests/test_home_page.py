import allure
import pytest
from pages.home_page import HomePage
from data import FAQ_DATA

@allure.title("Тесты на проверку главной страницы")
class TestHomePage:

    @allure.title("Проверка ответов на вопросы о важном")
    @allure.description("При клике на вопрос должен открываться соответствующий ответ")
    @pytest.mark.parametrize("num", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_faq(self, home_page, num):
        home_page.click_faq_question(num)  
        actual_faq_question_text = home_page.get_faq_question_text(num)
        actual_faq_answer_text = home_page.get_faq_answer_text(num)
        assert actual_faq_question_text == FAQ_DATA[num][0], "Текст вопроса {index}: {actual_faq_question_text} не совпадает с ожидаемым {FAQ_DATA[num][0]}" 
        assert actual_faq_answer_text == FAQ_DATA[num][1],  "Текст ответа {index}: {actual_faq_answer_text} не совпадает с ожидаемым {FAQ_DATA[num][1]}" 
