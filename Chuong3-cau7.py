: #Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày  
vừa nhập (ngày/tháng/năm).
def tim_quy_trong_nam(Thang):
    quy = (Thang-1)//3+1
    return quy

thang = int(input("Xin vui lòng nhập vào 1 tháng:"))

if(1<= thang <= 12):
    quy = tim_quy_trong_nam(thang)
    print(f"Tháng {thang} thuộc vào quý {quy} trong năm.")
else:
    print("Tháng không hợp lệ!!!(SOS), xin vui lòng nhập lại :)))")