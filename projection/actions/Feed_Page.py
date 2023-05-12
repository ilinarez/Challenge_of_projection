"""This module contains the methods of the login pages """
import inspect
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from projection.helpers import helpers
from projection.selectors.FeedSelectors import Feed_Selectors

class FeedPages:

    def __init__(self, driver, test_screenshots_folder_path):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.test_screenshot_folder_path = test_screenshots_folder_path + inspect.stack()[1].function
        self.all_option = Feed_Selectors.alloptionLi
        self.add_to_favorites_button = Feed_Selectors.addToFavoritesButton
        self.favorite_option_li = Feed_Selectors.favoritesoptionLi
        self.content_provider_img = Feed_Selectors.contentproviderImg
        self.collections_option_li = Feed_Selectors.collectionsoptionLi

    def verify_if_all_option_is_displayed(self):
        """
            Verify if the "all" option is displayed or not
            Returns 
            -------
            bool
                returns true if the  "all" option is displayed
        """ 
        self.wait.until(EC.visibility_of_element_located(self.all_option))
        self.wait.until(EC.visibility_of_element_located(self.content_provider_img))
        alloption = self.driver.find_element(by=self.all_option[0], value=self.all_option[1])
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'verify_if_all_option_is_displayed'))
        return alloption.is_displayed()
    
    def click_add_to_favorites_button(self):
        """
            Click the "add to favortites" button
        """
        add_to_favorites_btn = self.driver.find_elements(by=self.add_to_favorites_button[0], value=self.add_to_favorites_button[1])
        add_to_favorites_btn[1].click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_add_to_favorites_button'))

    def click_favorite_option_li(self):
        """
            Click the "favorites" option
        """
        favorite_option_li = self.driver.find_element(by=self.favorite_option_li[0], value=self.favorite_option_li[1])
        favorite_option_li.click()

        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_favorite_option_li'))

    def click_collections_option_li(self):
        """
            Click the "collection" option
        """
        collectionsoption_li = self.driver.find_element(by=self.collections_option_li[0], value=self.collections_option_li[1])
        collectionsoption_li.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_collections_option_li'))
