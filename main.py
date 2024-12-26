from web_scrap import *

def create_dictionary(moneys):
    coin_dictionary = dict()
    for i in moneys:
        coin,ammount = i[:3],i[3:].split(" CUP")[0]
        coin_dictionary[coin]=float(ammount)
    return coin_dictionary

if __name__ == "__main__":
    response = initialize()
    try:
        response.raise_for_status()
        moneys = get_money_table(response)[1:]
        coin_dictionary = create_dictionary(moneys)
        print(coin_dictionary)
        print(f"El dolar esta en 1 USD = {coin_dictionary['USD']} CUP")
    except Exception as e:
        print(e.with_traceback())