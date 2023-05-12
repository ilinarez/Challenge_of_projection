"""This module contains the common methods """
import inspect, pathlib
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from projection.helpers import helpers
from projection.selectors.CommonSelectors import Common_Selectors 
from projection.selectors.DetailOfCollectionSelectors import Detail_Collection_Selectors 
from selenium.webdriver.common.keys import Keys

class CommonMethods:

    def __init__(self, driver, test_screenshots_folder_path):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.test_screenshot_folder_path = test_screenshots_folder_path + inspect.stack()[1].function
        self.email_span = Common_Selectors.emailspan
        self.profile_li = Common_Selectors.profileLi
        self.user_name_txt = Common_Selectors.userNametxt
        self.bio_txt = Common_Selectors.biotxt
        self.role_txt = Common_Selectors.roletxt  
        self.edit_button = Common_Selectors.editButton
        self.user_name_input = Common_Selectors.userNameInput
        self.role_input = Common_Selectors.roleInput
        self.bio_input = Common_Selectors.bioInput
        self.update_button = Common_Selectors.updateButton


    def click_email_span(self):
        """
            Click the "email" text
        """
        self.wait.until(EC.visibility_of_element_located(self.email_span))
        emailspan = self.driver.find_element(by=self.email_span[0], value=self.email_span[1])
        emailspan.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_email_span'))

    def click_profile_li(self):
        """
            Click the "profile" option
        """
        profileli = self.driver.find_element(by=self.profile_li[0], value=self.profile_li[1])
        profileli.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_profile_li'))

    def click_user_name_txt(self):
        """
            Click the "user name" text
        """
        self.wait.until(EC.visibility_of_element_located(self.user_name_txt))
        usernametxt = self.driver.find_element(by=self.user_name_txt[0], value=self.user_name_txt[1])
        usernametxt.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_user_name_txt'))

    def click_edit_button(self):
        """
            Click the "edit" button
        """
        editbutton = self.driver.find_element(by=self.edit_button[0], value=self.edit_button[1])
        editbutton.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_edit_button'))

    def write_user_name(self,username):
        """
            Write the username
            
            Arguments 
            -------
            username: (str)
                the username of the user
        """
        self.wait.until(EC.visibility_of_element_located(self.user_name_input))
        user_name_in = self.driver.find_element(by=self.user_name_input[0], value=self.user_name_input[1])
        user_name_in.clear()
        user_name_in.send_keys(username)
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'write_user_name'))

    def write_the_role(self,role):
        """
            Write the role
            
            Arguments 
            -------
            username: (str)
                the role of the user
        """
        role_in = self.driver.find_element(by=self.role_input[0], value=self.role_input[1])
        role_in.clear()
        role_in.send_keys(role)
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'write_the_role'))

    def write_the_bio(self,role):
        """
            Write the bio
            
            Arguments 
            -------
            username: (str)
                the bio of the user
        """
        bio_in = self.driver.find_element(by=self.bio_input[0], value=self.bio_input[1])
        bio_in.clear()
        bio_in.send_keys(role)
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'write_the_bio'))

    def click_update_button(self):
        """
            Click the "update" button
        """
        updatebutton = self.driver.find_element(by=self.update_button[0], value=self.update_button[1])
        updatebutton.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_update_button'))


    def get_the_text_from_user_name_txt(self):
        """
            get the "user name" text

            Returns 
            -------
            str
                returns the text of the user name
        """
        self.wait.until(EC.visibility_of_element_located(self.user_name_txt))
        usernametxt = self.driver.find_element(by=self.user_name_txt[0], value=self.user_name_txt[1])
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'get_the_text_from_user_name_txt'))
        return usernametxt.text

    def get_the_text_from_role_txt(self):
        """
            get the "role" text

            Returns 
            -------
            str
                returns the text of the role
        """
        role_txt = self.driver.find_element(by=self.role_txt[0], value=self.role_txt[1])
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'get_the_text_from_role_txt'))
        return role_txt.text

    def get_the_text_from_bio_txt(self):
        """
            get the "bio" text

            Returns 
            -------
            str
                returns the text of the bio
        """
        biotxt = self.driver.find_element(by=self.bio_txt[0], value=self.bio_txt[1])
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'get_the_text_from_bio_txt'))
        return biotxt.text
   