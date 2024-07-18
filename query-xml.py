from lxml import etree
from tabulate import tabulate

def create_read_file_XML():
                                                                                 # NHẬP KHOẢN ĐIỂM ĐỂ TÌM RA CÁC HỌC SINH ĐỂ ĐIỂM TRONG KHOẢNG ĐÓ 
    diem_thap = float(input("Nhập ngưỡng điểm thấp: "))
    diem_cao = float(input("Nhập ngưỡng điểm cao: "))

                                                                                 # ĐỌC ĐƯỜNG DẪN CHỨA FILE XML ,
                                                                                 # EM TIẾN HÀNH CẬP NHẬT ĐƯỜNG DẪN THỦ CÔNG KHI TRUY VẤN 1 THÔNG TIN HỌC SINH MỚI
                                                                                 # COPY TÊN FILE THAY THẾ CHO ĐƯỜNG DẪN PHÍA DƯỚI KHI CÓ TRUY VẤN MỚI
    tree = etree.parse("D:\\22520617_NGUYEN-DANG-NGUYEN-KHANG\\XML\\TRUONGHOC2-Trường THCS D-2022-Xuất sắc.xml")

    xpath_query = f"//Student[DiemTB >= {diem_thap} and DiemTB <= {diem_cao}]"   # SỬ DỤNG XPATH ĐỂ LỌC CÁC THÔNG TIN HỌC SINH          
    students = tree.xpath(xpath_query)                                           # PHẢIGIỐNG TERMINAL KHI TRUY VẤN Ở CÂU 4

                                                                                 
    for student in students:                                                     # VÒNG FOR ĐỂ IN RA THÔNG TIN CÁC HỌC SINH TRONG XML
        hoten = student.find("HoTen").text
        ntns = student.find("NTNS").text
        diem_tb = float(student.find("DiemTB").text)
        xep_loai = student.find("XepLoai").text
        ket_qua = student.find("KetQua").text

        print("Họ tên:", hoten)
        print("NTNS:", ntns)
        print("Điểm TB:", diem_tb)
        print("Xếp loại:", xep_loai)
        print("Kết quả:", ket_qua)
        

create_read_file_XML()                                                                              # CUỐI CÙNG LÀ THỰC THI HÀM create_read_file_XML
