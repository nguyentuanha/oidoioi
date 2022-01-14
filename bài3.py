ten = str(input("Nhap ho ten: "))
n = int(input("Nhap n bang so ki tu co trong moi tu trong ten vao: "))
print("\n\nTen cua ban:", ten)
cast1 = str(n)
cast2 = cast1[::-1]
if cast1 == cast2:
    print("day la so thuan nghich")
else:
    print("day khong la so thuan nghich")