from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
import os.path


q = 'forest'
url = f'https://www.google.com/search?&tbm=isch&q={q}'
num = 1000

#opt = webdriver.firefox.options.Options()
#opt.headless = True
opt = None
driver = webdriver.Firefox(options=opt)
driver.get(url)

# 3.1: initialize folders
if not os.path.isdir('pic'):
    os.mkdir('pic')
if not os.path.isdir(f'pic/{q}'):
    os.mkdir(f'pic/{q}')

# 1st: load page untill number of picture reachs requirement

driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
elems = driver.find_elements_by_css_selector("img.Q4LuWd")
num_count = len(elems)
curr_count = 0
while num_count < num:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    driver.implicitly_wait(5)
    elems = driver.find_elements_by_css_selector("img.Q4LuWd")
    num_count = len(elems)
    print(num_count)
    if curr_count == num_count:
        try:
            driver.find_element_by_css_selector("input.mye4qd").click()
        except:
            break
        try:
            driver.find_element_by_css_selector("div.DwpMZe[data-status='3']")
            break
        except:
            pass
    curr_count = num_count
    #print(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.YstHxe")))
        #driver.find_element_by_css_selector("input.mye4qd").click()
    time.sleep(2)
selected = driver.find_elements_by_css_selector("img.Q4LuWd")[:num]


# 2nd: get url of all
def image_loaded(driver):
    number = driver.execute_script("return document.images.length")
    return all(driver.execute_script(f"return document.images[{i}].complete") for i in range(number))

# 3nd: go to each element and download it
for i, img in enumerate(selected, 1):
    try:
        img.click()
        WebDriverWait(driver, 10).until(image_loaded)
        #driver.implicitly_wait(2)
        time.sleep(0.5)
    finally:
        pass
    actual_image = driver.find_element_by_xpath("//div[@class='tvh9oe BIB1wf']//img[@class='n3VNCb']")
    image = actual_image.get_attribute('src')
    print(image[:20])

    try:
        r = requests.get(image)
    except:
        continue

    path = f'pic/{q}/{i}.jpg'
    
    with open(path, 'wb') as f:
        f.write(r.content)

driver.close()
