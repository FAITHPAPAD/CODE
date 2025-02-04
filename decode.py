from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import base64
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Admin ID (replace with your actual admin user ID)
ADMIN_ID = 6830887977  # Example admin ID, replace it with your own ID

# Function to decode base64 (if file is base64 encoded)
def decode_base64(encoded_data: str):
    try:
        decoded_data = base64.b64decode(encoded_data)
        return decoded_data.decode('utf-8', errors='ignore')
    except Exception as e:
        return f"Error decoding base64: {e}"

# Decode command (only accessible by admin)
def decode(update: Update, context: CallbackContext):
    # Check if the user is admin
    if update.message.from_user.id == ADMIN_ID:
        if len(context.args) YOUR_BOT_TOKEN== 1:
            bot_username = context.args[0]

            # Example of base64 encoded Python code (this should be replaced with actual logic)
            encoded_code = "cHJpbnQoIkhlbGxvLCBXb3JsZCIpCg=="  # This is "print('Hello, World')"

            # Decode it
            decoded_code = decode_base64(encoded_code)

            # Send the decoded content back to the user
            update.message.reply_text(f"Decoded Content from bot @{bot_username}:\n\n{decoded_code}")
        else:
            update.message.reply_text("Usage: /decode <bot_username>")
    else:
        update.message.reply_text("You do not have permission to use this command.")

# Start command to welcome the user
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Only the admin can use /decode <bot_username>.")

def main():
    # Replace '7533748861:AAF_m0GOXfuchvHNO002gahj4f_TWQjhxbM' with your bot's token
    updater = Updater("YOUR_BOT_TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handler for /start
    dp.add_handler(CommandHandler("start", start))

    # Add command handler for /decode (restricted to admin)
    dp.add_handler(CommandHandler("decode", decode))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()