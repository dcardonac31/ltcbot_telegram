#Jangan Di ubah ubah  cuk kodennya nanti erorr
#Impor
from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from bs4 import BeautifulSoup
from time import sleep
import requests, json, re, sys, os
import colorama
from colorama import Fore, Back, Style
from datetime import datetime
from decimal import Decimal
import psycopg2
from psycopg2 import Error

#warna
colorama.init(autoreset=True)
hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
hijau2 = Style.NORMAL+Fore.GREEN
putih = Style.RESET_ALL
abu = Style.DIM+Fore.WHITE
ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
ungu2 = Style.NORMAL+Fore.MAGENTA
yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
yellow2 = Style.NORMAL+Fore.YELLOW
red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
red2 = Style.NORMAL+Fore.RED


#File Conn Postgresql
paramsConnDB = open("paramsConnDB.config","r")
listParamsConnDB = [row for row in paramsConnDB.readlines()]
paramsConnDB.close()

#Connection SQL SERVER

hostConn = listParamsConnDB[0].rstrip()
dbConn = listParamsConnDB[1].rstrip()
userConn = listParamsConnDB[2].rstrip()
passConn = listParamsConnDB[3].rstrip()

connDB = psycopg2.connect(
    host = hostConn,
    port = "5432",
    database = dbConn,
    user = userConn,
    password = passConn
)

cursor = connDB.cursor()

def balance_history_log(phone, bot_number,balance_value, apiid, apihash):
    if balance_value.startswith('Available balance:'):
        today = datetime.now()
        balance_value = balance_value.replace(".",",")
        balance_history = phone_number + ';' + bot + ';' + str(today) + ';' + balance_value +'\n' 
        insertbot = bot_number+";"+'insert into ltcbottelegram.bots values('+bot_number+','+'"'+phone_number+'",'+api_id+','+'"'+api_hash+'")'+'\n'
        print(balance_history)
        f = open("/storage/emulated/0/Download/bot_ltc/ltcbot_telegram/balance_history.txt","a")
        f.write(balance_history)
        f.close()
        f2 = open("/storage/emulated/0/Download/bot_ltc/ltcbot_telegram/sqlbots.txt","a")
        f2.write(insertbot)
        f2.close()

#banner
print ("===================================================")
print ("~Telegram Click bot Tuyul~")
print ("AUTHOR: RIANTO")
print ("Youtube: Master Termux Indonesia")
print ("Suport&thanks: Jejaka Tutorial")
print ("MODIFIED: dcardonac31")
print ("https://github.com/dcardonac31")
print ("===================================================")

#Sistem_Script
if not os.path.exists('session'):
    os.makedirs('session')

api_id = '2164319'
api_hash = 'c5509e9a858be29a9d34aba24404cd46'
phone_number = '+16605944101'
bot = '21'
walletltc = 'M9P4J6mAwBTV3Yvuxyzyf9qwmumpSaiXMq'
print(bot)
print(phone_number)

client = TelegramClient('session/'+phone_number,api_id,api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number,input('{}Masukan Code Anda {}>>{} '.format(hijau,abu,putih)))
    except SessionPasswordNeededError:
        password = input('{}Masukan Password 2fa Anda {}>>{} '.format(hijau,abu,putih))
        me = client.start(phone_number,password)

channel_username = '@Litecoin_click_bot'


c = requests.session()

ua = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

