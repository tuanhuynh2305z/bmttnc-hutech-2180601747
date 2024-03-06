def taotuple(list):
    return tuple(list)

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")

number = list(map(int, input_list.split(',')))

my_tuple = taotuple(number)

print("List: ", number)

print("Tuple từ List: ", my_tuple)