from telegram_imgur_bot.db import ITEMS_DB
import json

if __name__ == "__main__":
    result = [item for item in ITEMS_DB.fetch()]
    with open('current_standing_Test.json', 'w') as f:
        json.dump(result, f )

