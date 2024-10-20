import os
import telebot
from dotenv import load_dotenv

load_dotenv('../.env')

bot_token      : str = os.getenv('BOT_TOKEN')
database_url   : str = os.getenv('DB_URL')
database_token : str = os.getenv('DB_TOKEN')

request_header = { "Authorization": database_token }