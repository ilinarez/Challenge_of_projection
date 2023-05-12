import time
import pytest
from datetime import datetime

from projection.helpers import helpers
from projection.commands.commands import command
from projection.actions.Feed_Page import FeedPages
from projection.actions.Collection_Page import CollectionPage
from projection.actions.Detail_Collection_Page import Detail_Collection_Page

Test_name = "test_subscribe_to_a_collection"

@pytest.mark.parametrize('test_name', [Test_name])
def test_subscribe_to_a_collection(web_driver,test_screenshots_folder_path, config_users):
    helpers.remove_evidence(test_screenshots_folder_path,Test_name)
    client = config_users['User_feed']

    commands = command(web_driver,test_screenshots_folder_path)
    feedpage = FeedPages(web_driver,test_screenshots_folder_path)
    collectionpage = CollectionPage(web_driver,test_screenshots_folder_path)

    # Logs in
    commands.command_sign_in(client["email"],client["password"])

    # Subscribe a collection
    commands.command_subscribe_a_collection()

    # Click the "subscription" option
    collectionpage.click_subscription_h1()

    # Validate if the number of collection card increase
    assert collectionpage.get_the_number_collection_card() > 0