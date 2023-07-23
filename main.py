from defs import getUrl, getcards, phone
from flask import Flask
import telethon
import asyncio
import os, sys
import re
import requests
from telethon import TelegramClient, events
import random_address
from random_address import real_random_address
import names
from datetime import datetime
import time
import random
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

API_ID = 28883268
API_HASH = '2850e9f51b84512f603f962ee64ad517'
SEND_ID = -1001646069947
client = TelegramClient('session', API_ID, API_HASH)
ccs = []
chats = [
    '@LalaScrapperPublic',
    '@AstralScrapper',
    '@VegetaScrap',
    '@JLScrapper',
    '@BINEROS_CCS2',
    '@ozarkscrapper',
    '@ChatA2Assiad',
    '@kurumichat',
    '@techzillacheckerchat',
    '@oficialscorpionsgrupo',
    '@PublicExp',
    '@JohnnySinsChat',
    '@NfPrBroScraper',
    '@VenexChk',
    '@hcccdrops',
    '@ScrapperLost',
    '@CcsRoyals',
    '@RemChatChk',
    '@TeamBlckCard',
    '@astachkccs',
    '@ScrapeLive',
    '@leonbinerss',
    '@SexyDrops',
    '@cardesclub',
    '@kurumichks',
    '@binners_LA',
    '@CHECKEREstefany_bot',
    '@scrapper_ddrbins',
    '@valeryscrapp',
    '@ChatPFL',
    '@dSnowChat',
    '@KiraAccountsGrupo',
    '@onyxlivespublic',
    '@botsakuraa',
    '@BinsHellChat',
    '@secretgroup01',
    '@savagegroupoficial',  
    '@Venexchk',
    '@RemChatChk',
    '@ScrapperLala',
    '@alterchkchat',
    '@TechzillaChkChat',
    '@kurumichat',
    '@ChatA2Assiad',
    '@fbinschat',
    '@secretgroup01',
    '@BinSkillerChat',
    '@Venexchk',
    '@JohnnySinsChat',
    '@leonbinerss',
    '@RemChatChk',
    '@alterchkchat',
    '@AssociatonBinners1',
    '@dSnowChat',
    '@cardesclub',
    '@BinsHellChat', 
    '@secretgroup01',
    '@BinSkillerChat',
    '@RickPrimeChkFree',
    '@fbinschat',   
    '@RickPrimeChkFree',
    '@savagegroupoficial',
    '@savagegroupoficial', 
    '@CHECKEREstefany_bot', 
    '@CuartelCardingGrupo',
    '@CHECKEREstefany_bot', 
    '@astachkccs', 
    '@bcycc',
    '@fbinschat',
    '@MUGIWARAAC',     
    '@GodsOfTheBins',     
    '@fbinschat',     
    '@CuartelCardingGrupo',  
    '@botsakuraa',
    '@ArthurChkGroup',
    '@Sammy0007_Chat',
    '@SkadiScrapper',
    '@CCAUTH',
    '@Ikaroscrapper',
    '@Nasayuzakichkbot'
]

PALABRAS_CLAVE = [
     'APPROVED CCN',
     'Approved',
     'Non VBV',
     '✅ Approved ✅', 
     "Approved",
     "Succeeded! ",
     "APPROVED",
     "APPROVED ✅",
     "✅✅ Approved ✅✅",
     "Approved CCN",                    
     "Approved #AUTH! ✅",
     "Approved",
     "APPROVED ✅",
     "APPROVED ✓",
     "Security code incorrect",
     "Approved",
     "CVV2 FAILURE POSSIBLE CVV ⌯ N - AVS: G",
     "Succeeded!",
     "𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝒂𝒓𝒅 ✅",
     "𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅",                   
     "𝑪𝒉𝒂𝒓𝒈𝒆𝒅 𝟎.𝟐𝟓$",  
     "𝑪𝒉𝒂𝒓𝒈𝒆𝒅 $3 ✅",
     "Succeeded",   
     "Error: Your card has insufficient funds.",  
     "Subscription complete",             
     "CVV LIVE ✅",
     "Card Approved CCN/CCV Live",    
     "incorrect_cvc",
     "VIVA ✅",           
     "APPROVED ✓",
     "DECLINED INSUFFICIENT FUNDS",
     "DECLINED !",
     "Card Issuer Declined CVV",
     "CCN CARD / CVD ERROR 99048",
     "Order Placed. / Charged $228.64! ✅",
     "Approved / Invalid card verification number",
     "Order Placed. / Charged $22.64! ✅",
     "Order Placed. / Charged $281.00! ✅"
]



