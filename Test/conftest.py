import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

MAIN_URL = "http://automation.herolo.co.il"

@pytest.fixture(scope='class')
def init_driver(request):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(MAIN_URL)
    driver.maximize_window()
    request.cls.driver = driver
    
    
    yield
    driver.close()

