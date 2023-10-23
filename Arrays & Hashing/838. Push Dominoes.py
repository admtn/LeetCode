from typing import List
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes)
        r = [None] * len(dom)
        l = [None] * len(dom)
        R,L = None,None
        j = len(dom)-1
        for i in range(len(dom)):
            # r array
            if dom[i] == 'R':
                R = i
            elif dom[i] == 'L':
                R = None
            else: # dom[i] == '.'
                r[i] = R

            # l array
            if dom[j] == 'L':
                L = j
            elif dom[j] == 'R':
                L = None
            else: # dom[i] == '.'
                l[j] = L
            j -= 1
        
        for i in range(len(dom)):
            if dom[i] == '.':
                if ( r[i] == None and l[i] == None):
                    continue
                elif r[i] != None and l[i] == None:
                    dom[i] = 'R'
                elif l[i] != None and r[i] == None:
                    dom[i] = 'L'
                else:
                    if l[i] - i > i - r[i]:
                        dom[i] = 'R'
                    elif l[i] - i < i - r[i]:
                        dom[i] = 'L'
                    else:
                        continue
        return "".join(dom)
class aa:
    def pushDominoes(self, dominoes: str) -> str:
        temp = ''
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')
            dominoes = dominoes.replace('R.', 'RR')
            dominoes = dominoes.replace('.L', 'LL')
        return dominoes.replace('xxx', 'R.L')
        

s= aa()
print(s.pushDominoes(".L.R...LR..L.."))        


