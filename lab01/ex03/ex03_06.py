def xoapt(dic, key):
    if key in dic:
        del dic[key]
        return True
    else:
        return False

mydic = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4}

key_delete = 'b'

kq = xoapt(mydic, key_delete)

if kq:
    print("Phần tử được xóa từ Dictionary: ", mydic)
else:
    print("Không tìm thấy phần tử cần xóa trong Dictionary")    
    