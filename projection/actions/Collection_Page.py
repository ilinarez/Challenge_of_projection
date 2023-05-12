"""This module contains the methods of the login pages """
import inspect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from projection.helpers import helpers
from projection.selectors.CollectionsSelectors import Collection_Selectors

class CollectionPage:

    def __init__(self, driver, test_screenshots_folder_path):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.test_screenshot_folder_path = test_screenshots_folder_path + inspect.stack()[1].function
        self.my_collection_h1 = Collection_Selectors.mycollectionH1
        self.name_collection_text = Collection_Selectors.namecollectiontxt
        self.subscription_h1 = Collection_Selectors.subscriptionH1
        self.collection_marketplace_H1 = Collection_Selectors.collectionmarketplaceH1
        self.create_collection_button = Collection_Selectors.createcollectionButton
        self.create_collection_div = Collection_Selectors.createcollectionDiv
        self.name_collection_input = Collection_Selectors.namecollectionInput
        self.change_status_span = Collection_Selectors.changestatusSpan
        self.save_button = Collection_Selectors.saveButton
        self.delete_collection_button = Collection_Selectors.deletecollectionButton
        self.subscribe_button = Collection_Selectors.subscribeButton
        self.notification_collection_div = Collection_Selectors.notificationcollectionDiv

    def click_subscription_h1(self):
        """
            Click the "subscription" h1
        """
        self.wait.until(EC.visibility_of_element_located(self.subscription_h1))
        subscription_h1 = self.driver.find_element(by=self.subscription_h1[0], value=self.subscription_h1[1])
        subscription_h1.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'click_subscription_h1'))

    def click_collection_marketplace_H1(self):
        """
            Click the "collection marketplace" h1
        """
        self.wait.until(EC.visibility_of_element_located(self.collection_marketplace_H1))
        collection_marketplace_h1 = self.driver.find_element(by=self.collection_marketplace_H1[0], value=self.collection_marketplace_H1[1])
        collection_marketplace_h1.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'click_collection_marketplace_H1'))

    def click_create_collection_button(self):
        """
            Click the "+" button
        """
        self.wait.until(EC.visibility_of_element_located(self.my_collection_h1))
        create_collection_btn = self.driver.find_element(by=self.create_collection_button[0], value=self.create_collection_button[1])
        create_collection_btn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'click_create_collection_button'))

    def write_the_name_collection(self,name):
        """
            Click the "+" button
        """
        self.wait.until(EC.visibility_of_element_located(self.create_collection_div))
        name_collection_in = self.driver.find_element(by=self.name_collection_input[0], value=self.name_collection_input[1])
        name_collection_in.send_keys(name)
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'click_write_the_name_collection'))

    def click_save_button(self):
        """
            Click the "save" button
        """
        save_btn = self.driver.find_element(by=self.save_button[0], value=self.save_button[1])
        save_btn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'click_save_button'))
    
    def click_change_status_span(self):
        """
            Click the "change status" span
        """
        change_status = self.driver.find_element(by=self.save_button[0], value=self.change_status_span[1])
        change_status.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'click_change_status_span'))

    def get_the_number_collection_card(self):
        """
            Get the number of collection created
        """
        try:
            namecollection_text = self.driver.find_elements(by=self.name_collection_text[0], value=self.name_collection_text[1])
            self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'get_the_number_collection_card'))
            return len(namecollection_text)
        except:
            return 0

    def click_delete_collection_button(self):
        """
            Click the button with shape of trash
        """
        self.wait.until(EC.visibility_of_element_located(self.delete_collection_button))
        delete_collection_btn = self.driver.find_element(by=self.delete_collection_button[0], value=self.delete_collection_button[1])
        delete_collection_btn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'click_delete_collection_button'))

    def click_subscribe_button(self):
        """
            Click the "+/-" button
        """
        self.wait.until(EC.visibility_of_element_located(self.subscribe_button))
        subscribe_btn = self.driver.find_element(by=self.subscribe_button[0], value=self.subscribe_button[1])
        subscribe_btn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'click_subscribe_button'))

    def verify_if_notification_collection_div_is_displayed(self):
        """
            Verify if the notification of the collection is displayed or not
            Returns 
            -------
            bool
                returns true if the the notification of the collection is displayed
        """ 
        self.wait.until(EC.visibility_of_element_located(self.notification_collection_div))
        notification_collectiondiv = self.driver.find_element(by=self.notification_collection_div[0], value=self.notification_collection_div[1])
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'verify_if_notification_collection_div_is_displayed'))
        return notification_collectiondiv.is_displayed()
