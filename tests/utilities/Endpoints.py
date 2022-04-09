import base64

from tests.conftest import settings

KEY = base64.b64decode(settings['key']).decode('ascii')
TOKEN = base64.b64decode(settings['token']).decode('ascii')
URI = settings['baseURI']
BOARD_ENDPOINT = URI + "boards/"
LIST_ENDPOINT = URI + "lists/"
CARD_ENDPOINT = URI + "cards/"
COMMENTS_ENDPOINT = "/actions/comments/"
AUTH = "?key=" + KEY + "&token=" + TOKEN

HOME = settings['url']
USERNAME = settings['username']
PASSWORD = settings['password']
