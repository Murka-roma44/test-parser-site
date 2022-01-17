#подключение библиотек
import settings
from READABILLITY import newlines
import os

# url='https://lenta.ru/news/2021/08/16/zohvat/'
url = str(input('Введите url сайта: '))
#получаем путь
adrres_record = url.replace("https://", "")
adrres_record = adrres_record.replace("https://", "")
#проверяем последний символ для создания директории
if adrres_record[-1:]=='/':
   adrres_record=adrres_record[:-1]
#создание директории
try:
    os.makedirs(adrres_record)
except OSError:
    print ("this directory has already been created")
#получаем текст по заданным настройкам
texts= settings.main(url)
#создаем и открываем для записи файл
f = open(adrres_record+'/text.txt', 'w')
# записываем отсортированный список ссылок, каждая с новой строки
for i in texts:
    f.write(i)
# закрываем файл
f.close()
#открываем файл для записи
f = open(adrres_record+'/index.txt', 'w')
#xbnftv файл построчно
with open(adrres_record+'/text.txt', "r") as file:
    for line in file:
        #разбиваем по 80 символов в строке
        text = newlines.insert_newlines(line)
        f.write(text)
#удаляем файл
if os.path.isfile(adrres_record+'/text.txt'): 
    os.remove(adrres_record+'/text.txt') 
    print("success") 
else: 
    print("File doesn't exists!")

f.close()