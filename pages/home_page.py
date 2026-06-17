import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import urls
from locators.home_page_locators import HomePageLocators

class HomePage(BasePage):
  
    @allure.step("Открыть главную страницу")
    def open_page(self):
        self.open(urls.BASE_URL)
        self.accept_cookies()

    @allure.step("Проверить, что открыта домашняя страница")
    def is_home_page_opened(self):
        return self.get_current_url() == urls.BASE_URL
    
    @allure.step("Получить текст вопроса №{index}")
    def get_faq_question_text(self, index):
        return self.get_text(HomePageLocators.get_faq_question_locator(index-1)) 
     
    @allure.step("Нажать на вопрос №{index}")
    def click_faq_question(self, index):
        question_locator = HomePageLocators.get_faq_question_locator(index-1)
        self.scroll_to_element(question_locator)
        self.click(question_locator)

    @allure.step("Получить текст ответа на вопрос №{index}")
    def get_faq_answer_text(self, index):
        answer_locator = HomePageLocators.get_faq_answer_locator(index-1)
        return self.get_text(answer_locator)
        
    @allure.step("Разрешить cookies, если появилось сообщение")
    def accept_cookies(self):
        if self.is_displayed(HomePageLocators.ACCEPT_COOKIES_BUTTON):
            self.click(HomePageLocators.ACCEPT_COOKIES_BUTTON)
 
    @allure.step("Нажать кнопку 'Заказать' в header")
    def click_top_order_button(self):
        self.click(HomePageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать логотип 'Самокат'")
    def click_scooter_logo(self):
        self.click(HomePageLocators.SCOOTER_LOGO)

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        self.click(HomePageLocators.YANDEX_LOGO)