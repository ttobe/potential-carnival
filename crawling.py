from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
from selenium.webdriver.common.by import By
from utils import getIntRating
# 크롬 드라이버 옵션 설정
options = Options()
# options.add_argument('--headless')  # 창 숨기기 옵션

# 크롬 드라이버 실행
driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

# 크롤링할 페이지 URL 설정
url = 'https://www.tripadvisor.co.kr/Restaurant_Review-g294197-d1371740-Reviews-Mugyodong_Bugeokukjib-Seoul.html'

# 페이지 열기
driver.get(url)

# 식당 자체에 관한 평점들을 저장하는 배열
restaurant_ratings = []

# 식당의 전체 평점 구하기
rating_element = driver.find_element(By.XPATH, "//span[@class='MFMAn']")
rating = rating_element.find_element(By.CSS_SELECTOR, '.ui_bubble_rating').get_attribute('class')
rating = getIntRating(rating)

restaurant_ratings.append(rating)

# 기준 별 평점 구하기
rating_elements = driver.find_elements(By.XPATH, "//span[@class='vzATR']")

# 각 기준별 평점 출력하기
for rating_element in rating_elements:
    rating = rating_element.find_element(By.CSS_SELECTOR, '.ui_bubble_rating').get_attribute('class')
    rating = getIntRating(rating)
    restaurant_ratings.append(rating)

print('전체 평점:', restaurant_ratings[0])
print('음식:', restaurant_ratings[1])
print('서비스:', restaurant_ratings[2])
print('가격:', restaurant_ratings[3])
print('분위기:', restaurant_ratings[4])

# 페이지가 로드될 때까지 대기
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'review-container')))

# 더보기 버튼 누르기
driver.find_elements(By.CSS_SELECTOR, ".ulBlueLinks")[0].click()
print("더보기 완료")
reviews = driver.find_elements(By.CLASS_NAME, 'review-container')

# 딕셔너리를 저장하는 배열
results = {}
results['test1'] = []

# 각 리뷰의 정보 추출
for review in reviews:
    review_id = review.get_attribute('data-reviewid')
    rating = review.find_element(By.CSS_SELECTOR, '.ui_bubble_rating').get_attribute('class')
    rating = getIntRating(rating)
    review_text = review.find_element(By.CLASS_NAME, 'partial_entry').text
    
    print('Review ID:', review_id)
    print('Rating:', rating)
    print('Review Text:', review_text)
    print('--------------------------')
    d = {"ID" : review_id, "Rating": rating, "Text": review_text}
    results['test1'].append(d)

with open('test.json', 'a', encoding='utf-8') as f:
    json.dump(results, f, indent='\t', ensure_ascii=False)


# 드라이버 종료
driver.quit()
