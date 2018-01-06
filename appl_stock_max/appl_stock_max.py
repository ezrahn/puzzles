#https://www.interviewcake.com/?utm_campaign=interviewingio&utm_source=interviewingio&utm_medium=affiliate

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

def get_max_profit(spy=[]):
    if ! spy:
        return 0
    
    lows = []
    for i in xrange(0,spy):
        if i+1 < len(spy) and spy[i+1] > spy[i]:
            

get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)
