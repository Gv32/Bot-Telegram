from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


TOKEN = "830944828:AAFO8jvFu7azCpRShxcCZYw77-OtsoIMULQ"

def start(update, context):
    update.message.reply_text("Suca")

def rispondi(update, context):
    testo = update.message.text.lower()
    if "pikenco" in testo:
        update.message.reply_text("Garibaldi")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, rispondi))
#updater.dispatcher.add_handler()
print("Bot in ascolto....")
updater.start_polling()