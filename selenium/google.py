from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("C:/Users/Administrator/chromedriver_win32/chromedriver")
driver.get('https://www.google.com/')
# ID 로 태그 검색하기
# search_bar = driver.find_element_by_id('lst-ib')
search_bar = driver.find_element_by_css_selector("input[title='검색']")
# 데이터 값 삽입
search_bar.send_keys('스크랩핑 대상')
# form 을 전송한다

search_bar.submit()
sleep(10) # 10 간 대기
driver.close()

