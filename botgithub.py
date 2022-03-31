from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random
from PySimpleGUI import PySimpleGUI as sg

sg.theme('BrightColors')
layout = [
    [sg.Text('Email ou Usuário:'), sg.Input(key='emailuser', size=(40, 1))],
    [sg.Text('Senha:'), sg.Input(key='senhauser', password_char='*', size=(49, 1))],
    [sg.Text('Nome do repositório:'), sg.Input(key='repositorio', size=(38, 1))],
    [sg.Button('Iniciar')]

]

janela = sg.Window('Criar repositório Github', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Iniciar':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get('https://github.com/login')
        digitar_email = driver.find_element_by_id('login_field')
        time.sleep(1)
        digitar_email.send_keys(valores['emailuser'])
        digitar_email = driver.find_element_by_id('password')
        digitar_email.send_keys(valores['senhauser'])
        digitar_email.send_keys(Keys.ENTER)
        time.sleep(1)
        criar_repositorio = driver.find_element_by_xpath(
            '//*[@id="repos-container"]/h2/a').click()
        criar_repositorio = driver.find_element_by_id('repository_name')
        criar_repositorio.send_keys(valores['repositorio'])
        time.sleep(1)
        criar_repositorio = driver.find_element_by_xpath(
            '//*[@id="new_repository"]/div[4]/button').click()
