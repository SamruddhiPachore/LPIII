def fractional_knapsack(items,capacity):
        
    #sorting items accorsing to the value to weight ratio in descending order
    items.sort(key=lambda x:x[1]/x[0],reverse=True)     #performs inplace sorting
    print("Sorted Items: ",items)
    selected_items=[]
    total_value = 0

    for weight,value in items:
          if capacity==0:
                break

          fraction = min(1,capacity/weight)
          selected_items.append((weight,value,fraction))

          total_value += fraction * value
          capacity -= fraction * weight

    return total_value,selected_items


if __name__=="__main__":
        items = [(10,60),(20,100),(30,120)]
        example= items.sort(key=lambda x: x[1] / x[0], reverse=True)
        print("items: ",)
        capacity = 50 
        max_value , selected_items = fractional_knapsack(items,capacity)
        print("Maximum value is  : ",max_value)
        print("Selected items: ",selected_items)
