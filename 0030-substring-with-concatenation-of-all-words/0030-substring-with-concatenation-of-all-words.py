class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_length = len(words[0])
        total_words_length = word_length * len(words)
        word_count = Counter(words)
        result = []
        
        for offset in range(word_length):
            left = offset
            seen_words = {}
            count = 0
            
            for right in range(offset, len(s) - word_length + 1, word_length):
                word = s[right:right + word_length]
                
                if word in word_count:
                    seen_words[word] = seen_words.get(word, 0) + 1
                    count += 1
                    
                    while seen_words[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        seen_words[left_word] -= 1
                        left += word_length
                        count -= 1
                    
                    if count == len(words):
                        result.append(left)
                
                else:
                    seen_words.clear()
                    count = 0
                    left = right + word_length
        
        return result