def knapsack_dp(items,capacity):
    
    n = len(items)
    dp=[[0]*(capacity+1) for _ in range(n+1)]
    selected = [[False]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        weight_i, value_i = items[i-1]
        for w in range(capacity+1):
            if weight_i <= w:
                take_item = dp[i-1][w-weight_i] + value_i
                if take_item > dp[i-1][w]:
                    dp[i][w] = take_item
                    selected[i][w] = True
                else :
                    dp[i][w] = dp[i-1][w]
            else :
                dp[i][w] = dp[i-1][w]
    
    max_value = dp[n][capacity]
    selected_items = []
    w= capacity

    for i in range(n,0,-1):
        if selected[i][w]:
            selected_items.append(items[i-1])
            w-= items[i-1][0]
    
    return max_value, selected_items



if __name__=="__main__":

    items = [(10,60),(20,100),(30,120)]
    capacity = 50

    max_value,selected = knapsack_dp(items,capacity)
    print("Max Profit: ",max_value)
    print("Selected : ", selected)