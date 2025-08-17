#Ask how many tuples
list_tuple=[]
n=int(input('Enter the number of tuples in the list :'))
for i in range (n):
    elements=input(f'Enter the elements of the tuple {i+1} separated by space :').split()
    #Convert to integer
    t=tuple(map(int,elements))
    list_tuple.append(t)
print(list_tuple)
print('Tuple with max sum',max(list_tuple))

#Output :
#Enter the number of tuples in the list :3
#Enter the elements of the tuple 1 separated by space :1 2 3 
#Enter the elements of the tuple 2 separated by space :2 3 5
#Enter the elements of the tuple 3 separated by space :1 2 6
#[(1, 2, 3), (2, 3, 5), (1, 2, 6)]
#Tuple with max sum (2, 3, 5)