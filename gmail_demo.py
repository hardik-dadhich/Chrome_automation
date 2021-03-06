# import essential libraries
from selenium import webdriver
import time
import configparser
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import bs4 as bs
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib.request
from  selenium.common.exceptions import *
class Demo:
   
    
    def main():
        # --------------credintials reading-----------!
        config = configparser.ConfigParser()
        config.read("details.ini")
        sections = config.sections()
        username_for_email = config.get('login_details', 'username_for_email')
        password_for_email = config.get('login_details', 'password_for_email')
        sending_email_add  = config.get('login_details', 'sending_email_add')
        driverpath = config.get('login_details', 'driverpath')  
        
        # driver path for chrome
        driver = webdriver.Chrome(driverpath)
        driver.maximize_window()
        driver.get(config.get('login_details', 'url_path')) 
             
        # email username
        
        

        try:
            mark1 = 0
            elem = driver.find_element_by_id("identifierId")
            elem.send_keys(username_for_email)
            mark1 = 1
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementNotVisibleException) as exception:
            
            if mark1 == 0:
                driver.refresh()
                time.sleep(2)
                elem = driver.find_element_by_id("identifierId")
                elem.send_keys(username_for_email)
            print("exception has been  thown--> " + str(exception))
        
        #driver.refresh()
          

        try:
            mark2 = 0
            next_btn_for_email = driver.find_element_by_id('identifierNext')
            next_btn_for_email.click()
            mark2 = 1
            time.sleep(5)
        
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementNotVisibleException) as exception:
            if mark2 == 0:

                driver.refresh()
                time.sleep(3)
                driver.find_element_by_id('identifierNext').click()
                time.sleep(3)
            print("exception thrown : " + str(exception))    
        #driver.refresh()
        
         

        try:
            mark3 = 0
            password_field = driver.find_element_by_name('password')
            password_field.send_keys(password_for_email)
            mark3 = 1
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementNotVisibleException) as exception:
            if mark3 == 0:
                driver.find_element_by_name('password').send_keys(password_for_email)
            print("exception has been  thown--> " + str(exception))
            #driver.refresh()
        
            
        try:
            mark4 = 0
            next_btn_for_password = driver.find_element_by_id('passwordNext')
            next_btn_for_password.click()
            mark4 = 1
            time.sleep(5)
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementNotVisibleException) as exception:
            if mark4 == 0:
                driver.refresh()
                time.sleep(3)
                driver.find_element_by_id('passwordNext').click()

            print("exception has been  thown---> " + str(exception))
            
            #driver.refresh()

        time.sleep(8)
        html_code = driver.page_source
        soup = BeautifulSoup(html_code, "html.parser")
        table_obj_code = soup.findAll('table', attrs={'id' : ':34'})
        
        #selection of grid
        try:
            mark5 = 0
            for elem in table_obj_code:
                tr_obj= elem.findAll('tr')  

            for tr in tr_obj:
                td_obj = tr.findAll('td')[0]
                p = driver.find_element_by_id(':3e')
            p.click()
            mark5 = 1
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementNotVisibleException) as exception:
            if mark5 == 0:
                driver.refresh()
                time.sleep(4)
                for elem in table_obj_code:
                   tr_obj= elem.findAll('tr')  

                for tr in tr_obj:
                    td_obj = tr.findAll('td')[0]
                    p = driver.find_element_by_id(':3e')
                p.click()
            print("exception has been  thown--> " + str(exception))
            print("grid of emails not found due to slow internet !")    
             
        
        next_soup = BeautifulSoup(driver.page_source, "html.parser")
        button = next_soup.findAll('td', attrs= {'class' : 'gH acX bAm'})   

        for el in button:
            all_td = el.findAll('div')[1]
                

        try:
            mark6 = 0
            class_obj = next_soup.findAll('div' , attrs={'class': 'amn'})
            for i in class_obj:
                pq = driver.find_element_by_class_name('bkG')
                pq.click()
            mark6 = 1    
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementNotVisibleException) as exception:
            if mark6 == 0:
                class_obj = next_soup.findAll('div' , attrs={'class': 'amn'})
                for i in class_obj:
                    pq = driver.find_element_by_class_name('bkG')
                    pq.click()
                  
            print("exception has been  thown--> " + str(exception))   
            
            #driver.refresh()

        third_soup = BeautifulSoup(driver.page_source, "html.parser")   

        filed = third_soup.findAll('table', attrs= {'class': 'GS'})
        try:    
            flag =0
            for i in filed:
                nm = third_soup.find('div', attrs= {'class': 'l1'})
                driver.find_element_by_class_name('vO').send_keys(sending_email_add)
                flag = 1
                succ = driver.find_element_by_class_name('btA')
                succ.click()
                time.sleep(1)
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException, ElementNotVisibleException)as exception:
            if flag == 0:
                driver.refresh()
                time.sleep(4)
                driver.find_element_by_class_name('vO').send_keys(sending_email_add)
                driver.find_element_by_class_name('btA').click()
                
            else:
                driver.find_element_by_class_name('btA').click()
             
            print("button not clicked succesfully! " + str(exception))        
        driver.refresh()

        

        print("process finished")
        driver.quit()




#driver function
if __name__ == "__main__":
    obj = Demo
    obj.main()