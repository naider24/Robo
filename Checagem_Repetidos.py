import pandas as pd
from selenium import webdriver  # navegador
from selenium.webdriver.common.by import By  # ACHAR OS ELEMENTOS
from selenium.webdriver.common.keys import Keys  # para digitar no teclado na web
from selenium.webdriver.chrome.options import Options
import time


arquivo = "Sabin.xlsx"
tabela_Excel = pd.read_excel(arquivo)


codigos = []     
codigosUnicos = []
codigosRepetidos = []

Serviços = []
serviçosUnicos = []
serviçosRepetidos = []

def transformando_em_array():
    for index, row in tabela_Excel.iterrows():
     array_codigos=codigos.append( str(row["CODIGO"]).split('.')[0]) 
     array_serviços=Serviços.append(str(row["Serviço"]))
     Tabela = ("Index: " + str(index) )

def contador_repetidos (s):
    
    ocorrencias = {}
    for c in s:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrencias 

    
transformando_em_array()

time.sleep(2)

for codigo  in codigos:
       if codigo not in codigosUnicos:
        codigosUnicos.append(codigo )
       else:
         codigosRepetidos.append(codigo)

print("CODIGOS UNICOS -------------------------------------------------------------------------------------------------------------------------------------------------------------")

 #print com quebra de linha usando for
for codigos in codigosUnicos:print(codigos)

print("____________________________________________________________________________________________________________________________________________________________________________")

print("CODIGOS REPETIDOS  --------------------------------------------------------------------------------------------------------------------------------------------------------")

for codigos in codigosRepetidos:print(codigos)
print(contador_repetidos(codigosRepetidos))


print("____________________________________________________________________________________________________________________________________________________________________________")

#CHECANDO SE HÁ SERVIÇOS REPETIDOS
time.sleep(1)
for servico  in Serviços:
    if servico not in serviçosUnicos:
        serviçosUnicos.append(servico)
    else:
        serviçosRepetidos.append(servico)

print("SERVICOS UNICOS -------------------------------------------------------------------------------------------------------------------------------------------------------------")
 
for servicos in serviçosUnicos:print(servicos)

print("____________________________________________________________________________________________________________________________________________________________________________")

print("SERVICOS REPETIDOS  --------------------------------------------------------------------------------------------------------------------------------------------------------")
for servicos in serviçosRepetidos:print(servicos)
print(contador_repetidos(serviçosRepetidos))

print("____________________________________________________________________________________________________________________________________________________________________________")

