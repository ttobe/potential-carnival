import pandas as pd

# CSV 파일 불러오기
csv_file_path = '../result/df.csv'  # 파일 경로를 적절히 수정하세요
df = pd.read_csv(csv_file_path)

# DataFrame 확인
print(df)


predicted_ratings = []
# txt 파일 불러오기
txt_file_path = '../result/final_predicted.txt'  # 파일 경로를 적절히 수정하세요
with open(txt_file_path, 'r') as file:
    # 각 줄을 읽어와서 쉼표로 나누고, 각 숫자의 길이 출력
    for line in file:
        predicted_ratings = line.strip().split(',')

print(len(predicted_ratings))


# 결과를 저장할 빈 리스트 생성
kakao_ratings = []

# kakao.txt 파일 읽기
with open("../result/kakao_rating.txt", "r") as file:
    for line in file:
        # 각 줄의 공백 제거 후 리스트에 추가
        rating = line.strip()
        kakao_ratings.append(float(rating))  # 문자열을 실수로 변환하여 저장 (필요에 따라 타입 변경)

# 결과 출력
print(len(kakao_ratings))

# DataFrame에 열 추가
df['Kakao_Ratings'] = kakao_ratings
df['Predicted_Ratings'] = predicted_ratings

# DataFrame 확인
print(df)

# DataFrame을 CSV 파일로 저장
output_csv_path = '../result/restaurantDB_with_ratings.csv'
df.to_csv(output_csv_path, index=False)