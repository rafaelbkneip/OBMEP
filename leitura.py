#Importações / Imports
from selenium.webdriver.common.by import By
from time import sleep

#Definir função / Define function
def leitura (navegador):

    #Lista auxiliar / Auxiliary list
    final = []

    #Na página de cada estado, os resultados de interesse iniciam nos links localizados a partir do sexto elemento clicável / In each page state, the results of interest are localized after the sixth clickable element
    cont_link = 6

    #Cada página de estado contém os resultados separados por grupos. Cada grupo possui seu link e, então, sua página / Each state page has the results separated in groups. Each group has its own link and, then, its page
    for cont_link in range(6, 13):  
      
        #Obter o link de cada um dos grupos / Get each group link
        try:
            link = navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a/p/table/tbody/tr[' + str(cont_link)+ ']/td[2]/a').get_attribute('href')
        except Exception as e:
            print(e)
            break 

        #Obter o nome do grupo / Get the group name
        link_texto = navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a/p/table/tbody/tr[' + str(cont_link)+ ']/td[2]/a').text
        
        #Acessar a página de cada um dos grupos / Access each group page
        navegador.get(link)
        #Garantir que a página está totalmente carregada / Make sure the page is completely loaded
        sleep(10)

        #Do sexto ao décimo segundo elemento, as informações são referentes à premiações da OBMEP e estão dispostas de forma similar / From the sixth to the twelfth element, the information regarding the OBMEP awards is disposed in a similar way
        if(cont_link < 12):
                
                #Obter resutados do nível 1 / Get level 1 results
                e = True
                cont = 1

                while(e):
                        
                        try:
                            aux = []
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[1]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[2]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[3]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[4]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[5]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[6]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[7]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/thead/tr[1]/th').text)
                            aux.append(link_texto)
                            final.append(aux)
                            cont = cont + 1

                        except:
                            e = False

                #Obter resutados do nível 2 / Get level 2 results
                e = True
                cont = 1

                while(e):
                        
                        try:
                            aux = []
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[3]/table/tbody/tr[' + str(cont) + ']/td[1]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[3]/table/tbody/tr[' + str(cont) + ']/td[2]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[3]/table/tbody/tr[' + str(cont) + ']/td[3]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[3]/table/tbody/tr[' + str(cont) + ']/td[4]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[3]/table/tbody/tr[' + str(cont) + ']/td[5]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[3]/table/tbody/tr[' + str(cont) + ']/td[6]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[3]/table/tbody/tr[' + str(cont) + ']/td[7]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[3]/table/thead/tr[1]/th').text)
                            aux.append(link_texto)
                            final.append(aux)
                            cont = cont + 1
                        
                        except:
                            e = False

                #Obter resutados do nível 3 / Get level 3 results
                e = True
                cont = 1

                while(e):
                        
                        try:
                            aux = []
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[4]/table/tbody/tr[' + str(cont) + ']/td[1]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[4]/table/tbody/tr[' + str(cont) + ']/td[2]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[4]/table/tbody/tr[' + str(cont) + ']/td[3]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[4]/table/tbody/tr[' + str(cont) + ']/td[4]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[4]/table/tbody/tr[' + str(cont) + ']/td[5]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[4]/table/tbody/tr[' + str(cont) + ']/td[6]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[4]/table/tbody/tr[' + str(cont) + ']/td[7]').text)
                            aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[4]/table/thead/tr[1]/th').text)
                            aux.append(link_texto)
                            final.append(aux)
                            cont = cont + 1

                        except:
                            e = False

                #Voltar a página com os links dos grupo / Get back to the group links page
                navegador.back()
                #Acessar o próximo link / Access the next link
                cont_link = cont_link + 1
                
    print(final)
    
    return(final)



