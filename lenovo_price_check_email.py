import requests as rq
from bs4 import BeautifulSoup
import smtplib


def get_price():
    url = 'https://www.lenovo.com/ca/en/laptops/ideapad/ideapad-700-series/IdeaPad-Slim-7-14IIL05/p/88IPS701399'
    # Replace 'insert' with personal user agent details
    #agent = {'User-Agent': 'insert'}
    page = rq.get(url, headers = agent).text
    soup = BeautifulSoup(page, 'lxml')

    try:
        price_1 = soup.find_all(class_ = 'tabbedBrowse-productListing-container only-allow-small-pricingSummary',producttype = 'NemoMTMVariantProduct')
        price_2 = price_1[len(price_1) - 1].find(class_ = 'saleprice pricingSummary-details-final-price').text
        clean_price = float(price_2.strip()[1:].replace(",",""))
    except:
        price = 0

    if clean_price < 1200:
        send_email(clean_price)

def send_email(money):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Replace 'inserts' with personal username and password - (password auto-generated to surpass 2 factor authentication)
    #server.login('insert', 'insert')

    subject = "Check the Price of the Lenovo Slim 14 You Want!"
    body = "The price has fallen below $1,2000. \n\nCheck https://www.lenovo.com/ca/en/laptops/ideapad/ideapad-700-series/IdeaPad-Slim-7-14IIL05/p/88IPS701399 \n\n the price is now $"  + str(money)

    msg = f"Subject: {subject}\n\n{body}"

    # Replace 'inserts' with sending email and to email
    #server.sendmail('insert', 'insert', msg)
    server.quit()

get_price()
