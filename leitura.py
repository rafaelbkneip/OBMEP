
from selenium.webdriver.common.by import By

def leitura (navegador):
    final = []

    cont_link = 6

    while(True):
            try:


                print(cont_link)
                
                                            
                link = navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a/p/table/tbody/tr[' + str(cont_link)+ ']/td[2]/a').get_attribute('href')

                print(link)

                navegador.get(link)

                

                cont = 1

                while (True):
                    try: 
                        aux = []
                        aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[1]').text)
                        aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[2]').text)
                        aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[3]').text)
                        aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[4]').text)
                        aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[5]').text)
                        aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[6]').text)
                        aux.append(navegador.find_element(By.XPATH, '//*[@id="internalPage"]/a[2]/table/tbody/tr[' + str(cont) + ']/td[7]').text)

                        final.append(aux)
                        
                        cont = cont + 1

                    except:
                        print("Finalizado")
                        break


                cont_link = cont_link + 1
                navegador.back()

            except:

                break
    print(final)
    
    return(final)