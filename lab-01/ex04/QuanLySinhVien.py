class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def them(self, sv):
        self.danh_sach.append(sv)

    def cap_nhat(self, id_sv, **kwargs):
        for sv in self.danh_sach:
            if sv.id == id_sv:
                sv.ten = kwargs.get("ten", sv.ten)
                sv.gioi_tinh = kwargs.get("gioi_tinh", sv.gioi_tinh)
                sv.chuyen_nganh = kwargs.get("chuyen_nganh", sv.chuyen_nganh)
                sv.diem_tb = kwargs.get("diem_tb", sv.diem_tb)
                break

    def xoa(self, id_sv):
        self.danh_sach = [sv for sv in self.danh_sach if sv.id != id_sv]

    def tim_kiem(self, keyword):
        return [sv for sv in self.danh_sach if keyword.lower() in sv.ten.lower()]

    def sap_xep_diem(self):
        self.danh_sach.sort(key=lambda x: x.diem_tb, reverse=True)

    def sap_xep_chuyen_nganh(self):
        self.danh_sach.sort(key=lambda x: x.chuyen_nganh)

    def hien_thi(self):
        for sv in self.danh_sach:
            print(sv)
