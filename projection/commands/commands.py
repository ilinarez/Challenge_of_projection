import time
from projection.actions.Login_Page import LogInPages
from projection.actions.Feed_Page import FeedPages
from projection.actions.Common_Methods import CommonMethods
from projection.actions.Edit_Profile_Page import EditProfilePage
from projection.actions.Collection_Page import CollectionPage
from projection.actions.Detail_Collection_Page import Detail_Collection_Page

class command:
    
    def __init__(self, driver,test_screenshots_folder_path):
        self.driver = driver
        self.loginpage = LogInPages(driver=driver,test_screenshots_folder_path=test_screenshots_folder_path)
        self.feedpage = FeedPages(driver=driver,test_screenshots_folder_path=test_screenshots_folder_path)
        self.commonmethods = CommonMethods(driver=driver,test_screenshots_folder_path=test_screenshots_folder_path)
        self.editprofilepage = EditProfilePage(driver=driver,test_screenshots_folder_path=test_screenshots_folder_path)
        self.collectionpage = CollectionPage(driver=driver,test_screenshots_folder_path=test_screenshots_folder_path)
        self.detailcollectionpage = Detail_Collection_Page(driver=driver,test_screenshots_folder_path=test_screenshots_folder_path)

    def command_sign_in(self,email,password):

        # Write the email
        self.loginpage.write_email(email)
        # Write the password
        self.loginpage.write_password(password) 
        # Click to the "Log In" button
        self.loginpage.click_log_in_button()
        # validate if the "all" option is displayed
        assert self.feedpage.verify_if_all_option_is_displayed() == True

    def command_edit_profile(self):

        # Click to the email span
        self.commonmethods.click_email_span()
        # Click the profile option
        self.commonmethods.click_profile_li()
        # Click to the user name
        self.commonmethods.click_user_name_txt()
        # Click to the edit button
        self.commonmethods.click_edit_button()

    def command_create_collections(self,name,public):
        
        # Click on the button with shape of plus
        self.collectionpage.click_create_collection_button()

        # Complete the fields
        self.collectionpage.write_the_name_collection(name)
        
        #If the collection is public, click the checkbox
        if public == 'Yes':
            self.collectionpage.click_change_status_span
        
        # Click the Done button
        self.collectionpage.click_save_button()

        # Validate the name of the collection
        assert self.detailcollectionpage.get_the_name_of_the_collection() == name

    def command_go_to_favorites_section(self):
        
        # Click to the favorites option
        self.feedpage.click_favorite_option_li()
        
        time.sleep(5)
        
        # Click to the favorites option
        self.feedpage.click_favorite_option_li()
        
        time.sleep(5)

    def command_subscribe_a_collection(self):
        
        # Click the "collection" option
        self.feedpage.click_collections_option_li()

        # Click the "collection marketplace" option
        self.collectionpage.click_collection_marketplace_H1()

        # Click the buttton with shape of +
        self.collectionpage.click_subscribe_button()
    
        # Validate if the notification is displayed
        assert self.collectionpage.verify_if_notification_collection_div_is_displayed() == True

    def command_unsubscribe_a_collection(self):
        
         # Click the "collection" option
        self.feedpage.click_collections_option_li()

        # Click the "subscription" option
        self.collectionpage.click_subscription_h1()

        # Click the buttton with shape of -
        self.collectionpage.click_subscribe_button()

        # Validate if the notification is displayed
        assert self.collectionpage.verify_if_notification_collection_div_is_displayed() == True


    def command_upload_a_file(self,path):
        
        # Select the file
        self.editprofilepage.select_the_file_to_upload(path)

        # time.sleep(5)

        # Click the "select file" button next to the file selected
        self.editprofilepage.click_cloud_button()

    def command_add_resource(self,source,medium):
        
        # Click to the resource detail text
        self.editprofilepage.click_resource_details_txt()
        # Click to the continue button
        self.editprofilepage.click_first_continue_button()
        # Click to the "2" button 
        self.editprofilepage.click_second_number_button()
        # Click to the "3" button 
        self.editprofilepage.click_third_number_button()
        # Click to the "4" button 
        self.editprofilepage.click_fourth_number_button()
        # Click to the "5" button 
        self.editprofilepage.click_fifth_number_button()
        # Write the source modal
        self.editprofilepage.write_source_modal(source)
        # Click to the "6" button 
        self.editprofilepage.click_sixth_number_button()

        if medium == "Link":
            # Select the medium modal
            self.editprofilepage.select_the_medium_modal(medium)

        # Click to the "7" button
        self.editprofilepage.click_seventh_number_button()
        # Click to the "8" button
        self.editprofilepage.click_eighth_number_button()
        # Click to the "9" button
        self.editprofilepage.click_nineth_number_button()
        # Click to the finish button
        self.editprofilepage.click_finish_button()
