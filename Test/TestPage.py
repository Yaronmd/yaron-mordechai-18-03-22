import pytest
import time
from Page.abra_page import Abra_Page
from Test.BaseTest import BaseTest


class TestPage(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_module(self):
        self.abra_page = Abra_Page(self.driver)


    def test_fill_lower_form_currect(self):
        #testing filling lower form
        self.abra_page.scroll_to_object("name")
        self.abra_page.set_name("Yaron")
        self.abra_page.set_company("MRL")
        self.abra_page.set_email("yaronmord@gmail.com")

        self.abra_page.set_telephone("0545651550")

        if self.abra_page.get_name() == "Yaron":
            pass
        if self.abra_page.get_email() == "yaronmord@gmail.com":
            pass

        assert  self.abra_page.click_talk_with_us()

        current_page = "https://automation.herolo.co.il/"
        time.sleep(20)
        res = self.abra_page.check_url_page(current_page)
        if not res:
            assert False
        else:
            if "thank-you" not in res:
                assert False

