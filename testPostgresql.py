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

#File pass2fac
filepass2fac = open("pass2fac.txt","r")
pass2fac = filepass2fac.readline()

#File Conn Postgresql
paramsConnDB = open("paramsConnDB.config","r")
listParamsConnDB = [row for row in paramsConnDB.readlines()]
paramsConnDB.close()

#Connection Postgresql

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

initialBot = 151
endBot = 153


cursor = connDB.cursor()
cursor.execute('SELECT * FROM bots where IdBot >='+str(initialBot)+' and IdBot <='+str(endBot))

listBots = []

for row in cursor:
    listBots.append(row)

api_id = ''
api_hash = ''
phone_number = ''
bot = ''
number_ramdom = 0

control_End_Bucle = 0

# for item in listBots:
#     while item[0] != control_End_Bucle:
#         api_id = str(item[2])
#         print("api_id: " + api_id)
#         api_hash = item[3]
#         print("api_hash: "+ api_hash)
#         phone_number = item[1]
#         print("phone_number: "+ item[1])
#         bot = item[0]
#         print("bot: "+ str(item[0]))
#         print("--------------------")

while control_End_Bucle == 0:
    for item in listBots:
        api_id = str(item[2])
        print("api_id: " + api_id)
        api_hash = item[3]
        print("api_hash: "+ api_hash)
        phone_number = item[1]
        print("phone_number: "+ item[1])
        bot = item[0]
        print("bot: "+ str(item[0]))
        print("--------------------")
        if item[0] == endBot:
            print("Esperando 10 segundo")
            sleep(10)
