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
    print('몇번째: ',i)
    print('단어:\t',data[i]['word'])
    print('단어 root:',data[i]['word_root'])
    print('극성', data[i]['polarity'])
    choose = int(input('어디로 분류: '))
    plor = int(input('극성 입력: '))

    