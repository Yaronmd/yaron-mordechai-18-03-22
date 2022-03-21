import pytest
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sys import platform

class BasePage:

    def _init_(self, driver):
        self.driver = driver

    def perform_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).click()
        except TimeoutException or NoSuchElementException:
            return False
        return True

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            print(element.text)
            return element.text
        except TimeoutException:
            return False

    def is_element_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator))
        except ElementNotVisibleException:
            return False
        return True

    def scroll_to_element(self, element,perform_click=False):
        element = self.driver.find_element(by=By.XPATH,value=element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        if perform_click:
            actions.click()
        actions.perform()

    def check_url_page(self,old_url):
        try:

            element = WebDriverWait(self.driver, 10).until(lambda driver: old_url != self.driver.current_url
                                                       )
            print(element)
            return self.driver.current_url
        except TimeoutException:
            return False



    def switch_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


    def clear_text_box(self,to_clear):

            if not self.perform_click(to_clear):
                return False
            if platform == "darwin":
                self.send_keys(to_clear, Keys.COMMAND + 'a')
                self.send_keys(to_clear, Keys.BACKSPACE)
                return True
            elif platform == "windows":
                self.send_keys(to_clear, Keys.CONTROL + 'a')
                self.send_keys(to_clear, Keys.BACKSPACE)
                return True
            return False

    def get_element_value(self, by_locator, attribute="value"):
        val = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(by_locator)). \
            get_attribute(attribute)
        return val