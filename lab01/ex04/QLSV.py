from SinhVien import SinhVien

class QLSV:
    listSV = []
    
    def generateID(self):
        maxID = 1   
        if(self.soluongSV() > 0):
            maxID = self.listSV[0]._id
            for sv in self.listSV:
                if(maxID < sv._id):
                    maxID = sv._id 
            maxID = maxID + 1 
        return maxID
    
    def soluongSV(self):
        return self.listSV.__len__()
    
    def nhapSV(self):
        svID = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm trung bình của sinh viên: "))
        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSV.append(sv)
        
    def updateSV(self, ID):
        sv:SinhVien = self.findByID(ID)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành của sinh viên: ")
            diemTB = float(input("Nhập điểm trung bình của sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID = {} không tồn tại.".format(ID))
            
    def sortByID(self):
        self.listSV.sort(key = lambda x: x._id, reverse = False)
        
    def sortByName(self):
        self.listSV.sort(key = lambda x: x._name, reverse = False)
        
    def sortBydiemTB(self):
        self.listSV.sort(key = lambda x: x._diemTB, reverse = False)
        
    def fineByID(self, ID):
        searchResult = None
        if(self.soluongSV() > 0):
            for sv in self.listSV:
                if(sv._id == ID):
                    searchResult = sv
        return  searchResult
    
    def findByName(self, kw):
        liSV = []
        if(self.soluongSV() > 0):
            for sv in self.listSV:
                if(kw.upper() in sv._name.upper()):
                    liSV.append(sv)
        return liSV

    def deleteByID(self, ID):
        isDelete = False
        sv = self.fineByID(ID)
        if(sv != None):
            self.listSV.remove(sv)
            isDelete =  True
        return isDelete
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._diemTB >= 8):
            sv._hocLuc = "Giỏi"
        elif(sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif(sv._diemTB >= 5):
            sv._hocLuc = "Trung Bình"
        else:
            sv._hocLuc = "Yếu"
            
    def showSV(self, liSV):
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Điểm TB", "Học Lực"))
        if(liSV.__len__() > 0):
            for sv in liSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")
        
    def getListSV(self):
        return self.listSV