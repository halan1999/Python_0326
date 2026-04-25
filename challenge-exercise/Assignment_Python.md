# 🚀 BÀI TẬP LỚN: HỆ THỐNG QUẢN LÝ NHÂN SỰ & TÍNH LƯƠNG TEAM DỰ ÁN

Chào mừng bạn đến với bài tập lớn của khóa học Python Core! 🔥 
Trong bài tập này, bạn sẽ không chỉ viết code mà còn hóa thân thành một **Team Leader** thực thụ. Nhiệm vụ của bạn là xây dựng một phần mềm Console Application giúp tự động hóa quá trình phân bổ nhân sự và tính lương cho dự án mới.

Hãy sẵn sàng áp dụng mọi kiến thức đã học, từ cấu trúc dữ liệu, vòng lặp, hàm, cho đến xử lý file và bẫy lỗi ngoại lệ. Chúc bạn code thật "mượt" và không gặp bug nào "khó nhằn"! 💻✨

---

## 🎯 A. BỐI CẢNH & NGHIỆP VỤ HỆ THỐNG

Một dự án mới đang được khởi động và team của bạn cần **6 thành viên**. Để đảm bảo tiến độ, dự án yêu cầu cơ cấu nhân sự gồm 4 cấp độ:
- **Senior:** > 5 năm kinh nghiệm
- **Middle:** 3 - 5 năm kinh nghiệm
- **Junior:** 1 - 3 năm kinh nghiệm
- **Fresher:** < 1 năm kinh nghiệm

**Tài nguyên của bạn:** Phòng HR đã gửi cho bạn một file dữ liệu (ví dụ: `list-member.json`) chứa thông tin của 6 nhân sự đang "available". Tuy nhiên, dữ liệu này ban đầu chưa được phân bổ vai trò.

**Nhiệm vụ cốt lõi:**
1. **Phân loại tự động:** Dựa vào số năm kinh nghiệm từ file HR, tự động gán vai trò tương ứng cho từng người.
2. **Quản lý chấm công & Tính lương:** Ghi nhận số ngày công đi làm và tính lương cho team theo công thức sau:

> **💰 Công thức tính lương 1 tháng:** 
> `Lương = (Số ngày thực đi làm / Tổng số ngày làm việc trong tháng) * Hệ số lương * Lương cơ bản`

**Thông tin phục vụ tính lương:**
*   **Lương cơ bản:** 500 USD (Có thể điều chỉnh tùy công ty).
*   **Quy định ngày làm việc:** Công ty nghỉ Thứ 7 và Chủ Nhật. *(Tổng số ngày làm việc trong tháng = Tổng số ngày của tháng - số ngày Thứ 7, Chủ Nhật).*
*   **Hệ số lương theo vị trí:**
    *   👑 **Leader:** 3.5
    *   🌟 **Senior:** 5.0
    *   🚀 **Middle:** 2.5
    *   🌱 **Junior:** 1.5
    *   🐣 **Fresher:** 1.0

*(Chú ý: Mức lương Senior cao hơn Leader là một bài toán thực tế ở nhiều công ty chuyên về kỹ thuật!)*

---

## 🖥️ B. TỔNG QUAN CHƯƠNG TRÌNH

Phần mềm của bạn cần đáp ứng các tính năng chính sau:
1. **Khởi tạo dữ liệu:** Tự động phân chia vai trò dựa trên kinh nghiệm và lưu ra một file dữ liệu mới (Tuyệt đối không ghi đè làm hỏng file gốc của HR).
2. **Hiển thị danh sách:** Liệt kê danh sách thành viên trực quan dưới dạng bảng.
3. **Cập nhật thông tin:** Cho phép cập nhật vai trò (Role) của thành viên. *Lưu ý: Chỉ cập nhật các trường đã có sẵn, không tự ý thêm trường dữ liệu khác ngoài yêu cầu.*
4. **Chấm công & Tính lương:** Tính toán lương cho **tháng trước** (Tháng hiện tại - 1) của toàn bộ nhân viên.
5. **Tra cứu:** Tìm kiếm và in ra phiếu lương chi tiết của một nhân viên bất kỳ.

