import requests
from bs4 import BeautifulSoup
import re

url = "https://testmoa.com/korea-mbti-statistics/#hangug_MBTI_biyul"

response = requests.get(url)

mbti = []
def check_value(x,check_list) :
    total = 0
    for i in check_list :
        if x.upper() in i[0] :
            total+= int(i[1])
    return total
def check_two_value(x,y,check_list) :
    total = 0
    for i in check_list :
        if x.upper() in i[0] and y.upper() in i[0] :
            total+= int(i[1])
    return total

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('#post-3691 > div > div.dynamic-entry-content > figure > table > tbody >tr')

    for row in title[1:]:
        text = row.get_text(' ', strip=True).split()
        mbti.append((text[1], re.sub(r'[^0-9]', '', text[-1])))

else:
    print(response.status_code)

print(check_value('i',mbti))
print(check_value('e',mbti))

print(check_value('t',mbti))
print(check_value('f',mbti))

print(check_two_value('e','f',mbti))
print(check_two_value('e','t',mbti))

print(check_two_value('i','f',mbti))
print(check_two_value('i','t',mbti))
