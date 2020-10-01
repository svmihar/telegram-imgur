from telegram_imgur_bot import __version__
from telegram_imgur_bot.upload import upload_image


def test_version():
    assert __version__ == "0.1.0"


def test_upload():
    image_test = open("./test.jpg", "rb").read()
    result = upload_image(image_test)
    assert result["success"]
