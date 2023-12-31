import webbrowser
from time import sleep
import pyautogui
from urllib.parse import quote

telefone = '11933770366'
mensagem = 'Teste'

link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone=55{telefone}&text={quote(mensagem)}'
webbrowser.open(link_mensagem_whatsapp)
sleep(10)
seta = pyautogui.locateCenterOnScreen('seta.png')
sleep(2)
pyautogui.click(seta[0],seta[1])
sleep(2)
pyautogui.hotkey('ctrl','w')
sleep(2)