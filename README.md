# Telegram Music Bot
This Telegram bot receives a music file from you, changes its metadata, adds a caption based on the music file information, and sends it to the desired channel when you want it to be sent.

## Installation

1. Clone the repository or download the ZIP file.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Please rename the `.env_file` to `.env` and add the following variables in the file:
   - `TOKEN`: your Telegram bot token
   - `PASSWORD`: a password that authorized users will use to access the bot
   - `AUTHORIZED_USERS_FILE`: the name of the file where authorized user IDs will be stored
   - `CHANNEL_ID`: the ID of the Telegram channel where the music files will be sent
   - `CHANNEL`: the name of the Telegram channel where the music files will be sent
Make sure to add each variable in its designated place.
4. Run the script by running `python admin_bot.py`.

## Usage

The bot has the following commands:

- `/start password`: starts the bot and checks the password to authorize the user
- `/list password` or `/list`: lists the available music files
- `/send password [file_name]` or `/send [file_name]` or `/send`: Sends the specified music file to the Telegram channel with a caption or sends the first music file in the directory if no file name is specified.
- `/delete password [file_name]` or `/delete [file_name]`: deletes the specified music file
- Sending an audio file to the bot will download it to the `Music` directory and change the metadata of the file.
