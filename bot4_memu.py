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
import psycopg2
from psycopg2 import Error
import random
from decimal import Decimal
import os

#File pass2fac
filepass2fac = open("pass2fac.txt","r")
pass2fac = filepass2fac.readline()

#File Conn Postgresql
paramsConnDB = open("paramsConnDB.config","r")
listParamsConnDB = [row for row in paramsConnDB.readlines()]
paramsConnDB.close()

#File sentence sql
file_sql_sentences = open("sql_sentences.sql","r")
list_sql_sentences = [row for row in file_sql_sentences.readlines()]
file_sql_sentences

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

initialBot = 13
endBot = 1000
endBotAux = 0
wallet = ''

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
blue = Style.NORMAL+Fore.BLUE

def balance_history_log(phone, bot_number,balance_value):
    if balance_value.startswith('Available balance:'):
        today = datetime.now()
        balance_value = balance_value.replace(".",",")
        balance_history = phone_number + ';' + bot + ';' + str(today) + ';' + balance_value +'\n' 
        insertbot = bot_number+";"+'insert into ltcbottelegram.bots values('+bot_number+','+'"'+phone_number+'",'+api_id+','+'"'+api_hash+'")'+'\n'
        print(balance_history)

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

api_id = ''
api_hash = ''
phone_number = ''
bot = ''
number_ramdom = 0
number_ramdom = 0
control_End_Bucle = 0


