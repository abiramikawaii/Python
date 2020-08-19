from collections import Counter

def word_count(sentence):

    count = 0
    a = sentence.lower()
    a1 = a.split()
    cnt = Counter()

    for word in a1:
        cnt[word] += 1
    return  cnt

 

word_count("caat hi jim hi")
