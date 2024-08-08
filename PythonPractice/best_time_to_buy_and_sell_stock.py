def find_best_time_to_buy_sell(stock_arr):
    left_pointer = 0 
    right_pointer = 1
    max_profit = 0

    while (right_pointer < len(stock_arr)):
        print('Left pointer=', left_pointer)
        print('Right pointer=', right_pointer)
        
        buy = stock_arr[left_pointer]
        sell = stock_arr[right_pointer]
        
        if buy < sell:
            profit = sell - buy
            max_profit = max(profit, max_profit)
        else:
            left_pointer = right_pointer

        right_pointer += 1
            
    return left_pointer, right_pointer-1

stock_arr = [7, 5, 1, 11, 25, 30, 35, 0, 0, 0, 40000]

print('Best time to buy and sell stock:', find_best_time_to_buy_sell(stock_arr))

                
