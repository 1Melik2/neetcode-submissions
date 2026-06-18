class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = []
        y = []

        for i in s:
            x.append(i)
        for i in t:
            y.append(i)
        
        x.sort()
        y.sort()

        print(x)
        print(y)
    

        if x == y:
            return True
        else:
            return False

            



        