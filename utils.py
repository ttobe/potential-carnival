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
import pandas as pd
import os
def getIntRating(rating):
    rating = str(rating).split("ui_bubble_rating bubble_")
    rating = int(rating[1])
    return rating

def JsonToDic():
    # JSON 감성 사전 파일 경로
    json_file = 'Data/SentiWord_info.json'

    # 변환된 감성 사전을 저장할 변수
    sentiment_dictionary = {}

    # JSON 파일 열기
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        
        # JSON 데이터를 순회하면서 사전에 추가
        for item in data:
            word = item['word']
            polarity = int(item['polarity'])
            sentiment_dictionary[word] = polarity
    # 저장할 파일 경로
    output_file = 'sentiment_dictionary_saved.json'

    # sentiment_dictionary를 JSON 파일로 저장
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(sentiment_dictionary, file, ensure_ascii=False, indent=4)

# 공백 지우기
def removeBlanks():

    # CSV 파일이 위치한 디렉토리 경로
    directory = 'Data/reviews/csv'

    # 디렉토리 내의 모든 CSV 파일을 처리
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            
            # CSV 파일 읽기
            df = pd.read_csv(file_path)

            # 공백이나 빈 행이 아닌 행만 필터링하여 새로운 DataFrame 생성
            filtered_df = df.dropna(how='all').dropna(axis=0, how='all')

            # 수정된 내용을 원래 파일에 덮어쓰기
            filtered_df.to_csv(file_path, index=False, encoding='utf-8')

result_file = 'Data/results.csv'

