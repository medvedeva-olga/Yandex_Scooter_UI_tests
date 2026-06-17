from selenium.webdriver.common.by import By

class HomePageLocators:

    ACCEPT_COOKIES_BUTTON = By.ID, "rcc-confirm-button"

    @staticmethod
    def get_faq_question_locator(index):
        return By.ID, f"accordion__heading-{index}"
    
    @staticmethod
    def get_faq_answer_locator(index):
        return By.ID, f"accordion__panel-{index}"
    
    ORDER_BUTTON_TOP = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text() = 'Заказать']"
    ORDER_BUTTON_BOTTOM = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text() = 'Заказать']"

    SCOOTER_LOGO = By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"
    YANDEX_LOGO = By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"
