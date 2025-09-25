# main.py

import pyautogui
import keyboard
import requests
from io import BytesIO

API_URL = "  "  # Seu endpoint no Render

def tirar_e_enviar():
    screenshot = pyautogui.screenshot()
    buffer = BytesIO()
    screenshot.save(buffer, format='PNG')
    buffer.seek(0)

    files = {'screenshot': ('screenshot.png', buffer, 'image/png')}
    
    try:
        response = requests.post(API_URL, files=files)
        if response.status_code == 200:
            print("[OK] Screenshot enviada com sucesso!")
        else:
            print("[ERRO] Falha ao enviar:", response.status_code, response.text)
    except Exception as e:
        print("[ERRO] Falha de conexão:", e)

def main():
    print("Pressione '/' para tirar screenshot e enviar. Pressione ESC para sair.")
    while True:
        if keyboard.is_pressed('/'):
            tirar_e_enviar()
            keyboard.wait('/')
        if keyboard.is_pressed('esc'):
            print("Saindo...")
            break

if _name_ == "_main_":
    main()
