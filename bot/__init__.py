from telegram.ext import Updater
import logging, os, time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

TOKEN = os.environ.get("TOKEN", None)

updater = Updater(token='TOKEN')

updater.start_polling()
