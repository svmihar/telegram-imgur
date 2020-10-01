from base64 import b64encode
from .auth import IMGUR
import requests
from .db import ITEMS_DB

headers = {"Authorization": f"Client-ID {IMGUR['client_id']}"}

POST_URL = "https://api.imgur.com/3/image"


def upload_image(image: bytes):
    result = requests.post(
        POST_URL,
        headers=headers,
        data={
            "image": b64encode(image),
        },
    )
    return result.json()

def insert_db(item_json):
    ITEMS_DB.put(item_json)
    return True