def myfunc(*args):
    even_list = []
    for num in args:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
print(myfunc(2,3,4,5,6))