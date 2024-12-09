class Solution:
    def simplifyPath(self, path: str) -> str:
        ls1 = [p for p in path.split("/") if p != '']
        ls2 = []
        result = ""
        
        for p in ls1:
            if p == '.':
                continue
            elif p == '..':
                if ls2:
                    ls2.pop()
            else: 
                ls2.append(p)
            
        result = "/" + "/".join(ls2)
        return result