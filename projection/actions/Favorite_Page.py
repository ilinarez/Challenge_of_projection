import inspect
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from projection.helpers import helpers
from projection.selectors.FavoriteSelectors import Favorite_Selectors

class FavoritePage:


    def __init__(self, driver, test_screenshots_folder_path):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.test_screenshot_folder_path = test_screenshots_folder_path + inspect.stack()[1].function
        self.favorites_h1 = Favorite_Selectors.favoritesH1
        self.first_content_div = Favorite_Selectors.firstcontentdiv
        self.star_button = Favorite_Selectors.starButton

    def click_first_content_div(self):
        """
            Click the "content" div
        """
        self.wait.until(EC.visibility_of_element_located(self.first_content_div))
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'before_click_the_content'))
        firstcontent_div = self.driver.find_element(by=self.first_content_div[0], value=self.first_content_div[1])
        firstcontent_div.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'click_first_content_div'))

    def click_star_button(self):
        """
            Click the "star" button
        """
        self.wait.until(EC.visibility_of_element_located(self.star_button))
        starbutton = self.driver.find_elements(by=self.star_button[0], value=self.star_button[1])
        favorites_h1 = self.driver.find_element(by=self.favorites_h1[0], value=self.favorites_h1[1])
        favorites_h1.click()
        starbutton[1].click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'click_star_button'))

    def get_the_number_star_button(self):
        """
            Verify if the star button is displayed or not
            Returns 
            -------
            bool
                returns true if the star button is displayed
        """ 
        self.wait.until(EC.visibility_of_element_located(self.star_button))
        star_button = self.driver.find_elements(by=self.star_button[0], value=self.star_button[1])
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'get_the_number_star_button'))
        return len(star_button)
