import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()

TOKEN = os.getenv("TOKEN")
PASSWORD = os.getenv("PASSWORD")
AUTHORIZED_USERS_FILE = os.getenv("AUTHORIZED_USERS_FILE")
MUSIC_PATH = os.getcwd() + '/Music/'

# Create the authorized users file if it doesn't exist
if not os.path.isfile(AUTHORIZED_USERS_FILE):
    with open(AUTHORIZED_USERS_FILE, "w") as f:
        f.write("")

# Check if the Music directory exists, if not create it
if not os.path.isdir(MUSIC_PATH):
    os.mkdir(MUSIC_PATH)

# Command Functions
def start(update, context):
    user_id = update.effective_user.id
    if check_password(user_id, context.args):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, welcome to the admin bot of the channel!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Incorrect password.")

def check_password(user_id, args):
    if args and args[0] == PASSWORD:
        # Save the user ID to the authorized_users file
        with open("authorized_users.txt", "a") as f:
            f.write(str(user_id) + "\n")
        return True
    else:
        # Check if the user ID is in the authorized_users file
        with open("authorized_users.txt", "r") as f:
            authorized_users = [int(line.strip()) for line in f]
        if user_id in authorized_users:
            return True
        else:
            return False

def download_audio(update, context):
    user_id = update.effective_user.id
    if check_password(user_id, context.args):
        audio_file = update.message.audio
        file_id = audio_file.file_id
        file_name = audio_file.file_name
        artist = file_name.split('-')[0]
        title = file_name.split('-')[1][0:-4]
        title = title.replace("(320)", "").replace("(128)", "") if "(320)" in title or "(128)" in title else title
        new_file = context.bot.get_file(file_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"downloading...")
        new_file.download(MUSIC_PATH + f'{title.strip()}.mp3')
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"downloaded...")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You don't have access.")

def list_music(update, context):
    user_id = update.effective_user.id
    if check_password(user_id, context.args):
        files = [file for file in os.listdir(MUSIC_PATH) if file.endswith('.mp3')]
        if files:
            context.bot.send_message(chat_id=update.effective_chat.id, text="List of available music files:")
            for file in files:
                context.bot.send_message(chat_id=update.effective_chat.id, text=file)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="No music files found.")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You don't have access.")
        
def main():
    # create an Updater object and attach it to your bot's token
    updater = Updater(token=TOKEN, use_context=True)

    # create a dispatcher object to register handlers
    dispatcher = updater.dispatcher

    # register a handler for the all command
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.audio, download_audio))
    dispatcher.add_handler(CommandHandler('list', list_music))

    # start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()