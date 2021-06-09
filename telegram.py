import telepot

import load_xml

TOKEN = "1867883299:AAFbISAlTqHjdIsUGzzwbppY371nZc8k8HU"
bot = None


def sendMessage(user, msg):
    bot.sendMessage(user, msg)


def reply_list(lib_list, user):
    if len(lib_list) == 0:
        sendMessage(user, "결과를 찾을 수 없습니다.")
        return

    msg = ''
    i = 0
    for library in lib_list:
        msg += library['LIBRRY_NM'] + '\n'
        i += 1
        if i >= 5:
            sendMessage(user, msg)
            msg = ''
            i -= 5


def reply_info(lib_list, user):
    if len(lib_list) == 0:
        sendMessage(user, "결과를 찾을 수 없습니다.")
        return
    if len(lib_list) > 5:
        reply_list(lib_list, user)
        return

    for library in lib_list:
        msg = library["LIBRRY_NM"]+"\n주소: "+library["ADDRESS"]+"\n전화번호: "+library["LIBRRY_TELNO"]+"\n휴관일: "+\
            library["CLOSE_DE_INFO"]+"\n평일 운영시간: "+library["BEGIN_TM"]+"~"+library["END_TM"]+"\n토요일 운영시간"+\
            library["SAT_BEGIN_TM"]+"~"+library["SAT_END_TM"]+"\n공휴일 운영시간"+library["HOLI_BEGIN_TM"]+"~"+\
            library["HOLI_END_TM"]
        sendMessage(user, msg)



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        sendMessage(chat_id, '[시/군] [주소 혹은 ]')
        return

    text = msg['text']
    args = text.split(' ')
    if len(args) == 1:
        lib_list = load_xml.search(args[0])
        reply_list(lib_list, chat_id)
    else:
        to_search = text.replace(args[0]+" ", '')
        lib_list = load_xml.search_name(to_search, load_xml.search(args[0]))
        reply_info(lib_list, chat_id)

def create_bot():
    global bot
    bot = telepot.Bot(TOKEN)
    bot.message_loop(handle)



