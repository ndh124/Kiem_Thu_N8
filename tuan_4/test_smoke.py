from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

try:
    # Mở ứng dụng Swag Labs
    driver.get("https://www.saucedemo.com/")

    # Đợi tối đa 5 giây để phần tử xuất hiện và tìm ô username
    wait = WebDriverWait(driver, 5)
    username_field = wait.until(EC.presence_of_element_located((By.ID, "user-name")))

    # Kiểm tra xem ô nhập có hiển thị không
    assert username_field.is_displayed(), "Không tìm thấy ô nhập tên đăng nhập!"
    print("✅ TEST THÀNH CÔNG: Đã tìm thấy ô nhập tên đăng nhập.")

finally:
    driver.quit()