## https://leetcode.com/problems/online-stock-span/submissions/

# problem is this:  write a class with a single method, next, that 
# return takes in a price and return the number of previous prices 
# that were equal to or less than that price (in a row).

# I think there's a somewhat smarter way to do it than what I'm doing
# (as evidenced by the fact that I'm only at 16th pecentile for runtime
# and, unsurprisingly, 5th percentile for memory), but what I do is keep
# track of what number broke each span, so that I can keep skipping back
# until I hit a number that breaks it for me.  makes it so I don't have
# to touch each previous price; just the ones where a previous span ended

class StockSpanner:
    def __init__(self):
        self.previous_prices = []
        self.previous_spans = []
        self.previous_span_ender = []
        
    def next(self, price: int) -> int:        
        self.previous_prices.append(price)        
        
        if len(self.previous_prices) == 1:
            span = 1
            self.previous_spans.append(span)
            self.previous_span_ender.append(None)
            
        elif len(self.previous_prices) == 2:
            if self.previous_prices[0] <= price:
                span = 2
                self.previous_span_ender.append(None)
            else:
                span = 1
                self.previous_span_ender.append(self.previous_prices[0])
            self.previous_spans.append(span)
            
        else:
            idx = len(self.previous_prices) - 2
            span = 1
            while True:
                if price >= self.previous_prices[idx]:
                    span = span + self.previous_spans[idx]
                    if self.previous_span_ender[idx] is None:
                        span_ender = None
                        break
                    elif self.previous_span_ender[idx] > price:
                        span_ender = self.previous_span_ender[idx]
                        break
                    else:
                        idx = idx - self.previous_spans[idx]
                else:
                    span_ender = self.previous_prices[idx]
                    break                    
            self.previous_spans.append(span)
            self.previous_span_ender.append(span_ender)
        return span                
