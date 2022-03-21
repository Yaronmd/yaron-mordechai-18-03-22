import pytest
import time
from Page.abra_page import Abra_Page
from Test.BaseTest import BaseTest


class TestWhatsApp(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_module(self):
        self.abra_page = Abra_Page(self.driver)

    def test_whatsapp_float_button(self):
        current_page = "https://automation.herolo.co.il/"
        self.abra_page.click_whatsapp_float_button()

        #test if whatsapp web opened
        self.abra_page.switch_tab()
        res = self.abra_page.check_url_page(current_page)
        if not res:
            assert False
        else:
            assert "whatsapp.com" in res