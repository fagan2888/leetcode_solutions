## https://leetcode.com/problems/complex-number-multiplication/

## given two complex numbers as strings ("a+ib"), where a and b are
## integers, multiply them together and return the result as a similar
## string

## so just some string parsing and simple algebra

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        real_a, complex_a = a.split('+')
        real_b, complex_b = b.split('+')
        
        real_a = int(real_a)
        real_b = int(real_b)
        
        complex_a = int(complex_a[:-1])
        complex_b = int(complex_b[:-1])
        
        real_output = (real_a * real_b) - (complex_a * complex_b)
        complex_output = (real_a * complex_b) + (real_b * complex_a)
        output = str(real_output)+'+'+str(complex_output)+'i'
        return output
