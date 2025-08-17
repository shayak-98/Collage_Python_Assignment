num=[]
#inputs number of elements in the list :

n=int(input("Enter the number of elements you want to add to the list :"))
for i in range(n):
    value=int(input('Enter the number you want to add :'))
    num.append(value)
print('The original list is :',num)
square=[x**2 for x in num if x%2==0]
print('The square of even numbers list is :',square)

#Output :
#Enter the number of elements you want to add to the list :3
#Enter the number you want to add :4
#Enter the number you want to add :5
#Enter the number you want to add :6
#The original list is : [4, 5, 6]
#The square of even numbers list is : [16, 36]