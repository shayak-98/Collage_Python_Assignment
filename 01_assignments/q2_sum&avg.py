num=[]
#Inputs the elements of list using for loop :
n=int(input('Enter the number of element you want to add to the list :'))
for i in range(n):
    value=int(input("Enter the number you want to add :"))
    num.append(value)
sum=sum(num)
avarage=sum/n
print('The sum of all the elements in the list is :',sum)
print('The avarage of all the elements in the list is :',avarage)

#Output:
#Enter the number of element you want to add to the list :3
#Enter the number you want to add :23
#Enter the number you want to add :43
#Enter the number you want to add :21
#The sum of all the elements in the list is : 87
#The avarage of all the elements in the list is : 29.0