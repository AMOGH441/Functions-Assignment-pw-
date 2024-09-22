def accept_integers():
    num = int(input("How many numbers are needed to add in the list of number?: "))
    list1 = []
    for i in range(1,num+1):
        number_add = int(input(f"give the {i} number to add the list: "))
        list1.append(number_add)
    print(list1)
    square=[]
    for i in  list1:
        sq= i*i
        square.append(sq)
    return square 

a = accept_integers()
print(f"list of square numbers:  {a}" )