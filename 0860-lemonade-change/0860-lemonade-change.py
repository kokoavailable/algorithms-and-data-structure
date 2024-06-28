class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        pocket = {}
        
        for bill in bills:
            if not pocket.get(bill):
                pocket[bill] = 1
            else:
                pocket[bill] += 1

            if bill == 10:
                if pocket.get(5, 0) >= 1:
                    pocket[5] -= 1
                else:
                    return False
            elif bill == 20:
                if pocket.get(10, 0) >= 1 and pocket.get(5, 0) >= 1:
                    pocket[10] -= 1 
                    pocket[5] -= 1
                elif pocket.get(5, 0) >= 3 :
                    pocket[5] -= 3
                else:
                    return False
        
        return True
                    
            