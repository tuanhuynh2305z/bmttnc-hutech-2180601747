def demsolan(list):
    count_dict = {}
    for item in list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")

word_list = input_string.split()

solanxh = demsolan(word_list)

print("Số lần xuất hiện của các phần tử: ", solanxh)