def chiahetcho5(sonhiphan):
    sothapphan = int(sonhiphan, 2)
    
    if(sothapphan % 5):
        return True
    else:
        return False
    
chuoisonhiphan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")

sonhiphanlist = chuoisonhiphan.split(',')

sochiahetcho5 = [so for so in sonhiphanlist if chiahetcho5(so)]

if len(sochiahetcho5) > 0:
    kq = ','.join(sochiahetcho5)
    print("Các số nhị phân chia hết cho 5 là: ", kq)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuổi vừa nhập.")