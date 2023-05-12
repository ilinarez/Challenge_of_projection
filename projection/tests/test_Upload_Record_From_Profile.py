import time
import pytest

from projection.helpers import helpers
from projection.commands.commands import command
from projection.actions.Common_Methods import CommonMethods
from projection.actions.Edit_Profile_Page import EditProfilePage
Test_name = "test_upload_record_from_profile"

@pytest.mark.parametrize('test_name', [Test_name])
def test_upload_record_from_profile(web_driver,test_screenshots_folder_path, config_users):
    helpers.remove_evidence(test_screenshots_folder_path,Test_name)
    client = config_users['User_feed']

    commands = command(web_driver,test_screenshots_folder_path)
    commonmethods = CommonMethods(web_driver,test_screenshots_folder_path)
    editprofilepage = EditProfilePage(web_driver,test_screenshots_folder_path)

    # Logs in
    commands.command_sign_in(client["email"],client["password"])
    
    # Edit profile
    commands.command_edit_profile()

    # Click the "Select file" button
    editprofilepage.click_audio_resource_button()

    # Click the upload button
    editprofilepage.click_upload_button()

    # Upload a file
    commands.command_upload_a_file('projection/data/STAY.mp3')

    # Complete the form to add the resource
    commands.command_add_resource('Blog','audio')

    # Validate if the number of Audio resource card increase
    assert editprofilepage.get_the_number_of_resource_audio_card() > 0