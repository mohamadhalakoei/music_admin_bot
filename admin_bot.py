import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

load_dotenv()

TOKEN = os.getenv("TOKEN")

# Command Functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, welcome to the admin bot of the channel!")

def main():
    # create an Updater object and attach it to your bot's token
    updater = Updater(token=TOKEN, use_context=True)

    # create a dispatcher object to register handlers
    dispatcher = updater.dispatcher

    # register a handler for the all command
    dispatcher.add_handler(CommandHandler('start', start))

    # start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()