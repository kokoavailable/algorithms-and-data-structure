def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    count_valid_words = 0
    
    for word in babbling:
        is_invalid = False
        
        for sound in valid_sounds:
            if sound * 2 in word:
                is_invalid = True
                break
                
        if is_invalid:
            continue
            
        temp_word = word
        for sound in valid_sounds:
            temp_word = temp_word.replace(sound, ' ')
            
        if temp_word.strip() == '':
            count_valid_words += 1
            
    return count_valid_words
                    
            
        
    return answer