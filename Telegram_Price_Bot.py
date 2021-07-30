import requests 
import time
from os import system
system("title " + "@c9zd - Telegram Coin Price Bot")
import colorama
from colorama import Fore
colorama.init(autoreset=True)

print("""
 _____    _                                 ______     _           ______       _   
|_   _|  | |                                | ___ \   (_)          | ___ \     | |  
  | | ___| | ___  __ _ _ __ __ _ _ __ ___   | |_/ / __ _  ___ ___  | |_/ / ___ | |_ 
  | |/ _ \ |/ _ \/ _` | '__/ _` | '_ ` _ \  |  __/ '__| |/ __/ _ \ | ___ \/ _ \| __|
  | |  __/ |  __/ (_| | | | (_| | | | | | | | |  | |  | | (_|  __/ | |_/ / (_) | |_ 
  \_/\___|_|\___|\__, |_|  \__,_|_| |_| |_| \_|  |_|  |_|\___\___| \____/ \___/ \__|
                  __/ |                                                             
                 |___/                                                              """)

print(Fore.RED + """
Cᴏᴅᴇᴅ Bʏ Aʜᴍᴇᴅ Iɴsᴛᴀ: @c9zd""")
print(Fore.GREEN +"""
        0 - Bitcoin
        1 - Etherium
        2 - Tether
        5 - XRP
        6 - DogeCoin
        11 - Bitcoin Cash
        12 - Litecoin
        17 - Stellar
        26 - Monero
""")
print("To find the code of a certain coin go to https://coinmarketcap.com")
print("code = its number-1")

#Global Variables

market_api_key = "COINMARKETCAP API TOKEN"
bot_api_key = "TELEGRAM API TOKEN"
chat_id = "YOUR TELEGRAM CHAT ID"
while 1: #to make sure user enters a number
    try:
        coin_code = int(input("Whats the Code of the Coin you'd like to Get Notified About? "))
        break
    except:
        print("Value must be a number!")
        continue
    else: break

while 1: #to make sure user enters a number
    try:
        limit = int(input("At What Price Would You Like to Get Notified? "))
        break
    except:
        print("Value must be a number!")
        continue
    else: break
    
while 1: #to make sure user enters a number
    try:
        time_interval = int(input("How Often Would You Like us to Chack The Price?(in minutes) ")) * 60
        break
    except:
        print("Value must be a number!")
        continue
    else: break

def get_price(): #Getting the Price of said coin
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest" #Coin Market Cap's api url

    headers = { #setting the headers
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': market_api_key,
    }

    response = requests.get(url, headers=headers).json() #receive the response in json format
    coin_price = response["data"][coin_code]["quote"]["USD"]["price"] #get said coin's price 
    return coin_price #return price

def bot_message(chat_id, message): #send a message to you via telegram
    url = f"https://api.telegram.org/bot{bot_api_key}/sendMessage?chat_id={chat_id}&text={message}" #Telegram's api url to send a message
    requests.get(url) #make the request aka send the message

def main(): #main function to detect if the price of said coin dips below certain price
    while 1:
        price_comp = int(get_price()) #gets the price and converts to integer
        price = "{:,}".format(price_comp) #adds commas
        # print(price)
        if price_comp < limit: #checks if the price is below given limit
            bot_message(chat_id, f"YOUR MESSAGE: ${price}") #if true sends a message
        time.sleep(time_interval) #sleeps for a given amount of time

main() 
    
