from deta import Deta
from .auth import DETA

DB = Deta(DETA["project_key"])
ITEMS_DB = DB.Base("toys")
