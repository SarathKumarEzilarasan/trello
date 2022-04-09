import requests
from pytest_bdd import scenarios, given, when, then, parsers

# Constants
from tests.page_objects.workSpacePage import WorkSpacePage
from tests.conftest import settings
from tests.page_objects.home import HomePage
from tests.utilities.Logger import Logger
from tests.utilities.Endpoints import BOARD_ENDPOINT, AUTH, LIST_ENDPOINT, CARD_ENDPOINT, COMMENTS_ENDPOINT, HOME, USERNAME, \
    PASSWORD

scenarios('../features/board.feature')

logger = Logger()


# Given Steps

@given('Create a Board')
def create_board(browser, context):
    board_name = "board"
    response = requests.post(BOARD_ENDPOINT + AUTH + "&name=" + board_name)
    assert response.status_code == 200
    resp_body = response.json()
    context['board_id'] = resp_body['id']
    list_name = "list"
    response = requests.post(LIST_ENDPOINT + AUTH + "&idBoard=" + resp_body['id'] + "&name=" + list_name)
    assert response.status_code == 200
    resp_body = response.json()
    context['list_id'] = resp_body['id']


# When Steps

@when(parsers.parse('Create a card'))
def create_card(context):
    board_id = context['board_id']
    list_id = context['list_id']
    description = "test"
    response = requests.post(CARD_ENDPOINT + AUTH +
                             "&idList=" + list_id +
                             "&idBoard=" + board_id +
                             "&desc=" + description)
    assert response.status_code == 200
    resp_body = response.json()
    context['card_id'] = resp_body['id']


# Then Steps

@then(parsers.parse('Edit card'))
def edit_card(context):
    card_id = context['card_id']
    expected_description = "testing"
    response = requests.put(CARD_ENDPOINT + card_id + AUTH + "&desc=" + expected_description)
    assert response.status_code == 200
    resp_body = response.json()
    description = resp_body['desc']
    assert expected_description == description


@then(parsers.parse('Delete a card'))
def delete_card(context):
    card_id = context['card_id']
    response = requests.delete(CARD_ENDPOINT + card_id + AUTH)
    assert response.status_code == 200
    resp_body = response.json()


@then(parsers.parse('Add a comment to the card API'))
def add_comment_card(context):
    card_id = context['card_id']
    comment = 'comment'
    response = requests.post(CARD_ENDPOINT + card_id + COMMENTS_ENDPOINT + AUTH + "&text=" + comment)
    assert response.status_code == 200
    resp_body = response.json()


@given(parsers.parse('User logs in'))
def user_login(browser, context):
    browser.get(HOME)
    homePage = HomePage(browser)
    homePage.login(USERNAME, PASSWORD)


@when(parsers.parse('Verify card with comment'))
def assert_card_ui(browser, context):
    workSpacePage = WorkSpacePage(browser)
    workSpacePage.add_comment()


@then(parsers.parse('Add a comment in UI'))
def add_comment_ui(browser, context):
    """"""


@then(parsers.parse('Set card as done'))
def card_done_ui(browser, context):
    workSpacePage = WorkSpacePage(browser)
    workSpacePage.mark_card_done()
