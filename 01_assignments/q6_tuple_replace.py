num=[]
n=int(input("Enter the no of elements :"))
for i in range(n):
    element=int(input('Enter the element :'))
    num.append(element)
x=int(input('Enter a number you want to change in the tuple :'))
y=int(input('Enter the new value :'))
print("The old tuple is :",tuple(num))
num=list(num)
num[num.index(x)]=y
num=tuple(num)
print("The new tuple is :",num)

#Output :
#Enter the no of elements :3
#Enter the element :2
#Enter the element :4
#Enter the element :6
#Enter a number you want to change in the tuple :2
#Enter the new value :100
#The old tuple is : (2, 4, 6)
#The new tuple is : (100, 4, 6)