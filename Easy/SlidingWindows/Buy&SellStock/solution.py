def BuySell(prices):
    '''minPrice=[105,105] #first element represents index (day), second represents price that day
    maxPrice=[200,0]

    #you must buy before you sell
    #the index of minPrice has to be smaller than
    #the index of maxPrice
    for index,price in enumerate(prices):
        if (price<minPrice[1] and index<=maxPrice[0]):
            minPrice[0]=index
            minPrice[1]=price
        elif (price>maxPrice[1] and index>minPrice[0]):
            maxPrice[0]=index
            maxPrice[1]=price

    if maxPrice[1]==0:
        return 0
        
    return maxPrice[1]-minPrice[1]    
    '''
    
    
    '''currMin, currMax = 200, -200
    minDate, maxDate = 100, 100

    #this solution works but not for corner cases
    for index, price in enumerate(prices):
        if price<currMin and index<maxDate:
            currMin, minDate = price, index
        elif price>currMax and index>minDate:
            currMax, maxDate = price, index
    
    profit = currMax-currMin
    if profit<0:
        return 0
    else:
        return profit'''
    

    #i can only think of brute force for now
    #but brute force cant pass all the tests, too slow for long arrays    

if __name__=="__main__":
    prices1=[2,1,2,1,0,1,2]
    print(BuySell(prices1)) #should be 5

    prices2=[7,6,4,3,1]
    print(BuySell(prices2)) #should be 0

