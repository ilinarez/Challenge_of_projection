import time
import pytest
from datetime import datetime

from projection.helpers import helpers
from projection.commands.commands import command
from projection.actions.Feed_Page import FeedPages

Test_name = "test_create_public_collection"

@pytest.mark.parametrize('test_name', [Test_name])
def test_create_public_collection(web_driver,test_screenshots_folder_path, config_users):
    helpers.remove_evidence(test_screenshots_folder_path,Test_name)
    client = config_users['User_feed']

    commands = command(web_driver,test_screenshots_folder_path)
    feedpage = FeedPages(web_driver,test_screenshots_folder_path)

    # Logs in
    commands.command_sign_in(client["email"],client["password"])

    # Click the "collection" option
    feedpage.click_collections_option_li()

    # get the current time 
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    
    # Create a collection
    commands.command_create_collections(client["name_public_collection"]+current_time,"Yes")
   