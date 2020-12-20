
from selenium import webdriver
import io
# io.StringIO or io.BytesIO
from PIL import Image


driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com/")

# 1. use relative path
driver.save_screenshot('..\screenshot_1.png')

# 2.
driver.get_screenshot_as_file('screenshot_2.png')

# 3.
# screenshot = driver.get_screenshot_as_png()
# #
# screenshot_size = (20, 10, 480, 600)
# image = Image.open(io.StringIO(screen))
# region = image.crop(screenshot_size)
# region.save('screenshot_3.jpg', 'JPEG', optimize=True)
driver.close()
