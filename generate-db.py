import random
from datetime import date, timedelta
import pymysql
import mysql.connector

#HÀM CHECK_UNIQUE DÙNG ĐỂ KIỂM TRA TÍNH TRÙNG LẶP CỦA MATR
def CHECK_UNIQUE(CODES):   
    code = str(random.randint(100000, 999999))                                              # MATR GỒM 6 CHỮ SỐ 
    while code in CODES:
        code = str(random.randint(100000,999999))                                           
    return code

# HÀM Create_birthday để tạo NTNS cho từng học sinh bằng số năm hiện tại , 
# số tuổi được lấy từ 3->18 tuổi là số tuổi bắt đầu từ mẫu giáo cho đến hết cấp 3 ( tương đối)
def Create_birthday():
    today = date.today()
    start = today - timedelta(days=18*365) 
    end = today - timedelta(days=3*365)  
    random_date = start + timedelta(days=random.randint(0, (start - end).days))
    return random_date.strftime("%d-%m-%Y")

def create_truong(num_rows_truong):
    CODES = set()
    data = []                                                                   # ĐỂ LƯU THÔNG TIN CỦA 3 TRƯỜNG THUỘC TÍNH
    for _ in range(num_rows_truong):
        matr = CHECK_UNIQUE(CODES)                                              # EM CHỦ ĐỘNG TẠO TÊN TRƯỜNG ĐƠN GIẢN
        CODES.add(matr)                                                        
                                                                                #  ĐỂ KHI CẦN "TRUY VẤN Ở CÂU 4" CÓ THỂ DỄ DÀNG NHẬP VÀ KIỂM SOÁT
        type_truong = ["Trường mầm non", "Trường tiểu học", "Trường THCS", "Trường THPT"]
        name_truong = ["A", "B", "C", "D"]
        tentr = random.choice(type_truong) + " " + random.choice(name_truong)   # TẠO RA TÊN TRƯỜNG HOÀN CHỈNH 
        
        
        # ĐÂY LÀ TẤT CẢ DANH SÁCH CÁC QUẬN, HUYỆN CỦA 63 TỈNH THÀNH ĐƯỢC EM NỐI THEO TỪNG CỤM ĐỂ LÀM ĐỊA CHỈ CỦA TRƯỜNG.
        add_address =["Huyện Mỹ Đức, Thành phố Hà Nội", "Huyện Ứng Hòa, Thành phố Hà Nội","Huyện Phú Xuyên, Thành phố Hà Nội","Huyện Thường Tín, Thành phố Hà Nội","Huyện Thanh Oai, Thành phố Hà Nội","Huyện Chương Mỹ, Thành phố Hà Nội",
            "Huyện Thạch Thất, Thành phố Hà Nội",
            "Huyện Quốc Oai, Thành phố Hà Nội",
            "Huyện Hoài Đức, Thành phố Hà Nội",
            "Huyện Đan Phượng, Thành phố Hà Nội",
            "Huyện Phúc Thọ, Thành phố Hà Nội",
            "Huyện Ba Vì, Thành phố Hà Nội",
            "Thị xã Sơn Tây, Thành phố Hà Nội",
            "Quận Hà Đông, Thành phố Hà Nội",
            "Huyện Mê Linh, Thành phố Hà Nội",
            "Quận Bắc Từ Liêm, Thành phố Hà Nội",
            "Huyện Thanh Trì, Thành phố Hà Nội",
            "Quận Nam Từ Liêm, Thành phố Hà Nội",
            "Huyện Gia Lâm, Thành phố Hà Nội",
            "Huyện Đông Anh, Thành phố Hà Nội",
            "Huyện Sóc Sơn, Thành phố Hà Nội",
            "Quận Thanh Xuân, Thành phố Hà Nội",
            "Quận Hoàng Mai, Thành phố Hà Nội",
            "Quận Hai Bà Trưng, Thành phố Hà Nội",
            "Quận Đống Đa, Thành phố Hà Nội",
            "Quận Cầu Giấy, Thành phố Hà Nội",
            "Quận Long Biên, Thành phố Hà Nội",
            "Quận Tây Hồ, Thành phố Hà Nội",
            "Quận Hoàn Kiếm, Thành phố Hà Nội",
            "Quận Ba Đình, Thành phố Hà Nội",
            "Huyện Đồng Văn, Tỉnh Hà Giang", "Huyện Mèo Vạc, Tỉnh Hà Giang", "Huyện Yên Minh, Tỉnh Hà Giang",
            "Huyện Quản Bạ, Tỉnh Hà Giang", "Huyện Vị Xuyên, Tỉnh Hà Giang", "Huyện Bắc Mê, Tỉnh Hà Giang", 
            "Huyện Hoàng Su Phì, Tỉnh Hà Giang", "Huyện Xín Mần, Tỉnh Hà Giang", "Huyện Bắc Quang, Tỉnh Hà Giang", "Huyện Quang Bình, Tỉnh Hà Giang"
            "Huyện Bảo Lâm, Tỉnh Cao Bằng", "Huyện Bảo Lạc, Tỉnh Cao Bằng", "Huyện Hà Quảng, Tỉnh Cao Bằng", "Huyện Trùng Khánh, Tỉnh Cao Bằng", "Huyện Hạ Lang, Tỉnh Cao Bằng", "Huyện Quảng Hòa, Tỉnh Cao Bằng", "Huyện Hoà An, Tỉnh Cao Bằng", "Huyện Nguyên Bình, Tỉnh Cao Bằng", "Huyện Thạch An, Tỉnh Cao Bằng"
            "Huyện Pác Nặm, Tỉnh Bắc Kạn",
            "Huyện Ba Bể, Tỉnh Bắc Kạn",
            "Huyện Ngân Sơn, Tỉnh Bắc Kạn",
            "Huyện Bạch Thông, Tỉnh Bắc Kạn",
            "Huyện Chợ Đồn, Tỉnh Bắc Kạn",
            "Huyện Chợ Mới, Tỉnh Bắc Kạn",
            "Huyện Na Rì, Tỉnh Bắc Kạn",
            "Thành phố Tuyên Quang, Tỉnh Tuyên Quang", "Huyện Lâm Bình, Tỉnh Tuyên Quang", "Huyện Na Hang, Tỉnh Tuyên Quang", "Huyện Chiêm Hóa, Tỉnh Tuyên Quang", "Huyện Hàm Yên, Tỉnh Tuyên Quang", "Huyện Yên Sơn, Tỉnh Tuyên Quang", "Huyện Sơn Dương, Tỉnh Tuyên Quang",
            "Thành phố Lào Cai, Tỉnh Lào Cai", "Huyện Bát Xát, Tỉnh Lào Cai", "Huyện Mường Khương, Tỉnh Lào Cai", "Huyện Si Ma Cai, Tỉnh Lào Cai", "Huyện Bắc Hà, Tỉnh Lào Cai", "Huyện Bảo Thắng, Tỉnh Lào Cai", "Huyện Bảo Yên, Tỉnh Lào Cai", "Thị xã Sa Pa, Tỉnh Lào Cai", "Huyện Văn Bàn, Tỉnh Lào Cai",
            "Thành phố Điện Biên Phủ, Tỉnh Điện Biên", "Thị xã Mường Lay, Tỉnh Điện Biên", "Huyện Mường Nhé, Tỉnh Điện Biên", "Huyện Mường Chà, Tỉnh Điện Biên", "Huyện Tủa Chùa, Tỉnh Điện Biên", "Huyện Tuần Giáo, Tỉnh Điện Biên", "Huyện Điện Biên, Tỉnh Điện Biên", "Huyện Điện Biên Đông, Tỉnh Điện Biên", "Huyện Mường Ảng, Tỉnh Điện Biên", "Huyện Nậm Pồ, Tỉnh Điện Biên",
            "Thành phố Lai Châu, Tỉnh Lai Châu", "Huyện Tam Đường, Tỉnh Lai Châu", "Huyện Mường Tè, Tỉnh Lai Châu", "Huyện Sìn Hồ, Tỉnh Lai Châu", "Huyện Phong Thổ, Tỉnh Lai Châu", "Huyện Than Uyên, Tỉnh Lai Châu", "Huyện Tân Uyên, Tỉnh Lai Châu", "Huyện Nậm Nhùn, Tỉnh Lai Châu",
            "Thành phố Sơn La, Tỉnh Sơn La", "Huyện Quỳnh Nhai, Tỉnh Sơn La", "Huyện Thuận Châu, Tỉnh Sơn La", "Huyện Mường La, Tỉnh Sơn La", "Huyện Bắc Yên, Tỉnh Sơn La", "Huyện Phù Yên, Tỉnh Sơn La", "Huyện Mộc Châu, Tỉnh Sơn La", "Huyện Yên Châu, Tỉnh Sơn La", "Huyện Mai Sơn, Tỉnh Sơn La", "Huyện Sông Mã, Tỉnh Sơn La", "Huyện Sốp Cộp, Tỉnh Sơn La", "Huyện Vân Hồ, Tỉnh Sơn La",
            "Thành phố Yên Bái, Tỉnh Yên Bái", "Thị xã Nghĩa Lộ, Tỉnh Yên Bái", "Huyện Lục Yên, Tỉnh Yên Bái", "Huyện Văn Yên, Tỉnh Yên Bái", "Huyện Mù Căng Chải, Tỉnh Yên Bái", "Huyện Trấn Yên, Tỉnh Yên Bái", "Huyện Trạm Tấu, Tỉnh Yên Bái", "Huyện Văn Chấn, Tỉnh Yên Bái", "Huyện Yên Bình, Tỉnh Yên Bái",
            "Thành phố Hòa Bình, Tỉnh Hoà Bình", "Huyện Đà Bắc, Tỉnh Hoà Bình", "Huyện Lương Sơn, Tỉnh Hoà Bình", "Huyện Kim Bôi, Tỉnh Hoà Bình", "Huyện Cao Phong, Tỉnh Hoà Bình", "Huyện Tân Lạc, Tỉnh Hoà Bình", "Huyện Mai Châu, Tỉnh Hoà Bình", "Huyện Lạc Sơn, Tỉnh Hoà Bình", "Huyện Yên Thủy, Tỉnh Hoà Bình", "Huyện Lạc Thủy, Tỉnh Hoà Bình",
            "Thành phố Thái Nguyên, Tỉnh Thái Nguyên", "Thành phố Sông Công, Tỉnh Thái Nguyên", "Huyện Định Hóa, Tỉnh Thái Nguyên", "Huyện Phú Lương, Tỉnh Thái Nguyên", "Huyện Đồng Hỷ, Tỉnh Thái Nguyên", "Huyện Võ Nhai, Tỉnh Thái Nguyên", "Huyện Đại Từ, Tỉnh Thái Nguyên", "Thành phố Phổ Yên, Tỉnh Thái Nguyên", "Huyện Phú Bình, Tỉnh Thái Nguyên",
            "Thành phố Lạng Sơn, Tỉnh Lạng Sơn", "Huyện Tràng Định, Tỉnh Lạng Sơn", "Huyện Bình Gia, Tỉnh Lạng Sơn", "Huyện Văn Lãng, Tỉnh Lạng Sơn", "Huyện Cao Lộc, Tỉnh Lạng Sơn", "Huyện Văn Quan, Tỉnh Lạng Sơn", "Huyện Bắc Sơn, Tỉnh Lạng Sơn", "Huyện Hữu Lũng, Tỉnh Lạng Sơn", "Huyện Chi Lăng, Tỉnh Lạng Sơn", "Huyện Lộc Bình, Tỉnh Lạng Sơn", "Huyện Đình Lập, Tỉnh Lạng Sơn",
            "Thành phố Hạ Long, Tỉnh Quảng Ninh", "Thành phố Móng Cái, Tỉnh Quảng Ninh", "Thành phố Cẩm Phả, Tỉnh Quảng Ninh", "Thành phố Uông Bí, Tỉnh Quảng Ninh", "Huyện Bình Liêu, Tỉnh Quảng Ninh", "Huyện Tiên Yên, Tỉnh Quảng Ninh", "Huyện Đầm Hà, Tỉnh Quảng Ninh", "Huyện Hải Hà, Tỉnh Quảng Ninh", "Huyện Ba Chẽ, Tỉnh Quảng Ninh", "Huyện Vân Đồn, Tỉnh Quảng Ninh", "Thị xã Đông Triều, Tỉnh Quảng Ninh", "Thị xã Quảng Yên, Tỉnh Quảng Ninh", "Huyện Cô Tô, Tỉnh Quảng Ninh",
            "Thành phố Bắc Giang, Tỉnh Bắc Giang", "Huyện Yên Thế, Tỉnh Bắc Giang", "Huyện Tân Yên, Tỉnh Bắc Giang", "Huyện Lạng Giang, Tỉnh Bắc Giang", "Huyện Lục Nam, Tỉnh Bắc Giang", "Huyện Lục Ngạn, Tỉnh Bắc Giang", "Huyện Sơn Động, Tỉnh Bắc Giang", "Huyện Yên Dũng, Tỉnh Bắc Giang", "Huyện Việt Yên, Tỉnh Bắc Giang", "Huyện Hiệp Hòa, Tỉnh Bắc Giang",
            "Thành phố Việt Trì, Tỉnh Phú Thọ", "Thị xã Phú Thọ, Tỉnh Phú Thọ", "Huyện Đoan Hùng, Tỉnh Phú Thọ", "Huyện Hạ Hoà, Tỉnh Phú Thọ", "Huyện Thanh Ba, Tỉnh Phú Thọ", "Huyện Phù Ninh, Tỉnh Phú Thọ", "Huyện Yên Lập, Tỉnh Phú Thọ", "Huyện Cẩm Khê, Tỉnh Phú Thọ", "Huyện Tam Nông, Tỉnh Phú Thọ", "Huyện Lâm Thao, Tỉnh Phú Thọ", "Huyện Thanh Sơn, Tỉnh Phú Thọ", "Huyện Thanh Thuỷ, Tỉnh Phú Thọ", "Huyện Tân Sơn, Tỉnh Phú Thọ",
            "Thành phố Vĩnh Yên, Tỉnh Vĩnh Phúc", "Thành phố Phúc Yên, Tỉnh Vĩnh Phúc", "Huyện Lập Thạch, Tỉnh Vĩnh Phúc", "Huyện Tam Dương, Tỉnh Vĩnh Phúc", "Huyện Tam Đảo, Tỉnh Vĩnh Phúc", "Huyện Bình Xuyên, Tỉnh Vĩnh Phúc", "Huyện Yên Lạc, Tỉnh Vĩnh Phúc", "Huyện Vĩnh Tường, Tỉnh Vĩnh Phúc", "Huyện Sông Lô, Tỉnh Vĩnh Phúc",
            "Thành phố Bắc Ninh, Tỉnh Bắc Ninh", "Huyện Yên Phong, Tỉnh Bắc Ninh", "Thị xã Quế Võ, Tỉnh Bắc Ninh", "Huyện Tiên Du, Tỉnh Bắc Ninh", "Thành phố Từ Sơn, Tỉnh Bắc Ninh", "Thị xã Thuận Thành, Tỉnh Bắc Ninh", "Huyện Gia Bình, Tỉnh Bắc Ninh", "Huyện Lương Tài, Tỉnh Bắc Ninh",
            "Thành phố Hải Dương, Tỉnh Hải Dương", "Thành phố Chí Linh, Tỉnh Hải Dương", "Huyện Nam Sách, Tỉnh Hải Dương", "Thị xã Kinh Môn, Tỉnh Hải Dương", "Huyện Kim Thành, Tỉnh Hải Dương", "Huyện Thanh Hà, Tỉnh Hải Dương", "Huyện Cẩm Giàng, Tỉnh Hải Dương", "Huyện Bình Giang, Tỉnh Hải Dương", "Huyện Gia Lộc, Tỉnh Hải Dương", "Huyện Tứ Kỳ, Tỉnh Hải Dương", "Huyện Ninh Giang, Tỉnh Hải Dương", "Huyện Thanh Miện, Tỉnh Hải Dương",
            "Quận Hồng Bàng, Thành phố Hải Phòng", "Quận Ngô Quyền, Thành phố Hải Phòng", "Quận Lê Chân, Thành phố Hải Phòng", "Quận Hải An, Thành phố Hải Phòng", "Quận Kiến An, Thành phố Hải Phòng", "Quận Đồ Sơn, Thành phố Hải Phòng", "Quận Dương Kinh, Thành phố Hải Phòng", "Huyện Thuỷ Nguyên, Thành phố Hải Phòng", "Huyện An Dương, Thành phố Hải Phòng", "Huyện An Lão, Thành phố Hải Phòng", "Huyện Kiến Thuỵ, Thành phố Hải Phòng", "Huyện Tiên Lãng, Thành phố Hải Phòng", "Huyện Vĩnh Bảo, Thành phố Hải Phòng", "Huyện Cát Hải, Thành phố Hải Phòng", "Huyện Bạch Long Vĩ, Thành phố Hải Phòng",
            "Thành phố Hưng Yên, Tỉnh Hưng Yên", "Huyện Văn Lâm, Tỉnh Hưng Yên", "Huyện Văn Giang, Tỉnh Hưng Yên", "Huyện Yên Mỹ, Tỉnh Hưng Yên", "Thị xã Mỹ Hào, Tỉnh Hưng Yên", "Huyện Ân Thi, Tỉnh Hưng Yên", "Huyện Khoái Châu, Tỉnh Hưng Yên", "Huyện Kim Động, Tỉnh Hưng Yên", "Huyện Tiên Lữ, Tỉnh Hưng Yên", "Huyện Phù Cừ, Tỉnh Hưng Yên",
            "Thành phố Thái Bình, Tỉnh Thái Bình", "Huyện Quỳnh Phụ, Tỉnh Thái Bình", "Huyện Hưng Hà, Tỉnh Thái Bình", "Huyện Đông Hưng, Tỉnh Thái Bình", "Huyện Thái Thụy, Tỉnh Thái Bình", "Huyện Tiền Hải, Tỉnh Thái Bình", "Huyện Kiến Xương, Tỉnh Thái Bình", "Huyện Vũ Thư, Tỉnh Thái Bình",
            "Thành phố Phủ Lý, Tỉnh Hà Nam", "Thị xã Duy Tiên, Tỉnh Hà Nam", "Huyện Kim Bảng, Tỉnh Hà Nam", "Huyện Thanh Liêm, Tỉnh Hà Nam", "Huyện Bình Lục, Tỉnh Hà Nam", "Huyện Lý Nhân, Tỉnh Hà Nam",
            "Thành phố Nam Định, Tỉnh Nam Định", "Huyện Mỹ Lộc, Tỉnh Nam Định", "Huyện Vụ Bản, Tỉnh Nam Định", "Huyện Ý Yên, Tỉnh Nam Định", "Huyện Nghĩa Hưng, Tỉnh Nam Định", "Huyện Nam Trực, Tỉnh Nam Định", "Huyện Trực Ninh, Tỉnh Nam Định", "Huyện Xuân Trường, Tỉnh Nam Định", "Huyện Giao Thủy, Tỉnh Nam Định", "Huyện Hải Hậu, Tỉnh Nam Định",
            "Thành phố Tam Điệp, Tỉnh Ninh Bình", "Huyện Nho Quan, Tỉnh Ninh Bình", "Huyện Gia Viễn, Tỉnh Ninh Bình", "Huyện Hoa Lư, Tỉnh Ninh Bình", "Huyện Yên Khánh, Tỉnh Ninh Bình", "Huyện Kim Sơn, Tỉnh Ninh Bình", "Huyện Yên Mô, Tỉnh Ninh Bình",
            "Thành phố Thanh Hóa, Tỉnh Thanh Hóa", "Thị xã Bỉm Sơn, Tỉnh Thanh Hóa", "Thành phố Sầm Sơn, Tỉnh Thanh Hóa", "Huyện Mường Lát, Tỉnh Thanh Hóa", "Huyện Quan Hóa, Tỉnh Thanh Hóa", "Huyện Bá Thước, Tỉnh Thanh Hóa", "Huyện Quan Sơn, Tỉnh Thanh Hóa", "Huyện Lang Chánh, Tỉnh Thanh Hóa", "Huyện Ngọc Lặc, Tỉnh Thanh Hóa", "Huyện Cẩm Thủy, Tỉnh Thanh Hóa", "Huyện Thạch Thành, Tỉnh Thanh Hóa", "Huyện Hà Trung, Tỉnh Thanh Hóa", "Huyện Vĩnh Lộc, Tỉnh Thanh Hóa", "Huyện Yên Định, Tỉnh Thanh Hóa", "Huyện Thọ Xuân, Tỉnh Thanh Hóa", "Huyện Thường Xuân, Tỉnh Thanh Hóa", "Huyện Triệu Sơn, Tỉnh Thanh Hóa", "Huyện Thiệu Hóa, Tỉnh Thanh Hóa", "Huyện Hoằng Hóa, Tỉnh Thanh Hóa", "Huyện Hậu Lộc, Tỉnh Thanh Hóa", "Huyện Nga Sơn, Tỉnh Thanh Hóa", "Huyện Như Xuân, Tỉnh Thanh Hóa", "Huyện Như Thanh, Tỉnh Thanh Hóa", "Huyện Nông Cống, Tỉnh Thanh Hóa", "Huyện Đông Sơn, Tỉnh Thanh Hóa", "Huyện Quảng Xương, Tỉnh Thanh Hóa", "Thị xã Nghi Sơn, Tỉnh Thanh Hóa",
            "Thành phố Vinh, Tỉnh Nghệ An", "Thị xã Cửa Lò, Tỉnh Nghệ An", "Thị xã Thái Hoà, Tỉnh Nghệ An", "Huyện Quế Phong, Tỉnh Nghệ An", "Huyện Quỳ Châu, Tỉnh Nghệ An", "Huyện Kỳ Sơn, Tỉnh Nghệ An", "Huyện Tương Dương, Tỉnh Nghệ An", "Huyện Nghĩa Đàn, Tỉnh Nghệ An", "Huyện Quỳ Hợp, Tỉnh Nghệ An", "Huyện Quỳnh Lưu, Tỉnh Nghệ An", "Huyện Con Cuông, Tỉnh Nghệ An", "Huyện Tân Kỳ, Tỉnh Nghệ An", "Huyện Anh Sơn, Tỉnh Nghệ An", "Huyện Diễn Châu, Tỉnh Nghệ An", "Huyện Yên Thành, Tỉnh Nghệ An", "Huyện Đô Lương, Tỉnh Nghệ An", "Huyện Thanh Chương, Tỉnh Nghệ An", "Huyện Nghi Lộc, Tỉnh Nghệ An", "Huyện Nam Đàn, Tỉnh Nghệ An", "Huyện Hưng Nguyên, Tỉnh Nghệ An", "Thị xã Hoàng Mai, Tỉnh Nghệ An",
            "Thành phố Hà Tĩnh, Tỉnh Hà Tĩnh", "Thị xã Hồng Lĩnh, Tỉnh Hà Tĩnh", "Huyện Hương Sơn, Tỉnh Hà Tĩnh", "Huyện Đức Thọ, Tỉnh Hà Tĩnh", "Huyện Vũ Quang, Tỉnh Hà Tĩnh", "Huyện Nghi Xuân, Tỉnh Hà Tĩnh", "Huyện Can Lộc, Tỉnh Hà Tĩnh", "Huyện Hương Khê, Tỉnh Hà Tĩnh", "Huyện Thạch Hà, Tỉnh Hà Tĩnh", "Huyện Cẩm Xuyên, Tỉnh Hà Tĩnh", "Huyện Kỳ Anh, Tỉnh Hà Tĩnh", "Huyện Lộc Hà, Tỉnh Hà Tĩnh", "Thị xã Kỳ Anh, Tỉnh Hà Tĩnh",
            "Thành Phố Đồng Hới, Tỉnh Quảng Bình", "Huyện Minh Hóa, Tỉnh Quảng Bình", "Huyện Tuyên Hóa, Tỉnh Quảng Bình", "Huyện Quảng Trạch, Tỉnh Quảng Bình", "Huyện Bố Trạch, Tỉnh Quảng Bình", "Huyện Quảng Ninh, Tỉnh Quảng Bình", "Huyện Lệ Thủy, Tỉnh Quảng Bình", "Thị xã Ba Đồn, Tỉnh Quảng Bình",
            "Thành phố Đông Hà, Tỉnh Quảng Trị", "Thị xã Quảng Trị, Tỉnh Quảng Trị", "Huyện Vĩnh Linh, Tỉnh Quảng Trị", "Huyện Hướng Hóa, Tỉnh Quảng Trị", "Huyện Gio Linh, Tỉnh Quảng Trị", "Huyện Đa Krông, Tỉnh Quảng Trị", "Huyện Cam Lộ, Tỉnh Quảng Trị", "Huyện Triệu Phong, Tỉnh Quảng Trị", "Huyện Hải Lăng, Tỉnh Quảng Trị", "Huyện Cồn Cỏ, Tỉnh Quảng Trị",
            "Thành phố Huế, Tỉnh Thừa Thiên Huế", "Huyện Phong Điền, Tỉnh Thừa Thiên Huế", "Huyện Quảng Điền, Tỉnh Thừa Thiên Huế", "Huyện Phú Vang, Tỉnh Thừa Thiên Huế", "Thị xã Hương Thủy, Tỉnh Thừa Thiên Huế", "Thị xã Hương Trà, Tỉnh Thừa Thiên Huế", "Huyện A Lưới, Tỉnh Thừa Thiên Huế", "Huyện Phú Lộc, Tỉnh Thừa Thiên Huế", "Huyện Nam Đông, Tỉnh Thừa Thiên Huế",
            "Quận Liên Chiểu, Thành phố Đà Nẵng", "Quận Thanh Khê, Thành phố Đà Nẵng", "Quận Hải Châu, Thành phố Đà Nẵng", "Quận Sơn Trà, Thành phố Đà Nẵng", "Quận Ngũ Hành Sơn, Thành phố Đà Nẵng", "Quận Cẩm Lệ, Thành phố Đà Nẵng", "Huyện Hòa Vang, Thành phố Đà Nẵng", "Huyện Hoàng Sa, Thành phố Đà Nẵng",
            "Thành phố Tam Kỳ, Tỉnh Quảng Nam", "Thành phố Hội An, Tỉnh Quảng Nam", "Huyện Tây Giang, Tỉnh Quảng Nam", "Huyện Đông Giang, Tỉnh Quảng Nam", "Huyện Đại Lộc, Tỉnh Quảng Nam", "Thị xã Điện Bàn, Tỉnh Quảng Nam", "Huyện Duy Xuyên, Tỉnh Quảng Nam", "Huyện Quế Sơn, Tỉnh Quảng Nam", "Huyện Nam Giang, Tỉnh Quảng Nam", "Huyện Phước Sơn, Tỉnh Quảng Nam", "Huyện Hiệp Đức, Tỉnh Quảng Nam", "Huyện Thăng Bình, Tỉnh Quảng Nam", "Huyện Tiên Phước, Tỉnh Quảng Nam", "Huyện Bắc Trà My, Tỉnh Quảng Nam", "Huyện Nam Trà My, Tỉnh Quảng Nam", "Huyện Núi Thành, Tỉnh Quảng Nam", "Huyện Phú Ninh, Tỉnh Quảng Nam", "Huyện Nông Sơn, Tỉnh Quảng Nam",
            "Thành phố Quảng Ngãi, Tỉnh Quảng Ngãi", "Huyện Bình Sơn, Tỉnh Quảng Ngãi", "Huyện Trà Bồng, Tỉnh Quảng Ngãi", "Huyện Sơn Tịnh, Tỉnh Quảng Ngãi", "Huyện Tư Nghĩa, Tỉnh Quảng Ngãi", "Huyện Sơn Hà, Tỉnh Quảng Ngãi", "Huyện Sơn Tây, Tỉnh Quảng Ngãi", "Huyện Minh Long, Tỉnh Quảng Ngãi", "Huyện Nghĩa Hành, Tỉnh Quảng Ngãi", "Huyện Mộ Đức, Tỉnh Quảng Ngãi", "Thị xã Đức Phổ, Tỉnh Quảng Ngãi", "Huyện Ba Tơ, Tỉnh Quảng Ngãi", "Huyện Lý Sơn, Tỉnh Quảng Ngãi",
            "Thành phố Quy Nhơn, Tỉnh Bình Định", "Huyện An Lão, Tỉnh Bình Định", "Thị xã Hoài Nhơn, Tỉnh Bình Định", "Huyện Hoài Ân, Tỉnh Bình Định", "Huyện Phù Mỹ, Tỉnh Bình Định", "Huyện Vĩnh Thạnh, Tỉnh Bình Định", "Huyện Tây Sơn, Tỉnh Bình Định", "Huyện Phù Cát, Tỉnh Bình Định", "Thị xã An Nhơn, Tỉnh Bình Định", "Huyện Tuy Phước, Tỉnh Bình Định", "Huyện Vân Canh, Tỉnh Bình Định",
            "Thành phố Tuy Hoà, Tỉnh Phú Yên", "Thị xã Sông Cầu, Tỉnh Phú Yên", "Huyện Đồng Xuân, Tỉnh Phú Yên", "Huyện Tuy An, Tỉnh Phú Yên", "Huyện Sơn Hòa, Tỉnh Phú Yên", "Huyện Sông Hinh, Tỉnh Phú Yên", "Huyện Tây Hoà, Tỉnh Phú Yên", "Huyện Phú Hoà, Tỉnh Phú Yên", "Thị xã Đông Hòa, Tỉnh Phú Yên",
            "Thành phố Nha Trang, Tỉnh Khánh Hòa", "Thành phố Cam Ranh, Tỉnh Khánh Hòa", "Huyện Cam Lâm, Tỉnh Khánh Hòa", "Huyện Vạn Ninh, Tỉnh Khánh Hòa", "Thị xã Ninh Hòa, Tỉnh Khánh Hòa", "Huyện Khánh Vĩnh, Tỉnh Khánh Hòa", "Huyện Diên Khánh, Tỉnh Khánh Hòa", "Huyện Khánh Sơn, Tỉnh Khánh Hòa", "Huyện Trường Sa, Tỉnh Khánh Hòa",
            "Thành phố Phan Rang-Tháp Chàm, Tỉnh Ninh Thuận", "Huyện Bác Ái, Tỉnh Ninh Thuận", "Huyện Ninh Sơn, Tỉnh Ninh Thuận", "Huyện Ninh Hải, Tỉnh Ninh Thuận", "Huyện Ninh Phước, Tỉnh Ninh Thuận", "Huyện Thuận Bắc, Tỉnh Ninh Thuận", "Huyện Thuận Nam, Tỉnh Ninh Thuận",
            "Thành phố Phan Thiết, Tỉnh Bình Thuận", "Thị xã La Gi, Tỉnh Bình Thuận", "Huyện Tuy Phong, Tỉnh Bình Thuận", "Huyện Bắc Bình, Tỉnh Bình Thuận", "Huyện Hàm Thuận Bắc, Tỉnh Bình Thuận", "Huyện Hàm Thuận Nam, Tỉnh Bình Thuận", "Huyện Tánh Linh, Tỉnh Bình Thuận", "Huyện Đức Linh, Tỉnh Bình Thuận", "Huyện Hàm Tân, Tỉnh Bình Thuận", "Huyện Phú Quí, Tỉnh Bình Thuận",
            "Thành phố Kon Tum, Tỉnh Kon Tum", "Huyện Đắk Glei, Tỉnh Kon Tum", "Huyện Ngọc Hồi, Tỉnh Kon Tum", "Huyện Đắk Tô, Tỉnh Kon Tum", "Huyện Kon Plông, Tỉnh Kon Tum", "Huyện Kon Rẫy, Tỉnh Kon Tum", "Huyện Đắk Hà, Tỉnh Kon Tum", "Huyện Sa Thầy, Tỉnh Kon Tum", "Huyện Tu Mơ Rông, Tỉnh Kon Tum", "Huyện Ia H' Drai, Tỉnh Kon Tum",
            "Thành phố Pleiku, Tỉnh Gia Lai", "Thị xã An Khê, Tỉnh Gia Lai", "Thị xã Ayun Pa, Tỉnh Gia Lai", "Huyện KBang, Tỉnh Gia Lai", "Huyện Đăk Đoa, Tỉnh Gia Lai", "Huyện Chư Păh, Tỉnh Gia Lai", "Huyện Ia Grai, Tỉnh Gia Lai", "Huyện Mang Yang, Tỉnh Gia Lai", "Huyện Kông Chro, Tỉnh Gia Lai", "Huyện Đức Cơ, Tỉnh Gia Lai", "Huyện Chư Prông, Tỉnh Gia Lai", "Huyện Chư Sê, Tỉnh Gia Lai", "Huyện Đăk Pơ, Tỉnh Gia Lai", "Huyện Ia Pa, Tỉnh Gia Lai", "Huyện Krông Pa, Tỉnh Gia Lai", "Huyện Phú Thiện, Tỉnh Gia Lai", "Huyện Chư Pưh, Tỉnh Gia Lai",
            "Thành phố Buôn Ma Thuột, Tỉnh Đắk Lắk", "Thị xã Buôn Hồ, Tỉnh Đắk Lắk", "Huyện Ea H'leo, Tỉnh Đắk Lắk", "Huyện Ea Súp, Tỉnh Đắk Lắk", "Huyện Buôn Đôn, Tỉnh Đắk Lắk", "Huyện Cư M'gar, Tỉnh Đắk Lắk", "Huyện Krông Búk, Tỉnh Đắk Lắk", "Huyện Krông Năng, Tỉnh Đắk Lắk", "Huyện Ea Kar, Tỉnh Đắk Lắk", "Huyện M'Đrắk, Tỉnh Đắk Lắk", "Huyện Krông Bông, Tỉnh Đắk Lắk", "Huyện Krông Pắc, Tỉnh Đắk Lắk", "Huyện Krông A Na, Tỉnh Đắk Lắk", "Huyện Lắk, Tỉnh Đắk Lắk", "Huyện Cư Kuin, Tỉnh Đắk Lắk",
            "Thành phố Gia Nghĩa, Tỉnh Đắk Nông", "Huyện Đắk Glong, Tỉnh Đắk Nông", "Huyện Cư Jút, Tỉnh Đắk Nông", "Huyện Đắk Mil, Tỉnh Đắk Nông", "Huyện Krông Nô, Tỉnh Đắk Nông", "Huyện Đắk Song, Tỉnh Đắk Nông", "Huyện Đắk R'Lấp, Tỉnh Đắk Nông", "Huyện Tuy Đức, Tỉnh Đắk Nông",
            "Thành phố Đà Lạt, Tỉnh Lâm Đồng", "Thành phố Bảo Lộc, Tỉnh Lâm Đồng", "Huyện Đam Rông, Tỉnh Lâm Đồng", "Huyện Lạc Dương, Tỉnh Lâm Đồng", "Huyện Lâm Hà, Tỉnh Lâm Đồng", "Huyện Đơn Dương, Tỉnh Lâm Đồng", "Huyện Đức Trọng, Tỉnh Lâm Đồng", "Huyện Di Linh, Tỉnh Lâm Đồng", "Huyện Bảo Lâm, Tỉnh Lâm Đồng", "Huyện Đạ Huoai, Tỉnh Lâm Đồng", "Huyện Đạ Tẻh, Tỉnh Lâm Đồng", "Huyện Cát Tiên, Tỉnh Lâm Đồng",
            "Thị xã Phước Long, Tỉnh Bình Phước", "Thành phố Đồng Xoài, Tỉnh Bình Phước", "Thị xã Bình Long, Tỉnh Bình Phước", "Huyện Bù Gia Mập, Tỉnh Bình Phước", "Huyện Lộc Ninh, Tỉnh Bình Phước", "Huyện Bù Đốp, Tỉnh Bình Phước", "Huyện Hớn Quản, Tỉnh Bình Phước", "Huyện Đồng Phú, Tỉnh Bình Phước", "Huyện Bù Đăng, Tỉnh Bình Phước", "Thị xã Chơn Thành, Tỉnh Bình Phước", "Huyện Phú Riềng, Tỉnh Bình Phước",
            "Thành phố Tây Ninh, Tỉnh Tây Ninh", "Huyện Tân Biên, Tỉnh Tây Ninh", "Huyện Tân Châu, Tỉnh Tây Ninh", "Huyện Dương Minh Châu, Tỉnh Tây Ninh", "Huyện Châu Thành, Tỉnh Tây Ninh", "Thị xã Hòa Thành, Tỉnh Tây Ninh", "Huyện Gò Dầu, Tỉnh Tây Ninh", "Huyện Bến Cầu, Tỉnh Tây Ninh", "Thị xã Trảng Bàng, Tỉnh Tây Ninh",
            "Thành phố Biên Hòa, Tỉnh Đồng Nai", "Thành phố Long Khánh, Tỉnh Đồng Nai", "Huyện Tân Phú, Tỉnh Đồng Nai", "Huyện Vĩnh Cửu, Tỉnh Đồng Nai", "Huyện Định Quán, Tỉnh Đồng Nai", "Huyện Trảng Bom, Tỉnh Đồng Nai", "Huyện Thống Nhất, Tỉnh Đồng Nai", "Huyện Cẩm Mỹ, Tỉnh Đồng Nai", "Huyện Long Thành, Tỉnh Đồng Nai", "Huyện Xuân Lộc, Tỉnh Đồng Nai", "Huyện Nhơn Trạch, Tỉnh Đồng Nai",
            "Thành phố Vũng Tàu, Tỉnh Bà Rịa - Vũng Tàu", "Thành phố Bà Rịa, Tỉnh Bà Rịa - Vũng Tàu", "Huyện Châu Đức, Tỉnh Bà Rịa - Vũng Tàu", "Huyện Xuyên Mộc, Tỉnh Bà Rịa - Vũng Tàu", "Huyện Long Điền, Tỉnh Bà Rịa - Vũng Tàu", "Huyện Đất Đỏ, Tỉnh Bà Rịa - Vũng Tàu", "Thị xã Phú Mỹ, Tỉnh Bà Rịa - Vũng Tàu", "Huyện Côn Đảo, Tỉnh Bà Rịa - Vũng Tàu",
            "Quận 1, Thành phố Hồ Chí Minh", "Quận 12, Thành phố Hồ Chí Minh", "Quận Gò Vấp, Thành phố Hồ Chí Minh", "Quận Bình Thạnh, Thành phố Hồ Chí Minh", "Quận Tân Bình, Thành phố Hồ Chí Minh", "Quận Tân Phú, Thành phố Hồ Chí Minh", "Quận Phú Nhuận, Thành phố Hồ Chí Minh", "Thành phố Thủ Đức, Thành phố Hồ Chí Minh", "Quận 3, Thành phố Hồ Chí Minh", "Quận 10, Thành phố Hồ Chí Minh", "Quận 11, Thành phố Hồ Chí Minh", "Quận 4, Thành phố Hồ Chí Minh", "Quận 5, Thành phố Hồ Chí Minh", "Quận 6, Thành phố Hồ Chí Minh", "Quận 8, Thành phố Hồ Chí Minh", "Quận Bình Tân, Thành phố Hồ Chí Minh", "Quận 7, Thành phố Hồ Chí Minh", "Huyện Củ Chi, Thành phố Hồ Chí Minh", "Huyện Hóc Môn, Thành phố Hồ Chí Minh", "Huyện Bình Chánh, Thành phố Hồ Chí Minh", "Huyện Nhà Bè, Thành phố Hồ Chí Minh", "Huyện Cần Giờ, Thành phố Hồ Chí Minh",
            "Thành phố Tân An, Tỉnh Long An", "Thị xã Kiến Tường, Tỉnh Long An", "Huyện Tân Hưng, Tỉnh Long An", "Huyện Vĩnh Hưng, Tỉnh Long An", "Huyện Mộc Hóa, Tỉnh Long An", "Huyện Tân Thạnh, Tỉnh Long An", "Huyện Thạnh Hóa, Tỉnh Long An", "Huyện Đức Huệ, Tỉnh Long An", "Huyện Đức Hòa, Tỉnh Long An", "Huyện Bến Lức, Tỉnh Long An", "Huyện Thủ Thừa, Tỉnh Long An", "Huyện Tân Trụ, Tỉnh Long An", "Huyện Cần Đước, Tỉnh Long An", "Huyện Cần Giuộc, Tỉnh Long An", "Huyện Châu Thành, Tỉnh Long An",
            "Thành phố Mỹ Tho, Tỉnh Tiền Giang", "Thị xã Gò Công, Tỉnh Tiền Giang", "Thị xã Cai Lậy, Tỉnh Tiền Giang", "Huyện Tân Phước, Tỉnh Tiền Giang", "Huyện Cái Bè, Tỉnh Tiền Giang", "Huyện Châu Thành, Tỉnh Tiền Giang", "Huyện Chợ Gạo, Tỉnh Tiền Giang", "Huyện Gò Công Tây, Tỉnh Tiền Giang", "Huyện Gò Công Đông, Tỉnh Tiền Giang", "Huyện Tân Phú Đông, Tỉnh Tiền Giang",
            "Thành phố Bến Tre, Tỉnh Bến Tre", "Huyện Châu Thành, Tỉnh Bến Tre", "Huyện Chợ Lách, Tỉnh Bến Tre", "Huyện Mỏ Cày Nam, Tỉnh Bến Tre", "Huyện Giồng Trôm, Tỉnh Bến Tre", "Huyện Bình Đại, Tỉnh Bến Tre", "Huyện Ba Tri, Tỉnh Bến Tre", "Huyện Thạnh Phú, Tỉnh Bến Tre", "Huyện Mỏ Cày Bắc, Tỉnh Bến Tre",
            "Thành phố Trà Vinh, Tỉnh Trà Vinh", "Huyện Càng Long, Tỉnh Trà Vinh", "Huyện Cầu Kè, Tỉnh Trà Vinh", "Huyện Tiểu Cần, Tỉnh Trà Vinh", "Huyện Châu Thành, Tỉnh Trà Vinh", "Huyện Cầu Ngang, Tỉnh Trà Vinh", "Huyện Trà Cú, Tỉnh Trà Vinh", "Huyện Duyên Hải, Tỉnh Trà Vinh", "Thị xã Duyên Hải, Tỉnh Trà Vinh",
            "Thành phố Vĩnh Long, Tỉnh Vĩnh Long", "Huyện Long Hồ, Tỉnh Vĩnh Long", "Huyện Mang Thít, Tỉnh Vĩnh Long", "Huyện Vũng Liêm, Tỉnh Vĩnh Long", "Huyện Tam Bình, Tỉnh Vĩnh Long", "Thị xã Bình Minh, Tỉnh Vĩnh Long", "Huyện Trà Ôn, Tỉnh Vĩnh Long", "Huyện Bình Tân, Tỉnh Vĩnh Long",
            "Thành phố Cao Lãnh, Tỉnh Đồng Tháp", "Thành phố Sa Đéc, Tỉnh Đồng Tháp", "Thành phố Hồng Ngự, Tỉnh Đồng Tháp", "Huyện Tân Hồng, Tỉnh Đồng Tháp", "Huyện Hồng Ngự, Tỉnh Đồng Tháp", "Huyện Tam Nông, Tỉnh Đồng Tháp", "Huyện Tháp Mười, Tỉnh Đồng Tháp", "Huyện Cao Lãnh, Tỉnh Đồng Tháp", "Huyện Thanh Bình, Tỉnh Đồng Tháp", "Huyện Lấp Vò, Tỉnh Đồng Tháp", "Huyện Lai Vung, Tỉnh Đồng Tháp", "Huyện Châu Thành, Tỉnh Đồng Tháp",
            "Thành phố Long Xuyên, Tỉnh An Giang", "Thành phố Châu Đốc, Tỉnh An Giang", "Huyện An Phú, Tỉnh An Giang", "Thị xã Tân Châu, Tỉnh An Giang", "Huyện Phú Tân, Tỉnh An Giang", "Huyện Châu Phú, Tỉnh An Giang", "Thị xã Tịnh Biên, Tỉnh An Giang", "Huyện Tri Tôn, Tỉnh An Giang", "Huyện Châu Thành, Tỉnh An Giang", "Huyện Chợ Mới, Tỉnh An Giang", "Huyện Thoại Sơn, Tỉnh An Giang",
            "Thành phố Rạch Giá, Tỉnh Kiên Giang", "Thành phố Hà Tiên, Tỉnh Kiên Giang", "Huyện Kiên Lương, Tỉnh Kiên Giang", "Huyện Hòn Đất, Tỉnh Kiên Giang", "Huyện Tân Hiệp, Tỉnh Kiên Giang", "Huyện Châu Thành, Tỉnh Kiên Giang", "Huyện Giồng Riềng, Tỉnh Kiên Giang", "Huyện Gò Quao, Tỉnh Kiên Giang", "Huyện An Biên, Tỉnh Kiên Giang", "Huyện An Minh, Tỉnh Kiên Giang", "Huyện Vĩnh Thuận, Tỉnh Kiên Giang", "Thành phố Phú Quốc, Tỉnh Kiên Giang", "Huyện Kiên Hải, Tỉnh Kiên Giang", "Huyện U Minh Thượng, Tỉnh Kiên Giang", "Huyện Giang Thành, Tỉnh Kiên Giang",
            "Quận Ninh Kiều, Thành phố Cần Thơ", "Quận Ô Môn, Thành phố Cần Thơ", "Quận Bình Thuỷ, Thành phố Cần Thơ", "Quận Cái Răng, Thành phố Cần Thơ", "Quận Thốt Nốt, Thành phố Cần Thơ", "Huyện Vĩnh Thạnh, Thành phố Cần Thơ", "Huyện Cờ Đỏ, Thành phố Cần Thơ", "Huyện Phong Điền, Thành phố Cần Thơ", "Huyện Thới Lai, Thành phố Cần Thơ",
            "Thành phố Vị Thanh, Tỉnh Hậu Giang", "Thành phố Ngã Bảy, Tỉnh Hậu Giang", "Huyện Châu Thành A, Tỉnh Hậu Giang", "Huyện Châu Thành, Tỉnh Hậu Giang", "Huyện Phụng Hiệp, Tỉnh Hậu Giang", "Huyện Vị Thuỷ, Tỉnh Hậu Giang", "Huyện Long Mỹ, Tỉnh Hậu Giang", "Thị xã Long Mỹ, Tỉnh Hậu Giang",
            "Thành phố Sóc Trăng, Tỉnh Sóc Trăng", "Huyện Châu Thành, Tỉnh Sóc Trăng", "Huyện Kế Sách, Tỉnh Sóc Trăng", "Huyện Mỹ Tú, Tỉnh Sóc Trăng", "Huyện Cù Lao Dung, Tỉnh Sóc Trăng", "Huyện Long Phú, Tỉnh Sóc Trăng", "Huyện Mỹ Xuyên, Tỉnh Sóc Trăng", "Thị xã Ngã Năm, Tỉnh Sóc Trăng", "Huyện Thạnh Trị, Tỉnh Sóc Trăng", "Thị xã Vĩnh Châu, Tỉnh Sóc Trăng", "Huyện Trần Đề, Tỉnh Sóc Trăng",
            "Thành phố Bạc Liêu, Tỉnh Bạc Liêu", "Huyện Hồng Dân, Tỉnh Bạc Liêu", "Huyện Phước Long, Tỉnh Bạc Liêu", "Huyện Vĩnh Lợi, Tỉnh Bạc Liêu", "Thị xã Giá Rai, Tỉnh Bạc Liêu", "Huyện Đông Hải, Tỉnh Bạc Liêu", "Huyện Hoà Bình, Tỉnh Bạc Liêu",
            "Huyện U Minh, Tỉnh Cà Mau", "Huyện Thới Bình, Tỉnh Cà Mau", "Huyện Trần Văn Thời, Tỉnh Cà Mau", "Huyện Cái Nước, Tỉnh Cà Mau", "Huyện Đầm Dơi, Tỉnh Cà Mau", "Huyện Năm Căn, Tỉnh Cà Mau", "Huyện Phú Tân, Tỉnh Cà Mau", "Huyện Ngọc Hiển, Tỉnh Cà Mau"
            ]
        dchitr = random.choice(add_address)                     # LẤY NGẪU NHIÊN 1 TRƯỜNG 1 ĐỊA CHỈ TƯƠNG ỨNG Ở CHUỖI ĐỊA CHỈ TRÊN 
        data.append((matr, tentr, dchitr))                      # THÊM 3 TRƯỜNG THUỘC TÍNH VÀO DATA
    
    return data                                                 # TẠO XONG DỮ LIỆU TRƯỜNG .

