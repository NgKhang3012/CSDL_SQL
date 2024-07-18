import os
import xml.etree.ElementTree as ET
import time
import pymysql

def query_data(database_name, truong_name, nam_hoc, xep_loai):
    # Kết nối tới cơ sở dữ liệu
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='123cmnr123',
        database=database_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:                                                                        # THỰC THI 
        cursor = connection.cursor()
        
        start_time = time.time()                                                # GHI LẠI THỜI GIAN BẮT ĐẦU TỪ KHI TRUY VẤN 
                                                                                # THỰC THI CÁC THÔNG TIN SQL THÔNG QUA CODE
        cursor.execute("""                                                      
            SELECT HS.HO, HS.TEN, HS.NTNS, HOC.DIEMTB, HOC.XEPLOAI, HOC.KQUA
            FROM HS
            INNER JOIN HOC ON HS.MAHS = HOC.MAHS
            INNER JOIN TRUONG ON HOC.MATR = TRUONG.MATR
            WHERE TRUONG.TENTR = %s AND HOC.NAMHOC = %s AND HOC.XEPLOAI = %s
        """, (truong_name, nam_hoc, xep_loai))

        query_time = time.time() - start_time                                 # DÙNG ĐỂ LẤY THỜI GIAN TRUY VẤN 

        results = cursor.fetchall()                                           # LẤY RA DANH SÁCH TRUY VẤN 
        
        print("Danh sách học sinh:")                                          # VÀ TIẾN HÀNH IN RA DANH SÁCH CÁC HỌC SINH THÍCH HỢP VỚI THÔNG TIN TRUY VẤN
        for result in results:
            print("Họ tên học sinh:", result['HO'], result['TEN'])
            
            print("NTNS:", result['NTNS'])
            
            print("Điểm TB:", result['DIEMTB'])
            
            print("Xếp loại:", result['XEPLOAI'])
            
            print("Kết quả:", result['KQUA'])
            print()

       
        root = ET.Element("Data")                                              # TẠO 1 FILE XML THEO YÊU CẦU ĐỀ BÀI 
        for result in results:
            student = ET.SubElement(root, "Student")
            ET.SubElement(student, "HoTen").text = result['HO'] + " " + result['TEN']
            ET.SubElement(student, "NTNS").text = str(result['NTNS'])
            ET.SubElement(student, "DiemTB").text = str(result['DIEMTB'])
            ET.SubElement(student, "XepLoai").text = result['XEPLOAI']
            ET.SubElement(student, "KetQua").text = result['KQUA']

        tree = ET.ElementTree(root)

       
        directory = "D:\\22520617_NGUYEN-DANG-NGUYEN-KHANG\\XML"                 # TẠO ĐƯỜNG DẪN ĐỂ ĐƯA FILE XML VÀO TRONG THƯ MỤC CỦA MÌNH MUỐN TẠO 


        if not os.path.exists(directory):                                        # TẠO 1 ĐƯỜNG DẪN MỚI NẾU KHONG TỒN TẠI ĐƯỜNG DẪN TRÊN HOẶC ĐƯỜNG DẪN TRÊN BỊ MẤT ĐI
            os.makedirs(directory)

        file_name = f"{database_name}-{truong_name}-{nam_hoc}-{xep_loai}.xml"    # LƯU TÊN FILE THEO ĐỊNH DẠNG YÊU CẦU CỦA ĐỀ BÀI ĐƯA RA 
        file_path = os.path.join(directory, file_name)                           # VÀ TIẾN HÀNH THÊM DỮ LIỆU VÀ IN RA 
        tree.write(file_path)
        print("Dữ liệu đã được xuất ra file:", file_path)

       
        print("Thời gian truy vấn dữ liệu:", query_time, "giây")                 # IN RA THỜI GIAN TRUY VÂN ( TÍNH BẰNG GIÂY ) ĐỂ SO SÁNH GIỮA 
                                                                                 # TRUONGHOC1 VÀ TRUONGHOC2 VỚI NHAU KHI NHẬP CÙNG 1 HỌC SINH

    except pymysql.Error as error:
        print(f"Lỗi khi truy vấn dữ liệu: {error}")                              # IN RA CÁC LỖI NẾU TRUY VẤN SAI HOẶC LỖI THỰC THI KHI INSERT DỮ LIỆU
    finally:    
        connection.close()                                                       #ĐÓNG KẾT NỐI


#=========================================================NHẬP THÔNG TIN ==============================================
database_name = input("Nhập tên database: ")
truong_name = input("Nhập tên trường: ")
nam_hoc = input("Nhập năm học: ")
xep_loai = input("Nhập xếp loại học tập: ")
#==========================================================TRUY VẤN =================================================
query_data(database_name, truong_name, nam_hoc, xep_loai)       # HÀM THỰC THI 
