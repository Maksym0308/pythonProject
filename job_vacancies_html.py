import requests
import re


def get_content():
    url = 'https://www.lejobadequat.com/emplois'
    response = requests.get(url)
    print(response.status_code)
    return response.text



def extract_job_titles(html):

    pattern = r'>([A-Za-zÀ-ÿ\s\-/’]+ H/F)<'
    job_titles = re.findall(pattern, html)
    return job_titles


def main():
    html_content = get_content()
    job_titles = extract_job_titles(html_content)

    print(job_titles)


if __name__ == '__main__':
    main()

