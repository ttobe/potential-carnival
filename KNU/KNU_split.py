# KNU 형태소 새로 분류하기
import os
import json
standard = os.listdir('data')
standard.sort()
print(standard)

path = 'KNU/KnuSentiLex-master/data/SentiWord_info.json'

with open(path, 'r', encoding="UTF-8") as file:
    data = json.load(file)
    
# 14853 {'word': '알쏭달쏭하다', 'word_root': '알쏭달쏭', 'polarity': '-1'}
for i in range(100):
    json_path = ''
    word = data[i]['word']
    word_root = data[i]['word_root']
    polarity = data[i]['polarity']
    print('몇번째: ',i)
    print('단어:\t',word)
    print('단어 root:',word_root)
    print('극성', polarity)
    choose = int(input('어디로 분류 0 분위기 1 가격 2 만족 3 서비스: '))
    if choose == 0:
        json_path = 'KNU/data/atomsphere.json'
    elif choose == 1:
        json_path = 'KNU/data/price.json'
    elif choose == 2:
        json_path = 'KNU/data/satisfaction.json'
    elif choose == 3:
        json_path = 'KNU/data/service.json'
    else:
        json_path = 'KNU/data/else.json'
    # 파일로 분류된 데이터 저장
    with open(json_path, 'a', encoding='utf-8') as category_file:
        json.dump(data[i], category_file, indent='\t', ensure_ascii=False)
        category_file.write('\n,')

    # plor = int(input('극성 입력: '))

    