## https://leetcode.com/problems/basic-calculator/

## not 100% positive why this is hard -- it's not trivial, but it
## seems like it could be a whole lot harder.  basic algorithm is 
## pretty simple -- use a stack to handle parentheses, and everything
## else is evaluate as you go.

## not the fastest at 30th percentile for runtime, nor the best 
## for memory at ~22nd percentile

class Solution:
    def evalutate_no_parentheses(self, expr: List[str]):
        ## wow, only +/-, so don't have to worry about PEMDAS
        output = int(expr[0])
        for ii in range(1, len(expr)):
            if expr[ii-1] == '-':
                output = output - int(expr[ii])
            elif expr[ii-1] == '+':
                output = output + int(expr[ii])
            else:
                assert expr[ii] == '-' or expr[ii] == '+'
        return output
    
    def calculate(self, s: str) -> int:
        ## wow, this is way harder than RPN!  I see why that came about now.
        ## I think I can learn something from that though and use a stack again...
        
        ## wait, I read too much into the problem and was going to deal with 
        ## multiplication and division too.  if it's just +/-, then parentheses
        ## don't matter as much.  still matter though, since 1-(2+3) != 1-2+3
        
        ## drop white space cause it's meaningless and unreliable
        s = s.replace(' ', '')

        
        digits = set(str(i) for i in range(10))
        
        from collections import deque
        in_progress_expressions = deque([])
        current_expr = ['']
        
        for ii, char in enumerate(s):
            if char == '(':
                ## push our current expression to the stack
                in_progress_expressions.append(current_expr[:-1])
                ## start a new expression to capture what's in the 
                ## parentheses
                current_expr = ['']
            elif char == ')':
                ## evaluate our current string, then prepend the previous
                ## ongoing expression to it's result
                print(current_expr)
                res = self.evalutate_no_parentheses(current_expr[:-1])
                current_expr = in_progress_expressions.pop() + [str(res)] + ['']
            else:
                if char in digits and (ii != len(s) - 1) and (s[ii+1] in digits):
                    ## multi-digit number
                    current_expr[-1] += char
                else:
                    ## last digit in a number or not a number; add a new value after this
                    current_expr[-1] += char   
                    
                    ## append a new string to capture the next operator or number.
                    ## however, note that this means we'll always have to chop off 
                    ## the final entry of our current_expr anytime we do anything at
                    ## all with it (i.e. evaluate it or append it to our stack)
                    current_expr.append('')
                    
        # now at this point I should have a current_string to evaluate as my final answer
        # because closing parentheses had their own evaluation occur
        
        # only case in which that's not true is if the entire thing is enclosed in parentheses,
        # but my evalutor should handle that ok
        return self.evalutate_no_parentheses(current_expr[:-1])
        