'''
DEMANDA:
PRECISO AUTOMATIZAR MINHAS MENSAGENS P/ MEUS CLIENTES, GOSTARIA DE SABER VALORES, E GOSTARIA QUE ENTRASSEM EM CONTATO COMIGO P/ EXPLICAR MELHOR, 
QUERO PODER MANDAR MENSAGENS DE COBRANÇA EM DETERMINADO DIA COM CLIENTES COM VENCIMENTO DIFERENTE
'''

#Instalando bibliotecas essenciais para o funcionamento do código.
import openpyxl
import time
import webbrowser
import pyautogui
from urllib.parse import quote

#Abrindo o WebWhatsApp
webbrowser.open("https://web.whatsapp.com")
time.sleep(30)

#Abrindo a planilha
plan_cliente = openpyxl.load_workbook("clientes.xlsx")
pag_plan_cliente = plan_cliente["Pagina1"]

#Iterando sobre cada linha
for linha in pag_plan_cliente.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    #Verifica se acabou os valores da planilha
    if not nome and not telefone and not vencimento:
        print("Fim da planilha!")
        break

    #Personalizade sua mensagem!
    mensagem_personalizada = f'Hello World! Essa mensagem é um teste de uma automação que estou produzindo, portanto ignorar. Se eu te usei de cobaia? Pode-se dizer que sim.'

    try:
        #Fechando a página inicial
        pyautogui.hotkey('ctrl', 'w')
        #Abrindo o convite de contato e colando a mensagem
        link_direto_wpp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem_personalizada)}'
        webbrowser.open(link_direto_wpp)
        time.sleep(5)
        #Localizando o ícone a ser clicado
        clicar_icone_enviar = pyautogui.locateCenterOnScreen('icone_enviar.png')
        time.sleep(1)
        #Passando a coordernada da imagem utilizada
        pyautogui.click(clicar_icone_enviar[0], clicar_icone_enviar[1])
        time.sleep(2)
        #Combinando tecla para fechar a aba
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(2)
    except:
        print("OPS! Ocorreu um erro.")
        time.sleep(1)
        print(f"Não foi possível enviar a mensagem para {nome}")