---

## 🛠️ C. YÊU CẦU CHI TIẾT TỪNG CHỨC NĂNG

### 1. Màn hình Khởi động (Start Screen)
Khi chạy chương trình, giao diện đầu tiên cần hiển thị:

```text
|*** PHẦN MỀM QUẢN LÝ THÔNG TIN THÀNH VIÊN TEAM DỰ ÁN ***|
|                                                        |
|************* [1. START] ----- [2. CANCEL] *************|
|                                                        |
|********************************************************|
|                                                        |
XIN MỜI BẠN NHẬP LỰA CHỌN: 
```
*   Nhập `1` (START): Chương trình chạy ngầm chức năng tự động phân chia vai trò theo kinh nghiệm, cập nhật vào file dữ liệu **MỚI**, sau đó chuyển sang Màn hình Menu Chính.
*   Nhập `2` (CANCEL): Thoát chương trình lập tức.

### 2. Màn hình Menu Chính (Main Menu)
```text
|*** PHẦN MỀM QUẢN LÝ THÔNG TIN THÀNH VIÊN TEAM DỰ ÁN ***|
|                                                        |
|***************** Xin mời bạn lựa chọn *****************|
|                                                        |
| 1. In danh sách Member khả dụng                        |
| 2. Cập nhật vai trò Member                             |
| 3. Tính toán tiền lương tháng trước                    |
| 4. Tìm kiếm thông tin tiền lương                       |
| 0. Exit                                                |
|                                                        |
|********************************************************|
|                                                        |
XIN MỜI BẠN NHẬP LỰA CHỌN: 
```

### 3. Chi tiết các lựa chọn Menu

#### 🟢 Option 1: In danh sách Member khả dụng
Hiển thị danh sách nhân sự hiện tại theo format bảng:
```text
|  IDs  |        Tên      | Tuổi | Kinh nghiệm | Vai trò |
|-------|-----------------|------|-------------|---------|
| MB-01 | Nguyễn Nam Khoa |  30  |    5 năm    | Senior  |
...
```
Sau khi in bảng, hệ thống hiển thị câu hỏi: `Back (Y/N)?`
*   Nhập `Y` hoặc `y`: Trở lại Menu Chính ban đầu.
*   Nhập `N` hoặc `n`: Giữ nguyên màn hình và hiển thị lại câu hỏi `Back (Y/N)?`.
*   Nhập ký tự khác: Báo lỗi `"Giá trị bạn lựa chọn không hợp lệ! Yêu cầu nhập lại"` sau đó hiển thị lại `Back (Y/N)?`.

#### 🟡 Option 2: Cập nhật vai trò Member
Quy trình thực hiện:
1.  Hệ thống yêu cầu: `"Xin mời bạn nhập ID: "`
2.  **Kiểm tra ID:**
    *   **Sai ID (Không có trong file):** Thông báo `"Giá trị ID không tồn tại! Bạn có muốn tiếp tục (Y/N): "`. 
        * Nhập `Y`/`y` -> Hỏi lại ID; Nhập `N`/`n` -> Về Menu Chính.
    *   **Đúng ID:** In thông tin hiện tại của Member (ID, Tên, Vai trò hiện tại) và hiển thị prompt `"Vai trò muốn gán cho Member: "`.
3.  **Kiểm tra Vai trò nhập vào:**
    *   **Vai trò không tồn tại (Theo nghiệp vụ bài toán):** Thông báo `"Vai trò bạn chọn không có trong danh sách! Xin mời nhập lại: "`.
    *   **Vai trò hợp lệ (Bình thường):** Cập nhật thành công. Thông báo `"Cập nhật thành công! Bạn có muốn tiếp tục (Y/N): "`.
    *   **⚠️ TRƯỜNG HỢP ĐẶC BIỆT - Thay tướng (Gán role Leader):** 
        *   Nếu trong team **đã có** một thành viên khác đang làm Leader, phải cảnh báo: `"Đã có <Tên Leader Cũ> đang làm Leader! Bạn có vẫn muốn chọn <Tên Member Mới> làm Leader (Y/N): "`
        *   Nếu **Đồng ý (Y/y)**:
            *   Gán vai trò `Leader` cho người mới.
            *   Cập nhật vai trò của Leader cũ về lại **vai trò trước đó** của họ.
            *   Thông báo `"Cập nhật thành công! Bạn có muốn tiếp tục (Y/N): "`.
        *   Nếu **Từ chối (N/n)**: Hủy bỏ thao tác gán Leader, hệ thống hiển thị `"Bạn có muốn tiếp tục (Y/N): "` để người dùng quyết định nhập ID khác hay về Menu.

