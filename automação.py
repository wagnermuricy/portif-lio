import pandas as pd 
tabela = pd.read_csv("produtos.csv")
print(tabela)

import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=603, y=473)
pyautogui.write("wagnermuricy16@gmail.com")
pyautogui.press("tab")
pyautogui.write("W@g160694")
pyautogui.click(x=953, y=671)

for linha in tabela.index:
    pyautogui.doubleClick(x=592, y=318)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    pyautogui.scroll(5000)
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
        pyautogui.click(x=594, y=685)
        pyautogui.scroll(5000)  






    





