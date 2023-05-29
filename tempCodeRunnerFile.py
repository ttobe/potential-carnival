def load_sentiment_lexicon(file_path):
    sentiment_lexicon = {}
    with open(file_path, 'r', encoding='utf-8-sig') as lexicon_file:
        for line in lexicon_file:
            word, sentiment = line.strip().split('\t')
            sentiment_lexicon[word] = float(sentiment)
    return sentiment_lexicon

def analyze_sentiment(text, sentiment_lexicon):
    words = text.split()
    sentiment_score = 0
    for word in words:
        if word in sentiment_lexicon:
            sentiment_score += sentiment_lexicon[word]
    return sentiment_score

# KNU 감성사전 로드
lexicon_file_path = 'KNU_SentiLex.txt'
sentiment_lexicon = load_sentiment_lexicon(lexicon_file_path)

# 텍스트 감성 분석
text = '이 음식은 정말 맛있어요!'
sentiment_score = analyze_sentiment(text, sentiment_lexicon)

# 결과 출력
print(f'텍스트: {text}')
print(f'감성 점수: {sentiment_score}')