# Hàm này dùng để kiểm tra tính duy nhất của cccd ( nếu hs đó trên 14 tuổi )
def check_unique_of_cccd (cccds): 
    CCCD = str(random.randint(100000000000, 999999999999))      # cccd gồm 12 chữ số duy nhất với mỗi người 
    while CCCD in cccds:
        CCCD = str(random.randint(100000000000, 999999999999))  # nếu trùng lặp thì tạo mới
    return CCCD
# Tạo trường dữ liệu HS
def create_hs_data(num_rows_hs):
    CODES = set()                                                # set khong chứ các phần tử trùng lặp 
    cccds =set()                                                 # set khong chứ các phần tử trùng lặp 
    data = []                                                    # lưu dữ liệu các thuộc tính HS 
    ho_list = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng" , "Huỳnh", "Vũ" ,"Võ", "Phan", "Trương", "Bùi", "Đặng", "Đỗ", "Ngô", "Hồ", "Dương", "Đinh"]
    ten_list = ["Huy", "Khang", "Bảo", "Minh", "Phúc", "Anh", "Khoa", "Phát", "Đạt", "Khôi", "Long", "Nam",
                "Duy", "Quân", "Kiệt", "Thịnh", "Tuấn", "Hưng", "Hoàng", "Hiếu", "Nhân", "Trí", "Tài", "Phong",
                "Nguyên", "An", "Phú", "Thành", "Đức", "Dũng", "Lộc", "Khánh", "Vinh", "Tiến", "Nghĩa", "Thiện",
                "Hào", "Hải", "Đăng", "Quang", "Lâm", "Nhật", "Trung", "Thắng", "Tú", "Hùng", "Tâm", "Sang", "Sơn", 
                "Thái", "Cường", "Vũ", "Toàn", "Ân", "Thuận", "Bình", "Trường", "Danh", "Kiên", "Phước", "Thiên", 
                "Tân", "Việt", "Khải", "Tín", "Dương", "Tùng", "Quý", "Hậu", "Trọng", "Triết", "Luân", "Phương", 
                "Quốc", "Thông", "Khiêm", "Hòa", "Thanh", "Tường", "Kha", "Vỹ", "Bách", "Khanh", "Mạnh", "Lợi", 
                "Đại", "Hiệp", "Đông", "Nhựt", "Giang", "Kỳ", "Phi", "Tấn", "Văn", "Vương", "Công", "Hiển", "Linh", "Ngọc", "Vĩ"]
    dchi_list = [
        "Hòa Bình", "Sơn La", "Điện Biên", "Lai Châu", "Lào Cai", "Yên Bái", "Phú Thọ", "Hà Giang", "Tuyên Quang",
        "Cao Bằng", "Bắc Kạn", "Thái Nguyên", "Lạng Sơn", "Bắc Giang", "Quảng Ninh", "Hà Nội", "Bắc Ninh", "Hà Nam",
        "Hải Dương", "Hải Phòng", "Hưng Yên", "Nam Định", "Thái Bình", "Vĩnh Phúc", "Ninh Bình", "Thanh Hóa",
        "Nghệ An", "Hà Tĩnh", "Quảng Bình", "Quảng Trị", "Thừa Thiên Huế", "Đà Nẵng", "Quảng Nam", "Quảng Ngãi",
        "Bình Định", "Phú Yên", "Khánh Hòa", "Ninh Thuận", "Bình Thuận", "Kon Tum", "Gia Lai", "Đắk Lắk", "Lâm Đồng",
        "Tp Hồ Chí Minh", "Bà Rịa Vũng Tàu", "Bình Dương", "Bình Phước", "Đồng Nai", "Tây Ninh", "An Giang",
        "Bạc Liêu", "Bến Tre", "Cà Mau", "Cần Thơ", "Đồng Tháp", "Hậu Giang", "Kiên Giang", "Long An", "Sóc Trăng",
        "Tiền Giang", "Trà Vinh", "Vĩnh Long"
    ]
    
    mahs_counter = 1
    for i in range(1, num_rows_hs + 1):
        mahs = str(i).zfill(7)                  # mahs sẽ hiển thị từ 000001 (6 chữ số ) cho tới 7 chữ số ( 1.000.000 trở lên ) 
        ho = random.choice(ho_list)             # lấy từ ds trên và tạo ngẫu nhiên
        ten = random.choice(ten_list)           # lấy từ ds trên và tạo ngẫu nhiên 
        age = random.randint(3, 18)             # tạo bắt đầu từ 3 tuổi đến 18 tuổi
        today = date.today()                    #  lấy theo thời gian thực
        ntns = today - timedelta(days=age*365)  # năm sinh bắt đầu từ năm nay,
        ntns = ntns.strftime("%d-%m-%Y")        # hiển thị thứ tự năm sinh
        
        cccd = None                             # tạo cccd là NULL nếu như chưa đủ tuổi có cccd
        
        if age >= 14:                           # kiểm tra nếu đủ tuổi thì tạo cccd
           cccd = check_unique_of_cccd(cccds)
           cccds.add(cccd)
        
        dchi_hs = random.choice(dchi_list)
        
        data.append((mahs, ho, ten, cccd, ntns, dchi_hs))       # thêm các trường đã tạo vào data chứa dữ liệu 
    
    return data

