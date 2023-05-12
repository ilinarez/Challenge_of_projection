import pytest

from projection.helpers import helpers
from projection.commands.commands import command
from projection.actions.Favorite_Page import FavoritePage

Test_name = "test_remove_content_from_favorites_section"

@pytest.mark.parametrize('test_name', [Test_name])
def test_remove_content_from_favorites_section(web_driver,test_screenshots_folder_path, config_users):
    helpers.remove_evidence(test_screenshots_folder_path,Test_name)
    client = config_users['User_feed']

    commands = command(web_driver,test_screenshots_folder_path)
    favoritepage = FavoritePage(web_driver,test_screenshots_folder_path)

    # Logs in
    commands.command_sign_in(client["email"],client["password"])

    # Go to favorites section
    commands.command_go_to_favorites_section()
    
    num_content = favoritepage.get_the_number_star_button()
    
    # Click the button with shape of star 
    favoritepage.click_star_button()
    
    # Verify if the star button is displayed
    assert favoritepage.get_the_number_star_button() < num_content