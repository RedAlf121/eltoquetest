from bs4 import BeautifulSoup
import requests
from config import *
def get_money_table(response):
    soup = BeautifulSoup(response.text,PARSER)
    table_money = soup.find("table",class_="table")
    money_splitted = table_money.text.split("1 ")
    return money_splitted

def initialize():
    headers = {
    "user-agent": USER_AGENT
    }

    response = requests.get(URL,headers=headers)
    return response