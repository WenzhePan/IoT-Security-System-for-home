import bs4.element
import requests
from bs4 import BeautifulSoup
import pymysql
from selenium import webdriver


class Movie:

    def __init__(self):
        self.driver = webdriver.chrome()
        self.url = "https://pwa.blinker.app/device/C4ABBDA29LQ7"
        self.header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.db = pymysql.connect(host='127.0.0.1', port=3306, database='django_mysql', user='root', password='root')
        EVA_date = ""
        EVA_rank = 0
        EVA_Weekend=0
        EVA_To_Date=0
        EVA_ID = 0

    def GetData(self):

        req = requests.get(self.url, headers=self.header)
        soup = BeautifulSoup(req.text, features="lxml")
        div = soup.find('div', attrs={'class': 'numbox'})
        num = 0
        print(div)
        value = soup.select('body > app-root > ion-app > ion-router-outlet > app-device > ion-content > layouter2 > div:nth-child(2) > gridster > '
                            'gridster-item:nth-child(31) > widget-dynamic > widget-number > div > div > div.valuebox > span.value')
        # for span in div.find_all('span'):
        #     if isinstance(span,bs4.element.Tag):
        #         num=num+1
        print(value)
        # for i in range(1, num):
        #     j=div.find_all('tr')[i]
        #     EVA_ID = i
        #     EVA_date = j.find_all('td')[0].text.replace(" ",'')
        #     EVA_rank = j.find_all('td')[1].text
        #     EVA_Weekend = j.find_all('td')[2].text.replace('$', '').replace(',', '')
        #     EVA_To_Date = j.find_all('td')[7].text.replace('$', '').replace(',', '')
        #     print(EVA_date,EVA_rank,EVA_Weekend,EVA_To_Date,EVA_ID)
        #
        #     cursor = self.db.cursor()
        #     cursor.execute("insert ignore into echarts_eva values('%s','%d','%d','%d','%d')" % (
        #         str(EVA_date), int(EVA_rank), int(EVA_Weekend), int(EVA_To_Date), int(EVA_ID)
        #     ))
        #     self.db.commit()

        # td = tr.find_all('td')[0].text
        # for r in tr:
        #     td = r.find_all('td')
        #     EAV_date = td[0].text.replace(' ', '')



    def SaveData(self):
        pass


if __name__ == "__main__":
    movie = Movie()
    movie.GetData()
