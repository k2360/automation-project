# 1- Entrar no sistema da empresa
# 2- Fazer login
# 3- Importar a base de dados
# 4- Cadastrar os produtos no formulário
# 5- Repetir o passo 4 até cadastrar todos os produtos

import pandas
import pyautogui
import time

pyautogui.PAUSE = 0.6

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

#--------------------------------------------------------------------------------------------------------------------------------------
pyautogui.click(x=617, y=468)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("example@gmail.com")

pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("enter")

time.sleep(3)

#--------------------------------------------------------------------------------------------------------------------------------------
tabela = pandas.read_csv("produtos.csv")
print(tabela)

#--------------------------------------------------------------------------------------------------------------------------------------
for linha in tabela.index:

    pyautogui.click(x=596, y=324)
    pyautogui.hotkey("ctrl", "a")

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
