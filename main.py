import requests
from bs4 import BeautifulSoup

url = "https://testmoa.com/korea-mbti-statistics/#hangug_MBTI_biyul"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('#post-3691 > div > div.dynamic-entry-content > figure > table > tbody >tr')

    for row in title:
        text = row.get_text(' ', strip=True)
        print(text)

else:
    print(response.status_code)