while control_End_Bucle == 0:
    contbots = 0
    contbotsaux = 0    
    urlaux = ''
    cursor = connDB.cursor()
    cursor.execute(list_sql_sentences[3])

    cursor2 = connDB.cursor()
    cursor2.execute('SELECT MAX(idbot) FROM bots WHERE idbot <= '+str(endBot))


    listBots = []

    for row in cursor:
        listBots.append(row)
        print(blue+"bot: "+str(row[0]) + " balance: "+str(row[4]))
        contbots = contbots + 1

    for row in cursor2:
        endBotAux = row[0]
  

    print("--------------------")
    print("Last bots: ")
    print(endBotAux)
    print("--------------------")

    for item in listBots:
        contbotsaux = contbotsaux + 1
        print(blue+"bot  "+str(contbotsaux)+" of "+str(contbots))        
        today = datetime.now()
        number_ramdom = random.randint(1,128)
        print("Number ramdon: "+str(number_ramdom))
        cursor3 = connDB.cursor()
        cursor3.execute('SELECT "walletAddress" FROM wallet WHERE id = ' + str(number_ramdom))
        for row in cursor3:
            wallet = row[0]  
        print("--------------------")        
        api_id = str(item[2])
        print("api_id: " + api_id)
        api_hash = item[3]
        print("api_hash: "+ api_hash)
        phone_number = item[1]
        print("phone_number: "+ item[1])
        bot = str(item[0])
        print("bot: "+ str(item[0]))
        print("--------------------")
        print("Datetime: "+ str(today))
        print("Hour: "+ str(today.hour))
        print("---------------------")
        client = TelegramClient('session/'+phone_number,api_id,api_hash)
        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone_number)
                me = client.sign_in(phone_number,input('{}Code Sign in {}>>{} '.format(hijau,abu,putih)))
            except SessionPasswordNeededError:
                me = client.start(phone_number,pass2fac)
            except:
                sentence_insert_botsuspend = "INSERT INTO public.botsuspend(idbotsuspend) VALUES (%s);"
                value = (int(bot))
                cursor.execute(sentence_insert_botsuspend, [value])
                connDB.commit()
                print(red+"accountbanned id: " + bot)
                break

        channel_username = '@Litecoin_click_bot'


        c = requests.session()

        ua = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }

        channel_entity = client.get_entity(channel_username)
        try:
            for ulang in range(999999999):
                print(red + "Url aux :" + urlaux)    
                sys.stdout.write('\r                                                        \r')
                sys.stdout.write('\r{}Trying to Fetch the URL'.format(yellow2))
                # client.send_message(entity=channel_entity,message='Cancel')
                client.send_message(entity=channel_entity,message='🖥 Visit sites')
                sleep(3)
                message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                channel_id = message_history.messages[0].id
                if message_history.messages[0].message.find('Sorry, there are no new ads available.') != -1:
                    print('\r                                                     \r')
                    print('\r{}Sorry, there are no new ads available.\n'.format(red2))
                    break

                if message_history.messages[0].message.find('In order to use this bot, you must agree to our') != -1:
                    print('In order to use this bot, you must agree to our')
                    sentence_insert_botsuspend = "INSERT INTO public.botsuspend(idbotsuspend) VALUES (%s);"
                    value = (int(bot))
                    cursor.execute(sentence_insert_botsuspend, [value])
                    connDB.commit()
                    print(red+"accountbanned id: " + bot)
                    break


                url = message_history.messages[0].reply_markup.rows[0].buttons[0].url

                if url == urlaux:
                    break

                urlaux = url
                
                sys.stdout.write('\r                                                     \r')
                sys.stdout.write('\r{}Visit To URL {}'.format(yellow2,putih)+url)                
                sys.stdout.write('\r                                                     \r')
                r = c.get(url,headers=ua)
                soup = BeautifulSoup(r.text,"html.parser")
                if soup.text.find('Checking your browser before accessing doge.click'):
                    print(blue+"Bot: "+bot)
                    print(blue+"bot  "+str(contbotsaux)+" of "+str(contbots))                    
                    os.system("termux-open-url \""+url+"\"")
                    print(hijau2 + message_history.messages[0].message)
                    sleep(2)
                    print("Time")
                    message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                    message = message_history.messages[0].message
                    print(hijau2 +"Time: " + message)
                    if message.find('Please stay on the site for at least') != -1:
                        timer = message.replace("Please stay on the site for at least ","")
                        timer = timer.replace(" seconds...","") 
                        print(blue + "Wait "+ timer +" seconds")
                        sleep(int(timer))
                    else:
                        print(blue + "Wait 60 s")
                        sleep(60)

                    client.send_message(entity=channel_entity,message='balance')
                    sleep(6)
                    message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
                    balance_value = message_history.messages[0].message.replace("Available balance: ","")
                    print(balance_value)

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
                        # jsn = json.loads(r.text)
                        # sys.stdout.write('\r                                                     \r')
                        # sys.stdout.write(hijau+"\rYou earned "+jsn['reward']+" LTC for visiting sites\n")
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
            today = datetime.now()
            balance_history_log(phone_number,bot, message_history.messages[0].message)
            balance_value = message_history.messages[0].message.replace("Available balance: ","")
            balance_value = balance_value.replace(" LTC","")
            balance_value_decimal = Decimal(balance_value)
            sentence_insert_balance ="INSERT INTO public.balanceltcbot(idbot, datetimeexecution, balance) VALUES (%s, %s, %s);"
            values = (int(bot),today,balance_value_decimal)
            cursor.execute(sentence_insert_balance, values)
            connDB.commit()
            print(balance_value_decimal)
            if balance_value_decimal >= 0.0003010:
                print('Withdraw')
                client.send_message(entity=channel_entity,message='Withdraw')
                sleep(10)
                print('Wallet: '+wallet)
                client.send_message(entity=channel_entity,message=wallet)
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
                sentence_insert ="INSERT INTO withdrawlog (withdrawaldate, idbot, phonenumber, withdrawalvalue, withdrawfee, walletaddress) VALUES (%s, %s, %s, %s, %s, %s);"
                values = (datetime.now(), int(bot), phone_number, balance_value_decimal, fee_decimal, wallet)
                cursor.execute(sentence_insert, values)
                connDB.commit()
                client.disconnect()
        except:
            client.send_message(entity=channel_entity,message='balance')
            sleep(6)
            message_history = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
            balance_history_log(phone_number,bot, message_history.messages[0].message)
            print(red+"ERROR Detected")
            client.disconnect()
    if contbots == 1:
        print(blue+"Waiting 30 minutes for the next bot...")    
        sleep(1800)
    else:
        print(blue+"Waiting 20 minutes for the next bot...")    
        sleep(1200) 