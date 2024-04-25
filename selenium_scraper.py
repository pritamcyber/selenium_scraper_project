import pandas as pd
from pathlib import Path
from selenium import webdriver 
from selenium.webdriver.common.by import By
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# all_links= []
links_global =None
def link_founder(li:str):
    global links_global
    all_links = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--disable-notifications")
    options.add_argument('log-level=3')
    driver = webdriver.Chrome(options=options)
    driver.minimize_window()
    driver.implicitly_wait(20)
    driver.get(li)
    count = 0
    a_tags = driver.find_elements(By.TAG_NAME,'a')
    s =  str(li)
    ll = 'https://'
    com = str(s[0:int(str(s[8:]).find('/'))+len(ll)]).strip()
    
    for  i in range(len(a_tags)):
        try:
            if str(a_tags[i].get_attribute('href')) is not  None and not str(a_tags[i].get_attribute('href')).startswith("#"):
                if not str(a_tags[i].get_attribute('href')).startswith('https:/') and not str(a_tags[i].get_attribute('href')).startswith('http:/') and not str(a_tags[i].get_attribute('href')).startswith('//www'):
                    value = com+str(a_tags[i].get_attribute('href')).strip()
                    if value not in all_links:
                        all_links.append(value)
                        count+=1
                    else:
                        count+=1
                else:
                    all_links.append(str(a_tags[i].get_attribute('href')))
                    count+=1
            else:
                
                pass
        except IndexError as ee:
            print(e)
        except Exception as e:
            print('all again')
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

image_global = None
def image_link_founder(li:str):
    global image_global
    
    all_images = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--disable-notifications")
    options.add_argument('log-level=3')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    
    
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get(li)
    driver.minimize_window()
    
    # driver = driverr.get(url=li)
    s =  str(li)
    img = driver.find_elements(By.TAG_NAME,'img')
    print(len(img))
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
                    # print(value)
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
                # print(img[i])
                pass
        except IndexError as e:
            print(count,i)
            print(e)
        except Exception as ee :
            try:
                
                img = driver.find_elements(By.TAG_NAME,'img')
                print('image_error')
                
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
                        # print(value)
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
                    # print(img[i])
                    pass
            except Exception as r:
                print('this is image error can\'t be resolve')
            # print(ee)
    driver.quit()
    image_global = all_images
    return image_global

p_global = None
def all_p(li):
    
    global p_global
    # all_p = []
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('log-level=3')
   
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-notifications")

    
    driver = webdriver.Chrome(options=options)
    driver.minimize_window()
    driver.get(li)
    # print(driver)
    driver.implicitly_wait(10)
    
    all_p = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "p")))
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
    print('this is body')
    global body_global
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument('--headless')
    options.add_argument('log-level=3')
    
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

import docx
def getText(filename):
    doc = docx.Document(filename)
    # print(len(doc))
    fullText = []
    print(doc)
    for para in doc.paragraphs:
        
        s =  str(para.text)
        ll = 'https://'
        if s.startswith('https:/'):
            # print(para.text)
            fullText.append(para.text)
        else:
            if len(para.text.strip()) == 0 :
    
                pass
            else:
                heading = para.text
                fullText.append(para.text)
                # print(heading)
                pass
    return fullText



if __name__ == '__main__':
    
    
    # important
    # write your file name here which contains link only docx file  
    file_name = 'link_file.docx'
    
    links_name = getText(file_name)
    
    file_title = 'links'
    count= 0
    for i in range(len(links_name)):
        if not str(links_name[i]).strip().startswith('http'):
            file_title = str(links_name[i]).strip()
            # print(str(links_name[i]).strip())
            count = 0
                
        elif str(links_name[i]).strip().startswith('http'):
            count+=1
            # print(str(links_name[i]).strip())
            
            
            
            
        
    
  
            p= threading.Thread(target=link_founder,args=(str(links_name[i]).strip(),))
            q= threading.Thread(target=image_link_founder,args=(str(links_name[i]).strip(),))
            b= threading.Thread(target=body_text,args=(str(links_name[i]).strip(),))
            para= threading.Thread(target=all_p,args=(str(links_name[i]).strip(),))
            
            p.start()
            q.start()
            b.start()
            para.start()

            p.join()    
            q.join()
            b.join()
            para.join()
    
            
            
            link = links_global.copy()
            image = image_global.copy()
            scr = p_global.copy()
            body_t = body_global.copy()
            
            image_global.clear()
            links_global.clear()
            p_global.clear()
            body_global.clear()
            
            

            df1 = pd.DataFrame({'link':link})
            df2 = pd.DataFrame({'Image':image})
            df4 = pd.DataFrame({'Body_text':body_t})
            df3 = pd.DataFrame({'Para_text':scr})
            

            output_file = f'{str(file_title)}{count}'+'.xlsx'
            output_file_path = Path(output_file)

            output_file_path.parent.mkdir(parents=True, exist_ok=True)
        

            pd.concat([df1,df2,df4,df3],axis=1).to_excel(output_file_path, sheet_name=f'{file_title}', index=False)
