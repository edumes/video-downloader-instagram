import selenium
from selenium import webdriver
from time import sleep
import pyautogui as pg

pag = str(input('Insira o link da página: '))
navegador = webdriver.Chrome() #define o navegador como uma variavel
navegador.get("https://www.instagram.com/") #abre um site
sleep(1)
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').click()
pg.write("usuario")
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').click()
pg.write('senha')
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
sleep(3)
navegador.get(pag)
sleep(3)
pg.click(x=179, y=596)
sleep(1)
pg.click(x=970, y=211)
sleep(1)
pg.click(x=534, y=464)
pg.hotkey('ctrl', 't')
pg.write('https://pt.savefrom.net/download-from-instagram')
pg.hotkey('enter')
sleep(1)
pg.click(x=304, y=414)
pg.hotkey('ctrl', 'v')
sleep(5)
pg.click(x=506, y=653)
sleep(10)

navegador.quit()









