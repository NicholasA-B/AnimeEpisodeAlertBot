import requests
import re
import datetime
import time
import calendar
from bs4 import BeautifulSoup

urls = [
    'https://myanimelist.net/anime/42249/Tokyo_Revengers',
    'https://myanimelist.net/anime/41587/Boku_no_Hero_Academia_5th_Season',
    'https://myanimelist.net/anime/41025/Fumetsu_no_Anata_e'
]

shows = [
    'Tokyo Revengers',
    'My Hero Academia Season 5',
    'To Your Eternity'
]

times = []
days = []


headers = {'User-Agent': 'Chrome'}

def get_time(url):
    req = requests.get(url, headers=headers).text
    soup = BeautifulSoup(req, 'html.parser')
    broadcast = soup.find_all('div', class_='spaceit')
    output = broadcast[2].text
    timestamp = re.findall("\d{2}\:\d{2}", output)[0]
    day = re.findall("\w{3,6}day", output)[0]
    times.append(timestamp)
    days.append(day)

def alert():
    current_day = calendar.day_name[datetime.datetime.today().weekday()]
    current_time = re.findall("^\d{1,2}\:\d{2}", str(datetime.datetime.now().time()))[0]
    # current_day = "Sunday"
    # current_time = "02:08"
    print(f"{current_time}...")
    for i in range(len(shows)): 
        if current_day == days[i].capitalize():
            if current_time == times[i]:
                print(f"New Episode Is Out: {shows[i]}")
    time.sleep(60)

if __name__ == '__main__':
    for url in urls:
        get_time(url)
    while True:
        alert()