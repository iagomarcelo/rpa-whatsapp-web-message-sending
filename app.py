"""
PRECISO AUTOMATIZAR MINHAS MENSAGENS P/ MEUS CLIENTES GOSTARIA DE SABER VALORES, E GOSTARIA QUE ENTRASSEM EM CONTATO COMIGO P/ EXPLICAR MELHOR, QUERO PODER MANDAR MENSAGENS DE COBRANÇA EM DETERMINADO DIA COM CLIENTES COM VENCIMENTO DIFERENTE
"""
import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import traceback
from datetime import datetime
import pyautogui
import os 

# webbrowser.open('https://web.whatsapp.com/')
# sleep(10)
def send_messages():
    # Ler planilha e guardar informações sobre nome, telefone e data de vencimento
    workbook = openpyxl.load_workbook('C:\\Users\\Iago Lima\\Desktop\\Guaiamum Figital\\Projeto 1 - bot whatsapp\\database\\clientes.xlsx')
    pagina_clientes = workbook['Sheet1']

    for line in pagina_clientes.iter_rows(min_row=2):
        # nome, telefone, vencimento
        name = line[0].value
        phoneNumber = line[1].value
        message = f"teste"

        if line[0].value and line[1].value != '' and not None:

        # Criar links personalizados do whatsapp e enviar mensagens para cada cliente
        # com base nos dados da planilha
            link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={phoneNumber}&text={quote(message)}'
            webbrowser.open(link_mensagem_whatsapp)
            sleep(14)
            # seta = pyautogui.locateCenterOnScreen('seta.png')
            pyautogui.hotkey('enter')
            sleep(2)
            # pyautogui.click(seta[0],seta[1])
            # sleep(2)
            pyautogui.hotkey('ctrl','w')
            sleep(2)
    return(name, phoneNumber)

try:
    print(send_messages()[0])

except Exception as e:
    name = send_messages()[0]
    phoneNumber = send_messages()[1]

    
    print(f'Não foi possível enviar mensagem para {name}')

    # Imprime a última linha da trilha de pilha (onde ocorreu o erro)
    # Obtém detalhes do traceback
    tb = traceback.extract_tb(e.__traceback__)
    errorLine = tb[-1].lineno

    traceback_info = traceback.format_exc()
    linha_quebrada = traceback_info.split("\n")[-2]
    error_message = (linha_quebrada.strip()).split('NameError: name ')[1]


    now = datetime.now()
    formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
    error_message = f"Ocorreu uma exceção em {formatted_date}:\n erro {error_message}, na linha {errorLine}"
    print(error_message)


    print(name, phoneNumber)

    with open('logs\\erros.csv','a',newline='',encoding='utf-8') as logsArchive:
        logsArchive.write(f'{name},{phoneNumber},{traceback.format_exc()},{formatted_date}, {os.linesep}')