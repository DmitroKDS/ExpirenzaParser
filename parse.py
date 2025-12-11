from bs4 import BeautifulSoup

def boxes_ios(xml_source):
    soup = BeautifulSoup(xml_source, 'lxml-xml') 

    boxes = []

    cells = soup.find_all('XCUIElementTypeCell')
    print(soup)

    for cell in cells:
        sold_status = cell.find('XCUIElementTypeStaticText', {
            'value': 'Розпродано'
        })
        remain_status = cell.find('XCUIElementTypeStaticText', {
            'value': lambda name: name and 'Залишилось' in name
        })

        box = {
            "name": cell.find('XCUIElementTypeStaticText', {
                        'value': lambda name: name and 'Бокс від' in name
                    })['value'],
            "delivery_time": cell.find('XCUIElementTypeStaticText', {
                        'value': lambda name: name and 'Сьогодні з' in name
                    })['value'],
            "status": 'Розпродано' if sold_status else remain_status['value'],
            "sale_price": None,
            "real_price": None
        }

        # Обробка цін
        prices = cell.find_all('XCUIElementTypeStaticText', {
            'value': lambda name: name and '₴' in name
        })
        clean_price = lambda p: int(''.join(filter(str.isdigit, p)))
        try:
            if prices:
                box['sale_price'] = clean_price(prices[0])
                if len(prices) > 1:
                    box['real_price'] = clean_price(prices[1])
        except ValueError:
            pass


        boxes.append(box)

    return boxes


def boxes_android(xml_source):
    soup = BeautifulSoup(xml_source, 'lxml-xml')

    boxes = []

    candidates = soup.find_all('android.view.View', {'class': 'android.view.View'})

    for cell in candidates:
        textviews = cell.find_all('android.widget.TextView')
        if not textviews:
            continue

        texts = [tv.get('text', '').strip() for tv in textviews if tv.get('text')]
        if not any('₴' in t for t in texts):
            continue  # Пропускаємо непотрібні

        box = {
            "name": next((t for t in texts if 'Бокс від' in t), None),
            "delivery_time": next((t for t in texts if 'Сьогодні з' in t), None),
            "status": 'Розпродано' if 'Розпродано' in texts else next((t for t in texts if t.startswith('Залишилось')), None),
            "sale_price": None,
            "real_price": None
        }

        # Обробка цін
        prices = [t for t in texts if '₴' in t]
        clean_price = lambda p: int(''.join(filter(str.isdigit, p)))
        try:
            if prices:
                box['sale_price'] = clean_price(prices[0])
                if len(prices) > 1:
                    box['real_price'] = clean_price(prices[1])
        except ValueError:
            pass

        boxes.append(box)

    return boxes