def create_data_hoc(truong_data, hs_data):                      # được tạo từ dữ liệu từ bảng HS và bảng TRƯỜNG     
    data = []                                                   # chứa các trường được tạo 
    
    for hs in hs_data:      
        matr = random.choice(truong_data)[0]                    # mahs trong HOC tham chiếu lấy từ bảng HS
        mahs, ho, ten, cccd, ntns, dchi_hs = hs                 # lấy 2 trường mahs, ntns từ bảng HS , ho, ten, cccd, diachi không dùng trong bảng này
        
        today = date.today()                                    
        year_of_birth = int(ntns.split("-")[-1])
        
        num_years = random.randint(1, 3)                                            # lấy ngẫu nhiên từ 1 tới 3 năm học         
        start_year = today.year - num_years + 1                                     #  ứng với từ 1 tới 3 của 1 HS trong bảng HOC    
        namhoc_list = [str(year) for year in range(start_year, today.year + 1)]     # ví dụ 1 hs có thể học tại 1 trường từ (chỉ năm 2019) 
                                                                                    # đến hoặc (19,20) hoăc cả 19,20,21
        for namhoc in namhoc_list:
            diemtb = round(random.uniform(0, 10), 2)                                # diemtb là số thực ( 2 chữ số thập phân)
                                                                                    # tạo từ 0.00 đến 10 
            if diemtb >= 9:                                                         # if else là ràng buộc về khoản để xét tới xếploai, kqua đạt hay không đạt
                xeploai = "Xuất sắc"
                kqua = "Hoàn thành"
            elif diemtb >= 8:
                xeploai = "Giỏi"
                kqua = "Hoàn thành"
            elif diemtb >= 6.5:
                xeploai = "Khá"
                kqua = "Hoàn thành"
            elif diemtb >= 5:
                xeploai = "Trung bình"
                kqua = "Hoàn thành"
            else:
                xeploai = "Yếu"
                kqua = "Chưa hoàn thành"
            
            data.append((matr, mahs, namhoc, diemtb, xeploai, kqua))                #thêm vào data các trường thông tin 
    
    return data

