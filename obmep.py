#Main

#Importações / Imports
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from time import sleep
from datetime import date
import leitura
import save

#Definir configurações da janela do Google Chrome / Define Google Chrome tab configurations
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

navegador = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#Acessar o site da OBMEP / Access the OBMEP website
navegador.get("http://premiacao.obmep.org.br/17obmep/mapa.htm?_gl=1*1g0yvb0*_ga*Mzg4NTIwNzEzLjE2Nzk1NzYzNTM.*_ga_21HEQ7CQ8K*MTY4NDMyNDAxNC4zLjEuMTY4NDMyNDAyOC4wLjAuMA.")
sleep(5)

#Obter as siglas para os estados / Get the states abbreviations
estados = navegador.find_elements(By.XPATH, '//*[@id="filterState"]')
estados = estados[0].text.split("\n")
estados.pop(-1)

#Lista auxiliar / Auxiliary list
unica = []

#Cada estado possui uma página com os resultos / Each state has a specific page with results
for i in range(len(estados)): 
    
    #Acessar o site referente a cada estado / Access the corresponding website for each state
    navegador.get('http://premiacao.obmep.org.br/17obmep/verMenuAlunosPremiados-' + str(estados[i])  + '.htm') 

    #Obter os resultados para cada estado / Get the results for each state
    leitura_estado = leitura.leitura(navegador)

    #Adicionar os resultados em uma única lista / Add the results to a single list
    for j in range(len(leitura_estado)):
        unica.append(leitura_estado[j])

#Chamar a função para salvar o arquivo / Call the function to save the file
save.salvar(unica)