# WebDriver offers total three APIs to take screenshot of a web page.
#
# save_screenshot(‘filename’)
# get_screenshot_as_file(‘filename’)
# get_screenshot_as_png()
# First two APIs are used to take and store screenshots as ‘.png’ files.
#
# Third API, get_screenshot_as_png(), returns a binary data. This binary data will create an image in memory and
# can be useful if we want to manipulate before saving it.


# An important note to store screenshots is that save_screenshot(‘filename’) and get_screenshot_as_file(‘filename’)
# will work only when extension of file is ‘.png’

from selenium import webdriver
from time import sleep
from PIL import Image
browser = webdriver.Chrome() 
browser.get("https://www.lambdatest.com/feature") 
sleep(1) 
# <input pseudo="-internal-media-controls-overlay-cast-button" type="button" aria-label="play on remote device" style="display: none">
featureElement = browser.find_element_by_xpath("//section[contains(string(),'START SCREENSHOT TESTING')]")
location = featureElement.location
size = featureElement.size
browser.save_screenshot("fullPageScreenshot.png")


left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

fullImg = Image.open("fullPageScreenshot.png")
cropImg = fullImg.crop((int(left), int(top), int(right), int(bottom)))

# cropImg.show()
cropImg.save('cropImage.png') 
browser.quit()  

#--------------------------------------------------
from io import StringIO
driver = webdriver.Firefox()

driver.get("https://www.facebook.com/")

driver.save_screenshot('screenshot_1.png')

driver.get_screenshot_as_file('screenshot_2.png')

screenshot = driver.get_screenshot_as_png()    
screenshot_size = (20, 10, 480, 600)

# image = Image.open(StringIO(screen))
# region = image.crop(screenshot_size)
# region.save('screenshot_3.jpg', 'JPEG', optimize=True)
#
#-------------------------------------------------