from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import urllib.parse

# Lista de contatos
contatos = [
    '+5511999999999',
]


# Mensagem que será enviada
mensagem = """\
Olá! 👋

Temos uma ótima notícia para você! ✨

Aproveite 10% de desconto em todos os produtos do nosso site! 🤩 É a sua chance de garantir peças de excelente qualidade com um preço especial.

Para aproveitar, basta acessar nosso site: https://bgmultipecas.com.br/ e utilizar o cupom de desconto 10%OFF no carrinho de compras! 😉

Essa oferta é por tempo limitado, então não perca essa oportunidade! Corra para o nosso site e aproveite! 🏃‍♀️💨

Qualquer dúvida, estamos à disposição! 😊

Atenciosamente,

BG Multipeças
"""

# Configurações do navegador
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
options = Options()
options.binary_location = chrome_path
options.add_argument("--user-data-dir=C:/temp/whatsapp_profile")  # Sessão persistente
options.add_argument("--profile-directory=Default")
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Inicializa o navegador
service = Service()
driver = webdriver.Chrome(service=service, options=options)

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")
print("🔓 Aguarde escanear o QR Code se necessário...")
time.sleep(20)  # Tempo para login se necessário

# Envia mensagens para os contatos
for numero in contatos:
    try:
        print(f"📱 Enviando para {numero}...")

        # Codifica a mensagem na URL
        mensagem_codificada = urllib.parse.quote(mensagem)
        link = f"https://web.whatsapp.com/send?phone={numero}&text={mensagem_codificada}"
        driver.get(link)

        # Aguarda carregamento do chat
        time.sleep(8)

        # Envia a mensagem com Enter
        caixa = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        caixa.send_keys(Keys.ENTER)

        print(f"✅ Mensagem enviada para {numero}")
        time.sleep(4)  # Pausa entre os envios

    except Exception as e:
        print(f"❌ Erro ao enviar para {numero}: {e}")
        continue

# Finaliza
print("📤 Todas as mensagens foram processadas.")
driver.quit()
