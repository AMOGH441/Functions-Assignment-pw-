def accept_numbers():
    num = int(input("How many numbers are needed to add in the list of number?: "))
    list1 = []
    for i in range(1,num+1):
        number_add = int(input(f"give the {i} number to add the list: "))
        list1.append(number_add)
    print(list1)
    evenlist =[]
    for i in  list1:
        if i %2 ==0:
            evenlist.append(i)
    return evenlist  

accept_numbers
print(f"list of all even numbers:  {accept_numbers()}" )