#================================== Số dòng dữ liệu tạo theo yêu cầu đề bài ============================

num_rows_truong = 100                                 # tạo ít nhất 100 dòng cho bảng trường theo đề bài 
num_row_hs =1000000                                   # tạo ít nhất 1 triệu dòng cho bảng hs theo đề bài 

#====================================================================================

truong_data = create_truong(num_rows_truong)          # truyền số dòng truong để tạo ở trên
hs_data = create_hs_data(num_row_hs)                    # truyền số dòng hs để tạo ở trên       
hoc_data = create_data_hoc(truong_data, hs_data)        # truyền dữ liệu từ 2 bảng vào bảng HOC
#====================================================================================
                                                        # In ra dữ liệu


#===============Phần kết nối đến cơ sở dữ liệu SQL để insert dữ liệu từ code python đã tạo ở trên vào trong file SQL CreateSchema1===============
# Kết nối tới cơ sở dữ liệu
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123cmnr123',
    database='TRUONGHOC1',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor,
    connect_timeout=600000
)

try:                                                                        # thực hiện tạo 
    # Tạo đối tượng Cursor
    cursor = connection.cursor()
    cursor.execute("SET GLOBAL max_execution_time = 60000")                 # set thời gian chờ thực thi câu lệnh cho TH dữ liệu đầu vào lớn 
    cursor.execute("SET GLOBAL max_allowed_packet = 1024288000")            # Giới hạn tài nguyên cấp cho SQL ( hơn 1GB cho thoải mái )
    cursor.execute("SET NAMES utf8")                                        # để tránh lỗi form chữ trong SQL 
    
                                                                            # Nạp dữ liệu vào bảng TRUONG
    truong_data = create_truong(num_rows_truong)
    cursor.executemany("INSERT INTO TRUONG (MATR, TENTR, DCHITR) VALUES (%s, %s, %s)", truong_data)
    
                                                                            # Nạp dữ liệu vào bảng HS
    hs_data = create_hs_data(num_row_hs)
    cursor.executemany("INSERT INTO HS (MAHS, HO, TEN, CCCD, NTNS, DCHI_HS) VALUES (%s, %s, %s, %s, STR_TO_DATE(%s, '%%d-%%m-%%Y'), %s)", hs_data)
    
    
    cursor.execute("SELECT MATR FROM TRUONG")                               # Truy vấn để lấy danh sách giá trị MATR từ bảng TRUONG
    matr_values = cursor.fetchall()
    matr_set = {row['MATR'] for row in matr_values}                         # Chuyển đổi MATR thành một tập hợp (set) 
                                                                            # để loại bỏ các giá trị trùng lặp
    hoc_data = create_data_hoc(truong_data, hs_data)
    valid_hoc_data = []                                                     # chứa các thông tin các trường thuộc tính

    for matr, mahs, namhoc, diemtb, xeploai, kqua in hoc_data:
        if matr in matr_set:
                                                                            # Kiểm tra trùng lặp trước khi chèn vào bảng HOC
            cursor.execute("SELECT * FROM HOC WHERE MATR = %s AND MAHS = %s AND NAMHOC = %s", (matr, mahs, namhoc))
            if cursor.fetchone() is None:
                valid_hoc_data.append((matr, mahs, namhoc, diemtb, xeploai, kqua))

    if valid_hoc_data:
        cursor.executemany("INSERT INTO HOC (MATR, MAHS, NAMHOC, DIEMTB, XEPLOAI, KQUA) VALUES (%s, %s, %s, %s, %s, %s)", valid_hoc_data)
        
        connection.commit()                                                  # Commit các thay đổi vào cơ sở dữ liệu
        print("Nạp dữ liệu thành công")
    else:
        print("Không có dữ liệu hợp lệ để nạp vào bảng HOC")
    
