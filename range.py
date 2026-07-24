def ran_call(num,low,high):
    if num in range(low,high+1):
        print(f"{num} is in the range of {low} and {high}")
    else:
        print('not in range')
ran_call(5,1,10)