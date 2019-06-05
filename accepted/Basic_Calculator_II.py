## https://leetcode.com/problems/basic-calculator-ii/submissions/

## this is identical to Basic Calulator I, but now we're doing * and / too
## that's all relatively easily handled in evaluate_no_parentheses, fortunately

## result is basically the same, with a runtime of about 25th percentile.
## i'll take it though, because I feel like this is a very clean and easy to
## understand solution.

class Solution:   
    def evalutate_no_parentheses(self, expr: List[str]):
        ## ok, so I have +, -, * and /
        
        ## so let's find all my *'s and /'s and do them first, from left to right:
        indices = list(reversed([ii for ii, item in enumerate(expr) if item == '*' or item == '/']))
        n_removed = 0
        while len(indices):
            ## pop off the first index (which is at the end cause I flipped it)
            op_idx = indices.pop() - n_removed
            a = int(expr[op_idx-1])
            b = int(expr[op_idx+1])
            if expr[op_idx] == '*':
                res = a*b
            else:
                assert expr[op_idx] == '/'
                res = a/b
            
            ## now remove a, b, and the operator and replace with my value:
            expr[op_idx-1] = res
            del expr[op_idx:op_idx+2]
            
            ## and note that we've removed two items from our expression list
            n_removed = n_removed + 2
        
        ## now we do simple addition and subtraction of what's left
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
        
        ## ok so this is what I __thought__ the previous problem was asking, 
        ## which is to say that we're adding multiplication and division
        
        ## I can still use all of this though, cause it just handles parsing and 
        ## parentheses, which are unchanged from before -- all my changes go in 
        ## self.evalutate_no_parentheses
        
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
                    ## all with it (i.e. evaluate it or append it to our stack).
                    ## alternatively, we could skip any ''s in the evaluator.
                    current_expr.append('')
                    
        # now at this point I should have a current_string to evaluate as my final answer
        # because closing parentheses had their own evaluation occur
        
        # only case in which that's not true is if the entire thing is enclosed in parentheses,
        # but my evalutor should handle that ok
        return self.evalutate_no_parentheses(current_expr[:-1])
        