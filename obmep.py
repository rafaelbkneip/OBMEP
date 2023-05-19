import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from time import sleep
from datetime import date

options = Options()
options.add_experimental_option("detach", True)

import leitura
import save

navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)
navegador.get("http://premiacao.obmep.org.br/17obmep/mapa.htm?_gl=1*1g0yvb0*_ga*Mzg4NTIwNzEzLjE2Nzk1NzYzNTM.*_ga_21HEQ7CQ8K*MTY4NDMyNDAxNC4zLjEuMTY4NDMyNDAyOC4wLjAuMA.")
sleep(5)


estados = navegador.find_elements(By.XPATH, '//*[@id="filterState"]')

print(estados)
print(type(estados))

print(estados[0].text.split("\n"))

estados = estados[0].text.split("\n")

estados.pop(-1)

unica = []
for i in range(1): 
    
    navegador.get('http://premiacao.obmep.org.br/17obmep/verMenuAlunosPremiados-' + str(estados[i])  + '.htm') 

    leitura_estado = leitura.leitura(navegador)

    sleep(10)

    for j in range(len(leitura_estado)):
        unica.append(leitura_estado[j])

print(unica)
save.salvar(unica)