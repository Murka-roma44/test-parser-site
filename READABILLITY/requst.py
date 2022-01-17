from urllib.request import Request #Расширяемая библиотека для открытия URL-адресов
from urllib.request import urlopen #Расширяемая библиотека для открытия URL-адресов
from urllib.parse import urlencode #Разбор URL-адреса на компоненты

def get(url, payload, headers):
    payload = urlencode(payload)
    
    # создание url адреса
    url = url + '?' + payload
    
    # сделать запрос без налиция ошибок
    try:
        # создать объект запроса
        request = Request(url=url, headers=headers, method='GET')
        
        # объект ответа
        response = urlopen(request)
    
        # возвращаемый HTML-контент
        return response.read().decode('utf-8')
    # вернуть ошибку если запрос не вернулся
    except Exception as e:
        print('Request ERROR:', e)
        
        # возвращайте пустое содержимое
        return 'Контент недоступен!'