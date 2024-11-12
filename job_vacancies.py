import requests
import re

# Функція для отримання HTML-контенту
def get_content():
    url = 'https://www.lejobadequat.com/emplois'
    response = requests.get(url)
    print(response.status_code)
    return response.text


# Функція для витягування назв вакансій
def extract_job_titles(html):
    # Регулярний вираз для пошуку назв вакансій
    pattern = r'>([A-Za-zÀ-ÿ\s\-/’]+ H/F)<'
    job_titles = re.findall(pattern, html)
    return job_titles

# Основна функція
def main():
    html_content = get_content()
    job_titles = extract_job_titles(html_content)

    print(job_titles)

# Виконуємо код
if __name__ == '__main__':
    main()

