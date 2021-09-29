#! /data/data/com.termux/files/usr/bin/python3
#garpozir@gmail.com

from telegram.ext import(
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler)
import telegram,time,hashlib,sqlite3,logging,jdatetime,arabic_reshaper,os,requests,traceback
from telegram import Update,ForceReply,Sticker,KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
from googletrans import Translator
from gtts import gTTS
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from bidi.algorithm import get_display
from fpdf import FPDF
from os import system,name,path
import speech_recognition as sr
from pydub import AudioSegment

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)
tar,end = range(2)
voice=range(1)

def cancel(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('🙈 لغو شد',reply_markup=telegram.ReplyKeyboardRemove())
    return ConversationHandler.END

def start(update: Update, context: CallbackContext) -> None:
    group=r'https://t.me/dic_en_fa'
    update.message.reply_text(f'{group} گروه اعضای ربات')
    user = update.effective_user
    update.message.reply_markdown_v2(
    f'سلام {user.mention_markdown_v2()}\nراهنما /help')

def END(update: Update, context: CallbackContext) -> None:
    if update.message.text=='/cancel':
        update.message.reply_text('🙈 لغو شد',reply_markup=telegram.ReplyKeyboardRemove())
        return ConversationHandler.END
    hash_code=True
    er=True
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    tday=(str(jdatetime.date.today()).split('-'))
    tday='_'.join(tday)
    user_name = update.effective_user
    user_name = user_name.full_name
    chat_id=update['message']['chat'].id
    if update.message.text=='🙊انصراف':
        hash_code=False
    elif update.message.text=='👍متن':
        update.message.reply_text(ter)
    elif update.message.text=='👍صوت':
        if os.path.isfile(f'{m}.mp3'):
            bot.send_audio(chat_id,audio=open(f'./{m}.mp3','rb'),caption='صوت 👍')
        else:
            myobj = gTTS(text=ter, lang='en', slow=False)
            myobj.save(f"{m}.mp3")
            time.sleep(0.5)
            bot.send_audio(chat_id,audio=open(f'./{m}.mp3','rb'),caption='صوت 👍')
    elif update.message.text=='👍تصویر':
        if os.path.isfile(f'{m}.png'):
            bot.send_photo(chat_id,photo=open(f'./{m}.png','rb'),caption='تصویر 👍')
        else:
            whit=7
            final_txt=txt
            if len(txt)>90:
                line=(len(txt)//90)+1
                x=90
                rng=0
                final_txt=''
                rntr='\n'
                for i in range(1,line+1):
                    if i ==line:rntr=''
                    final_txt+=txt[rng:x*i]+rntr
                    rng+=x
                whit+=len(final_txt.split('\n'))
            final_ter=ter
            if len(ter)>90:
                line=(len(ter)//90)+1
                x=90
                rng=0
                final_ter=''
                rntr='\n'
                for i in range(1,line+1):
                    if i ==line:rntr=''
                    final_ter+=ter[rng:x*i]+rntr
                    rng+=x
                whit+=len(final_ter.split('\n'))
            text_img='ربات مترجم: @Dic_Fa_EnBot\n\nمتن\n'+final_txt+'\n\nترجمه\n'+final_ter
            reshaped_text = arabic_reshaper.reshape(text_img)
            bidi_text = get_display(reshaped_text)
            img = Image.new('RGB', (600, whit*25), color = (255, 255, 255))
            fnt = ImageFont.truetype('Sahel-Black.ttf',12)
            down = ImageDraw.Draw(img)
            down.text((10,10), bidi_text, font=fnt, fill=(0, 0, 0))
            img.save(f'{m}.png')
            time.sleep(0.5)
            bot.send_photo(chat_id,photo=open(f'./{m}.png','rb'),caption='تصویر 👍')
    elif update.message.text=='👍پی دی اف':
        if os.path.isfile(f'{m}.pdf'):
            bot.send_document(chat_id,document=open(f'./{m}.pdf','rb'),caption='پی دی اف 👍')
        else:
            whit=7
            final_txt=txt
            if len(txt)>90:
                line=(len(txt)//90)+1
                x=90
                rng=0
                final_txt=''
                rntr='\n'
                for i in range(1,line+1):
                    if i ==line:rntr=''
                    final_txt+=txt[rng:x*i]+rntr
                    rng+=x
                whit+=len(final_txt.split('\n'))
            final_ter=ter
            if len(ter)>90:
                line=(len(ter)//90)+1
                x=90
                rng=0
                final_ter=''
                rntr='\n'
                for i in range(1,line+1):
                    if i ==line:rntr=''
                    final_ter+=ter[rng:x*i]+rntr
                    rng+=x
                whit+=len(final_ter.split('\n'))
            text_img='ربات مترجم: @Dic_Fa_EnBot\n\nمتن\n'+final_txt+'\n\nترجمه\n'+final_ter
            reshaped_text = arabic_reshaper.reshape(text_img)
            bidi_text = get_display(reshaped_text)
            pdf = FPDF()
            pdf.add_page()
            pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
            pdf.set_font('DejaVu', '', 10)
            for bidi_ in bidi_text.split('\n'):
                pdf.cell(200, 10, txt = bidi_,ln = 1, align = 'L')
            pdf.output(f"./{m}.pdf")
            time.sleep(0.5)
            bot.send_document(chat_id,document=open(f'./{m}.pdf','rb'),caption='پی دی اف 👍')
            if name == 'nt':
                 _ = system('cls')
            else:
                _ = system('clear')
    else:
        er=False
        if src=='fa':
            reply_keyboard = [['👍پی دی اف', '👍تصویر', '👍متن',"👍صوت",'🙊انصراف']]
        else:
            reply_keyboard = [['👍پی دی اف', '👍تصویر', '👍متن','🙊انصراف']]
        update.message.reply_text('نوع خروجی را تعیین کنید',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,resize_keyboard=True,input_field_placeholder=''))
    if er==True:
        time.sleep(0.5)
        if hash_code==True:
            conn = sqlite3.connect('sqlite.db')
            cur = conn.cursor()
            cur.execute(f"SELECT count(*) FROM dic_en_fa WHERE chat_id='{chat_id}'")
            rows=cur.fetchall()
            conn.close()
            if int(rows[0][0])==0:
                os.system(f'python add_member.py {chat_id}')
            conn = sqlite3.connect('sqlite.db')
            cur = conn.cursor()
            cur.execute(f"SELECT count(*) FROM dic_en_fa WHERE sha256='{m}' and chat_id='{chat_id}'")
            rows=cur.fetchall()
            conn.close()
            if int(rows[0][0])==0:
                sqliteConnection = sqlite3.connect('sqlite.db')
                try:
                    cursor = sqliteConnection.cursor()
                    sqlite_insert_query = f"""INSERT INTO dic_en_fa (date, time, chat_id, user_name,text,dic,src,dest,sha256)
                                           VALUES
                                          ("{tday}","{current_time}","{chat_id}","{user_name}","{txt}","{ter}","{src}","{dest}","{m}")"""
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    cursor.close()
                except sqlite3.OperationalError:pass
            update.message.reply_text(f'هش این ترجمه\n{m}')
        update.message.reply_text('/begin شروع بکار مترجم\n\n/archive تاریخچه ترجمه',reply_markup=telegram.ReplyKeyboardRemove())
        return ConversationHandler.END

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('/start راه اندازی ربات\n\n/help راهنما\n\n/begin شروع بکار مترجم\n\n/archive تاریخچه ترجمه\n\n/send_voice ارسال فایل صوتی\n\n/cancel انصراف')

def begin(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['👍فارسی به انگلیسی', '👍انگلیسی به فارسی']]
    update.message.reply_text('نوع ترجمه را انتخاب کنید',
    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,resize_keyboard=True,input_field_placeholder=''))
    return tar

def Tar(update: Update, context: CallbackContext) -> None:
    if update.message.text=='/cancel':
        update.message.reply_text('🙈 لغو شد',reply_markup=telegram.ReplyKeyboardRemove())
        return ConversationHandler.END
    global noe
    dici=['👍فارسی به انگلیسی', '👍انگلیسی به فارسی']
    if update.message.text==dici[0]:
        noe='en'
        update.message.reply_text('متن فارسی مورد نظر را وارد کنید',reply_markup=telegram.ReplyKeyboardRemove())
    elif update.message.text==dici[1]:
        noe='fa'
        update.message.reply_text('متن انگلیسی مورد نظر را وارد کنید',reply_markup=telegram.ReplyKeyboardRemove())
    else:
        try:
            lang=ord(update.message.text[0])
            if (lang>64 and lang<123)or lang==47:lang='en'
            else:lang='fa'
            if (lang=='en'and noe=='fa') or (lang=='fa' and noe=='en'):
                reply_keyboard = [['👍پی دی اف', '👍تصویر', '👍متن','🙊انصراف']]
                if noe=='en':reply_keyboard = [['👍پی دی اف', '👍تصویر', '👍متن',"👍صوت",'🙊انصراف']]
                if len(update.message.text)<2 or len(update.message.text)>3000:
                    if noe=='en':update.message.reply_text('متن فارسی مورد نظر را وارد کنید')
                    elif noe=='fa':update.message.reply_text('متن انگلیسی مورد نظر را وارد کنید')
                else:
                    global m,txt,ter,src,dest
                    txt=update.message.text
                    if noe=='fa':txt=txt.lower()
                    m=hashlib.sha256(txt.encode()).hexdigest()
                    conn = sqlite3.connect('sqlite.db')
                    cur = conn.cursor()
                    cur.execute(f"SELECT * FROM dic_en_fa WHERE sha256='{m}' limit 1")
                    rows=cur.fetchall()
                    conn.close()
                    if len(rows)==0:
                        g = Translator()
                        ter=g.translate(txt, noe)
                        src=ter.src
                        dest=ter.dest
                        ter=ter.text
                    else:
                        rows=rows[0]
                        src=rows[7]
                        dest=rows[8]
                        ter=rows[6]
                    update.message.reply_text('نوع خروجی را تعیین کنید',
                    reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True,resize_keyboard=True,input_field_placeholder=''))
                    del noe
                    return end
            else:
                if noe=='en':update.message.reply_text('متن فارسی مورد نظر را وارد کنید')
                elif noe=='fa':update.message.reply_text('متن انگلیسی مورد نظر را وارد کنید')
        except NameError:update.message.reply_text('نوع ترجمه را انتخاب کنید',)

#chert_pert
def echo(update: Update, context: CallbackContext) -> None:
    chat_id=update['message']['chat'].id
    hash_txt=update.message.text
    if len(hash_txt)==65:hash_txt=hash_txt[1:]
    hash_find=True
    def send_bot_arshive(val) -> None:
        if os.path.isfile(val):
            if i=='mp3':bot.send_audio(chat_id,audio=open(f'{val}','rb'),caption='صوت 👍')
            elif i=='png':bot.send_photo(chat_id,photo=open(f'{val}','rb'),caption='تصویر 👍')
            elif i=='pdf':bot.send_document(chat_id,document=open(f'{val}','rb'),caption='پی دی اف 👍')
            global hash_find
            hash_find=False
    for i in ['png','mp3','pdf']:
        send_bot_arshive(f'{hash_txt}.{i}')
    if hash_find:
        conn = sqlite3.connect('sqlite.db')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM dic_en_fa WHERE sha256='{hash_txt}' limit 1")
        rows=cur.fetchall()
        conn.close()
        if len(rows)!=0:
            rows=rows[0]
            db_txt=rows[5]
            db_dic=rows[6]
            text_img1='ربات مترجم: @Dic_Fa_EnBot\n\nمتن\n'+db_txt+'\n\nترجمه\n'+db_dic
            update.message.reply_text(text_img1)
        else:
            mas=update.message.text.lower()
            if mas=='masi' or mas=='معصومه' or mas == 'مصی':
                update.message.reply_text('''❤️💋❤️💋❤️💋

/help راهنما
                                          ''')
            else:
                update.message.reply_text('😱 '+update.message.text+' دستور نامعتبر\nراهنما /help')

def send_voice(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('''فایل مورد نظر را وارد کنید\nفرمتهای استاندارد mp3-ogg(oga)\nحداکثر اندازه فایل 10 مگابایت\nانصراف /cancel
                              ''')
    return voice

def VOICE(update: Update, context: CallbackContext) -> None:
    try:
        if (update.message.audio)==None and (update.message.voice)==None:
            if update.message.text!=None:
                if update.message.text!='/cancel':update.message.reply_text(update.message.text+' دستور نامعتبر 😱\n/cancel انصراف')
                else:
                    update.message.reply_text('🙈 لغو شد',reply_markup=telegram.ReplyKeyboardRemove())
                    return ConversationHandler.END
            else:update.message.reply_text('😱 فایل نامعتبر\n/cancel انصراف\nفرمتهای استاندارد mp3-ogg(oga)')
        else:
            try:audio=update.message.audio.get_file()
            except:audio=update.message.voice.get_file()
            info = requests.head(audio['file_path'])
            if float(info.headers['Content-Length'])>11000000.0:update.message.reply_text('حجم فایل نباید بیشتر از ۱۰ مگابایت باشد 😔')
            elif float(info.headers['Content-Length'])<2000.0:update.message.reply_text('این فایل بسیار کوچک می باشد 😔')
            elif audio['file_path'][-3:] not in ('mp3','oga','ogg'):update.message.reply_text('فرمت فایل انتخابی غیر استاندارد\nفرمتهای استاندارد mp3-ogg(oga)')
            else:
                update.message.reply_text('لطفاً منتظر بمانید...')
                audio.download(f"voice.{audio['file_path'][-3:]}")
                update.message.reply_text('در حال پردازش...')
                time.sleep(0.5)
                if audio['file_path'][-3:]=='mp3':isound = AudioSegment.from_mp3(f"voice.{audio['file_path'][-3:]}")
                else:isound = AudioSegment.from_ogg(f"voice.{audio['file_path'][-3:]}")
                isound.export("transcript.wav", format="wav")
                time.sleep(0.5)
                os.remove(f"voice.{audio['file_path'][-3:]}")
                AUDIO_FILE = "transcript.wav"
                ur = sr.Recognizer()
                with sr.AudioFile(AUDIO_FILE) as source:
                    iaudio = ur.record(source)
                    txt=ur.recognize_google(iaudio)
                g = Translator()
                ter=g.translate(txt, 'fa')
                src=ter.src
                dest=ter.dest
                ter=ter.text
                text_img2='ربات مترجم: @Dic_Fa_EnBot\n\nصوت به متن\n'+txt+'\n\nترجمه\n'+ter+'\n\n******************************\nتذکر: کاربر گرامی برگردان صوت به متن آنهم به زبان فارسی یک فناوری جدید می باشد و خالی از ایراد نیست'
                update.message.reply_text(text_img2)
                update.message.reply_text('/begin شروع بکار مترجم\n\n/send_voice ارسال فایل صوتی',reply_markup=telegram.ReplyKeyboardRemove())
                return ConversationHandler.END
    except (telegram.error.BadRequest,AttributeError):update.message.reply_text('حجم فایل نباید بیشتر از ۱۰ مگابایت باشد 😔')

def archive(update: Update, context: CallbackContext) -> None:
    chat_id=update['message']['chat'].id
    conn = sqlite3.connect('sqlite.db')
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM dic_en_fa WHERE chat_id='{chat_id}' order by id DESC limit 10")
    rows=cur.fetchall()
    conn.close()
    if len(rows)!=0:
        row=rows
        del rows
        cont=0
        text_img2=''
        for rows in row:
            cont+=1
            tarikh=rows[1]
            zaman=rows[2]
            matn=rows[5]
            if len(matn)>35:matn=matn[:35]+'...'
            tarj=rows[6]
            if len(tarj)>35:tarj=tarj[:35]+'...'
            ramz=rows[9]
            text_img2+=f'\nشماره ترجمه: {rows[0]}\nتاریخ: {tarikh}\nزمان: {zaman}\nمتن: {matn}\nترجمه: {tarj}\n/{ramz}'
        update.message.reply_text(text_img2)
    else:
        update.message.reply_text('موردی پیدا نشد 🤔')

def main() -> None:
    try:
        r=requests.get('https://telegram.org')
    except:
        _=input('اتصال به سرور تلگرام ممکن نیست')
        exit()
    if os.path.isfile('sqlite.db'):pass
    else:
        conn = sqlite3.connect('sqlite.db')
        c = conn.cursor()
        c.execute(f'''CREATE TABLE dic_en_fa
([id] INTEGER PRIMARY KEY,[date] text, [time] text, [chat_id] text,[user_name] text,[text] text,[dic] text,[src] text,[dest]text, [sha256] text)''')
        conn.commit()
        conn.close()
    global bot
    tokeni='1970507900:AAErywobKdAgHAy4X3J4Sv3SFuVQCoiiBBc'
    updater = Updater(tokeni)
    bot=telegram.Bot(tokeni)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("archive", archive))
    conv_handler = ConversationHandler(
            entry_points=[CommandHandler('begin', begin)],
            states={
                    tar : [MessageHandler(Filters.text, Tar)]                    ,
                    end : [MessageHandler(Filters.text, END)]                    },
        fallbacks=[CommandHandler('cancel', cancel)]
        )
    dispatcher.add_handler(conv_handler)
    conv_handler = ConversationHandler(
            entry_points=[CommandHandler('send_voice', send_voice)],
            states={
                    voice: [MessageHandler(Filters.all, VOICE)]                    },
        fallbacks=[CommandHandler('cancel', cancel)]
        )

    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(MessageHandler(Filters.text | Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
