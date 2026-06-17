import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step('Заполнить данные об арендаторе и нажать далее')
    def fill_customer_data(self, first_name, last_name, address, metro_station, phone):
        self.set_text(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.set_text(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.set_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.set_text(OrderPageLocators.METRO_INPUT, metro_station)
        self.click(OrderPageLocators.get_metro_option_locator(metro_station))
        self.set_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)


    @allure.step('Заполнить данные об аренде')
    def fill_rent_data(self, date, period, color, comment):
        self.set_text(OrderPageLocators.DATE_INPUT, date)
        self.click(OrderPageLocators.HEADER)
        self.driver.find_element(*OrderPageLocators.RENT_PERIOD_DROPDOWN).click()
        self.click(OrderPageLocators.get_rent_period_option_locator(period))
        self.click(OrderPageLocators.get_color_checkbox(color))
        self.set_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Ввести данные в форму заказа')
    def fill_order_data(self, order_data):
        self.fill_customer_data(
            order_data["first_name"],
            order_data["last_name"],
            order_data["address"],
            order_data["metro_station"],
            order_data["phone"]
        )
        self.fill_rent_data(
            order_data["date"],            
            order_data["rent_period"],
            order_data["color"],
            order_data["comment"]
        )

    @allure.step('Нажать кнопку "Заказать"')
    def press_submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def press_confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверить отображение сообщения об успешном заказе')
    def is_success_modal_displayed(self):
        return self.find_element_with_wait(OrderPageLocators.SUCCESS_MODAL).is_displayed()

