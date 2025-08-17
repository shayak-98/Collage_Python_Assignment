# Q1.Creating tuple using user input :
tup=[]
n=int(input("Enter the number of elements you want :"))
for i in range (n):
    element=int(input(f'Enter the {i+1}th element :'))
    tup.append(element)
tup=tuple(tup)
print("Entered tuple is :",tup)

#output:

'''Enter the number of elements you want :3
Enter the 1th element :22
Enter the 2th element :53
Enter the 3th element :5
Entered tuple is : (22, 53, 5)'''

#Q2.Find the lenth of tuple :
lenth=len(tup)
print('The lenth of the tuple is :',lenth)

#output :

'''The lenth of the tuple is : 3'''

#Q3.Count the number of occurences of a elemnet :
x=int(int(input('Enter the number you want to the the number of occurences :')))
print(f'The occurrences of {x} is :',tup.count(x))

#output :
'''Enter the number of elements you want :5
Enter the 1th element :1
Enter the 2th element :1
Enter the 3th element :1
Enter the 4th element :5
Enter the 5th element :6
Entered tuple is : (1, 1, 1, 5, 6)
The lenth of the tuple is : 5
Enter the number you want to the the number of occurences :1
The occurrences of 1 is : 3'''

#Q4.concadinate Two tuple :
Tuple1=(2,45,5)
Tuple2=(3,5,7)
new_tuple=Tuple1+Tuple2
print(f'{Tuple1}+{Tuple2}={new_tuple}')
#output:
#(2, 45, 5)+(3, 5, 7)=(2, 45, 5, 3, 5, 7)

#Q5.Convert a list to tuple :
tup=[]
n=int(input("Enter the number of elements you want :"))
for i in range (n):
    element=int(input(f'Enter the {i+1}th element :'))
    tup.append(element)
tup=tuple(tup)
print("Converted  list into tuple is :",tup)
#Output :

'''Enter the 1th element :1
Enter the 2th element :2
Converted  list into tuple is : (1, 2)'''

