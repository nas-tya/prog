# Вариатиная самостоятельная работа № 1. Библиотека requests
Модуль requests — это элегантная и простая HTTP-библиотека для Python, созданная для людей. Модуль позволяет чрезвычайно легко отправлять HTTP/1.1 запросы. Нет необходимости вручную составлять URL-адреса или кодировать данные для PUT и POST запросов.

## Создание HTTP запроса к WEB-странице
Сделать HTTP-запрос очень просто. Сначала необходимо импортировать модуль requests. Далее попробуем запросить контент веб-страницы. Для примера запросим методом GET общедоступную HTTP страницу с временной шкалой сайта GitHub:
```python
import requests
resp = requests.get('https://api.github.com/events')
```
В результате запроса получили объект ответа под названием resp. Далее, из этого объекта можно получить всю необходимую информацию о этой странице.

Простой API запросов означает, что все формы HTTP-запросов столь же очевидны. Например, вот как вы делаете запрос HTTP POST:
```python
import requests
resp = requests.post('https://httpbin.org/post', data = {'key':'value'})
```
Создание других типов HTTP-запросов, таких как PUT, DELETE, HEAD и OPTIONS все это так же просто и очевидно.
```python
import requests
resp_put = requests.put('https://httpbin.org/put', data = {'key':'value'})
resp_del = requests.delete('https://httpbin.org/delete')
resp_head = requests.head('https://httpbin.org/get')
resp_opt = requests.options('https://httpbin.org/get')
```
При работе с библиотекой requests необходимо помнить следующее: всякий раз, когда вызываются методы requests.get() или requests.post() и т. д., то делаются две важные вещи.
1. Создается объект Request, который будет отправлен на сервер для запроса ресурса указанного в URL .
2. Создается объект Response, который генерируется после того, как запрос получает ответ от сервера.

Объект Response содержит всю информацию, возвращаемую сервером, а также объект запроса, который вы создали изначально

## Код ответа сервера (status code)
Можно проверить код состояния ответа сервера следующим способом:
```python
import requests
resp = requests.get('https://httpbin.org/get')
# статус ответа сервера
resp.status_code
# 200
```
Модуль requests также поставляется со встроенным объектом поиска кода состояния requests.codes для удобства использования:
```python
resp.status_code == requests.codes.ok
# True
```
Если сделан плохой запрос (ошибка клиента 4XX или ответ на ошибку сервера 5XX), то можно поднять его с помощью объекта ответа Response.raise_for_status():
```python
import requests
bad_r = requests.get('https://httpbin.org/status/404')
# статус ответа сервера
bad_r.status_code
# 404

# Поднимаем исключение
bad_r.raise_for_status()
# Traceback (most recent call last):
#   File "requests/models.py", line 832, in raise_for_status
#     raise http_error
# requests.exceptions.HTTPError: 404 Client Error
```
Но если вызвать Response.raise_for_status() для ответа сервера со статусом 200, то в результате получим None:
```python
resp.status_code == requests.codes.ok
# True
resp.raise_for_status()
# None
```

## Получение контента WEB-страницы в виде текста
Извлекать/читать контент/текст ответа сервера также легко как делать запросы. Еще раз рассмотрим временную шкалу GitHub:
```python
import requests
resp = requests.get('https://api.github.com/events')
resp.text
'[{"repository":{"open_issues":0,"url":"https://github.com/...
```
Запросы будут автоматически декодировать содержимое с сервера. Большинство кодировок юникода легко декодируются.

Когда посылается запрос, модуль requests делает обоснованные предположения о кодировке ответа на основе HTTP-заголовков. При доступе к атрибуту resp.text используется кодировка, прочитанная модулем requests во время запроса к серверу. Если сервер не предоставляет кодировку страницы в заголовках ответа или кодировка не распознана, то по умолчанию requests использует кодировку 'utf-8'. Можно узнать, какую кодировку использует конкретный запрос, и изменить ее, используя атрибут resp.encoding:
```python
# просмотр текущей кодировки страницы
resp.encoding
# 'utf-8'

# изменение кодировки страницы
resp.encoding = 'windows-1251'
```
Если изменить кодировку, то запросы будут использовать новое значение resp.encoding всякий раз, когда вызывается resp.text. Бывают случаи, когда заголовок ответа сервера выдает неправильную кодировку (отличную от той которая указана в HTML разметке) и в этой ситуации, необходимо применить специальную логику, чтобы определить, какой будет кодировка контента. Например, языки разметки HTML и XML имеют возможность указывать свою кодировку в своем теле. В подобных ситуациях необходимо использовать resp.content, чтобы найти указанную кодировку, а затем установить resp.encoding. Это позволит извлекать данные HTML-страницы resp.text с правильной кодировкой.

## Получение контента в виде байтов
Можно получить доступ к телу ответа в байтах для нетекстовых запросов, например для загрузки изображений:
```python
# получение контента в виде байтовой строки
resp.content
# b'[{"repository":{"open_issues":0,"url":"https://github.com/...
```
Кодировки gzip и передача-кодировки deflate автоматически декодируются.

Например, чтобы воссоздать изображение из двоичных данных, возвращаемых запросом, можно использовать следующий код:
```python
from PIL import Image
from io import BytesIO
img = Image.open(BytesIO(resp.content))
```

## Отслеживание перенаправлений, атрибут Response.history
По умолчанию модуль requests будет обрабатывать перенаправление для всех типов запросов, кроме HEAD (по умолчанию отключено). Для отслеживания всех перенаправления можно использовать атрибут .history объекта Response.

Список Response.history содержит объекты Response, созданные для выполнения запроса. Список отсортирован от самого старого до самого последнего ответа.

Например, GitHub перенаправляет все HTTP-запросы на HTTPS:
```python
import requests
r = requests.get('http://github.com/')
r.url
# 'https://github.com/'
r.status_code
# 200
r.history
# [<Response [301]>]
```
Если используется запросы GET, OPTIONS, POST, PUT, PATCH или DELETE, то можно отключить обработку перенаправления с помощью аргумента allow_redirects:
```python
import requests
r = requests.get('http://github.com/', allow_redirects=False)
r.status_code
# 301
r.history
# []
```
Если используется HEAD запрос, то также можно включить отслеживание перенаправления:
```python
import requests
r = requests.head('http://github.com/', allow_redirects=True)
r.url
# 'https://github.com/'
r.history
# [<Response [301]>]
```

