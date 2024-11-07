import requests
from bs4 import BeautifulSoup
import pandas as pd


# Функція для збору посилань на категорії
def get_category_links(base_url):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Отримуємо всі посилання на категорії
    categories = soup.find_all('div', class_='subcategory-item with-children')

    if not categories:
        print(f"Не знайдено жодної категорії на сторінці: {base_url}")
        return []

    # Збираємо посилання на категорії
    category_links = [category['href'] for category in categories]

    print(f"Знайдено {len(category_links)} категорій.")
    return category_links


# Функція для збору посилань на підкатегорії
def get_subcategory_links(category_url):
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Отримуємо всі посилання на підкатегорії
    subcategories = soup.find_all('a', class_='subcategory-item with-children')

    if not subcategories:
        print(f"Не знайдено жодної підкатегорії на сторінці: {category_url}")
        return []

    # Збираємо посилання на підкатегорії
    subcategory_links = [subcategory['href'] for subcategory in subcategories]

    print(f"Знайдено {len(subcategory_links)} підкатегорій у категорії: {category_url}")
    return subcategory_links


# Функція для збору посилань на товари з підкатегорій
def get_product_links(subcategory_url):
    response = requests.get(subcategory_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Збираємо посилання на кожен товар
    product_items = soup.find_all('a', class_='product-layout product-list item')

    if not product_items:
        print(f"Не знайдено жодного товару на сторінці: {subcategory_url}")
        return []

    # Збираємо посилання на товари
    product_links = [product['href'] for product in product_items]

    print(f"Знайдено {len(product_links)} товарів у підкатегорії: {subcategory_url}")
    return product_links


# Функція для збору інформації з картки товару
def parse_product_page(product_url):
    response = requests.get(product_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Отримуємо назву товару
    name_tag = soup.find("h1", class_="product-title")
    name = name_tag.text.strip() if name_tag else "Назва не знайдена"

    # Отримуємо нову (акційну) ціну товару
    price_new_tag = soup.find("span", class_="price-new")
    price_new = price_new_tag.text.strip() if price_new_tag else "Немає акційної ціни"

    # Отримуємо стару ціну товару (якщо є)
    price_old_tag = soup.find("span", class_="price-old")
    price_old = price_old_tag.text.strip() if price_old_tag else "Немає старої ціни"

    return {"Назва товару": name, "Акційна ціна": price_new, "Стара ціна": price_old}


# Основна функція для запуску парсера
def main():
    base_url = "https://vitals.ua/product-categories/"
    category_links = get_category_links(base_url)

    if not category_links:
        print("Не вдалося знайти жодних категорій.")
        return

    product_data = []

    # Проходимо по всіх категоріях
    for category_url in category_links:
        print(f"Парсинг категорії: {category_url}")
        subcategory_links = get_subcategory_links(category_url)

        if not subcategory_links:
            print(f"Не вдалося знайти підкатегорій у категорії {category_url}")
            continue

        # Проходимо по всіх підкатегоріях
        for subcategory_url in subcategory_links:
            print(f"Парсинг підкатегорії: {subcategory_url}")
            product_links = get_product_links(subcategory_url)

            if not product_links:
                print(f"Не вдалося знайти товарів у підкатегорії {subcategory_url}")
                continue

            # Проходимо по всіх товарах у підкатегорії
            for product_url in product_links:
                print(f"Парсинг товару: {product_url}")
                product_info = parse_product_page(product_url)
                product_data.append(product_info)

    # Зберігаємо зібрані дані в Excel
    if product_data:
        df = pd.DataFrame(product_data)
        df.to_excel("product_data.xlsx", index=False)
        print("Дані збережено у файл 'product_data.xlsx'")
    else:
        print("Не вдалося зібрати жодних товарів.")


if __name__ == "__main__":
    main()



