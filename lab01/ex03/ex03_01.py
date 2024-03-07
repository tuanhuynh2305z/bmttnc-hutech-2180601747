def tinhtongchan(sc):
    tong = 0
    for num in sc:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")

number = list(map(int, input_list.split(',')))
 
tongchan = tinhtongchan(number)

print("Tổng các số chẵn trong List là: ", tongchan) 