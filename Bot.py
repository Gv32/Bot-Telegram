from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = "830944828:AAFO8jvFu7azCpRShxcCZYw77-OtsoIMULQ"

def start(update, context):
    update.message.reply_text("Garibaldi?")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
#updater.dispatcher.add_handler()
print("Bot in ascolto....")
updater.start_polling()