import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginSwagLabs(unittest.TestCase):
    
    def setUp(self):
        # Khởi tạo trình duyệt Chrome trước mỗi bài test
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.wait = WebDriverWait(self.driver, 5)

    def tearDown(self):
        # Đóng trình duyệt sau khi chạy xong mỗi bài test
        self.driver.quit()

    def test_01_dang_nhap_thanh_cong(self):
        """Test Case 1: Đăng nhập với tài khoản hợp lệ"""
        # Bước 1 & 2: Nhập username và password
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # Bước 3: Bấm nút Login
        self.driver.find_element(By.ID, "login-button").click()
        
        # Bước 4: Kiểm tra kết quả (Url phải đổi sang trang inventory)
        self.wait.until(EC.url_contains("inventory.html"))
        self.assertIn("inventory.html", self.driver.current_url, "Đăng nhập thành công nhưng không chuyển trang!")
        print(" TC1 Pass: Đăng nhập thành công.")

    def test_02_tai_khoan_bi_khoa(self):
        """Test Case 2: Đăng nhập bằng tài khoản bị khóa (locked out)"""
        # Bước 1 & 2: Nhập username bị khóa và password
        self.driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # Bước 3: Bấm nút Login
        self.driver.find_element(By.ID, "login-button").click()
        
        # Bước 4: Kiểm tra thông báo lỗi xuất hiện
        error_msg = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        self.assertIn("Sorry, this user has been locked out", error_msg.text, "Thông báo lỗi tài khoản bị khóa không chính xác!")
        print(" TC2 Pass: Báo lỗi tài khoản bị khóa chính xác.")

    def test_03_sai_mat_khau(self):
        """Test Case 3: Đăng nhập với mật khẩu sai"""
        # Bước 1 & 2: Nhập username đúng và password sai
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("mat_khau_sai_123")
        
        # Bước 3: Bấm nút Login
        self.driver.find_element(By.ID, "login-button").click()
        
        # Bước 4: Kiểm tra thông báo lỗi sai mật khẩu
        error_msg = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        self.assertIn("do not match any user in this service", error_msg.text, "Thông báo lỗi sai mật khẩu không chính xác!")
        print(" TC3 Pass: Báo lỗi sai mật khẩu chính xác.")

if __name__ == "__main__":
    # Lệnh này giúp chạy tất cả các bài test trong file
    unittest.main()