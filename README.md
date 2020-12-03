# Customdriver (chrome)
- Khởi tạo webdriver(chrome) giống với người dùng nhất có thể, bằng cách xóa các tham số mặc định, thêm hồ sơ người dùng.
- Các phương thức với chromedriver(chrome) giảm thiểu code.

## Cách dùng:
- ### customdriver
```python
#!python 3.6.7
from customdriver import webdriver

driver = webdriver.Chrome(profile="chrome_user_data_dir", executable_path="YOUR_CHROMEDIRVER_PATH")
driver.get("chrome://version")
#can edit args command-lines at customdriver/webdriver/chrome/webdriver (COMMAND_LINDES_TO_REMOVE, ..ADD)
```
- ### custommethods
```python
from customdriver import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(profile="chrome_user_data_dir", executable_path="YOUR_CHROMEDIRVER_PATH")
cm = webdriver.CustomMethods(driver=driver)

ele = cm.wait_until_clickable((By.ID, "v112"), 15)
#if TimeoutException raised => ele = False

ele2 = cm.find_element((By.ID, "v112"))
#if NoSuchElementException raise => ele2 = False

```