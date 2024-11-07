import requests
from bs4 import BeautifulSoup


# Функція для парсингу сторінки
def parser(url: str):
    res = requests.get(url=url)
    soup = BeautifulSoup(res.text, features="lxml")

    # Отримуємо всі продукти на сторінці
    products = soup.find_all(name="div", class_="product-layout product-list item")

    # Проходимо по кожному продукту та отримуємо його назву та ціни
    for product in products:
        # Знаходимо назву товару
        name_tag = product.find("div", class_="item-description")
        if name_tag:
            name = name_tag.text.strip()
            print(f"Назва товару: {name}")

        price_tag = product.find("span", class_="price")
        if price_tag:
            price = price_tag.text.strip()
            print(f"Ціна: {price}")
        else:
            print("Ціна не знайдена")



if __name__ == "__main__":
    parser(url="https://vitals.ua/sadovo-parkovaya-tehnika/benzopily-tsepnyye/")
