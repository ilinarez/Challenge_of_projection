import pytest

from projection.helpers import helpers
from projection.commands.commands import command
from projection.actions.Edit_Profile_Page import EditProfilePage

Test_name = "test_add_a_image_resource_from_profile"

@pytest.mark.parametrize('test_name', [Test_name])
def test_add_a_image_resource_from_profile(web_driver,test_screenshots_folder_path, config_users):
    helpers.remove_evidence(test_screenshots_folder_path,Test_name)
    client = config_users['User_feed']

    commands = command(web_driver,test_screenshots_folder_path)
    editprofilepage = EditProfilePage(web_driver,test_screenshots_folder_path)

    # Logs in
    commands.command_sign_in(client["email"],client["password"])
    
    # Edit profile
    commands.command_edit_profile()

    # Click the button with shape of camera
    editprofilepage.click_camera_resource_button()

    # Click the upload button
    editprofilepage.click_upload_button()

    # Upload a file
    commands.command_upload_a_file('projection/data/flat.png')
    
    # Complete the form to add the resource
    commands.command_add_resource('Blog','image')

    # Validate if the number of Image resource card increase
    assert editprofilepage.get_the_number_of_resource_image_card() > 0
