from READABILLITY import requst
from READABILLITY import parser

#Http запрос
def main(url):
   html = requst.get(url, {}, {})
   texts = parser.find(content=html, query=['h1', '', 'text'])
   texts = parser.find(content=html, query=['p', '', 'text'])
   return texts