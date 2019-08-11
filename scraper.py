import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.ca/Canon-Rebel-DSLR-Camera-18-55mm/dp/B071K62DPN?ref_=Oct_BSellerC_3322598011_0&pf_rd_p=02895fb2-e445-5884-a92a-7e84f71dcafb&pf_rd_s=merchandised-search-6&pf_rd_t=101&pf_rd_i=3322598011&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_r=RGT83TCF31KTVM8PEFPD&pf_rd_r=RGT83TCF31KTVM8PEFPD&pf_rd_p=02895fb2-e445-5884-a92a-7e84f71dcafb"

headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = int(price[5:8])

    if (converted_price < 600):
        send_email()

    print(title.strip())
    print(converted_price)


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('ahilcar.s@gmail.com', 'xgqmnmpsbthohwvr')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.ca/Canon-Rebel-DSLR-Camera-18-55mm/dp/B071K62DPN?ref_=Oct_BSellerC_3322598011_0&pf_rd_p=02895fb2-e445-5884-a92a-7e84f71dcafb&pf_rd_s=merchandised-search-6&pf_rd_t=101&pf_rd_i=3322598011&pf_rd_m=A3DWYIK6Y9EEQB&pf_rd_r=RGT83TCF31KTVM8PEFPD&pf_rd_r=RGT83TCF31KTVM8PEFPD&pf_rd_p=02895fb2-e445-5884-a92a-7e84f71dcafb'

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'ahilcar.s@gmail.com',
        'ahilcar.s@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()

while(True):
    check_price()
    time.sleep(60*60)