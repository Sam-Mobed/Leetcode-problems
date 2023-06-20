def BuySell(prices):
    minPrice=[105,105] #first element represents index (day), second represents price that day
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

if __name__=="__main__":
    prices1=[7,1,5,3,6,4]
    print(BuySell(prices1)) #should be 5

    prices2=[7,6,4,3,1]
    print(BuySell(prices2)) #should be 0

