#Creating a nested list with user input :
cols=int(input('Enter the no of columns'))
rows=int(input('Enter the no of rows'))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        val=int(input(f'Enter the {i},{j}th element'))
        row.append(val)
    matrix.append(row)
print("MATRIX :")
for i in matrix:
    print(i)
#Square each element in nested list :
square_list=[]
for i in matrix:
    new=[]
    for item in i:
        new.append(item**2)
    square_list.append(new)
print("Squared matrix :")
for i in square_list:
    print(i)
#Output:
'''
Enter the no of columns2
Enter the no of rows2
Enter the 0,0th element3
Enter the 0,1th element4
Enter the 1,0th element3
Enter the 1,1th element5
MATRIX :
[3, 4]
[3, 5]
Squared matrix :
[9, 16]
[9, 25]'''