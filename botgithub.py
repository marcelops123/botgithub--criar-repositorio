from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random

padrao = ['']
mensagem = ('')
x = random.randint(1, 500)

emailuser = input('Digite seu email:')
senhauser = input('Digite sua senha:')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://github.com/login')
digitar_email = driver.find_element_by_id('login_field')
time.sleep(1)
digitar_email.send_keys(emailuser)
digitar_email = driver.find_element_by_id('password')
digitar_email.send_keys(senhauser)
digitar_email.send_keys(Keys.ENTER)
time.sleep(1)
digitar_email = driver.find_element_by_xpath(
    '//*[@id="repos-container"]/h2/a').click()
digitar_email = driver.find_element_by_id('repository_name')
digitar_email.send_keys('botgithub', (x))
time.sleep(1)
digitar_email = driver.find_element_by_xpath(
    '//*[@id="new_repository"]/div[4]/button').click()
