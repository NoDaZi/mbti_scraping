import requests
from bs4 import BeautifulSoup
import re

url = "https://testmoa.com/korea-mbti-statistics/#hangug_MBTI_biyul"

response = requests.get(url)
mbti_list = [("I", "E"), ("N", "S"), ("T", "F"), ("P", "J")]
mbti = []


# url 에서 스크래핑 하고,


def check_value(x, check_list):
    total = 0
    for i in check_list:
        if x.upper() in i[0]:
            total += int(i[1])
    return total


def check_two_value(x, y, check_list):
    total = 0
    for i in check_list:
        if x.upper() in i[0] and y.upper() in i[0]:
            total += int(i[1])
    return total


if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('#post-3691 > div > div.dynamic-entry-content > figure > table > tbody >tr')

    for row in title[1:]:
        text = row.get_text(' ', strip=True).split()
        mbti.append((text[1], re.sub(r'[^0-9]', '', text[-1])))  # mbti List (유형 , 인원) 저장

else:
    print(response.status_code)

for i in mbti_list:
    print(i[0], check_value(i[0], mbti))
    print(i[1], check_value(i[1], mbti))
    print()

for i in range(4):
    temp = mbti_list[:i - 4] + mbti_list[i + 1:]  # 해당 유형 분류 제외한 유형 리스트
    print(' ', temp)
    for j in mbti_list[i]:  # j = 대분류 두종류 (첫 번째,두 번째)
        value = [(round(check_two_value(j, a, mbti)/check_value(j, mbti)*100, 2),
                  round(check_two_value(j, b, mbti)/check_value(j, mbti)*100, 2)) for a, b in temp]
        print(j, value)

for i in range(4):
    temp = mbti_list[:i - 4] + mbti_list[i + 1:]  # 해당 유형 분류 제외한 유형 리스트
    print(' ', temp)
    for j in mbti_list[i]:  # j = 대분류 두종류 (첫 번째,두 번째)
        print(j, [(check_two_value(j, a, mbti),check_two_value(j, b, mbti)) for a, b in temp])
