from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
p_global = None
def all_p(li):
    
    global p_global
    # all_p = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('log-level=3')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-notifications")

    
    driver = webdriver.Chrome(options=options)
    driver.minimize_window()
    driver.get(li)
    # print(driver)
    driver.implicitly_wait(20)
    
    all_p = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "p")))
    all_para = []
    # print(driver)
    count = 0

    for i in range(len(all_p)):
        try:

            all_para.append(all_p[i].text)
            count+=1
        except IndexError as e:
                print(e)
        except Exception as ee :
            try:
                all_p = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "p")))
                all_para.append(all_p[i].text)
            except Exception as p :
                print(p)
    
    p_global = all_para
    driver.quit()
    return p_global
body_global = None
def body_text(li):
    
    global body_global
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument('--headless')
    options.add_argument('log-level=3')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-cookies')
    
    
    driver = webdriver.Chrome(options=options)
    driver.minimize_window()

    driver.get(li)
    driver.implicitly_wait(10)
    text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body"))).text

    body_global = list(text.splitlines())
    # print(text.splitlines())
    driver.quit()
    return body_global
links_global =None
def link_founder(li:str):
    global links_global
    all_links = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--disable-notifications")
    options.add_argument('log-level=3')
    
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    
    
    driver = webdriver.Chrome(options=options)
    driver.minimize_window()
    driver.implicitly_wait(20)
    driver.get(li)

    # global all_links
    # driver.get(li)
    
    # driver = driverr.get(url=li)
    count = 0
    a_tags = driver.find_elements(By.TAG_NAME,'a')
    # len = a
    s =  str(li)
    ll = 'https://'
    com = str(s[0:int(str(s[8:]).find('/'))+len(ll)]).strip()
    
    # all_links = []
    for  i in range(len(a_tags)):
        # print(count)
        try:
            if str(a_tags[i].get_attribute('href')) is not  None and not str(a_tags[i].get_attribute('href')).startswith("#"):
                if not str(a_tags[i].get_attribute('href')).startswith('https:/') and not str(a_tags[i].get_attribute('href')).startswith('http:/') and not str(a_tags[i].get_attribute('href')).startswith('//www'):
                    value = com+str(a_tags[i].get_attribute('href')).strip()
                    if value not in all_links:
                        all_links.append(value)
                        count+=1
                    else:
                        count+=1
                    # print(value)
                else:
                    all_links.append(str(a_tags[i].get_attribute('href')))
                    count+=1
            else:
                # print(i)
                
                pass
        except IndexError as ee:
            print(e)
        except Exception as e:
            print('all again')
            # print(e)
            try:
                a_tags = driver.find_elements(By.TAG_NAME,'a')
                if str(a_tags[i].get_attribute('href')) is not  None and not str(a_tags[i].get_attribute('href')).startswith("#"):
                    if not str(a_tags[i].get_attribute('href')).startswith('https:/') and not str(a_tags[i].get_attribute('href')).startswith('http:/') and not str(a_tags[i].get_attribute('href')).startswith('//www'):
                        value = com+str(a_tags[i].get_attribute('href')).strip()
                        if value not in all_links:
                            all_links.append(value)
                            count+=1
                        else:
                            count+=1
                        # print(value)
                    else:
                        all_links.append(str(a_tags[i].get_attribute('href')))
                        count+=1
                else:
                    # print(i)
                    
                    pass
            except Exception as eee:
                print(eee)
                print('error can\'t solve')
                
    driver.close()
    # driver.quit()
    links_global= all_links
    return links_global
url = 'https://mitsubishisolutions.com/the-role-of-artificial-intelligence-in-smart-packaging-lines/'
body_text(url)
link_founder(url)
all_p(url)
print(p_global)

print(links_global)
print(body_global)