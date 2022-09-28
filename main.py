import telegram.ext
import time
import os
import telegram

#https://api.telegram.org/bot/getUpdates
#762465380


timeDate = time.strftime('%Y:%m:%d:%H:%M:%S')

with open("token.txt","r") as f:

    TOKEN = f.read()



update = telegram.ext.Updater(TOKEN,use_context=True )
disp = update.dispatcher

def images(update,source):
    update.message.reply_text("Lütfen bekleyiniz..")
    resim = open("assets/images/images.jpg","rb")
    time.sleep(3)
    update.message.reply_photo(images)

def images1(update,source):
    update.message.reply_text("Lütfen bekleyiniz..")
    resim1 = open("assets/images/images(1).jpg","rb")
    time.sleep(3)
    update.message.reply_photo(images(1))

def indir(update,source):
    update.message.reply_text("Lütfen bekleyiniz..")
    indir = open("assets/images/indir.jpg","rb")
    time.sleep(3)
    update.message.reply_photo(indir)

def indir1(update,source):
    update.message.reply_text("Lütfen bekleyiniz..")
    indir1 = open("assets/images/indir (1).jpg","rb")
    time.sleep(3)
    update.message.reply_photo(indir(1))


update = telegram.ext.Updater(TOKEN,use_context=True )
disp = update.dispatcher

disp.add_handler(telegram.ext.CommandHandler("images",images))
disp.add_handler(telegram.ext.CommandHandler("images(1)",images(1)))
disp.add_handler(telegram.ext.CommandHandler("indir",indir))
disp.add_handler(telegram.ext.CommandHandler("indir(1)",indir(1)))

update.start_polling()
update.idle()