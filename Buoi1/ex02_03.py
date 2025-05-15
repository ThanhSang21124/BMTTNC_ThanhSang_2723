#nhập số từ người dùng 
so = int(input("nhập một số nguyên: "))
#kiểm tra xem số đó có phải số chẵn hay không 
if so % 2 ==0:
    print(so, "là số chẵn. ")
else:
    print(so, "không phải là số chẵn. ")
