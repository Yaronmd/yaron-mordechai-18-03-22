from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Page.BasePage import BasePage

class Abra_Page(BasePage):
    # fill form section
    NAME = (By.XPATH, "//input[@id='name']")
    COMPANY = (By.XPATH, "//input[@id='company']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    TELEPHONE = (By.XPATH, "//input[@id='telephone']")
    
    TALK_WITH_US_BUTTON = (By.XPATH, "//form[@id='section-inputs']/descendant::a")

    WHATSAPP_SHORTCUT = (By.XPATH,"//a[contains(@class, 'BtnWhatsapp')]")

    #error footers"
    WRONG_EMAIL = (By.XPATH,"//span[.='כתובת אימייל לא חוקית']//parent::label")
    WRONG_PHONE = (By.XPATH,"//span[.='מספר טלפון לא חוקי']//parent::label")
    #missing footers
    MISSING_NAME = (By.XPATH,"//span[text()='שדה שם הוא שדה חובה']")
    MISSING_COMPANY = (By.XPATH,"//span[text()='שדה חברה הוא שדה חובה']")
    MISSING_PHONE = (By.XPATH,"//span[text()='שדה טלפון הוא שדה חובה']")
    MISSING_EMAIL = (By.XPATH,"////span[text()='שדה אימייל הוא שדה חובה']")




    def __init__(self, driver):
        self.driver = driver

    def set_name(self, text):
        self.send_keys(self.NAME, text)

    def set_company(self, text):
        self.send_keys(self.COMPANY, text)

    def set_email(self, text):
        self.send_keys(self.EMAIL, text)

    def set_telephone(self, text):
        self.send_keys(self.TELEPHONE, text)

    def get_name(self):
        text = self.get_element_value(self.NAME)
        return text

    def get_email(self):
        text = self.get_element_value(self.EMAIL)
        return text

    def get_telephone(self):
        text = self.get_element_value(self.TELEPHONE)
        return text

    def get_company(self):
        text = self.get_element_value(self.COMPANY)
        return text

    def get_wrong_email_warning(self):
        text = self.get_element_text(self.WRONG_EMAIL)
        return text

    def get_wrong_telephone_warning(self):
        text = self.get_element_text(self.WRONG_PHONE)
        return text

    def get_missing_email_warning_exist(self):
        text = self.is_element_visible(self.MISSING_EMAIL)
        return text

    def get_missing_company_name_warning_exist(self):
        print("self.MISSING_COMPANY")
        return self.is_element_visible(self.MISSING_COMPANY)

    def get_missing_phone_warning_exist(self):
        return self.is_element_visible(self.MISSING_PHONE)

    def get_missing_name_warning_exist(self):
        return self.is_element_visible(self.MISSING_NAME)


    def click_whatsapp_float_button(self):
        result = self.perform_click(self.WHATSAPP_SHORTCUT)
        return result

    def click_talk_with_us(self):
        result = self.perform_click(self.TALK_WITH_US_BUTTON)
        return result

    def scroll_to_object(self, param):
        try:
            self.scroll_to_element("//input[@id='{}']".format(param))
            return True
        except Exception as e:
            return False

    def clear_name_textbox(self):
        self.clear_text_box(self.NAME)

    def clear_email_textbox(self):
        self.clear_text_box(self.EMAIL)

    def clear_company_textbox(self):
        self.clear_text_box(self.COMPANY)

    def cleat_telephone_textbox(self):
        self.clear_text_box(self.TELEPHONE)
