from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

import time
import json
from selenium.webdriver.common.by import By
from utils import getIntRating


def crawling(name, link):
    # 크롬 드라이버 옵션 설정
    options = Options()
    options.add_argument('--headless')  # 창 숨기기 옵션

    # 크롬 드라이버 실행
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()), options=options)

    # 크롤링할 페이지 URL 설정
    url = link

    # 페이지 열기
    driver.get(url)

    # 딕셔너리를 저장하는 배열
    results = {}
    results['reviews'] = []
    results['restaurant_ratings'] = []
    # 식당의 전체 평점 구하기
    rating_element = driver.find_element(By.XPATH, "//span[@class='MFMAn']")
    rating = rating_element.find_element(By.CSS_SELECTOR, '.ui_bubble_rating').get_attribute('class')
    rating = getIntRating(rating)

    results['restaurant_ratings'].append(rating)

    # 기준 별 평점 구하기
    rating_elements = driver.find_elements(By.XPATH, "//span[@class='vzATR']")

    # 각 기준별 평점 출력하기
    for rating_element in rating_elements:
        rating = rating_element.find_element(By.CSS_SELECTOR, '.ui_bubble_rating').get_attribute('class')
        rating = getIntRating(rating)
        results['restaurant_ratings'].append(rating)

    # print('전체 평점:', results['restaurant_ratings'][0])
    # print('음식:', results['restaurant_ratings'][1])
    # print('서비스:', results['restaurant_ratings'][2])
    # print('가격:', results['restaurant_ratings'][3])
    # print('분위기:', results['restaurant_ratings'][4])

    # 리뷰 수 추출
    review_count_element = driver.find_element(By.CLASS_NAME, 'count')
    review_count_text = review_count_element.text

    # 숫자 추출
    review_count = int(review_count_text.strip('()'))

    # 리뷰 수 출력
    print('한국어 리뷰 수:', review_count)

    pages = int(review_count / 10)

    print('돌 페이지 수',pages)
    # 페이지 수
    page_count = 1

    # 리뷰 크롤링
    for i in range(pages):
        # 페이지가 로드될 때까지 대기
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'review-container')))
        print(f'--- Page {page_count} ---')

        # 더보기 버튼 누르기
        try:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ulBlueLinks")))
            more_button = driver.find_elements(By.CSS_SELECTOR, ".ulBlueLinks")[0]
            more_button.click()
        except ElementClickInterceptedException:
            print("더보기 없음")
            pass
        except NoSuchElementException:
            print("더보기 없음")
            pass
        except StaleElementReferenceException:
            continue
        
        
        print("더보기 완료")

        # 리뷰 가져오기
        reviews = driver.find_elements(By.CLASS_NAME, 'review-container')
        time.sleep(3)

        # 각 리뷰의 정보 추출
        for review in reviews:
            # review_id = review.get_attribute('data-reviewid')
            rating = review.find_element(By.CSS_SELECTOR, '.ui_bubble_rating').get_attribute('class')
            rating = getIntRating(rating)
            review_text = review.find_element(By.CLASS_NAME, 'partial_entry').text
            
            # print('Review ID:', review_id)
            # print('Rating:', rating)
            # print('Review Text:', review_text)
            # print('--------------------------')
            # d = {"ID" : review_id, "Rating": rating, "Text": review_text}
            d = { "Rating": rating, "Text": review_text}

            results['reviews'].append(d)

        # 다음 페이지로 이동
        try:
            next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'next')]")
            if not next_button.is_enabled():
                break  # 다음 페이지가 없으면 종료
            next_button.click()
            page_count += 1
        except ElementClickInterceptedException:
            print("끝")
            break

    path = 'Data/reviews/' + name + '.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent='\t', ensure_ascii=False)


    # 드라이버 종료
    driver.quit()
    
