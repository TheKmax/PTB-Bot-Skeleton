from telegram.ext import Updater
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = os.environ.get(TOKEN, none)

updater = Updater(token='TOKEN')

updater.start_polling()
