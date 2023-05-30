# 분석하기

import csv
import json
import os
from konlpy.tag import Okt
import csv

# Okt 객체 생성
okt = Okt()

# data 폴더 경로 설정
data_folder = 'Data/reviews/csv'

# data 폴더 내의 파일 리스트 가져오기
file_list = os.listdir(data_folder)

# 형태소 분석된 결과를 저장할 리스트
analyzed_reviews = []

# 파일 리스트 출력
for i in range(len(file_list)):
    file_list[i] = os.path.join(data_folder, file_list[i])
    # print(file_list[i])

for i in range(1):
    with open(file_list[i], 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # 헤더 라인 스킵

        print("hi")

        # 리뷰들을 형태소 분석하여 리스트에 추가
        for row in reader:
            review = row[0]  # 리뷰 컬럼
            print(review)
            morphs = okt.morphs(review)
            print(morphs)
            analyzed_reviews.append(morphs)

    # 형태소 분석 결과 출력
    for review in analyzed_reviews:
        print(review)

