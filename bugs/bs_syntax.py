from bs4 import BeautifulSoup
import requests
'''
    BeautifulSoup 은 HTML 이나 XML 에서 데이터를 추출하는 파이썬 라이브러리
'''
base_url = 'http://dh.aks.ac.kr/Encyves/wiki/index.php/%EC%A1%B0%EC%84%A0_%EC%84%B8%EC%A2%85'
con = requests.get(base_url)
soup = BeautifulSoup(con.content, 'lxml')
# print(soup)
infoTable = soup.find("table",{"class":"wikitable sortable"})
infoPrint = []
for i in infoTable.find_all('tr'):
    infolist = []
    for j in i.find_all('td'):
        info = j.get_text()
        infolist.append(info)
    infoPrint.append(infolist)
print(infoPrint)
'''
    a.get('href')   태그 a 에서 href 속성의 값(하이퍼링크 url) 추출하기
    soup.title.name  title 태그의 이름 title 추출하기
    soup.title.string   title 태그의 문자값 추출하기
    soup.['class']  클래스 추출
    soup.find(id = 'link')   아이디가 link 인 태그와 값 추출
'''