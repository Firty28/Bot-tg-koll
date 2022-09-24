import requests
from bs4 import BeautifulSoup as BS
import re


headers = {
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

url = ('YOU URL')
html = requests.get(url, headers=headers)
soup = BS(html.content, 'lxml')
info = soup.find_all('tr', align='center')

week = {
    1: 'пн',
    2: 'вт',
    3: 'ср',
    4: 'чт',
    5: 'пт',
    6: 'сб',
    7: 'вс',
}

days_dict = {
    'пн': [],
    'вт': [],
    'ср': [],
    'чт': [],
    'пт': [],
    'сб': [],
    'вс': [],
}

days = 0

for i in range(len(info)):

    str_info = info[i].text.translate(str.maketrans('', '', '\n,\t,\r'))
    str_info = str_info.replace("перенос с 08:00", "")
    str_info = str_info.replace("Очно", "")

    if "№" in str_info:
        days += 1
        continue

    null_list = []
    for item in str_info:
        if item.isupper():
            null_list.append(' ' + item)
            continue
        null_list.append(item)

    null_list_a = ''.join(null_list)
    sss = null_list_a.split(sep='  ')
    null_lists = ' '.join(sss)
    null_list.insert(1, ' ')
    fake_list_items = ''.join(null_list)
    test_2 = fake_list_items

    para = ' '.join(null_lists.split(sep=' ')[:3])[0]

    _kabinet = re.findall(r'\s\d{3}', str_info)

    _name_predmet = re.findall(
        r'Информатика|Химия|Физика|Русский язык|Обществознание|Родной язык|Астрономия|Основы безопасности жизнедеятельности|Математика|Свободное время|Литература|Физическая культура|Иностранный язык|История', str_info)

    info_time = re.findall(r'\d{2}[:]\d{2}\s\S\s\d{2}[:]\d{2}', str_info)
    info_time = ''.join(info_time)
    kabinet = ''.join(_kabinet)
    name_predmet = ''.join(_name_predmet)

    list_items = fake_list_items[2:]
    list_items = list_items.replace(kabinet, '')
    list_items = list_items.replace(name_predmet, '')
    list_items = list_items.replace(info_time, '')
    list_items = list_items.replace('Кабинет:', "")
    name_prepod = list_items.strip()

    sss = name_prepod.split(sep='  ')
    name_prepod = ' '.join(sss)

    # print(f'День: {week[days]}')
    # print(f"\nПара {para}\nКабинет:{kabinet}\nПредмет: {name_predmet}\nВремя: {info_time}\nПреподаватель: {name_prepod}\n")

    info_array = [para, info_time, name_predmet,
                  name_prepod, kabinet, week[days]]

    if info_array[-1] == week[days]:
        days_dict[week[days]].append(info_array)
        if days_dict['вс'] == []:
            days_dict['вс'].append('Выходной')

