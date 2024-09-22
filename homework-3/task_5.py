from forex_python.bitcoin import BtcConverter
from datetime import datetime

"""
(*) დაწერეთ პროგრამა რომელიც მიიღებს წელს, თვეს და დღეს, 
როცა მომხმარებელმა იყიდა ბიტკოინი, 
ასევე მიიღებს დოლარში თანხას, 
რომელიც შემოყვანილ თარიღში გადაიხადა ბიტკოინის შესაძენად და 
ეკრანზე გამოიტანს დოლარში თანხას რომელიც მოიგო ან დაკარგა 
დღევანდელი ფასის გათვალისწინებით. 
იხ module forex-pytho
"""
bitcoin_converter = BtcConverter()
date_input_of_purchased_bitcoin = input("enter the date (DD.MM.YYYY) of purchased bitcoins :")
bitcoin_parchase_ammount = float(input("Amount of money paid for Bitcoin $: (eg.10)"))

# input - ის კონვერტაცია datetime object- ში.
date_obj = datetime.strptime(date_input_of_purchased_bitcoin, '%d.%m.%Y')
print("data obj:", date_obj)
# 1 ბიტკოინის ღირებულება მითითებულ თარიღში
bitcoin_price_on_date = bitcoin_converter.get_previous_price('USD', date_obj)
print("price on date :", bitcoin_price_on_date)
# 1 ბიტკოინის ღირებულება დღევანდელ დღეს
if bitcoin_price_on_date is None:
  print(f"Sorry, no Bitcoin price data available for {date_input_of_purchased_bitcoin}. Please try a different date.")
else:
   bitcoin_price_today = bitcoin_converter.get_latest_price("USD")
# გადახდილი თანხის რაოდენობის მიხედვით შეძენილი ბიტკოინების რაოდენობა
   amount_of_bitcoin = bitcoin_parchase_ammount / bitcoin_price_on_date
# შეძენილი ბიტკოინის ამჟამინდელი ღირებულება
   current_value_of_bitcoin = amount_of_bitcoin * bitcoin_price_today

   if current_value_of_bitcoin > bitcoin_parchase_ammount:
      print("YOU WIN")
   else:
      print("YOU LOSE")
 