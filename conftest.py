import pytest
from selenium import webdriver



# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture(scope='function')
def driver(capabilities=None):
    chrome_options = Options()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Remote(command_executor='http://172.17.0.2:4444/wd/hub',options=chrome_options)
    #    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    #    driver = webdriver.Chrome(service=driver_service)
    #    driver.maximize_window()
    yield driver
    driver.quit()
