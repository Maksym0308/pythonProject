from bs4 import BeautifulSoup
import requests
import json


def parse_html():
    url = 'https://www.bbc.com/sport'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'lxml')

    cards = soup.find_all('div', {'data-testid': 'promo'}, limit=5)
    urls = []

    for card in cards:
        link = card.find('a', href=True)
        if link:
            url = 'https://www.bbc.com' + link['href']
            urls.append(url)

    return urls


def parsed_pag(url: str) -> dict:
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    response = requests.get(url, headers={'User-Agent': user_agent})

    soup = BeautifulSoup(response.text, 'lxml')
    topics = soup.find_all('a', class_='ssrcss-1ef12hb-StyledLink ed0g1kj0')
    topic_texts = [topic.text.strip() for topic in topics]

    return {'link': url, 'Topics': topic_texts}


def parse_sync():
    urls = parse_html()
    results = []
    for url in urls:
        print(url)
        result = parsed_pag(url)
        if result:
            results.append(result)


    with open('bbc_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    parse_sync()
