
import requests
import re

def post_content():
    url = 'https://www.lejobadequat.com/emplois?'
    payload = {
        "action": "facetwp_refresh",
        "data": {
            "facets": {
                "recherche": [],
                "ou": [],
                "type_de_contrat": [],
                "fonction": [],
                "load_more": [4]
            },
            "frozen_facets": {
                "ou": "hard"
            },
            "http_params": {
                "get": [],
                "uri": "emplois",
                "url_vars": []
            },
            "template": "wp",
            "extras": {
                "counts": True,
                "sort": "default"
            },
            "soft_refresh": 1,
            "is_bfcache": 1,
            "first_load": 0,
            "paged": 4
        }
    }

    # Виконуємо POST-запит
    response = requests.post(url, json=payload)
    print(response.status_code)

    # Перевіряємо статус запиту
    if response.status_code == 200:
        # Парсимо JSON-відповідь
        try:
            data = response.json()
            # Витягуємо HTML з JSON
            html_content = data.get("template", "")
            return html_content
        except ValueError:
            print("Не вдалося обробити JSON.")
            return None
    else:
        print("Помилка запиту:", response.status_code)
        return None

def extract_job_titles(html):
    # Регулярний вираз для пошуку назв вакансій
    pattern = r'>([A-Za-zÀ-ÿ\s\-/]+ H/F)<'
    job_titles = re.findall(pattern, html)
    return job_titles

def main():
    # Отримуємо HTML-контент з POST-запиту
    html_content = post_content()

    if html_content:
        # Витягуємо назви вакансій
        job_titles = extract_job_titles(html_content)
        print(job_titles)

if __name__ == '__main__':
    main()
