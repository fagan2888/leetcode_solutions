## https://leetcode.com/problems/decode-string/submissions/

## this is basically a variant of a calculator problem.  solve 
## it via a couple lists that I append to and pop off from, so 
## i just keep building up an output string as I close brackets.

## this turns out to be pretty much (but not quite) optimal, as 
## it comes in at ~91st percentile for runtime and ~96th percentile
## for memory

class Solution:
    def decodeString(self, s: str) -> str:
        digits = '0123456789'
        out = ''

        tomult = ['']
        mults = [1]
        
        running_num = ''
        for ii, char in enumerate(s):
            if char in digits:
                running_num += char
            elif char == '[':
                mults.append(int(running_num))
                tomult.append('')
                running_num = ''
            elif char == ']':
                o = tomult.pop()*mults.pop()
                tomult[-1] += o
            else:
                tomult[-1] += char
        return out + tomult.pop()