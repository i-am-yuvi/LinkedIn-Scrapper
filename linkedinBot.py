from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

def loginToLinkedin(driver):
     username = driver.find_element_by_id("session_key")
     username.send_keys("example.com")
     password = driver.find_element_by_id("session_password")
     password.send_keys("password")
     driver.find_element_by_class_name("sign-in-form__submit-btn").click()

def  goto_network_page(driver,network_url):
     driver.get(network_url)

def  accept_invitations_from_users(driver):
     javaScript =  "window.scrollBy(0,0);"
     driver.execute_script(javaScript)
     element_exists =  True
     while element_exists:
          try:
               driver.find_element_by_class_name("invitation-card__action-btn")
          except NoSuchElementException:
               element_exists =  False
          finally:
               if element_exists:
                    driver.find_element_by_class_name("invitation-card__action-btn artdeco-button--secondary").click()


def  start_bot(driver,url,network_url):
     driver.get(url)
     sleep(1)
     loginToLinkedin(driver)
     goto_network_page(driver,network_url)
     accept_invitations_from_users(driver)

url = "http://linkedin.com"     
network_url = "http://linkedin.com/mynetwork"
# driver = webdriver.Chrome('/Users/yuvrajchhetri/Documents/chromedriver/chromedriver')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
start_bot(driver,url,network_url)

