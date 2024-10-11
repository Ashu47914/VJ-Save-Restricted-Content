import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27117413"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7913062926:AAGVmf80lNI1_ujw9e-RL0EGlzdrT-R4ReU")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ashudeharu18:cb2deeP3WcidzQMl@cluster0.bn8hc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
