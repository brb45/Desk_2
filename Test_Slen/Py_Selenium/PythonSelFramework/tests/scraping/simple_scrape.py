from selenium import webdriver
# from selenium.webdriver.firefox.options import  Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

opts= Options()
opts.headless = True
assert opts.headless
# browser = webdriver.Firefox(options=opts)
browser = webdriver.Chrome(options=opts)

browser.get("https://duckduckgo.com")
name_field = browser.find_element(By.ID,"search_form_input_homepage")
name_field.clear()
name_field.send_keys("real python")
print(name_field.get_attribute("value"))
name_field.submit()

# <div id="r1-0" class="result results_links_deep highlight_d result--url-above-snippet" data-domain="realpython.com" data-hostname="realpython.com" data-nir="1" xpath="1"><div class="result__body links_main links_deep"><h2 class="result__title" style=""><a class="result__a" rel="noopener" href="https://realpython.com/"><b>Real</b> <b>Python</b></a><a rel="noopener" class="result__check" href="https://realpython.com/"><span class="result__check__tt">Your browser indicates if you've visited this link</span></a></h2><div class="result__extras js-result-extras"><div class="result__extras__url"><span class="result__icon "><a href="/?q=real%20python+site:realpython.com&amp;va=z&amp;t=hk" title="Search domain realpython.com" class="js-result-extras-site_search"><img data-src="//external-content.duckduckgo.com/ip3/realpython.com.ico" height="16" width="16" title="Search domain realpython.com" class="result__icon__img js-lazyload-icons" src="//external-content.duckduckgo.com/ip3/realpython.com.ico"></a></span><a href="https://realpython.com/" rel="noopener" class="result__url js-result-extras-url"><span class="result__url__domain">https://realpython.com</span><span class="result__url__full"></span></a></div></div><div class="result__snippet js-result-snippet">At <b>Real</b> <b>Python</b> you can learn all things <b>Python</b> from the ground up. If you're wondering where to begin your <b>Python</b> journey, click the button below and we'll give you some guidance: Start Your <b>Python</b> Journey »</div></div></div>
results = browser.find_elements_by_class_name('result')
print(results[0].text)
print(results[0].get_property("id")) # r1-0
print()

# result = browser.find_element_by_id("r1-0")
# print(result.text)


browser.get("https://bandcamp.com")
play_field =  browser.find_element_by_class_name("playbutton")
# play_field.click()

tracks = browser.find_elements(By.CLASS_NAME,  "discover-item")
print(f"len(tracks) is {len(tracks)}")
tracks[3].click()
time.sleep(10)