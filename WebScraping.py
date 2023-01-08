import requests
from bs4 import BeautifulSoup

from requests_html import HTMLSession

session = HTMLSession()

# url_change_position = 'https://maya.tase.co.il/reports/company?q=%7B%22DateFrom%22:%222016-12-31T22:00:00.000Z%22,' \
#                       '%22DateTo%22:%222022-12-30T22:00:00.000Z%22,%22QOpt%22:1,%22events%22:%5B900%5D,' \
#                       '%22subevents%22:%5B909,908,903,901,902,911,912,914,905,906%5D,%22Page%22:1,' \
#                       '%22Q%22:%22%D7%A9%D7%99%D7%A0%D7%95%D7%99%20%D7%94%D7%97%D7%96%D7%A7%D7%95%D7%AA%22%7D '

url_start_stop_position = 'https://maya.tase.co.il/reports/company?q=%7B%22DateFrom%22:%222016-12-31T22:00:00.000Z%22,%22DateTo%22:%222022-12-30T22:00:00.000Z%22,%22events%22:%5B900%5D,%22subevents%22:%5B909,908,903,901,902,911,912,914,905,906%5D,%22Page%22:2,%22QOpt%22:1,%22Q%22:%22%D7%9C%D7%94%D7%99%D7%95%D7%AA%20%D7%91%D7%A2%D7%9C%20%D7%A2%D7%A0%D7%99%D7%99%D7%9F%22%7D'


responseStartStopPosition = requests.get(url_start_stop_position)
# responseChangePosition = requests.get(url_change_position)

soup = BeautifulSoup(responseStartStopPosition.text, 'html.parser')
results = soup.find_all('div', attrs={'class': 'feedItemLogoTxt'})

print(len(results))

responseStartStopPosition = session.get(url_start_stop_position)
# responseChangePosition = session.get(URL_CHANGE_POSITION)

print(responseStartStopPosition.html.find('maya-reports.ng-scope.ng-isolate-scope'))
print(responseStartStopPosition.html.text)
# print(responseChangePosition.status_code)
