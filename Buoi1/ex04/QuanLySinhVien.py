from SinhVien import SinhVien

class QuanLySinhvien:
    listSinhVien = []

    def generateID(self):
        maxid = 1
        if self.soLuongSinhVien() > 0:
            maxid = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxid < sv._id:
                    maxid = sv._id
            maxid = maxid + 1
        return maxid

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xeploaihocluc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xeploaihocluc(sv)
        else:
            print(f"Sinh vien co id = {ID} khong ton tai.")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def findByName(self, keyword):
        listSV = []
        for sv in self.listSinhVien:
            if keyword.lower() in sv._name.lower():
                listSV.append(sv)
        return listSV

    def deleteByID(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xeploaihocluc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung Bình"
        else:
            sv._hocLuc = "Yếu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if len(listSV) > 0:
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        else:
            print("Danh sách sinh viên trống.")

    def getListSinhVien(self):
        return self.listSinhVien