channel_entity = client.get_entity(channel_username)
try:
    for ulang in range(999999999):          
        sys.stdout.write('\r                                                        \r')
        sys.stdout.write('\r{}Trying to Fetch the URL'.format(yellow2))
        client.send_message(entity=channel_entity,message='Cancel')        
        client.send_message(entity=channel_entity,message='🖥 Visit sites')
        sleep(3)
        message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        channel_id = message_history.messages[0].id
        if message_history.messages[0].message.find('Sorry, there are no new ads available.') != -1:
            sys.stdout.write('\r                                                     \r')
            sys.stdout.write('\r{}Sorry, there are no new ads available.\n'.format(red2))
            break
        url = message_history.messages[0].reply_markup.rows[0].buttons[0].url
        sys.stdout.write('\r                                                     \r')
        sys.stdout.write('\r{}Visit To URL {}'.format(yellow2,putih)+url)

        r = c.get(url,headers=ua)
        soup = BeautifulSoup(r.text,"html.parser")

        if soup.find('div',class_='g-recaptcha') is None and soup.find('div',id='headbar') is None:
            sleep(2)
            message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
            message = message_history.messages[0].message
            sys.stdout.write('\r                                                     \r')
            sys.stdout.write('\r'+yellow+message)
            if message_history.messages[0].message.find('Please stay on') != -1 or message_history.messages[0].message.find('You must stay') != -1:
                timer = re.findall(r'([\d.]*\d+)',message)
                sleep(int(timer[0]))
                sleep(3)
                message_history = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0,add_offset=0, hash=0))
                sys.stdout.write('\r                                                     \r')
                sys.stdout.write('\r{}'.format(hijau)+message_history.messages[0].message+'\n')

        elif soup.find('div',id='headbar') is not None:
            for data in soup.find_all('div',class_='container-fluid'):
                code = data.get('data-code')
                timer = data.get('data-timer')
                token = data.get('data-token')
                sleep(int(timer))
                r = c.post('https://dogeclick.com/reward',data={'code': code, 'token': token},headers=ua)
                jsn = json.loads(r.text)
                sys.stdout.write('\r                                                     \r')
                sys.stdout.write(hijau+"\rYou earned "+jsn['reward']+" LTC for visiting sites\n")
        else:
            sys.stdout.write('\r                                                     \r')
            sys.stdout.write(red+'\rCaptcha detected')
            sleep(2)
            client(GetBotCallbackAnswerRequest(channel_username,channel_id,data=message_history.messages[0].reply_markup.rows[1].buttons[1].data))
            sys.stdout.write('\r                                                     \r')
            print (red+'\rSuccessfully Skip Captcha\n')

    client.send_message(entity=channel_entity,message='balance')
    sleep(6)
    message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
    balance_history_log(phone_number,bot, message_history.messages[0].message, api_id, api_hash)
    balance_value = message_history.messages[0].message.replace("Available balance: ","")
    balance_value = balance_value.replace(" LTC","")
    balance_value_decimal = Decimal(balance_value)
    print(balance_value_decimal)
    if balance_value_decimal >= 0.0003:
        print('Withdraw')
        client.send_message(entity=channel_entity,message='Withdraw')
        sleep(10)
        print('Wallet: '+walletltc)
        client.send_message(entity=channel_entity,message=walletltc)
        sleep(10)
        print(balance_value)
        client.send_message(entity=channel_entity,message=balance_value)
        sleep(12)
        confirmation_fee = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        sleep(10)
        print('Confirm')
        client.send_message(entity=channel_entity,message='Confirm')
        sleep(10)
        text_confirmation_fee = confirmation_fee.messages[0].message
        len_fee = len(text_confirmation_fee)
        fee = text_confirmation_fee[(len_fee-15):(len_fee-5)]
        fee_decimal = Decimal(fee)
        print(fee_decimal)
        sentence_insert ="INSERT INTO withdrawlog (withdrawaldate, idbot, phonenumber, withdrawalvalue, withdrawfee) VALUES (%s, %s, %s, %s, %s);"
        values = (datetime.now(), int(bot), phone_number, balance_value_decimal, fee_decimal )
        cursor.execute(sentence_insert, values)
        connDB.commit()
    client.disconnect()
except e:
    client.send_message(entity=channel_entity,message='balance')
    sleep(6)
    message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
    balance_history_log(phone_number,bot, message_history.messages[0].message, api_id, api_hash)
    print(red+"ERROR Detected: "+ e)
    client.disconnect()
    sys.exit()