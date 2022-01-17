from html.parser import HTMLParser #библиотека Простой HTML и XHTML парсер
#Анализатор HTML
class MyHTMLParser(HTMLParser):

   #переменная запроса
   query = []
   #переменая совпадения результатов поиска
   match = {}
   #переменная список результатов
   results=[]

   #объявление конца тега
   end_tag=''
   def handle_starttag(self, tag, attr):
      self.match['name'] = tag
      self.match['attr'] = attr
      try:
         if tag == self.query[0]:
            self.end_tag=tag
      except:
         pass

   def handle_data(self, data):
      #запрос по тегу
      tag = self.query[0]

      #запрос по атрибуту
      attr = self.query[1]

      #вывод запроса
      text = self.query[2]

      link = ''
      new_data = ''
      #фильтр по имени тега
      try:
         #проверка имини тега
         if self.end_tag==tag:
            self.results.append(data)
            if self.match['name']=='a':
               href='href'
               #цикл по списку атрибутов
               for item in self.match['attr']:
                  #иницилизация атрибутов
                  key = item[0]
                  val = item[1]

                  #если запрос в пределах запрашеваемого атрибута
                  if href == key:
                     link = ' ['+val+']'
               self.results.append(link)

      except :
         pass

   def handle_endtag(self, tag):
      #сбросить результат после сопоставления закрывающего тега
      self.match={}
      try:
         if tag == self.end_tag:
            self.end_tag=''
            self.results.append('\n\n')
      except:
         pass

def find(content, query):
   #объявление функции парсера
   parser = MyHTMLParser()

   #объявление переменной запроса
   parser.query = query

   #результаты совподения
   parser.feed(content)

   #закрытие парсера
   parser.close()


   #возвращаем результат
   return parser.results
