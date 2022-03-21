import pytest
import time

from selenium.webdriver import Keys

from Page.abra_page import Abra_Page
from Test.BaseTest import BaseTest


class TestWrongInput(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_module(self):
        self.abra_page = Abra_Page(self.driver)

    @pytest.mark.order(1)
    def test_wrong_input_email(self):
        self.abra_page.scroll_to_object("name")
        self.abra_page.set_name("Yaron")
        self.abra_page.set_company("MRL")

        self.abra_page.set_email("1L2L#L4dAd")

        if not self.abra_page.click_talk_with_us():
            assert False
        time.sleep(5)
        if self.abra_page.get_email() == "1L2L#L4dAd":
            if self.abra_page.get_wrong_email_warning() != "כתובת אימייל לא חוקית":
                assert False

    @pytest.mark.order(2)
    def test_wrong_phone_number(self):
        self.abra_page.scroll_to_object("name")
        self.abra_page.set_telephone("052123123123123")

        if not self.abra_page.click_talk_with_us():
            assert False

            time.sleep(5)
            if self.abra_page.get_telephone() == "052123123123123":
                if self.abra_page.get_wrong_telephone_warning() != "מספר טלפון לא חוקי":
                    assert False

    @pytest.mark.order(3)
    def test_submit_empty_fields(self):
        self.abra_page.scroll_to_object("name")
        #clearing textsboxes
        self.abra_page.clear_name_textbox()
        self.abra_page.clear_company_textbox()
        self.abra_page.clear_email_textbox()
        self.abra_page.cleat_telephone_textbox()

        assert self.abra_page.click_talk_with_us()

        time.sleep(5)
        #checking missing values
        if not self.abra_page.get_missing_company_name_warning_exist() and \
           not self.abra_page.get_missing_name_warning_exist() and \
           not self.abra_page.get_missing_email_warning_exist() and \
           not self.abra_page.get_missing_phone_warning_exist():
            assert False

