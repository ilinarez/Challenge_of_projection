import pytest

from projection.helpers import helpers
from projection.commands.commands import command
from projection.actions.Feed_Page import FeedPages
from projection.actions.Collection_Page import CollectionPage

Test_name = "test_delete_a_collection"

@pytest.mark.parametrize('test_name', [Test_name])
def test_delete_a_collection(web_driver,test_screenshots_folder_path, config_users):
    helpers.remove_evidence(test_screenshots_folder_path,Test_name)
    client = config_users['User_feed']

    commands = command(web_driver,test_screenshots_folder_path)
    feedpage = FeedPages(web_driver,test_screenshots_folder_path)
    collectionpage = CollectionPage(web_driver,test_screenshots_folder_path)

    # Logs in
    commands.command_sign_in(client["email"],client["password"])

    # Click the "collection" option
    feedpage.click_collections_option_li()

    # Click the button with shape of trash
    collectionpage.click_delete_collection_button()

    # Validate if the number of collection card decrease
    assert collectionpage.get_the_number_collection_card() == 0