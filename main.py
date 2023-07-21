import requests
from bs4 import BeautifulSoup

url = 'https://nobl.ru/sostav-pravitelstva-nizhegorodskoj-oblasti/'
headers = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cache-Control': 'max-age=0',
    # 'Cookie': 'srv_id=kJ-yl7XZtd3W_Hlx.syzpFuy0DV9gHIhxYxAgzaxT9PPuwMfUaMV_3FsIoBnrjTdl-OFcV8q72yWEq4BEUwxq.oCukT7NcGFR5vcwIaOQOOv-K8GS5ANtMUio36gUbJxo=.web; gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; u=2xzn26jv.ot98fb.1ciu26wvvlc00; v=1689623051; buyer_laas_location=640860; luri=nizhniy_novgorod; buyer_location_id=640860; sx=H4sIAAAAAAAC%2FwTAQQ6CMBQE0LvM2kVJYX6nt4H2V42LShqJhnB33wmSLNXYRC2cKbfNo6otoRSrQj5xIKONfk%2FreLbjG%2FWaPu8t7PHR%2Brr38XPHDY48McmCZqbr%2BgcAAP%2F%2Fffl%2BaVsAAAA%3D; dfp_group=31; abp=0; _gcl_a…pHtR1Rxv4gfKQavGsD"; tmr_detect=0%7C1689623066351; adrdel=1; adrcid=Ag-h_1548ZC8f3l3Y0KFqWQ; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyV2VkJTJDJTIwMTclMjBKdWwlMjAyMDI0JTIwMTklM0E0NCUzQTI4JTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnVmcCU1QyUyMiUzQSU1QyUyMjkxNDQ1NWMyOTY2MzA2ZDUzNzkxMWM5NTJhZjk5NDVjJTVDJTIyJTJDJTVDJTIyYnJvd3NlclZlcnNpb24lNUMlMjIlM0ElNUMlMjIxMTUuMCU1QyUyMiU3RCUyMiU3RA==',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'
}


# req = requests.get(url, headers)
#
# with open('index.html', 'w') as file:
#     file.write(req.text)
with open('index.html') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')
blocks = soup.find_all('div', class_='cabinet-list-item')
# 1 и 2 этаж
# for block in blocks:
#     name = block.find('a', class_='placeman-info__name link-hover').text.strip()
#     post = block.find('div', class_='placeman-info__position').text.strip()
#     print(f"ФИО: {name}\nДолжность: {post}")
# 3ий этаж
blocks_count = 0
for block in blocks[0:2]:
    name = block.find('a', class_='placeman-info__name link-hover').text.strip()
    post = block.find('div', class_='placeman-info__position').text.strip()
    print(f"ФИО: {name}\nДолжность: {post}")

    try:
        sub_block = block.find('div', class_='cabinet-list-item__inside _height-null js-common-collapse__item__toggle-container')

        persons = sub_block.find_all('div', class_='placeman')
        #print(persons)
        for person in persons:
            person_name = person.find('div', class_='placeman-container').find('a').text
            person_href = 'https://nobl.ru' + person.find('div', class_='placeman-container').find('a').get('href')
            person_post = person.find('div', class_='placeman-info__position').text
            person_photo = 'https://nobl.ru' + person.find('div', class_='placeman-photo').find('picture').find('img').get('data-src')
            print(f'Имя: {person_name}\nДолжность: {person_post}\nСсылка: {person_href}\nФото: {person_photo}')

    except Exception:
        print('NO SUB_BLOCK')
