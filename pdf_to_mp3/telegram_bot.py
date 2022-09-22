import telebot
import main
from private_data import token


def tele_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, f'Hello  {bot.user.username}.\nThis bot is converting pdf file containing '
                                          f'english text to mp3.\nJust send pdf file to this chat and You\'ll get mp3 file.')

    @bot.message_handler(content_types=["document"])
    def get_doc_and_convert(message):
        file_id = message.document.file_id
        file_name = message.document.file_name
        pdf_document = bot.get_file(file_id)
        downloaded_file = bot.download_file(pdf_document.file_path)
        with open(f'{file_name}', 'wb') as file:
            file.write(downloaded_file)
        bot.send_message(message.chat.id, "File converting is started,please wait\n")
        get_name_without_extension = file_name.split('.')[0]

        result = main.pdf_to_mp3(file_path=f'{get_name_without_extension}.pdf', language="en")
        bot.send_message(message.chat.id, result)
        bot.send_audio(chat_id=message.chat.id, audio=open(f'{get_name_without_extension}.mp3', 'rb'))

    bot.polling()


tele_bot(token)
