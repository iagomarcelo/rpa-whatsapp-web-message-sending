"""
PRECISO AUTOMATIZAR MINHAS MENSAGENS P/ MEUS CLIENTES GOSTARIA DE SABER VALORES, E GOSTARIA QUE ENTRASSEM EM CONTATO COMIGO P/ EXPLICAR MELHOR, QUERO PODER MANDAR MENSAGENS DE COBRANÇA EM DETERMINADO DIA COM CLIENTES COM VENCIMENTO DIFERENTE
"""
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import os 

# webbrowser.open('https://web.whatsapp.com/')
# sleep(10)

# Ler planilha e guardar informações sobre nome, telefone e data de vencimento
workbook = openpyxl.load_workbook('C:\\Users\\Iago Lima\\Desktop\\Guaiamum Figital\\Projeto 1 - bot whatsapp\\assets\\clientes.xlsx')
pagina_clientes = workbook['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2):
    # nome, telefone, vencimento
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    mensagem = f"teste"

    if linha[0].value and linha[1].value and linha[2].value != '' and not None:

    # Criar links personalizados do whatsapp e enviar mensagens para cada cliente
    # com base nos dados da planilha
        # try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(14)
        # seta = pyautogui.locateCenterOnScreen('seta.png')
        pyautogui.hotkey('enter')
        sleep(2)
        # pyautogui.click(seta[0],seta[1])
        # sleep(2)
        pyautogui.hotkey('ctrl','w')
        sleep(2)
        # except:
        # print(f'Não foi possível enviar mensagem para {nome}')
        # with open('logs\\erros.csv','a',newline='',encoding='utf-8') as arquivo:
        #     arquivo.write(f'{nome},{telefone}{os.linesep}')
    
