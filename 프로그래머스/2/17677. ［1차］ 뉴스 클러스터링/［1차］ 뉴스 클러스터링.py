from collections import Counter

def make_bigrams(s):
    bigrams = []
    for i in range(len(s) - 1):
        pair = s[i:i+2]
        if pair[0].isalpha() and pair[1].isalpha():
            bigrams.append(pair.lower())
    return bigrams

def solution(str1, str2):
    answer = 0
    bigrams1 = make_bigrams(str1)
    bigrams2 = make_bigrams(str2)
    
    counter1 = Counter(bigrams1)
    counter2 = Counter(bigrams2)
    
    intersection = sum((counter1 & counter2).values())
    
    union = sum((counter1 | counter2).values())
    
    if union == 0:
        jaccard_similarity = 1
    else:
        jaccard_similarity = intersection / union
        
    answer = int(jaccard_similarity * 65536)
        
    return answer