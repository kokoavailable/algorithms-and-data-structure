class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i
            num_spaces = maxWidth - sum(len(word) for word in line_words)

            if j == n or num_words == 1:
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                spaces_between_words = num_words - 1
                even_space = num_spaces // spaces_between_words
                extra_space = num_spaces % spaces_between_words

                line = ""
                for k in range(spaces_between_words):
                    line += line_words[k]
                    space_to_add = even_space + (1 if k < extra_space else 0)
                    line += ' ' * space_to_add
                line += line_words[-1]

            
            res.append(line)
            i = j

        return res