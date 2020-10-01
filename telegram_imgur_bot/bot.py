import telebot
from telebot.apihelper import send_data
from .item import Item
from telegram_imgur_bot import auth
from .upload import insert_db, upload_image

b = telebot.TeleBot(auth.API_TOKEN)
item_dict = {}


@b.message_handler(commands=["start"])
def welcome(message):
    b.reply_to(message, 'Let"s start the image uploading shall we?')
    t = b.reply_to(message, """Title?""")
    b.register_next_step_handler(t, process_title)


def process_title(message):
    chat_id = message.chat.id
    title = message.text
    item = Item(title)
    item_dict[chat_id] = item
    photo = b.reply_to(message, "Upload photo")
    b.register_next_step_handler(photo, process_images1)


def process_images1(message):
    chat_id = message.chat.id
    photo_id = message.photo[-1].file_id
    photo = b.get_file(photo_id)  # verifier for image uploaded, dari file type nya aja
    photo_file = b.download_file(photo.file_path)  # binary file
    link = upload_image(photo_file)["data"]["link"]
    item_dict[chat_id].images.append(link)
    b.send_message(chat_id, f'you"re image is uploaded to {link} ')
    photo2 = b.reply_to(message, "upload second photo")
    b.register_next_step_handler(photo2, process_images2)

def process_images2(message):
    chat_id = message.chat.id
    photo_id = message.photo[-1].file_id
    photo = b.get_file(photo_id)  # verifier for image uploaded, dari file type nya aja
    photo_file = b.download_file(photo.file_path)  # binary file
    link = upload_image(photo_file)["data"]["link"]
    item_dict[chat_id].images.append(link)
    b.send_message(chat_id, f'you"re image is uploaded to {link} ')
    confirm = b.reply_to(message, 'confirm?')
    b.register_next_step_handler(confirm, send_database)

def send_database(message):
    if message.text =='yes':
        item_upload = item_dict[message.chat.id].to_json()
        insert_db(item_upload)
        b.send_message(message.chat.id, 'you have successfully update the toys database ')



print("bot started")
b.polling()
