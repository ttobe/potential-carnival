# KNU 형태소 새로 분류하기
import os
import json
standard = os.listdir('data')
standard.sort()
print(standard)

path = 'KnuSentiLex-master/data/SentiWord_info.json'

with open(path, 'r', encoding="UTF-8") as file:
    data = json.load(file)
    
# 14853 {'word': '알쏭달쏭하다', 'word_root': '알쏭달쏭', 'polarity': '-1'}
for i in range(100):
    print(i)
    print(data[i]['word'])
    print(data[i]['word_root'])
    choose = int(input('어디로 분류: '))
    
    


    

    