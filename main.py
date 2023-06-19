import requests
from bs4 import BeautifulSoup
import re

url = "https://testmoa.com/korea-mbti-statistics/#hangug_MBTI_biyul"

response = requests.get(url)

mbti = []

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('#post-3691 > div > div.dynamic-entry-content > figure > table > tbody >tr')

    for row in title:
        text = row.get_text(' ', strip=True).split()
        mbti.append((text[1], re.sub(r'[^0-9]', '', text[-1])))

else:
    print(response.status_code)

print(mbti)