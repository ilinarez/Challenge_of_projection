"""This module contains the methods of the login pages """
import inspect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from projection.helpers import helpers
from projection.selectors.LoginSelectors import Login_Selectors

class LogInPages:

    def __init__(self, driver, test_screenshots_folder_path):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.test_screenshot_folder_path = test_screenshots_folder_path + inspect.stack()[1].function
        self.login_txt = Login_Selectors.loginTxt
        self.email_in = Login_Selectors.emailTxt
        self.password_in = Login_Selectors.passwordTxt
        self.log_in_button = Login_Selectors.logInButton

    def write_email(self,email):
        """
            Write the email
            
            Arguments 
            -------
            email: (str)
                the email of the user
        """
        
        self.wait.until(EC.visibility_of_element_located(self.login_txt))
        email_in = self.driver.find_element(by=self.email_in[0], value=self.email_in[1])
        email_in.send_keys(email)
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'write_email'))

    def write_password(self,password):
        """
            Write the password
            
            Arguments 
            -------
            password: (str)
                the password of the user
        """
        
        passw = self.driver.find_element(by=self.password_in[0], value=self.password_in[1])
        passw.send_keys(password)
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'write_password'))


    def click_log_in_button(self):
        """
            Click the "log in" button
        """
        continue_btn = self.driver.find_element(by=self.log_in_button[0], value=self.log_in_button[1])
        continue_btn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_continue_button'))
