from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from bot import dispatcher

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start, run_async=True)
dispatcher.add_handler(start_handler)
