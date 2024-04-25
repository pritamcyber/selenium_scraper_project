from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver

# we are importing this for sending any key over any input or to press it  doing some key interaction 
import selenium.webdriver.chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import  numpy  as np
import threading
from collections import OrderedDict
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException
import selenium.webdriver.remote.webelement

import time

# from threading import thread

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-cookies')
# options.add_experimental_option("prefs", {"profile.default_content_set/ting_values.cookies": 2})
driver = webdriver.Chrome(options=options)

url = 'https://mitsubishisolutions.com/the-role-of-artificial-intelligence-in-smart-packaging-lines/'
driver.get(url=url)
driver.implicitly_wait(20)
# print(driver.find_element(By.TAG_NAME,'iframe'))

all_links = []
all_images = []
all_para = []
all_h = []
text_list = []

def driver_setup():
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('log-level=3')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(20)
    url = 'https://mitsubishisolutions.com/the-role-of-artificial-intelligence-in-smart-packaging-lines/'

    driver.get(url)

    return driver

def link_founder(driver,li:str):
    # driver = driverr.get(url=li)
    count = 0
    a_tags = driver.find_elements(By.TAG_NAME,'a')
    # len = a
    s =  str(li)
    ll = 'https://'
    com = str(s[0:int(str(s[8:]).find('/'))+len(ll)]).strip()
    
    # all_links = []
    for  i in range(len(a_tags)):
        print(count)
        try:
            if str(a_tags[count].get_attribute('href')) is not  None and not str(a_tags[count].get_attribute('href')).startswith("#"):
                if not str(a_tags[count].get_attribute('href')).startswith('https:/') and not str(a_tags[count].get_attribute('href')).startswith('http:/') and not str(a_tags[count].get_attribute('href')).startswith('//www'):
                    value = com+str(a_tags[count].get_attribute('href')).strip()
                    if value not in all_links:
                        all_links.append(value)
                        count+=1
                    else:
                        count+=1
                    # print(value)
                else:
                    all_links.append(str(a_tags[count].get_attribute('href')))
                    count+=1
            else:
                # print(i)
                
                pass
        except IndexError as ee:
            print(e)
        except Exception as e:
            print('all again')
            # print(e)
            a_tags = driver.find_elements(By.TAG_NAME,'a')
    
  
def all_h(driverr,li):
    driver = driverr.get(url=li)
    
    for i in driver.find_elements(By.TAG_NAME,"h"):
        all_h.append(i.text)
    for i in driver.find_elements(By.TAG_NAME,"h2"):
        all_h.append(i.text)
    for i in driver.find_elements(By.TAG_NAME,"h3"):
        all_h.append(i.text)
    for i in driver.find_elements(By.TAG_NAME,"h3"):
        all_h.append(i.text)
    for i in driver.find_elements(By.TAG_NAME,"h3"):
        all_h.append(i.text)
    for i in driver.find_elements(By.TAG_NAME,"h3"):
        all_h.append(i.text)
  
def all_p(driverr,li):
    driver = driverr.get(url=li)
    print(driver)
    # driver.find_elements(By.TAG_NAME, "p")
    all_para = []
    print(driver)
    for i in driver.find_elements(By.TAG_NAME, "p"):
        print('start')
        
        print('alfa')
        
        all_para.append(i.text)
        print(i.text)
    print(all_para)
    return all_para
                      
def image_link_founder(driver,li:str):
    # driver = driverr.get(url=li)
    s =  str(li)
    img = driver.find_elements(By.TAG_NAME,'img')
    ll = 'https://'
    com = str(s[0:int(str(s[8:]).find('/'))+len(ll)]).strip()
    # img_tags=driver.find_elements(By.TAG_NAME,'img')
    count = 0
    for i in range(len(img)):
        # print('image')
        # print(i.get_property('src'))
        # print(i.get_property('data-src'))
        # img[i]
        try:
            if img[i].get_property('data-src') is not None:                
                    
                if not str(img[i].get_property('data-src')).startswith('https:/') and not str(img[i].get_property('data-src')).startswith('http:/') :
                    value = com+str(img[i].get_property('data-src')).strip()
                    all_images.append(value)
                    # print(value)
                    count+=1
                    
                else:
                    all_images.append(str(img[i].get_property('data-src')))
                    count+=1
                        
            elif img[i].get_property('src') is not None:
                
                if not str(img[i].get_property('src')).startswith('https:/') and not str(img[i].get_property('src')).startswith('http:/') :
                    value = com+str(img[i].get_property('src')).strip()
                    all_images.append(value)
                    print(value)
                    count+=1
                    
                else:
                    all_images.append(str(img[i].get_property('src')))
                    count+=1
        
            elif img[i].get_property('data-lsrc'):
                
                if not str(img[i].get_property('data-lsrc')).startswith('https:/') and not str(img[i].get_property('data-lsrc')).startswith('http:/') :
                    value = com+str(img[i].get_property('data-lsrc')).strip()
                    all_images.append(value)
                    count+=1
                else:
                    all_images.append(str(img[i].get_property('data-lsrc')))
                    count+=1
            else:
                print(img[i])
        except IndexError as e:
            print(e)
        except Exception as ee :
            img = driver.find_elements(By.TAG_NAME,'img')
            print('all_again')
            # print(ee)
            
            
    
        
 
def add(a,b):
    print(a+b)
# drivers = [driver_setup() for _ in range(3)]
driver1 = driver_setup()
driver2 = driver_setup()
# chunks = np.array_split(np.arange(1,126), 4)

functions = [link_founder,image_link_founder,all_p]


thread1 =  threading.Thread(target=lambda:link_founder(driver1,url))
# thread2 =  threading.Thread(target=lambda:image_link_founder(driver2,url))

# thread3 =  threading.Thread(target=lambda: add(7,3))


# thread1 = threading.Thread(target=lambda:link_founder(driver,url))
# thread2 = threading.Thread(target=lambda:image_link_founder(drivers[1],url))
# thread3 = threading.Thread(target=lambda:all_p(drivers[2],url))

# Start all threads
# thread2.start()
# thread3.start()
thread1.start()


# Wait for all threads to complete
# thread2.join()
# thread3.join()
thread1.join()
print(all_links)
driver1.quit()

# link_founder(driver,url)
# print(all_links)

# print(list(OrderedDict.fromkeys(all_links)))
# print(len(all_links))

# with ThreadPoolExecutor(max_workers=6) as executor:
    
#     for driver,fun in zip(drivers,functions):
#         print(fun)
#         executor.submit(fun, driver,url)
#     print(executor.)
        
# print(all_links)
        
    # image = executor.submit(image_link_founder, driver,url)
    # p = executor.submit(all_p,driver,url)
    # futures.append(executor.submit(fibonacci, 8))

    # Wait for all tasks to complete and get results
    # results = [future.result() for future in futures]
    
    
    # bucket = executor.map(crawler, chunks, drivers)
    # results = [item for block in bucket for item in block]
    






# image_link_founder(driver,url)
# print(all_images)
# thread1.join()


# def body_text(driver,li)-> list:
#     text = driver.find_element(By.XPATH, "/html/body").text
#     return text.splitlines()
    
# print(body_text(driver_setup(),url))

# for number in range(number_of_threads):
#     t = Thread(target=func, args=(number,)) # get number for place in list `buttons`
#     t.start()
#     threads.append(t)
#     buttons.append(False) # create place 

# for t in threads:
#     t.join()

# time.sleep(15)



# driver.quit()