import pytest

from projection.helpers import helpers
from projection.commands.commands import command
from projection.actions.Common_Methods import CommonMethods

Test_name = "test_update_user_info"

@pytest.mark.parametrize('test_name', [Test_name])
def test_update_user_info(web_driver,test_screenshots_folder_path, config_users):
    helpers.remove_evidence(test_screenshots_folder_path,Test_name)
    client = config_users['User_feed']

    commands = command(web_driver,test_screenshots_folder_path)
    commonmethods = CommonMethods(web_driver,test_screenshots_folder_path)

    # Logs in
    commands.command_sign_in(client["email"],client["password"])
    
    # Edit profile
    commands.command_edit_profile()

    # Complete the form
    commonmethods.write_user_name(client["name"])
    commonmethods.write_the_role(client["role"])
    commonmethods.write_the_bio(client["bio"])

    # Click the "update" button
    commonmethods.click_update_button()

    # Validate if the information is updated
    assert commonmethods.get_the_text_from_user_name_txt() == client["name"]
    assert commonmethods.get_the_text_from_role_txt() == client["role"]
    assert commonmethods.get_the_text_from_bio_txt() == client["bio"]
