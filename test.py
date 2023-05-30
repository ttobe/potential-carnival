import csv

# CSV 파일 경로
csv_file = 'Data/result_with_ratings.csv'

# 나누고자 하는 행의 인덱스
target_row_index = 0

# 나누는 행의 인덱스
divider_row_index = 1

# CSV 파일 열기
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)
    
    # 나누기 연산 수행
    result_row = []
    for i in range(len(rows[target_row_index])):
        numerator = float(rows[target_row_index][i])
        denominator = float(rows[divider_row_index][i])
        
        # 나눈 결과를 임시 리스트에 추가
        result_row.append(numerator / denominator)
    
    # 원본 행들을 새로운 리스트에 추가
    new_rows = [row for row in rows if row != rows[target_row_index] and row != rows[divider_row_index]]
    
    # 연산 결과 행을 새로운 리스트에 추가
    new_rows.append(result_row)

# 결과를 저장할 새로운 CSV 파일 경로
output_csv_file = 'result.csv'

# 새로운 CSV 파일 생성 및 결과 저장
with open(output_csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(new_rows)
