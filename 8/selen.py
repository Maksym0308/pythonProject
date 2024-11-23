import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def parse():
    driver = webdriver.Chrome()
    max_page = 2

    wait = WebDriverWait(driver, 10)
    result = []

    for page in range(1, max_page + 1):
        driver.get(f'https://jobs.marksandspencer.com/job-search?country%5B0%5D=United%20Kingdom&page={page}')

        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ais-Hits-item')))

        jobs = driver.find_elements(By.CLASS_NAME, 'ais-Hits-item')

        for job in jobs:

                url = job.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')

                title = job.find_element(By.CSS_SELECTOR, 'h3').text

                result.append({
                    'title': title,
                    'url': url
                })


    driver.quit()

    with open('result.json', 'w') as f:
        json.dump(result, f, indent=4)



if __name__ == '__main__':
    parse()
