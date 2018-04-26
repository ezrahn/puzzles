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
     
    highs = []
    if spy[num_days - 1] > spy[num_days - 2]:
        highs.append[spy[num_days - 1]]

    for i in xrange(1,num_days-1):
        if spy[i-1] > spy[i] and spy[i] < spy[i+1]:
           lows.append((i,spy[i]))
        if spy[i-1] < spy[i] and spy[i] > spy[i+1]:
           highs.append((i,spy[i]))
           
    print "Lows: %s" % lows
    print "Highs: %s" % highs
    
    solution_mtx = []
    #i => the day to buy
    for i in xrange(0, num_days):
        row = []
        #j = > the day to sell
        for j in xrange(0, num_days):
            #if the day to sell is less than the buy, no point
            if j == 0 or j < i:
                row.append(0)
            else:
                profit = spy[j] - spy[i]
                if profit < row[j - 1]:
                    profit = row[j - 1]
                print "i-1: %s, j: %s" % (i-1, j)
                if len(solution_mtx) > 0:
                #if i > 0:
                    print "i-1: %s, j: %s, solution_mtx[i-1][j]: %s" %(i-1, j, solution_mtx[i-1][j])
                    if profit < solution_mtx[i-1][j]:
                        profit =  solution_mtx[i-1][j]
                row.append(profit)
        solution_mtx.append(row)
        
    print "Solution_mtx: %s" % solution_mtx
    return solution_mtx[num_days - 1][num_days - 1]
    
                
            
            
            

stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
print get_max_profit(stock_prices_yesterday)
# returns 6 (buying for $5 and selling for $11)

stock_prices_yesterday = [100,10, 7, 5, 8, 11, 9,8,4,2,5,6,3,7,8,4,5,10,11,23,4,5,6,2,34,65,64,1]
print get_max_profit(stock_prices_yesterday)

#stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
#get_max_profit(stock_prices_yesterday)

