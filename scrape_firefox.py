from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests
import os.path


q = 'doom'
url = f'https://www.google.com/search?&tbm=isch&q={q}'
num = 10

driver = webdriver.Firefox()
driver.get(url)

# 3.1: initialize folders
if not os.path.isdir('pic'):
    os.mkdir('pic')
if not os.path.isdir(q):
    os.mkdir(f'pic/{q}')

# 1st: load page untill number of picture reachs requirement

elems = driver.find_elements_by_css_selector("img.Q4LuWd")
num_count = len(elems)
while num_count < num:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    driver.implicitly_wait(5)
    elems = driver.find_elements_by_css_selector("img.Q4LuWd")
    num_count = len(elems)
selected = driver.find_elements_by_css_selector("img.Q4LuWd")[:num]


# 2nd: get url of all
def image_loaded(driver):
    number = driver.execute_script("return document.images.length")
    return all(driver.execute_script(f"return document.images[{i}].complete") for i in range(number))


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
    #print(image)

    r = requests.get(image)

    path = f'pic/{q}/{i}.jpg'
    
    with open(path, 'wb') as f:
        f.write(r.content)

driver.close()
