from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import json
import time


def create_driver():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver


def parse_product_modifications(driver, product_url):

    data = []

    driver.get(product_url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product"))
    )

    def extract_data():
        soup = BeautifulSoup(driver.page_source, "html.parser")
        product_data = {}

        # Заголовок
        try:
            product_data["title"] = soup.find("h1", class_="product-title").get_text(strip=True)
        except AttributeError:
            product_data["title"] = None

        # Артикул
        try:
            product_data["article"] = soup.find("div", class_="product-header__code").get_text(strip=True).replace(
                "Артикул:", "").strip()
        except AttributeError:
            product_data["article"] = None

        # Ціна нова
        try:
            product_data["price_new"] = soup.find("div", class_="product-price__item--new").get_text(strip=True)
        except AttributeError:
            product_data["price_new"] = None

        # Ціна стара
        try:
            product_data["price_old"] = soup.find("div", class_="product-price__old-price").get_text(strip=True)
        except AttributeError:
            product_data["price_old"] = None

        # Наявність
        try:
            product_data["availability"] = soup.find("div", class_="product-price__availability").get_text(strip=True)
        except AttributeError:
            product_data["availability"] = None

        return product_data

    # Отримуємо дані про товар
    base_data = extract_data()
    data.append(base_data)

    # Шукаємо модифікацій
    try:
        modifications = driver.find_elements(By.CLASS_NAME, "modification__item")
        for i in range(len(modifications)):

            modifications = driver.find_elements(By.CLASS_NAME, "modification__item")

            modifications[i].click()
            time.sleep(1)

            mod_data = extract_data()

            # Перевірка модифікації на дублі
            if mod_data["article"] != base_data["article"]:
                data.append(mod_data)
    except Exception as e:
        print(f"Помилка під час парсингу модифікацій: {e}")

    return data


def parse_all_products_on_page(driver):

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "catalog__content"))
    )

    data = []


    try:
        product_links = driver.find_elements(By.CLASS_NAME, "catalogCard-image")
        product_urls = [link.get_attribute("href") for link in product_links]

        # Парсимо кожен товар на сторінці
        for product_url in product_urls:
            print(f"Парсимо товар: {product_url}")
            product_data = parse_product_modifications(driver, product_url)
            data.extend(product_data)
    except Exception as e:
        print(f"Помилка під час парсингу товарів на сторінці: {e}")

    return data


def scrape_category_with_dynamic_urls(driver, category_url, max_pages):

    all_data = []

    category_start_time = time.time()

    for page in range(1, max_pages + 1):
        page_url = f"{category_url}filter/page={page}/"
        print(f"Парсимо сторінку {page} категорії: {page_url}")

        try:
            driver.get(page_url)

            # Парсинг усіх товарів на сторінці
            page_start_time = time.time()
            products_data = parse_all_products_on_page(driver)
            all_data.extend(products_data)

            # Вимір часу для сторінки
            page_end_time = time.time()
            print(f"Час на парсинг сторінки {page}: {page_end_time - page_start_time:.2f} секунд")
        except Exception as e:
            print(f"Помилка під час парсингу сторінки {page}: {e}")
            print("Пропускаємо цю сторінку...")
            continue

    # Вимір часу для всієї категорії
    category_end_time = time.time()
    print(f"Час на парсинг категорії: {category_end_time - category_start_time:.2f} секунд")

    return all_data


def main():
    category_url = "https://tokio.com.ua/elektroskutery_classic/"
    max_pages = 4
    driver = create_driver()

    try:
        all_products_data = scrape_category_with_dynamic_urls(driver, category_url, max_pages)
        with open("tokio_all_products.json", "w", encoding="utf-8") as f:
            json.dump(all_products_data, f, indent=4, ensure_ascii=False)
        print("Дані успішно збережено в tokio_all_products.json")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()


