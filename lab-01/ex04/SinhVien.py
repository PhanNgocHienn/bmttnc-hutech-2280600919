class SinhVien:
    auto_id = 1

    def __init__(self, ten, gioi_tinh, chuyen_nganh, diem_tb):
        self.id = SinhVien.auto_id
        SinhVien.auto_id += 1
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_tb = diem_tb

    def hoc_luc(self):
        if self.diem_tb >= 8:
            return "Giỏi"
        elif self.diem_tb >= 6.5:
            return "Khá"
        elif self.diem_tb >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        return f"{self.id} - {self.ten} - {self.gioi_tinh} - {self.chuyen_nganh} - {self.diem_tb} - {self.hoc_luc()}"