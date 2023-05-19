
from selenium.webdriver.common.by import By
from time import sleep

def leitura (navegador):
    final = []

    cont_link = 6

    for cont_link in range(6, 13):
            
        cont = 0
        print(cont_link)
        sleep(5)

        try:
            link = navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a/p/table/tbody/tr[' + str(cont_link)+ ']/td[2]/a').get_attribute('href')
        except Exception as e:
            print(e)
            break 

        sleep(5)
        
        link_texto = navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a/p/table/tbody/tr[' + str(cont_link)+ ']/td[2]/a').text
        
        sleep(5)
        navegador.get(link)
        sleep(3)

        print((cont_link<12))

        if(cont_link<12):
                e = True
                cont = cont + 1
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
                            aux.append(link_texto)
                            final.append(aux)
                            cont = cont + 1
                        
                            print(aux)
                        
                        except:
                            e = False

                navegador.back()
                cont_link = cont_link + 1
                
    print(final)
    
    return(final)