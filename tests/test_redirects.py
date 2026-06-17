import allure
from pages.home_page import HomePage


@allure.title("Тесты переходов")
class TestRedirects:

    @allure.title('Проверка редиректа на главную страницу по логотипу Самоката')
    def test_scooter_logo_redirect(self, home_page):
        home_page.click_top_order_button()
        home_page.click_scooter_logo()
        assert home_page.is_home_page_opened()

    @allure.title('Проверка редиректа на Дзен по логотипу Яндекса')
    def test_yandex_logo_redirect(self, home_page):
        home_page.click_yandex_logo()
        home_page.wait_for_new_window()
        home_page.switch_to_another_window()

        assert home_page.wait_for_url_contains("dzen")
        home_page.close_current_window()
        home_page.switch_to_another_window()
        assert home_page.is_home_page_opened()