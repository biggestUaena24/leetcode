class StockSpanner:

    # we first initialize the stock with a stack of the first day that will always be there
    def __init__(self):
        self.stack = [[inf, 0]]


    #We then pop the day that have smaller or equal of today's price to see the last day that will have larger price than today
    def next(self, price: int) -> int:
        day = self.stack[-1][1] + 1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop(-1)
        
        res = day - self.stack[-1][1]
        self.stack.append([price, day])
        return res