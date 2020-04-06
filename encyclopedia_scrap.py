# -*- coding: utf-8 -*-
import requests, json
from bs4 import BeautifulSoup

############### Get Passengers list ###############

# urls = []
# for url in ['https://www.encyclopedia-titanica.org/titanic-first-class-passengers/', 
#             'https://www.encyclopedia-titanica.org/titanic-second-class-passengers/',
#             'https://www.encyclopedia-titanica.org/titanic-third-class-passengers/']:
#     urls += [
#         a['href'] for a in BeautifulSoup(requests.get(url).text, 'html.parser').
#         find('table', attrs={'id':'manifest'}).
#         find_all('a', attrs={'itemprop':'url'})
#     ]
# print(len(urls))

# with open('scrap/json/passengers.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(urls))

##################################################
