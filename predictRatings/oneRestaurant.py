from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-software-rasterizer')
# 추가
# chromedriver_path = os.path.join(os.getcwd(), 'chromedriver.exe')
# service = webdriver.chrome.service.Service(chromedriver_path)
# review_driver = webdriver.Chrome(service=service, options=chrome_options)
 
review_driver = webdriver.Chrome(options=chrome_options)
url = input()
review_driver.get(url+"/review/visitor")
time.sleep(2)


# "더보기" 버튼 클릭하기
while True:
    try:
        more_button = review_driver.find_element(By.CSS_SELECTOR, '.lfH3O')
        if more_button.text == "접기":
            break
        if more_button.is_enabled():  # 더보기 버튼의 클래스명
            more_button.click()
            time.sleep(1)

    except Exception as e:
        
        break
print("더보기 끝")
#find_elements 찾기로 진행
review_text_crawl_list = review_driver.find_elements(By.CLASS_NAME, "zPfVt")
reviews = []
# find element's' 메 소드를 통해 가져온 내용은 리스트로 저장되고, 리스트 타입을 풀어서(for문 사용) 임시 데이터에 모아 두어야 한다
for review_crawl_data in review_text_crawl_list:
    reviews.append(review_crawl_data.text.replace("\n", ""))
result = '|'.join(reviews)
file_name = 'reviews_' + url.replace("https://", "").replace(".", "_").replace("/", "_") + '.txt'
with open(file_name, "w+", encoding="utf-8") as file:
    file.write(result)
# 그 리스트에 저장된 텍스트 (한 식당에 대한 여러 리뷰들)를 한 텍스트 덩어리로 모아(join)줍니다.
review_driver.quit()

import csv
import json
import os
from konlpy.tag import Okt
import csv

# Okt 객체 생성
okt = Okt()

review_path = "./" + file_name
# 감성 사전 파일 경로
sentiment_dict_file = 'C:\Git\potential-carnival\predictRatings\KNU\KnuSentiLex-master\data\SentiWord_info.json'

# 감성 사전 로드
with open(sentiment_dict_file, 'r', encoding='utf-8') as file:
    sentiment_dictionary = json.load(file)
# 결과를 저장할 빈 리스트 생성
reviews_list = []
with open(review_path, 'r', encoding='utf-8') as file:
    for line in file:
        # 각 줄을 파이프 문자 "|"를 기준으로 분리하여 리뷰 리스트 생성
        parts = line.strip().split("|")

        review = parts[1:]  # 첫 번째 요소는 번호이므로 제외
        reviews_list.append(review)

print(reviews_list)

results = []
for i in range(len(reviews_list)):
    print(i,"번째 분석중")

    # 형태소 분석된 결과를 저장할 리스트와 변수 초기화
    analyzed_reviews = []

    # 리뷰들을 형태소 분석하여 리스트에 추가
    for row in reviews_list[i]:
        review = row  # 리뷰 컬럼
        morphs = okt.morphs(review)
        analyzed_reviews.append(morphs)

    # 형태소 분석된 결과를 활용한 감성 점수 계산
    review_Num = len(analyzed_reviews)
    sentiment_score = 0  # 초기 감성 점수
    neg_freq = 0 # 나쁜 말이 나온 수
    neg_val = 0
    pos_freq = 0 # 좋은 말이 나온 수
    pos_val = 0
    review_scores = []
    # 모든 분석된 리뷰들에 대해
    for review in analyzed_reviews:
        # 각 리뷰의 모든 형태소들에 대해
        for morph in review:
            review_score = 0
            # 만약 형태소가 사전에 있다면
            if morph in sentiment_dictionary:

                # 그 극성을 저장하기
                tmp = sentiment_dictionary[morph]
                # 나쁜 형태소가 나온 빈도
                if tmp < 0:
                    neg_freq += 1
                    neg_val += tmp
                # 좋은 형태소가 나온 빈도
                elif tmp > 0:
                    pos_freq += 1
                    pos_val += tmp
                review_score += tmp
                sentiment_score += tmp

            if review_score != 0:
                review_scores.append(review_score)
    # print(review_scores)
    # print('총 감성 점수:', sentiment_score)
    # print("pos: ", pos)
    # print("neg: ", neg)
    results.append((sentiment_score/review_Num, pos_freq/review_Num, pos_val/review_Num, neg_freq/review_Num, neg_val/review_Num))