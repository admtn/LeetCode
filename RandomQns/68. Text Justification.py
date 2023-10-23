from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justify(strings,cnt,length,last) -> str:
            if len(strings) == 1:
                return strings[0] + " "*(maxWidth-length)
            res = ""
            if last:
                for i,w in enumerate(strings):
                    if i == len(strings)-1:
                        padding = maxWidth - len(res) - len(w)
                        res += w + " "*padding
                    else:
                        res += w + " "
                return res
                    
            num_space = cnt - 1
            space_size = (maxWidth-length)//num_space
            num_extra = maxWidth-length-space_size*(cnt-1)
            for i,w in enumerate(strings):
                if i == len(strings)-1:
                    res += w
                elif num_extra:
                    res += w + " "*space_size + " "
                    num_extra -= 1
                else:
                    res += w + " "*space_size
            return res

        res = []
        substring = []
        wordCnt, length = 0,0
        for w in words:
            length += len(w)
            wordCnt += 1
            if wordCnt-1 + length > maxWidth:
                res.append(justify(substring,wordCnt-1,length-len(w),False))
                substring,length,wordCnt = [], len(w), 1
            substring.append(w)
        res.append(justify(substring,wordCnt,length,True))
        return res

words = ["This", "is", "an", "example", "of", "text", "justification."]
print(Solution().fullJustify(words,16))
        
