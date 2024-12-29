class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        
        for letter in letters:
            if ord(letter) > ord(target):
                return letter

        return letters[0]