import pandas as pd
import os

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
