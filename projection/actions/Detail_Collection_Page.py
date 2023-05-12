import inspect
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from projection.helpers import helpers
from projection.selectors.DetailOfCollectionSelectors import Detail_Collection_Selectors

class Detail_Collection_Page:

    def __init__(self, driver, test_screenshots_folder_path):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.test_screenshot_folder_path = test_screenshots_folder_path + inspect.stack()[1].function
        self.collection_name_h1 = Detail_Collection_Selectors.collectionnameH1

    def get_the_name_of_the_collection(self):
        """
            Get the name of collection created
        """
        self.wait.until(EC.visibility_of_element_located(self.collection_name_h1))
        namecollection_text = self.driver.find_element(by=self.collection_name_h1[0], value=self.collection_name_h1[1])
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'get_the_name_of_the_collection'))
        return namecollection_text.text