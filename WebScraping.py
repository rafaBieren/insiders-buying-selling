from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import ipdb

# החל\חדל להיות בעל עניין בשנת 2022
url_start_stop_position = 'https://maya.tase.co.il/reports/company?q=%7B%22DateFrom%22:%222021-12-31T22:00:00.000Z' \
                          '%22,%22DateTo%22:%222022-12-30T22:00:00.000Z%22,%22events%22:%5B900%5D,' \
                          '%22subevents%22:%5B909,908,903,901,902,911,912,914,905,906%5D,%22Page%22:1,%22QOpt%22:1,' \
                          '%22Q%22:%22%D7%9C%D7%94%D7%99%D7%95%D7%AA%20%D7%91%D7%A2%D7%9C%20%D7%A2%D7%A0%D7%99%D7%99' \
                          '%D7%9F%22%7D '

# שינוי החזקות בעלי עניין ב2022
url_change_position = 'https://maya.tase.co.il/reports/company?q=%7B%22DateFrom%22:%222021-12-31T22:00:00.000Z%22,' \
                      '%22DateTo%22:%222022-12-30T22:00:00.000Z%22,%22QOpt%22:1,%22events%22:%5B900%5D,' \
                      '%22subevents%22:%5B909,908,903,901,902,911,912,914,905,906%5D,%22Page%22:1,' \
                      '%22Q%22:%22%D7%A9%D7%99%D7%A0%D7%95%D7%99%20%D7%94%D7%97%D7%96%D7%A7%D7%95%D7%AA%22%7D '

path = r"C:\Users\repha\OneDrive\שולחן העבודה\python files\chromedriver_win32"


service = Service(path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url_start_stop_position)
loadMoreButton = driver.find_element(By.XPATH, '//button[@class="loadMoreButton ng-binding"]')
loadMoreButton.click()
# print(loadMoreButton)
# elem = driver.find_element(By.NAME, "q")

# ipdb.set_trace()
driver.close()
# driver.quit()