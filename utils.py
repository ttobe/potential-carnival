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