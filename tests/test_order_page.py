import allure
import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from data import ORDER_DATA


@allure.title("Тесты для страницы заказа")
class TestOrderPage:

    @allure.title("Проверка успешного заказа самоката")
    @allure.description("Проверить весь флоу позитивного сценария с двумя наборами данных.")
    @pytest.mark.parametrize(
        "order_button_locator, order_data", [
        (HomePageLocators.ORDER_BUTTON_TOP, ORDER_DATA[0]), 
        (HomePageLocators.ORDER_BUTTON_BOTTOM, ORDER_DATA[1])
        ])
    def test_create_order(self, driver, order_button_locator, order_data):
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.scroll_to_element(order_button_locator)
        home_page.click(order_button_locator)
        
        order_page = OrderPage(driver)
        order_page.fill_order_data(order_data)
        order_page.press_submit_order()
        order_page.press_confirm_order()

        assert order_page.is_success_modal_displayed()
