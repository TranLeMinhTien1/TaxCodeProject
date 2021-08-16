import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse


def get(a):

    link = 'https://masothue.com'

    c=requests.get(link, params=a+'-b')
    if '?' in c.url:
        c.url = c.url.replace('?', '')
    d=requests.get(c.url)
    soup = BeautifulSoup(d.content, "html.parser")
    try:
        company = soup.find('th', {'itemprop': 'name'})
        tax = soup.find('td', {'itemprop': 'taxID'})
        address = soup.find('td', {'itemprop': 'address'})
        situation = soup.find('a', {'title': 'tra cứu mã số thuế công ty Đang hoạt động (đã được cấp GCN ĐKT)'}) or soup.find('a', {'title': 'tra cứu mã số thuế công ty Ngừng hoạt động và đã đóng MST'})
        company = company.text
        tax = tax.text
        address = address.text
        if situation is not None:
            situation =situation.text
            A = [company,  address, situation]
            return A
        else:
            A = [company,  address]
            return A
    except:
        alert =soup.find('p', {'class': 'lead'})
        alert = alert.text
        alert = alert.replace(':(','')
        A =[alert]
        return A