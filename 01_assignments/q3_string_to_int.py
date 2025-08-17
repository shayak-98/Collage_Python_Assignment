str_list=[]
#Inputs the elements of list using for loop :
n=int(input('Enter the number of element you want to add to the list :'))
for i in range(n):
    value=input("Enter the number you want to add :")
    str_list.append(value)

print(type(str_list[1]))     #Shows that the elemnet of the list is stored as  string
print('The list of string number is :',str_list)
int_list=[]
for x in str_list:
    int_list.append(int(x))

print(type(int_list[1]))     #Shows that the elemnet of the list is stored as  integer
print('The list of integer numbers is :',int_list)
#Output:
#Enter the number of element you want to add to the list :3
#Enter the number you want to add :3
#Enter the number you want to add :4
#Enter the number you want to add :2
#<class 'str'>
#The list of string number is : ['3', '4', '2']
#<class 'int'>
#The list of integer numbers is : [3, 4, 2]