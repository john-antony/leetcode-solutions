class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        orderdict = {c : i for i, c in enumerate(order)}


        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                
                if w2[j] != w1[j]:
                    if orderdict[w2[j]] < orderdict[w1[j]]:
                        return False
                    break
        
        return True
