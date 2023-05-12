import time
import pytest

from projection.helpers import helpers
from projection.commands.commands import command
from projection.actions.Feed_Page import FeedPages
from projection.actions.Favorite_Page import FavoritePage

Test_name = "test_add_content_to_favorites_section"

@pytest.mark.parametrize('test_name', [Test_name])
def test_add_content_to_favorites_section(web_driver,test_screenshots_folder_path, config_users):
    helpers.remove_evidence(test_screenshots_folder_path,Test_name)
    client = config_users['User_feed']

    commands = command(web_driver,test_screenshots_folder_path)
    feedpage = FeedPages(web_driver,test_screenshots_folder_path)
    favoritepage = FavoritePage(web_driver,test_screenshots_folder_path)

    # Logs in
    commands.command_sign_in(client["email"],client["password"])

    # Click to the button with shape of star   
    feedpage.click_add_to_favorites_button()
 
    # Go to favorites section
    commands.command_go_to_favorites_section()

    # Click to the content
    favoritepage.click_first_content_div()