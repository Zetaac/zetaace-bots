from telegram.ext import updater, commandhandler


def start(update, context):

    update.messager.replay_text('hola mundo')

0
if __name__ == '__main__':

    updater = updater(token='1777471394:AAFcUVag03ueTiOpZ831MKT8djCm_8eQ3ZM', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(commandhandler('start, start'))  

    updater.start_polling()
    updater.idle()