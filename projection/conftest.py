import json
from optparse import Option
import pytest
from selenium import webdriver as selenium_driver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService

Chrome_driver_path = "projection/drivers/chromedriver"
firefox_driver_path = "projection/drivers/geckodriver"
Default_wait_time = 15
Url = 'https://projectiononline.co/login'
Users_path = 'projection/data/userData.json'


# @pytest.fixture(scope='session')
# def config():
#     """
#         Get the data from config.json

#         -------
#         Returns: str
#             data : returns a string with the information of the config.json
#     """
#     with open(Config_path, encoding='utf-8') as config_file:
#         data = json.load(config_file)
#         print(data)
#         return data


@pytest.fixture(scope='session')
def url():
    """
        Get the url for projection

        Returns
        -------
        str
            Url_li : returns a string with the information of the url
    """
    return Url
   

@pytest.fixture(scope='function')
def web_driver():
    """
        Set up the driver

        Returns
        -------
        WebDriver
            driver : returns the webdriver
    """
    option = Options()
    option.add_argument('--allow-running-insecure-content')
    option.add_argument("--disable-web-security")

    # s = ChromeService(Chrome_driver_path)

    driver = selenium_driver.Chrome(executable_path=Chrome_driver_path, options=option)

    driver.implicitly_wait(Default_wait_time)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def config_users():
    """
        Get the data from config.json

        Returns
        -------
        str
            data : returns a string with the information of the users.json
    """
    with open(Users_path, encoding='utf-8') as users_file:
        data = json.load(users_file)

        return data
