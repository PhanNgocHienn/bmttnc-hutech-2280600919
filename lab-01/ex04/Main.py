class SinhVien:
    def __init__(self, ten, gioi_tinh, chuyen_nganh, diem_tb):
        self.id = None
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_tb = diem_tb

    def __str__(self):
        return f"ID: {self.id}, Tên: {self.ten}, Giới tính: {self.gioi_tinh}, Chuyên ngành: {self.chuyen_nganh}, Điểm TB: {self.diem_tb}"

class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []
        self.next_id = 1

    def them(self, sv):
        sv.id = self.next_id
        self.next_id += 1
        self.danh_sach.append(sv)

    def cap_nhat(self, id_sv, ten=None, gioi_tinh=None, chuyen_nganh=None, diem_tb=None):
        for sv in self.danh_sach:
            if sv.id == id_sv:
                if ten is not None:
                    sv.ten = ten
                if gioi_tinh is not None:
                    sv.gioi_tinh = gioi_tinh
                if chuyen_nganh is not None:
                    sv.chuyen_nganh = chuyen_nganh
                if diem_tb is not None:
                    sv.diem_tb = diem_tb
                return True
        print("Không tìm thấy sinh viên với ID:", id_sv)
        return False

    def xoa(self, id_sv):
        for sv in self.danh_sach:
            if sv.id == id_sv:
                self.danh_sach.remove(sv)
                return True
        print("Không tìm thấy sinh viên với ID:", id_sv)
        return False

    def tim_kiem(self, keyword):
        return [sv for sv in self.danh_sach if keyword.lower() in sv.ten.lower()]

    def sap_xep_diem(self):
        self.danh_sach.sort(key=lambda sv: sv.diem_tb, reverse=True)
        print("Đã sắp xếp theo điểm trung bình.")

    def sap_xep_chuyen_nganh(self):
        self.danh_sach.sort(key=lambda sv: sv.chuyen_nganh)
        print("Đã sắp xếp theo chuyên ngành.")

    def hien_thi(self):
        if not self.danh_sach:
            print("Danh sách sinh viên trống.")
        for sv in self.danh_sach:
            print(sv)

def main():
    qlsv = QuanLySinhVien()

    while True:
        print("\n1. Thêm sinh viên")
        print("2. Cập nhật sinh viên")
        print("3. Xóa sinh viên")
        print("4. Tìm kiếm sinh viên theo tên")
        print("5. Sắp xếp theo điểm trung bình")
        print("6. Sắp xếp theo chuyên ngành")
        print("7. Hiển thị danh sách")
        print("0. Thoát")

        chon = input("Chọn: ")

        if chon == "1":
            ten = input("Tên: ")
            gt = input("Giới tính: ")
            cn = input("Chuyên ngành: ")
            dtb = float(input("Điểm TB: "))
            sv = SinhVien(ten, gt, cn, dtb)
            qlsv.them(sv)
        elif chon == "2":
            id_sv = int(input("Nhập ID: "))
            ten = input("Tên mới: ")
            gt = input("Giới tính mới: ")
            cn = input("Chuyên ngành mới: ")
            dtb = float(input("Điểm TB mới: "))
            qlsv.cap_nhat(id_sv, ten=ten, gioi_tinh=gt, chuyen_nganh=cn, diem_tb=dtb)
        elif chon == "3":
            id_sv = int(input("Nhập ID cần xoá: "))
            qlsv.xoa(id_sv)
        elif chon == "4":
            keyword = input("Nhập tên: ")
            for sv in qlsv.tim_kiem(keyword):
                print(sv)
        elif chon == "5":
            qlsv.sap_xep_diem()
        elif chon == "6":
            qlsv.sap_xep_chuyen_nganh()
        elif chon == "7":
            qlsv.hien_thi()
        elif chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
