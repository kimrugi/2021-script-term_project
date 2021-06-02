import telepot

import load_xml

TOKEN = "1867883299:AAFbISAlTqHjdIsUGzzwbppY371nZc8k8HU"
bot = None

def sendMessage(user, msg):
    bot.sendMessage(user, msg)

def reply_list(lib_list, user):
    if len(lib_list) == 0:
        bot.sendMessage(user, "결과를 찾을 수 없습니다.")
        return
    msg = ''
    for library in lib_list:
        msg += library['LIBRRY_NM'] + '\n'
    bot.sendMessage(user, msg)
    pass

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')
    if len(args) == 1:
        lib_list = load_xml.indiependent_search(args[0])
        reply_list(lib_list, chat_id)
    elif len(args) == 2:
        pass



def create_bot():
    global bot
    bot = telepot.Bot(TOKEN)
    bot.message_loop(handle)


create_bot()
import time
while 1:
    time.sleep(10)