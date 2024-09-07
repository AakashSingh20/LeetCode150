'''
set the bp variable to first element then traverse the array , if the element is smaller than the bp then set bp to that
variable, then calculate the profit by subtracting the element with the bp, and keep track of the max profit.
'''

prices = [7,1,5,3,6,4]

buy_price = prices[0]
profit = 0

for i in range(len(prices)):
    if prices[i] < buy_price:
        buy_price = prices[i]
    
    curr_profit = prices[i] - buy_price
    if curr_profit > profit:
        profit = curr_profit
print(profit)