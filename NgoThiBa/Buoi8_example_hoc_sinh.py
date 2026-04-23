class HocSinh:
    def __init__(self, id:str, ho_ten:str, diem:float):
        self.id = id
        self.ho_ten = ho_ten
        self.diem = diem
        self.xep_loai = None
        
    # def nhap_thong_tin (self, id_hoc_sinh, ho_ten_hoc_sinh, diem_so):
    #     self.id = id_hoc_sinh
    #     self.ho_ten = ho_ten_hoc_sinh
    #     self.diem = diem_so
    def xep_loai_hoc_sinh(self):
        if self.diem > 9:
            self.xep_loai = "Học sinh xuất sắc"
        elif self.diem >= 8 and self.diem < 9:
            self.xep_loai = "Học sinh giỏi"
        elif self.diem >=7 and self.diem < 8:
            self.xep_loai = "Học sinh Khá"
        else:
            self.xep_loai = "Trung bình"
hoc_sinh_1 = HocSinh (id= "ID001", ho_ten= "Ngô Thị Ba", diem= 9)
hoc_sinh_1.xep_loai_hoc_sinh()
print(f"Học sinh có id = {hoc_sinh_1.id} với tên {hoc_sinh_1.ho_ten} đạt {hoc_sinh_1.diem} điểm ")