#Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm. 
while True:
    n=int(input("Nhập một số nguyên dương: "))
    dem=0
    for i in range (1,n+1):
        if n%1==0:
            dem += 1
    if dem == 2:
        print(n," Là Số Nguyên Tố")
    else:
        print(n," Không Là Số Nguyên Tố")
    question = input("Bạn có muốn tiếp tục sử dụng tool?(c/k):")
    if question == "k":
        break
    print("Bye!!!")