except pymysql.Error as error:
    print(f"Lỗi khi nạp dữ liệu vào cơ sở dữ liệu: {error}")                  # khối lệnh trên để hiển thị thông báo khi tiến hành nạp dữ liệu
finally:                                                                      # vào trong SQL , nếu có phát sinh lỗi thì có thể 
                                                                              # dễ dàng debug các lỗi, thuận tiện cho quá trình insert dữ liệu
    connection.close()                                                        # Đóng kết nối


#==================================== Tiến hành nạp dữ liệu vào TRUONGHOC2 =========================================

# Kết nối tới cơ sở dữ liệu TRUONGHOC2
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123cmnr123',
    database='TRUONGHOC2',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
 # Tạo đối tượng Cursor cho TRUONGHOC2
cursor2 = connection.cursor()
# Tạo đối tượng Cursor
cursor = connection.cursor()
cursor.execute("SET GLOBAL max_execution_time = 60000")                         # set thời gian chờ thực thi câu lệnh cho TH dữ liệu đầu vào lớn 
cursor.execute("SET GLOBAL max_allowed_packet = 10242800000")                     # Giới hạn tài nguyên cấp cho SQL ( hơn 1GB cho thoải mái )
cursor.execute("SET NAMES utf8")                                                # thiết lập form chữ utf8 để tránh lỗi form 

cursor.execute("INSERT INTO TRUONG SELECT * FROM TRUONGHOC1.TRUONG")            # thêm các dữ liệu từ TRUONGHOC1 vào TRUONGHOC2
cursor.execute("INSERT INTO HS SELECT * FROM TRUONGHOC1.HS")
cursor.execute("INSERT INTO HOC SELECT * FROM TRUONGHOC1.HOC")
connection.commit()                                                                # THỰC THI                                       

