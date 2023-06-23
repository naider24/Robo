import pandas as pd
from selenium import webdriver  # navegador
from selenium.webdriver.common.by import By  # ACHAR OS ELEMENTOS
from selenium.webdriver.common.keys import Keys  # para digitar no teclado na web
from selenium.webdriver.chrome.options import Options
from decimal import Decimal
import time



arquivo = "Sabin.xlsx"
tabela_Excel = pd.read_excel(arquivo)
url_do_forms = "https://app.prontosaude.digital/#/admin/providers/list"
NomeLogin = "rambo@huoli.com.br"
senhaLogin = "Manga1,50!"
NomeLaboratorio = "Sabin"


 #Arindo o Chrome-----------------------------------------------

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome = webdriver.Chrome(executable_path='chromedriver.exe', )
chrome = webdriver.Chrome(url_do_forms, chrome_options=chrome_options)
chrome.get(url_do_forms)
chrome.maximize_window

    #--------------------------------------------------------------    
# Logar na pronto
def Login():
    Campo_login = chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div/main/form/div/div/div[2]/label/div/div[1]/div[2]/input')
    Campo_Senha = chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div/main/form/div/div/div[3]/label/div/div[1]/div[2]/input')

    Campo_login.send_keys(NomeLogin)
    Campo_Senha.send_keys(senhaLogin)

    Button_enviar_login = chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div/main/form/div/div/div[4]/button/span[2]/span')
    Button_enviar_login.click()

# acessar o campo remuneração do laboratório
def Pesquisar_laboratorio_e_acessar_remuneração():
    Campo_pesquisar = chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div[3]/div/div/label/div[1]/div[1]/div/input')
    Campo_pesquisar.send_keys(NomeLaboratorio)
    time.sleep(2)

    Loopa = chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div[3]/div/div/label/div[2]/button/span[2]/span/i')
    Loopa.click()
    time.sleep(2)

    remuneração_tuss = chrome.find_element(
        By.XPATH, '/html/body/div[1]/div/div[2]/main/div/div[2]/div/div/div[3]/a[1]/span[2]/span/span')
    remuneração_tuss.click()
        
# Preencher os dados do procedimento , ou adicionar um novo procedimento se não existir
def registrar_ou_Adicionar_procedimento():

    try:
        Campo_Codigo = chrome.find_element(
            By.XPATH, '/html/body/div[1]/div/div[2]/main/form/div[2]/label/div/div[1]/div[1]/div[1]/input')
        Campo_Codigo.send_keys(Cadastrar_codigos)

        time.sleep(5)

        clickLabel = chrome.find_element(By.XPATH, '/html/body/div[3]/div[2]')
        clickLabel.click()

        time.sleep(1)

        Campo_Valor = chrome.find_element(
            By.XPATH, '/html/body/div[1]/div/div[2]/main/form/div[3]/label/div/div[1]/div/input')
        Campo_Valor.click()
        
        
        time.sleep(1)
               
        Campo_Valor.send_keys(Valor_convertido_string)

        time.sleep(2)

        Enviar_registro = chrome.find_element(
            By.XPATH, '/html/body/div[1]/div/div[2]/main/form/div[4]/button').click()
        
        time.sleep(1)
        Campo_Valor.click()
        time.sleep(1)
        Campo_Valor.send_keys(Keys.BACKSPACE)  
        Campo_Valor.send_keys(Keys.BACKSPACE) 
        Campo_Valor.send_keys(Keys.BACKSPACE) 
        Campo_Valor.send_keys(Keys.BACKSPACE) 
        Campo_Valor.send_keys(Keys.BACKSPACE) 
        Campo_Valor.send_keys(Keys.BACKSPACE) 
        Campo_Valor.send_keys(Keys.BACKSPACE)
        Campo_Valor.send_keys(Keys.BACKSPACE) 
        Campo_Valor.send_keys(Keys.BACKSPACE)
        Campo_Valor.send_keys(Keys.BACKSPACE)
           

    except:
        print("Entrei no except")
        Campo_add_Procedimento = chrome.find_element(
            By.XPATH, '/html/body/div[3]/div/div/button')
        Campo_add_Procedimento.click()
        time.sleep(2)
        Codigo_Procedimento = chrome.find_element(
            By.XPATH, '/html/body/div[4]/div[2]/div/div/form/label[1]/div/div[1]/div[1]/input')
        Nome_Procedimento = chrome.find_element(
            By.XPATH, '/html/body/div[4]/div[2]/div/div/form/label[2]/div/div[1]/div[1]/input')

        Codigo_Procedimento.send_keys(Cadastrar_codigos)
        Nome_Procedimento.send_keys(Serviço)

        Button_add_procedimento = chrome.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/div/form/div/button[2]')
        Button_add_procedimento.click()

        time.sleep(2)

        

 
Login()
time.sleep(3)
Pesquisar_laboratorio_e_acessar_remuneração()

#CADASTRANDO OS DADOS NO SISTEMA DA PRONTO
for index, row in tabela_Excel.iterrows():
    
    Cadastrar_codigos=( str(row["CODIGO"]).split('.')[0])       
    Tabela = ("Index: " + str(index) + " código  " + str(Cadastrar_codigos))
    valor = float(row['VALOR'])
    Valor_Monetario = "{:.2f}".format(valor)
    
    Valor_convertido_string = str(Valor_Monetario)

    print(Valor_convertido_string)
    print(Tabela)
    
    time.sleep(1)

    registrar_ou_Adicionar_procedimento()




