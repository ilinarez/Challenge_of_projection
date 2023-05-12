import pathlib
import pytest
import allure

@pytest.fixture(scope='function')
def test_screenshots_folder_path():
    """
        Get the path of the folder of the screenshots

        Returns 
        -------
        str
            path_to_folder : returns the path of the folder of the screenshots
    """
    base = pathlib.Path().absolute()
    path_to_folder = '{base}/projection/screenshots/'
    return path_to_folder.format(base=base)

@pytest.fixture(scope='function')
def web_driver(web_driver, url, test_screenshots_folder_path, test_name):
    """
        Open the caden app and after the test save the screenshots and close the driver

        Arguments
        -------
            app_driver: driver of appium
            test_screenshots_folder_path: the path of the folder of screenshots
            test_name: the name of the test case executed

        Returns 
        -------
        str
            app_driver : returns the driver of appium
    """
    web_driver.get(url)

    yield web_driver

    screenshot_name = 'image.png'
    path = '{directory}/{test_name}/{screenshot_name}'.format(directory=test_screenshots_folder_path,
                                                              test_name=test_name,
                                                              screenshot_name=screenshot_name)
    web_driver.save_screenshot(path)
    allure.attach.file(path,attachment_type=allure.attachment_type.PNG)

    web_driver.quit()