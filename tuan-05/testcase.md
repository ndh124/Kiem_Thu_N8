Kịch bản kiểm thử (Test Cases) - Chức năng Đăng nhập

Hệ thống: Swag Labs (https://www.saucedemo.com)
Mục tiêu: Kiểm tra chức năng đăng nhập với các trường hợp dữ liệu khác nhau.

Test Case 1: Đăng nhập thành công với tài khoản hợp lệ

    Mô tả: Kiểm tra hệ thống cho phép người dùng đăng nhập khi nhập đúng tên đăng nhập và mật khẩu.

    Các bước thực hiện:

        Mở trình duyệt và truy cập vào trang chủ Swag Labs.

        Nhập tên đăng nhập hợp lệ vào ô "Username".

        Nhập mật khẩu hợp lệ vào ô "Password".

        Bấm vào nút "Login".

        Dữ liệu kiểm thử (Test Data):

            Username: standard_user

            Password: secret_sauce

    Kết quả mong đợi:

        Người dùng đăng nhập thành công.

        Trang web chuyển hướng sang trang Danh sách sản phẩm (Inventory).

Test Case 2: Đăng nhập thất bại với tài khoản bị khóa

    Mô tả: Kiểm tra hệ thống chặn đăng nhập và hiển thị lỗi khi sử dụng tài khoản đã bị khóa (locked out).

    Các bước thực hiện:

        Mở trình duyệt và truy cập vào trang chủ Swag Labs.

        Nhập tên đăng nhập của tài khoản bị khóa.

        Nhập đúng mật khẩu của tài khoản đó.

        Bấm vào nút "Login".

        Dữ liệu kiểm thử (Test Data):

            Username: locked_out_user

            Password: secret_sauce

    Kết quả mong đợi:

        Đăng nhập thất bại, hệ thống ở nguyên trang đăng nhập.

        Hiển thị thông báo lỗi màu đỏ: "Epic sadface: Sorry, this user has been locked out."

Test Case 3: Đăng nhập thất bại khi sai mật khẩu

    Mô tả: Kiểm tra hệ thống báo lỗi khi người dùng nhập đúng tên đăng nhập nhưng sai mật khẩu.

    Các bước thực hiện:

        Mở trình duyệt và truy cập vào trang chủ Swag Labs.

        Nhập tên đăng nhập hợp lệ.

        Nhập một mật khẩu sai.

        Bấm vào nút "Login".

        Dữ liệu kiểm thử (Test Data):

            Username: standard_user

            Password: mat_khau_sai_123

    Kết quả mong đợi:

        Đăng nhập thất bại.

        Hiển thị thông báo lỗi: "Epic sadface: Username and password do not match any user in this service."