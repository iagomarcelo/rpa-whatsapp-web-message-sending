import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import traceback
from datetime import datetime
import pyautogui
import os 

def send_messages():
    # Carrega a planilha e obtém a folha desejada
    workbook = openpyxl.load_workbook('C:\\Users\\Iago Lima\\Desktop\\Guaiamum Figital\\Projeto 1 - bot whatsapp\\database\\clientes.xlsx')
    clientes_sheet = workbook['Sheet1']

    for line in clientes_sheet.iter_rows(min_row=2):
        name = line[0].value
        phone_number = line[1].value
        message = f"teste"

        # Verifica se ambos nome e número de telefone têm valor
        if name and phone_number:
            # Cria o link personalizado do WhatsApp
            whatsapp_link = f'https://web.whatsapp.com/send?phone={phone_number}&text={quote(message)}'
            webbrowser.open(whatsapp_link)
            sleep(14)
            pyautogui.hotkey('enter')
            sleep(2)
            pyautogui.hotkey('ctrl', 'w')
            sleep(2)

            return name, phone_number

    return None, None  # Retorna None se nenhum cliente válido for encontrado

try:
    # Chama a função send_messages uma vez e armazena o resultado
    name, phone_number = send_messages()

    if name is not None and phone_number is not None:
        print(f'Mensagem enviada para {name}')
except Exception as e:
    # Chama a função send_messages novamente para obter os valores
    name, phone_number = send_messages()

    if name is not None and phone_number is not None:
        print(f'Não foi possível enviar mensagem para {name}')

        # Obtém detalhes do traceback
        tb = traceback.extract_tb(e.__traceback__)
        error_line = tb[-1].lineno

        traceback_info = traceback.format_exc()
        error_message = traceback_info.split("\n")[-2].strip()

        now = datetime.now()
        formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
        error_message = f"Ocorreu uma exceção em {formatted_date}:\n{error_message}, na linha {error_line}"

        print(error_message)
        
        with open('logs\\erros.csv', 'a', newline='', encoding='utf-8') as logs_archive:
            logs_archive.write(f'{name},{phone_number},{error_message},{formatted_date},{os.linesep}')
