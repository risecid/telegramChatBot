from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import requests,json

def tentang(update, context):
    update.message.reply_text(
        "Hi Bro Namaku Mimi aku diintegrasikan dengan API SimSimi Premium Aku Di Buat Oleh Orang ini @rian1337 [Python 3.8.0] ".format(update.message.from_user.first_name))

def mulai(update, context):
    update.message.reply_text(
        'Halo {}, Sekarang Kamu Bisa Memulai Chat Denganku'.format(update.message.from_user.first_name))
	
def echo(update, context):
    url = 'https://secureapp.simsimi.com/v1/simsimi/talkset?uid=297390035&av=6.9.3.7&lc=id&cc=&tz=Asia%2FJakarta&os=a&ak=Nsh1x94iNA2oftvixJMmTj1awEk%3D&message_sentence={}&normalProb=8&isFilter=1&talkCnt=9&talkCntTotal=9&reqFilter=1&session=Yk3fdTR8FJiakMZFUSVoR5AGpk64EP1vszjwwMkKBsa3goD6haDHrd1tyJMZYaMPpV5KaXF2VvWyTvh1AAPDbos3&traceSentenceLinkId=138187571&triggerKeywords=%5B%5D'.format(update.effective_message.text)
    r = requests.get(url)
    data = json.loads(r.text)
    update.effective_message.reply_text(data['simsimi_talk_set']['answers'][0]['sentence'])

updater = Updater('1459712147:AAGIk8Q6DNyl-HbgtsbuP7u2AnItfIESqJE',
use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', mulai))
updater.dispatcher.add_handler(CommandHandler('tentang', tentang))
echo_handler = MessageHandler(Filters.text, echo)
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()
updater.idle()