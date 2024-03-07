from QLSV import QLSV

qlsv = QLSV()
while(1 == 1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("************************MENU************************")
    print("** 1. Thêm sinh viên.                             **")
    print("** 2. Cập nhật thông tin sinh viên bởi ID.        **")
    print("** 3. Xóa sinh viên bởi ID.                       **")
    print("** 4. Tìm kiếm thông tin sinh viên theo tên.      **")
    print("** 5. Sắp xếp sinh viên theo điểm trung bình.     **")
    print("** 6. Sắp xếp sinh viên theo tên chuyên ngành.    **")
    print("** 7. Hiển thị danh sách sinh viên.               **")
    print("** 0. Thoát.                                      **")
    print("****************************************************")
    
    key = int(input("Nhập tùy chọn: "))
    if(key == 1):
        print("\n1. Thêm sinh viên.")
        qlsv.nhapSV()
        print("\nThêm sinh viên thành công!")
    elif(key == 2):
        if(qlsv.soluongSV() > 0):
            print("\n2. Cập nhật thông tin sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updateSV(ID)
        else:
            print("\n Danh sách sinh viên trống!")
    elif(key == 3):
        if(qlsv.soluongSV() > 0):
            print("\n3. Xóa sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            if(qlsv.deleteByID(ID)):
                print("\nSinh viên có ID = ", ID, " đã bị xóa.")
            else:
                print("\nSinh viên có ID = ", ID, " không tồn tại.")
        else:
            print("\nDanh sách sinh viên trống!")
    elif(key == 4):
        if(qlsv.soluongSV() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên.")
            print("\nNhập tên để tìm kiếm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSV(searchResult)
        else:
            print("\nDanh sách sinh viên trống!")
    elif(key == 5):
        if(qlsv.soluongSV() > 0):
            print("\n5. Tìm kiếm sinh viên theo điểm trung bình (GPA).")
            qlsv.sortBydiemTB()
            qlsv.showSV(qlsv.getListSV())
        else:
            print("\nDanh sách sinh viên trống!")
    elif(key == 6):
        if(qlsv.soluongSV() > 0):
            print("\n6. Sắp xếp sinh viên theo tên.")
            qlsv.sortByName()
            qlsv.showSV(qlsv.getListSV())
        else:
            print("\nDanh sách sinh viên trống!")
    elif(key == 7):
        if(qlsv.soluongSV() > 0):
            print("\n7. Hiển thị danh sách sinh viên.")
            qlsv.showSV(qlsv.getListSV())
        else:
            print("\n Danh sách sinh viên trống!")
    elif(key == 0):
        print("\nBạn đã chọn thoát chương trình.")
    else:
        print("\nKhông có chức năng này!")
        print("\nHãy chọn chức năng trong menu.")