> *💡 LƯU Ý QUAN TRỌNG: Mọi cập nhật thông tin ở Option 2 phải được lưu lại. Khi thực hiện lại chức năng in danh sách (Option 1), dữ liệu in ra phải khớp đúng với những gì vừa cập nhật.*

#### 🔵 Option 3: Tính toán tiền lương tháng trước
Màn hình thực hiện chấm công hiển thị như sau:
```text
TỔNG SỐ NGÀY LÀM VIỆC CỦA THÁNG <Tháng hiện tại - 1>: <X> NGÀY 
(Chú ý: <X> là tổng số ngày làm việc thực tế, tự động loại bỏ Thứ 7 và Chủ Nhật)

Xin mời nhập số ngày của từng member:
Nhân viên MB-01
Nguyễn Nam Khoa
Số ngày thực đi làm của Member: ___

... (Tiếp tục lặp cho đến hết danh sách member)
```
*   Sau khi nhập đủ, chương trình tính toán lương.
*   **Thành công:** Thông báo `"Đã tính toán thành công!"` và tự động quay về Menu Chính.
*   **Thất bại (Có lỗi tính toán):** Thoát hẳn chương trình ngay lập tức và **không** cập nhật bất kỳ thông tin lỗi nào vào dữ liệu.

#### 🟣 Option 4: Tìm kiếm thông tin tiền lương
1.  Yêu cầu nhập ID cần tra cứu (Logic kiểm tra ID sai/đúng hoạt động giống hệt Option 2).
2.  Nếu ID tồn tại trong file dữ liệu, in ra thông tin lương theo format:
```text
+ Mã số nhân viên: MB-01
+ Tên nhân viên: Nguyễn Nam Khoa
+ Tuổi: 30
+ Vai trò: Senior
+ Hệ số lương: 5.0
+ Lương tháng <Tháng hiện tại - 1>: 2500 USD
```

#### 🔴 Option 0: Exit
Thoát hoàn toàn khỏi chương trình.

---

## 😈 D. THỬ THÁCH ẨN (HIDDEN CHALLENGES)

Yêu cầu chi tiết bên trên có thể chưa mô tả hết các "góc khuất" của hệ thống, nhưng một lập trình viên Python tương lai **bắt buộc** phải tự rèn luyện thói quen xử lý các vấn đề sau:

1.  **Kiểm soát ngoại lệ với dữ liệu đầu vào (Input Validation):** Điều gì xảy ra nếu người dùng cố tình nhập chữ vào chỗ cần nhập số (VD: Nhập số ngày đi làm là "abc")? Nhập khoảng trắng? Hãy dùng bẫy lỗi để đảm bảo chương trình luôn chạy mượt mà, không bao giờ bị văng (crash)!
2.  **Toán học thời gian:** Làm sao để thuật toán biết chính xác tháng trước có bao nhiêu ngày? Trừ đi Thứ 7, Chủ Nhật thế nào cho chuẩn xác ở mọi tháng, mọi năm? Thư viện xử lý thời gian của Python chính là chìa khóa.
3.  **Clean Code:** Thay vì nhồi nhét tất cả logic vào một file quá dài, hãy thử chia nhỏ chức năng thành các hàm (Functions), các khối module rõ ràng để dễ đọc, dễ bảo trì.

Chúc bạn vượt qua thử thách này một cách xuất sắc! Hãy tận hưởng quá trình tìm lỗi và sửa lỗi (debugging). Happy Coding! 🚀🐍
