"""This module contains the methods of the login pages """
import inspect, time, pathlib
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from projection.helpers import helpers
from projection.selectors.EditProfileSelectors import Edit_Profile_Selectors
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class EditProfilePage:

    def __init__(self, driver, test_screenshots_folder_path):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)
        self.test_screenshot_folder_path = test_screenshots_folder_path + inspect.stack()[1].function
        self.upload_resource_button = Edit_Profile_Selectors.uploadResourceButton
        self.resource_details_txt = Edit_Profile_Selectors.resourceDetailsTxt
        self.resource_details_modal = Edit_Profile_Selectors.resourceDetailsModal
        self.camera_resource_button =  Edit_Profile_Selectors.cameraResourceButton
        self.take_photo_button = Edit_Profile_Selectors.takePhotoButton
        self.audio_resource_button = Edit_Profile_Selectors.audioResourceButton
        self.select_file_button = Edit_Profile_Selectors.selectFileButton
        self.select_file_input = Edit_Profile_Selectors.selectFileInput
        self.cloud_button = Edit_Profile_Selectors.cloudButton
        self.first_continue_button = Edit_Profile_Selectors.firstContinueButton
        self.second_number_button = Edit_Profile_Selectors.secondNumberButton
        self.third_number_button = Edit_Profile_Selectors.thirdNumberButton
        self.fourth_number_button = Edit_Profile_Selectors.fourthNumberButton
        self.fifth_number_button = Edit_Profile_Selectors.fifthNumberButton
        self.sixth_number_button = Edit_Profile_Selectors.sixthNumberButton
        self.seventh_number_button = Edit_Profile_Selectors.seventhNumberButton
        self.eighth_number_button = Edit_Profile_Selectors.eighthNumberButton
        self.nineth_number_button = Edit_Profile_Selectors.ninethNumberButton
        self.source_type_modal_cmb = Edit_Profile_Selectors.sourceTypeModalCmb
        self.source_type_modal_input = Edit_Profile_Selectors.sourceTypeModalInput
        self.medium_modal_cmb = Edit_Profile_Selectors.mediumModalCmb
        self.finish_button = Edit_Profile_Selectors.finishButton
        self.upload_button = Edit_Profile_Selectors.uploadButton 
        self.resourceimagecard = Edit_Profile_Selectors.resourceImageCard
        self.resource_pdf_card = Edit_Profile_Selectors.resourcePdfCard
        self.resource_audio_card = Edit_Profile_Selectors.resourceAudioCard


    def click_upload_resource_button(self):
        """
            Click the "upload resource" button
        """
        upload_resource_btn = self.driver.find_element(by=self.upload_resource_button[0], value=self.upload_resource_button[1])
        upload_resource_btn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_upload_resource_button'))

    def click_resource_details_modal(self):
        """
            click the modal of the resource details is displayed or not
        """ 
        self.wait.until(EC.visibility_of_element_located(self.resource_details_modal))
        resource_details_mod = self.driver.find_element(by=self.resource_details_modal[0], value=self.resource_details_modal[1])
        resource_details_mod.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'click_resource_details_modal'))
    
    def click_resource_details_txt(self):
        """
            click to the "resource details" text
        """ 
        self.wait.until(EC.visibility_of_element_located(self.resource_details_txt))
        resource_details_text = self.driver.find_element(by=self.resource_details_txt[0], value=self.resource_details_txt[1])
        resource_details_text.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path, 'verify_if_resource_details_txt_is_displayed'))
    
    def click_camera_resource_button(self):
        """
            Click the "camera resource" button
        """
        camera_resource_btn = self.driver.find_element(by=self.camera_resource_button[0], value=self.camera_resource_button[1])
        camera_resource_btn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_camera_resource_button'))

    def click_audio_resource_button(self):
        """
            Click the "audio resource" button
        """
        audio_resource_btn = self.driver.find_element(by=self.audio_resource_button[0], value=self.audio_resource_button[1])
        audio_resource_btn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_audio_resource_button'))

    def click_select_file_button(self):
        """
            Click the "select file" button
        """
        select_file_btn = self.driver.find_element(by=self.select_file_button[0], value=self.select_file_button[1])
        select_file_btn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_select_file_button'))

    def select_the_file_to_upload(self,path):
        """
           Select the file to upload
        """
        base = pathlib.Path().absolute()
        fileInput = self.driver.find_element(by=self.select_file_input[0], value=self.select_file_input[1])
        print('{base}/{path}'.format(base=base,path=path))
        fileInput.send_keys('{base}/{path}'.format(base=base,path=path))

    def click_cloud_button(self):
        """
           Click the "cloud" button
        """
        self.wait.until(EC.visibility_of_element_located(self.cloud_button))
        cloudbutton = self.driver.find_element(by=self.cloud_button[0], value=self.cloud_button[1])
        cloudbutton.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_cloud_button'))


    def click_first_continue_button(self):
        """
           Click the "continue" button
        """
        self.wait.until(EC.visibility_of_element_located(self.first_continue_button))
        firstcontinuebtn = self.driver.find_element(by=self.first_continue_button[0], value=self.first_continue_button[1])
        firstcontinuebtn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_first_continue_button'))

    def click_second_number_button(self):
        """
           Click the "2" button
        """
        self.wait.until(EC.visibility_of_element_located(self.second_number_button))
        secondnumberbtn = self.driver.find_element(by=self.second_number_button[0], value=self.second_number_button[1])
        secondnumberbtn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_second_number_Button'))

    def click_third_number_button(self):
        """
           Click the "3" button
        """
        self.wait.until(EC.visibility_of_element_located(self.third_number_button))
        thirdnumberbtn = self.driver.find_element(by=self.third_number_button[0], value=self.third_number_button[1])
        thirdnumberbtn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_third_number_Button'))

    def click_fourth_number_button(self):
        """
           Click the "4" button
        """
        self.wait.until(EC.visibility_of_element_located(self.fourth_number_button))
        fourthnumberbtn = self.driver.find_element(by=self.fourth_number_button[0], value=self.fourth_number_button[1])
        fourthnumberbtn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_fourth_number_button'))

    def click_fifth_number_button(self):
        """
           Click the "5" button
        """
        self.wait.until(EC.visibility_of_element_located(self.fifth_number_button))
        fifthnumberbtn = self.driver.find_element(by=self.fifth_number_button[0], value=self.fifth_number_button[1])
        fifthnumberbtn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_fifth_number_button'))

    def click_sixth_number_button(self):
        """
           Click the "6" button
        """
        self.wait.until(EC.visibility_of_element_located(self.sixth_number_button))
        sixthnumberbtn = self.driver.find_element(by=self.sixth_number_button[0], value=self.sixth_number_button[1])
        sixthnumberbtn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_sixth_number_button'))

    def click_seventh_number_button(self):
        """
           Click the "7" button
        """
        self.wait.until(EC.visibility_of_element_located(self.seventh_number_button))
        seventhnumberbtn = self.driver.find_element(by=self.seventh_number_button[0], value=self.seventh_number_button[1])
        seventhnumberbtn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_seventh_number_button'))

    def click_eighth_number_button(self):
        """
           Click the "8" button
        """
        self.wait.until(EC.visibility_of_element_located(self.eighth_number_button))
        eighthnumberbtn = self.driver.find_element(by=self.eighth_number_button[0], value=self.eighth_number_button[1])
        eighthnumberbtn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_eighth_number_button'))

    def click_nineth_number_button(self):
        """
           Click the "9" button
        """
        self.wait.until(EC.visibility_of_element_located(self.nineth_number_button))
        ninethnumberbtn = self.driver.find_element(by=self.nineth_number_button[0], value=self.nineth_number_button[1])
        ninethnumberbtn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_nineth_number_button'))

    def write_source_modal(self,source):
        """
            Write the source modal
            
            Arguments 
            -------
            source: (str)
                the source of the content
        """
        self.wait.until(EC.visibility_of_element_located(self.source_type_modal_cmb))
        source_modal_cmb = self.driver.find_element(by=self.source_type_modal_cmb[0], value=self.source_type_modal_cmb[1])
        source_modal_in = self.driver.find_element(by=self.source_type_modal_input[0], value=self.source_type_modal_input[1])

        source_modal_cmb.click()
        time.sleep(8)
        source_modal_in.send_keys(source)
        source_modal_in.send_keys(Keys.ENTER)

        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'write_source_modal'))

    def select_the_medium_modal(self,medium):
        """
           Select the medium 
        """
        self.wait.until(EC.visibility_of_element_located(self.medium_modal_cmb))
        medium_modal_cmb = self.driver.find_element(by=self.medium_modal_cmb[0], value=self.medium_modal_cmb[1])
        select = Select(medium_modal_cmb)
        select.select_by_visible_text(medium)
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'select_the_medium_modal'))

    def click_finish_button(self):
        """
           Click the "finish" button
        """
        self.wait.until(EC.visibility_of_element_located(self.finish_button))
        finish_btn = self.driver.find_element(by=self.finish_button[0], value=self.finish_button[1])
        finish_btn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_finish_button'))

    def click_upload_button(self):
        """
           Click the "upload" button
        """
        self.wait.until(EC.visibility_of_element_located(self.upload_button))
        upload_btn = self.driver.find_element(by=self.upload_button[0], value=self.upload_button[1])
        upload_btn.click()
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'click_upload_button'))

    def get_the_number_of_resource_image_card(self):
        """
            Get the number of image card
        """
        self.wait.until(EC.visibility_of_element_located(self.resourceimagecard))
        resourceimagecards = self.driver.find_elements(by=self.resourceimagecard[0], value=self.resourceimagecard[1])
        self.driver.execute_script("arguments[0].scrollIntoView();",resourceimagecards[-1])
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'get_the_number_of_resource_image_card'))
        return len(resourceimagecards)

    def get_the_number_of_resource_pdf_card(self):
        """
            Get the number of image card
        """
        self.wait.until(EC.visibility_of_element_located(self.resource_pdf_card))
        resourcepdf_card = self.driver.find_elements(by=self.resource_pdf_card[0], value=self.resource_pdf_card[1])
        self.driver.execute_script("arguments[0].scrollIntoView();",resourcepdf_card[-1])
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'get_the_number_of_resource_pdf_card'))
        return len(resourcepdf_card)
    
    def get_the_number_of_resource_audio_card(self):
        """
            Get the number of audio card
        """
        self.wait.until(EC.visibility_of_element_located(self.resource_audio_card))
        resourceaudio_card = self.driver.find_elements(by=self.resource_audio_card[0], value=self.resource_audio_card[1])
        self.driver.execute_script("arguments[0].scrollIntoView();",resourceaudio_card[-1])
        self.driver.save_screenshot(helpers.screenshot_path(self.test_screenshot_folder_path,'get_the_number_of_resource_audio_card'))
        return len(resourceaudio_card)