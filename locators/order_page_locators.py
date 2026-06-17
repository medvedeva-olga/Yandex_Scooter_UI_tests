from selenium.webdriver.common.by import By


class OrderPageLocators:
    
    HEADER = By.CSS_SELECTOR, "[class*='Order_Header']"
    FIRST_NAME_INPUT = By.XPATH, '//input[@placeholder="* Имя"]'
    LAST_NAME_INPUT = By.XPATH, '//input[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_INPUT = By.XPATH, '//input[@placeholder="* Станция метро"]' 
    @staticmethod
    def get_metro_option_locator(station_name):
        return By.XPATH, f'//div[contains(@class, "select-search__select")]//button[.//div[text()="{station_name}"]]'


    PHONE_INPUT = By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'
    NEXT_BUTTON = By.XPATH, './/button[text()="Далее"]'
    DATE_INPUT = By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'
    RENT_PERIOD_DROPDOWN = By.CLASS_NAME, 'Dropdown-placeholder'
    @staticmethod
    def get_rent_period_option_locator(rent_period):
        return By.XPATH, f'.//div[contains(@class, "Dropdown-option") and text()="{rent_period}"]'
    @staticmethod
    def get_color_checkbox(color):
        return By.ID, color
    COMMENT_INPUT = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'

    ORDER_BUTTON = By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]'

    CONFIRM_ORDER_BUTTON = By.XPATH, '//div[contains(@class, "Order_Modal")]//button[text()="Да"]'
    SUCCESS_MODAL = By.XPATH, '//div[contains(@class, "Order_ModalHeader") and contains(text(), "Заказ оформлен")]'