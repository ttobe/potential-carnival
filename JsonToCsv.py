import csv
import json


import os

# data 폴더 경로 설정
data_folder = 'Data/reviews/'

# data 폴더 내의 파일 리스트 가져오기
file_list = os.listdir(data_folder)

# 파일 리스트 출력
for i in range(len(file_list)):
    file_list[i] = os.path.join(data_folder, file_list[i])
    print(file_list[i])

for i in range(len(file_list)):

    # JSON 파일 경로
    open_path = file_list[i]
    # 이게 있으면 그냥 넘기기
    if open_path == 'Data/reviews/csv':
        continue
    # 파일 열기
    with open(open_path, 'r') as json_file:
        data = json.load(json_file)

    # CSV 파일 쓰기
    out_path = os.path.join(data_folder, 'csv/' + os.path.split(file_list[i])[-1][:-5] + '.csv')
    with open(out_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # 헤더 쓰기
        writer.writerow(['Text'])

        # 데이터 쓰기
        for review in data['reviews']:
            text = review['Text']
            writer.writerow([text])