import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    @allure.step('Открыть страницу: {url}')
    def open(self, url):
        self.driver.get(url)
    
    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    @allure.step('Ввести в поле {locator} текст {text}')
    def set_text(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)     
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element_with_wait(locator).text
    
    @allure.step("Прокрутить к элементу {locator}")
    def scroll_to_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть по элементу {locator}')
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
      
    def is_displayed(self, locator):
        elements_by_locator = self.driver.find_elements(*locator)
        return len(elements_by_locator) > 0 and elements_by_locator[0].is_displayed
        
    @allure.step("Подождать открытия новой вкладки")
    def wait_for_new_window(self, expected_count=2):
        self.wait.until(EC.number_of_windows_to_be(expected_count))

    @allure.step('Перейти на открывшуюся вкладку')
    def switch_to_another_window(self):
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[-1])

    @allure.step("Закрыть текущее окно")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Подождать переход по URL, содержащему фрагмент {url_part}")
    def wait_for_url_contains(self, url_part):
        try:
            self.wait.until(EC.url_contains(url_part))
            return True
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url
    
