def daonguoclist(list):
    return list[::-1]

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")

number = list(map(int, input_list.split(',')))

listdaonguoc = daonguoclist(number)

print("List sau khi đảo ngược: ", listdaonguoc)