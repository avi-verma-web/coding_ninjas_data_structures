# Total Customers N = 4

# (sorted) budget_list = [14, 20, 30, 53]

# Fixed price = 14, all our customers buy our product

# Revenue = 14 * 4 = 56, Given by budget_list[0] * (N)

# Next price = 20, three customers buy the app(i.e expect the customer with budget 14)

# Revenue = 20 * 3, Given by budget_list[1] * (N-1)

def maximumProfit(arr):
	#Implement Your Function here
    numOfPeopleBuyingApp=len(arr)
    a=sorted(arr)
    maxPriceOfApp=0
    for InitialpriceOfAPP in a:
        if numOfPeopleBuyingApp*InitialpriceOfAPP>maxPriceOfApp:
            maxPriceOfApp=numOfPeopleBuyingApp*InitialpriceOfAPP
        numOfPeopleBuyingApp=numOfPeopleBuyingApp-1
    return maxPriceOfApp

a=[14, 20, 30, 53]
print(maximumProfit(a))