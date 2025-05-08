import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
import time

load_dotenv()  # Carrega as variáveis do .env

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA = os.getenv("SENHA_APP")

# Lista de e-mails
lista_emails = [
    "GMAIL@gmail.com",
]

mensagem = """\
Olá! 👋

Temos uma ótima notícia para você! ✨

Aproveite 10% de desconto em todos os produtos do nosso site! 🤩 É a sua chance de garantir peças de excelente qualidade com um preço especial.

Para aproveitar, basta acessar nosso site: https://bgmultipecas.com.br/ e utilizar o cupom de desconto 10%OFF no carrinho de compras! 😉

Essa oferta é por tempo limitado, então não perca essa oportunidade! Corra para o nosso site e aproveite! 🏃‍♀️💨

Qualquer dúvida, estamos à disposição! 😊

Atenciosamente,

BG Multipecas
"""

# Conexão segura
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL_REMETENTE, SENHA)

    for email in lista_emails:
        try:
            msg = EmailMessage()
            msg["Subject"] = "10% de DESCONTO exclusivo na BG MULTIPEÇAS!"
            msg["From"] = f"BG MULTIPEÇAS <{EMAIL_REMETENTE}>"
            msg["To"] = email
            msg.set_content(mensagem)

            smtp.send_message(msg)
            print(f"✅ Enviado para: {email}")
            time.sleep(2)  # Espera 2 segundos entre os envios para evitar bloqueio

        except Exception as e:
            print(f"❌ Erro ao enviar para {email}: {e}")
