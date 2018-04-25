#https://www.interviewcake.com/?utm_campaign=interviewingio&utm_source=interviewingio&utm_medium=affiliate


def get_max_profit(spy=[]):
    #if !spy:
    #    return 0
    print "Input: %s" % spy
    num_days = len(spy)
    
    if num_days < 2:
        return 0
    
    lows = []
    if spy[0] < spy[1]:
        lows.append[spy[0]]
     
    for i in xrange(1,num_days-1):
        if spy[i-1] > spy[i] and spy[i] < spy[i+1]:
           lows.append(spy[i])
           
    highs = []
    if spy[num_days - 1] > spy[num_days - 2]:
        highs.append[spy[num_days - 1]]
        
    for i in xrange(1,num_days-1):
        if spy[i-1] < spy[i] and spy[i] > spy[i+1]:
           highs.append(spy[i])
           
    print "Lows: %s" % lows
    print "Highs: %s" % highs
            

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

stock_prices_yesterday = [100,10, 7, 5, 8, 11, 9,8,4,2,5,6,3,7,8,4,5,10,11,23,4,5,6,2,34,65,64,1]
get_max_profit(stock_prices_yesterday)

#stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
#get_max_profit(stock_prices_yesterday)

