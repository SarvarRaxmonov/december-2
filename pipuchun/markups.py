
from os import name
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, callback_game, inline_keyboard
from aiohttp.helpers import parse_mimetype
from attr import resolve_types
btnprofile = KeyboardButton(' profil ')
profilekey = ReplyKeyboardMarkup(resize_keyboard= True).add(btnprofile)

btnurchannel = InlineKeyboardButton(text='azo bulish', url='https://t.me/b148uz')
btnurchannel2 = InlineKeyboardButton(text='azo bulish 2', url='https://t.me/elyorbekerkinbek')
btndonesub = InlineKeyboardButton(text='azo buldim', callback_data="subchanneldone")

checksubmenu = InlineKeyboardMarkup(row_width=1)
checksubmenu.insert(btnurchannel)
checksubmenu.insert(btnurchannel2)
checksubmenu.insert(btndonesub)





btnmain = InlineKeyboardButton('Quron 🎧')
btnmain2 = InlineKeyboardButton('Bot 📜')
btnmain3 = InlineKeyboardButton('Namoz ☪️')
btnmain4 = InlineKeyboardButton('Multifilimlar 📺')
btnmain5 = InlineKeyboardButton('Kitobxona 🏛')
from datetime import datetime
import jsonuz as jsuz
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

btnorder = InlineKeyboardButton(datetime.now().strftime("%H:%M:%S"),'boshqa')

sainmenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnmain, btnmain2, btnmain3,btnmain4,btnmain5)
orqagaa = ReplyKeyboardMarkup(resize_keyboard=True).add(btnmain, btnmain2, btnmain3,btnmain4,btnmain5)
orqagaall = InlineKeyboardButton('Menu 📜',callback_data='orqagaall')
orqaga = InlineKeyboardButton('⬅️ Orqaga', callback_data='orqaga')
keyingi = InlineKeyboardButton('Keyingi ➡️', callback_data='keyingi')
keyingi2 = InlineKeyboardButton('Keyingi ➡️', callback_data='keyingi2')
keyingi3 = InlineKeyboardButton('Keyingi ➡️', callback_data='keyingi3')
orqaga1 = InlineKeyboardButton('⬅️ Orqaga', callback_data='orqaga1')
orqaga2 = InlineKeyboardButton('⬅️ Orqaga', callback_data='orqaga2')
orqaga3 = InlineKeyboardButton('⬅️ Orqaga', callback_data='orqaga3')
sura1 = InlineKeyboardMarkup(resize_keyboard=True, row_width=5)
sura2 = InlineKeyboardMarkup(resize_keyboard=True, row_width=5)
sura3 = InlineKeyboardMarkup(resize_keyboard=True, row_width=5) 
sura4 = InlineKeyboardMarkup(resize_keyboard=True, row_width=7)

#birinchi qori
sura5 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=5)
sura6 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=5)
sura7 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=5)
sura8 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=7)
#ikinchi qori
sura9 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=5)
sura10 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=5)
sura11 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=5)
sura12 =  InlineKeyboardMarkup(resize_keyboard=True, row_width=7)

qorilists = InlineKeyboardMarkup(resize_keyboard=True, row_width=5)


    
hammadio1 = InlineKeyboardButton('📻', callback_data='hm1')
hammadio2 = InlineKeyboardButton('📻', callback_data='hm2')
hammadio3 = InlineKeyboardButton('📻', callback_data='hm3')
hammadio4 = InlineKeyboardButton('📻', callback_data='hm4')

for c in range(1,115):

    if c < 31:
          sura1.insert(InlineKeyboardButton(text=c, callback_data=f"sura3{c}"));
          sura5.insert(InlineKeyboardButton(text=c, callback_data=f"sura4{c}"));
          sura9.insert(InlineKeyboardButton(text=c, callback_data=f"sura5{c}"));
    elif c > 30:
         if c < 61:
              sura2.insert(InlineKeyboardButton(text=c, callback_data=f"sura3{c}"));
              sura6.insert(InlineKeyboardButton(text=c, callback_data=f"sura4{c}"));
              sura10.insert(InlineKeyboardButton(text=c, callback_data=f"sura5{c}"));
    if c > 60:
         if c < 91:
              sura3.insert(InlineKeyboardButton(text=c, callback_data=f"sura3{c}"));
              sura7.insert(InlineKeyboardMarkup(text=c, callback_data=f"sura4{c}"));
              sura11.insert(InlineKeyboardButton(text=c, callback_data=f"sura5{c}")); 
    if c > 91:
         if c < 115:
              sura4.insert(InlineKeyboardButton(text=c, callback_data=f"sura3{c}"));
              sura8.insert(InlineKeyboardButton(text=c, callback_data=f"sura4{c}"));
              sura12.insert(InlineKeyboardButton(text=c, callback_data=f"sura5{c}"));
#qorilar listi
    if c < 16:
             qorilists.insert(InlineKeyboardButton(text=c, callback_data=f"qori{c}"))

uzv = {sura5:'keyingi5', sura6:'keyingi6', sura7:'keyingi7', sura8:'keyingi8', 
       sura9:'keyingi9', sura10:'keyingi10', sura11:'keyingi11',
       }
uzv2 = {sura5:5,sura6:6,sura7:7,sura8:8,sura9:9,sura10:10,sura11:11,sura12:12}
for i,v in uzv2.items():
           i.insert(InlineKeyboardButton(text='⬅️ Orqaga', callback_data=f"ortga{v}"));
           i.insert(InlineKeyboardButton(text='📻', callback_data=f"hm{v}"))
for i,v in uzv.items():
     i.insert(InlineKeyboardButton(text='Keyingi ➡️', callback_data=v));          

          
sura1.insert(orqaga)
sura1.insert(hammadio1)
sura1.insert(keyingi)
sura2.insert(orqaga1)
sura2.insert(hammadio2)
sura2.insert(keyingi2)
sura3.insert(orqaga2)
sura3.insert(hammadio3)
sura3.insert(keyingi3)
sura4.insert(hammadio4)
sura4.insert(orqaga3)
btninfo = KeyboardButton(' quron')

btnerkak = KeyboardButton('Erkaklarga 👨‍🦰')
btnayol = KeyboardButton('Ayollarga 👩‍🦰')
orqaga = KeyboardButton('Menu 📜')
orqagaerkaklar = KeyboardButton('Menu 📜')
orqagaayollar= KeyboardButton('Menu 📜')


namozbulimi = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnayol, btnerkak, orqaga)


namozbulimia = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)


namozbulimie = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)



       
namozlist = ['Bomdod 🌃','Peshin 🌇','Asr 🏙','Shom 🌉','Xufton 🌌','Menu 📜']
for i in namozlist:
    namozbulimie.insert(KeyboardButton(text=i, one_time_keyboard=True))
    
    
    
namozlist2 = ['Bomdod 🌃ㅤ','Peshin 🌇ㅤ','Asr 🏙ㅤ','Shom 🌉ㅤ','Xufton 🌌ㅤ','Menu 📜']
    
for n in namozlist2:
     namozbulimia.insert(KeyboardButton(text=n))
     
     
     
multi = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)

multilist = ['Menu 📜','Qur\'onda zikri kelgan ajoyibotlar 🕋','Qur\'onda zikri kelgan insonlar qissasi 🏔','Imom Al-buxoriy ⚜️','Payg\'ambarlar Tarixi ☪️','Imom Termiziy 🕯']
for n in multilist:
    multi.insert(KeyboardButton(text=n))
    

pdf = KeyboardButton(text="Kitoblar 📚")
audio = KeyboardButton(text="Audio 🎧")

menukitob = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(pdf,audio)