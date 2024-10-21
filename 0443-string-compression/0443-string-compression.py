class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        
        while read < len(chars):
            current_char = chars[read]
            count = 0
            
            while read < len(chars) and chars[read] == current_char:
                read += 1
                count += 1
                
            chars[write] = current_char
            write += 1
            
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
                    
        return write