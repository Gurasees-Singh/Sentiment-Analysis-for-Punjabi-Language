# -*- coding: utf-8 -*-
def findValue(word, dict):
    temp = word
    # stemmer
    while(len(temp[:-1])!=0):
        if(temp in dict.keys()):
            # SentimentAnalysixs
            return  float(dict[temp][0]) - float(dict[temp][1])
        else:
            temp = temp[:-1]
            return findValue(temp, dict)
    return 0

file1 = open('PunjabiSentiLexicon-master\psl.txt', 'r', encoding="utf8")
Lines = file1.readlines()
total = 0
dict = {}
for i in Lines:
	j=i.split(' ')
	j.pop()
	dict[j[0]] = j[1:3]


text = " ਮਾਇਆਵਤੀ ਅਤੇ ਮੁਲਾਇਮ ਸਿੰਘ ਯਾਦਵ ਨੂੰ ਦੁਸ਼ਮਣ ਬਣਾਉਣ ਵਾਲਾ ਗੈਸਟ ਹਾਊਸ ਕਾਂਡ  ਭਰਤ ਸ਼ਰਮਾ ਬੀਬੀਸੀ ਪੱਤਰਕਾਰ ਉੱਤਰ ਪ੍ਰਦੇਸ਼ ਦੀ ਰਾਜਧਾਨੀ ਲਖਨਊ ਵਿੱਚ ਬਹੁਜਨ ਸਮਾਜ ਪਾਰਟੀ ਅਤੇ ਅਤੇ ਸਮਾਜਵਾਦੀ ਪਾਰਟੀ ਨੇ ਸਮਝੌਤੇ ਦਾ ਐਲਾਨ ਕੀਤਾ। ਬਸਪਾ ਦੀ ਸੁਪਰੀਮੋ ਮਾਇਆਵਤੀ ਅਤੇ ਸਪਾ ਮੁਖੀ ਅਖਿਲੇਸ਼ ਯਾਦਵ ਨੇ ਦੱਸਿਆ ਕਿ ਇਹ ਸਿਰਫ ਦੀਆਂ ਲੋਕ ਸਭਾ ਚੋਣਾਂ ਲਈ ਨਹੀਂ ਹੈ ਸਗੋਂ ਲੰਬੇ ਸਮੇਂ ਤੱਕ ਚੱਲੇਗਾ।ਦੋਹਾਂ ਧਿਰਾਂ ਨੇ ਕਿਹਾ ਕਿ ਉਹ ਲੋਕ ਸਭਾ ਚੋਣਾਂ ਵਿੱਚ ਸੂਬੇ ਦੀਆਂ 38-38 ਸੀਟਾਂ 'ਤੇ ਚੋਣ ਲੜਨਗੀਆਂ "
# tokenization
words = text.split(' ')

total = 0
word_count = 0
for word in words:
    total = total + findValue(word, dict)
print(total)