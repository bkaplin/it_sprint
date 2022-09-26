import tqdm
from bs4 import BeautifulSoup
import requests
import json


sess = requests.Session()
sess.headers.update({
    'location': 'https://spb.hh.ru/',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
})


base_url = 'https://hh.ru/search/vacancy'
query_params = 'text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&' \
               'from=suggest_post&area=1&hhtmFrom=vacancy_search_list'
page_params = '&page={}'
response = sess.get(f'{base_url}?{query_params}')
soup = BeautifulSoup(response.text, 'lxml')
max_page = soup.find(attrs={'data-qa': 'pager-block'}).find_all(attrs={'data-qa': 'pager-page'})[-1].text

print(max_page)

for page in range(int(max_page)):
    response = sess.get(f'{base_url}?{query_params}&{page_params.format(page)}')

    soup = BeautifulSoup(response.text, 'lxml')
    links = soup.find_all(attrs={'data-qa': 'serp-item__title'})
    data = {
        'data': []
    }

    for link in tqdm.tqdm(links):
        title = link.text
        item_url = link.attrs.get('href')
        if item_url:
            item_response = sess.get(item_url)
            item_soup = BeautifulSoup(item_response.text, 'lxml')

            salary = item_soup.find(attrs={'data-qa': 'vacancy-salary-compensation-type-net'})
            region = item_soup.find(attrs={'data-qa': 'vacancy-view-location'})
            experience = item_soup.find(attrs={'data-qa': 'vacancy-experience'})

            data["data"].append({
                "title": title,
                "work_experience": getattr(experience, 'text', ''),
                "salary": getattr(salary, 'text', '').replace(' ', ' '),
                "region": getattr(region, 'text', '').split(',')[0]
            })

            with open('data.json', 'w') as file:
                json.dump(data, file, ensure_ascii=False)