with open('cards.txt', 'r') as r:
    temp_cards = r.read().splitlines()

for x in temp_cards:
    car = getcards(x)
    if car:
        ccs.append(car[0])
    else:
        continue


@client.on(events.NewMessage(chats=chats, func=lambda x: getattr(x, 'text')))
async def my_event_handler(m):
    if m.reply_markup:
        text = m.reply_markup.stringify()
        urls = getUrl(text)
        if not urls:
            return
        text = requests.get(urls[0]).text
    else:
        text = m.text
    cards = getcards(text)
    if not cards:
        return
    cc, mes, ano, cvv = cards
    if cc in ccs:
        return
    ccs.append(cc)
    extra = cc[0:0 + 12]
    bin = requests.get(f'https://lookup.binlist.net/{cc[:6]}')
    if not bin:
        return
    bin_json = bin.json()
    addr = real_random_address()
    fullinfo = f"{cc}|{mes}|{ano}|{cvv}|{names.get_full_name()}|{addr['address1']}|{addr['city']}|{addr['state']}|{addr['postalCode']}|{phone()}|dob: {datetime.strftime(datetime(random.randint(1960, 2005), random.randint(1, 12), random.randint(1, 28), ), '%Y-%m-%d')}|United States Of America"

    print(f'{cc}|{mes}|{ano}|{cvv} - SCRAPPED SUCCESS ')
    with open('cards.txt', 'a') as w:
        w.write(fullinfo + '\n')

    scheme = bin_json['scheme'].upper()
    type = bin_json['type'].upper()
    brand = bin_json['brand'].upper()
    country_name = bin_json['country']['name'].upper()
    bank_name = bin_json['bank']['name'].upper()

    if 'bank' in bin_json and 'name' in bin_json['bank']:
        print("Bank Name:", bin_json['bank']['name'])
    else:
        print("Bank information not available.")

    selected_keyword = random.choice(PALABRAS_CLAVE)

    await client.send_message(
        PeerChannel(SEND_ID),
        f"""
     ❍ 𝐒𝐂𝐑𝐀𝐏𝐏𝐄𝐑 𝐀𝐔𝐑𝐎𝐑𝐀 2 [ 𝚂𝙸𝙼𝙿𝙻𝙴 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 ]
    ══════════════════
    𝐂𝐂 : ```{cc}|{mes}|{ano}|{cvv}```
    𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: ``` {selected_keyword} ```
    𝐄𝐗𝐓𝐑𝐀: ```{extra}xxxx|{mes}|{ano}|rnd ```
    ══════════════════
    𝐁𝐢𝐧 :  [ ```{cc[:6]}``` ]
    𝐁𝐢𝐧 𝐈𝐧𝐟𝐨 » : {scheme} - {type} - {brand}
    𝗕𝗮𝗻𝗸 » : {bank_name}
    𝗖𝗼𝘂𝗻𝘁𝗿𝘆 » : {country_name} - {bin_json['country']['emoji']}
    ══════════════════
    Dev: @ReyAustin
    ━━━━━━━━━━[⭐️]━━━━━━━━━━
    𝐀𝐔𝐑𝐎𝐑𝐀 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐎𝐅𝐈𝐂𝐈𝐀𝐋
    https://t.me/aurorabining
    ━━━━━━━━━━[⭐️]━━━━━━━━━━
        """,
    )


@client.on(events.NewMessage(outgoing=True, pattern=re.compile(r'.lives')))
async def my_event_handler(m):
    await m.reply(file='cards.txt')
    time.sleep(1)


client.start()
client.run_until_disconnected()
