import json
from collections import namedtuple

# TODO: make a json reader -> namedtuple / dataclass

_file = json.loads(open("./secret.json").read())[0]
API_TOKEN = _file["API"]
IMGUR = _file["imgur"]
DETA = _file["DETA"]
