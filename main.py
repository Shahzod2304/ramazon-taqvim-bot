from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler,ConversationHandler,MessageHandler,Filters)

BTN_TODAY, BTN_TOMORROW, BTN_MONTH, BTN_REGION, BTN_DUA = ('⌛️ Bugun','⌛️ Ertaga',"📝 To'liq taqvim",'📍 Mintaqa','🤲🏻 Duo')

main_buttons = ReplyKeyboardMarkup([
    [BTN_TODAY],[BTN_TOMORROW, BTN_MONTH],[BTN_REGION],[BTN_DUA]    
], resize_keyboard = True)

STATE_REGION = 1 
STATE_CALENDAR = 2 

def start(update,context):
    user = update.message.from_user

    buttons = [
        [
            InlineKeyboardButton("Toshkent", callback_data = 'region_1'),
            InlineKeyboardButton("Andijon", callback_data = 'region_2'),
        ],
        [
            InlineKeyboardButton("Toshkent", callback_data = 'region_3'),
            InlineKeyboardButton("Andijon", callback_data = 'region_4'),
        ],
        [
            InlineKeyboardButton("Toshkent", callback_data = 'region_5'),
            InlineKeyboardButton("Andijon", callback_data = 'region_6'),
        ],
        [
            InlineKeyboardButton("Toshkent", callback_data = 'region_7'),
            InlineKeyboardButton("Andijon", callback_data = 'region_8'),
        ],
        [
            InlineKeyboardButton("Toshkent", callback_data = 'region_9'),
            InlineKeyboardButton("Andijon", callback_data = 'region_10'),
        ],
        [
            InlineKeyboardButton("Toshkent", callback_data = 'region_11'),
            InlineKeyboardButton("Andijon", callback_data = 'region_12'),
        ],
    ]


    update.message.reply_html("Assalom alaykum <b>{}</b>\n \n<b>Ramazon oyi muborak bo'lsin</b> \nSizga qaysi mintaqa bo'yicha ma'lumot kerak ?".
        format(user.first_name), reply_markup=InlineKeyboardMarkup(buttons))
    return STATE_REGION
def inline_callback(update, context):
    try:
        query = update.callback_query
        query.message.delete()
        query.message.reply_html(text='<b>Ramazon taqvimi </b> 2️⃣0️⃣2️⃣2️⃣\n \nQuyidagilardan birini tanlang 👇🏻', reply_markup = main_buttons)
        return STATE_CALENDAR
    except Exception as e:
        print('Error ',str(e))

def calendar_today(update, context):
    update.message.reply_text('Bugun belgilandi')

def calendar_tomorrow(update, context):
    update.message.reply_text('Ertaga belgilandi belgilandi')

def calendar_month(update, context):
    update.message.reply_text('To\'liq taqvim belgilandi')

def select_region(update, context):
    update.message.reply_text('Mintaqa tanlash')

def select_dua(update, context):
    update.message.reply_text('Duoni ko\'rish belgilandi ')


def main():
    #Update ornatamiz
    updater = Updater('5127963368:AAGjDa6ZwcdAxuGQ_Qsq7dnUQcwkc26WrJs', use_context = True)
    
    #Dispatcher event aniqlash uchun
    dispatcher = updater.dispatcher

    #start uchun 
    # dispatcher.add_handler(CommandHandler('start', start))

    #inline button query
    # dispatcher.add_handler(CallbackQueryHandler(inline_callback))

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start',start)],
        states= {
            STATE_REGION: [CallbackQueryHandler(inline_callback)],
            STATE_CALENDAR: [
                MessageHandler(Filters.regex('^('+BTN_TODAY+')$'), calendar_today),
                MessageHandler(Filters.regex('^('+BTN_TOMORROW+')$'), calendar_tomorrow),
                MessageHandler(Filters.regex('^('+BTN_MONTH+')$'), calendar_month),
                MessageHandler(Filters.regex('^('+BTN_REGION+')$'), select_region),
                MessageHandler(Filters.regex('^('+BTN_DUA+')$'), select_dua)
            ],
        },
        fallbacks=[CommandHandler('start',start)]
    )
    dispatcher.add_handler(conv_handler)



    updater.start_polling()
    updater.idle()

main()