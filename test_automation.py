from playwright.sync_api import sync_playwright


def test_web():
    with sync_playwright() as p:
        #Запуск браузера
        browser = p.chromium.launch(headless=False)  # headless=False для визуального режима
        page = browser.new_page()

        #Открытие страницы
        try:
            page.goto("https://www.figma.com/", wait_until="networkidle")
            print("Страница загружена")
        except Exception as e:
            print(f"Ошибка загрузки страницы: {e}")
            browser.close()
            return

        #Проверка заголовка
        try:
            assert "figma" in page.title().lower(), f"Заголовок не содержит 'figma'. Актуальный: {page.title()}"
            print(f"Заголовок содержит 'figma': {page.title()}")
        except AssertionError as e:
            print(f"{e}")

        #Поиск и клик по ссылке
        try:
            link = page.locator("header >> text=Pricing").first

            if link.count() == 0:
                raise Exception("Элемент не найден")

            link.click()
            print("Успешный клик по 'Pricing'")
        except:
            print("Не удалось кликнуть по 'Pricing'")
            browser.close()
            return

        #Проверка URL после клика
        try:
            page.wait_for_url("https://www.figma.com/pricing/", wait_until="networkidle")
            print("Перенаправление на https://www.figma.com/pricing/")
        except:
            print(f"Неверный URL после клика. Актуальный URL: {page.url}")

        #Закрытие браузера
        browser.close()



if __name__ == "__main__":
    test_web()