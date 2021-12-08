A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]
print("list A:", A)
print("list B:", B)
c= list(set(A) & set(B))
print("phần tử của 2 mảng", c)
x= list(set(A) ^ set (c))
print("các phần tử list A k trùng B:",x)
y= list(set(B) ^ set (c))
print("các phần tử list B k trùng A:",y)
