from bs4 import BeautifulSoup
import requests
import time
url1 = "https://www.google.com/finance/quote/BTC-TRY"
sayfa1 = requests.get(url1)
html_sayfa1 = BeautifulSoup(sayfa1.content,features="lxml")
btc = html_sayfa1.find("div",class_="YMlKec fxKbKc").getText()
print(btc)
eskihesap = btc
time.sleep(150)

url1 = "https://www.google.com/finance/quote/BTC-TRY"
sayfa1 = requests.get(url1)
html_sayfa1 = BeautifulSoup(sayfa1.content)
btc2 = html_sayfa1.find("div",class_="YMlKec fxKbKc").getText()
print(btc2)
yenihesap = btc2



cleaned_yenihesap = yenihesap.replace(",", "").strip() 
cleaned_eskihesap = eskihesap.replace(",", "").strip()
cleaned_yenihesap = float(cleaned_yenihesap)
cleaned_eskihesap = float(cleaned_eskihesap)
print(cleaned_eskihesap)
print(cleaned_yenihesap)
 # Remove commas from new price
if (cleaned_yenihesap > cleaned_eskihesap +5.00):
    print("arttı")
elif (cleaned_yenihesap < cleaned_eskihesap -5.00):
    print("azaldı")
else:
    
    print("50 değerinde değişmedi(eşit)")



          
