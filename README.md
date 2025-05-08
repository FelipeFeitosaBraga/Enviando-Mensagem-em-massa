# 📣 Projeto de Envio de Mensagens Promocionais – BG Multipeças

Este projeto automatiza o envio de campanhas promocionais da BG Multipeças via **e-mail (Gmail)** e **WhatsApp Web**, usando **Python** com `smtplib` e `selenium`.

---

## 📂 Estrutura do Projeto

```
bg-campanha/
│
├── SendEmail.py          # Envia e-mails promocionais
├── SendNumber.py         # Envia mensagens via WhatsApp Web
├── .env                  # Armazena credenciais do Gmail
└── README.md             # Documentação
```

---

## ⚙️ Pré-requisitos

### Ambiente

- Python 3.9 ou superior
- Conta Gmail com autenticação via senha de aplicativo
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome
- WhatsApp Web com sessão ativa

### Instalação de dependências

```bash
pip install selenium python-dotenv
```

---

## 📧 Envio de E-mails Promocionais (`SendEmail.py`)

### Descrição

Esse script envia uma mensagem promocional personalizada para uma lista de destinatários via **SMTP com Gmail**.

### Configuração `.env`

Crie um arquivo `.env` com as seguintes variáveis:

```env
EMAIL_REMETENTE=seu_email@gmail.com
SENHA_APP=sua_senha_de_app
```

> **Atenção**: Você deve criar uma [senha de app](https://support.google.com/accounts/answer/185833?hl=pt-BR) no Google caso use autenticação em dois fatores.

### Como executar

```bash
python SendEmail.py
```

---

## 💬 Envio de Mensagens pelo WhatsApp Web (`SendNumber.py`)

### Descrição

Este script abre o navegador com o WhatsApp Web, carrega sua sessão (persistida) e envia uma mensagem promocional para cada número na lista.

### Requisitos adicionais

- Tenha o Chrome instalado no caminho padrão (ou ajuste o `chrome_path` no script).
- Configure o Chrome para usar um **perfil de usuário persistente** (`C:/temp/whatsapp_profile`) para evitar escanear o QR code a cada execução.

### Como executar

```bash
python SendNumber.py
```

### Observação

- O tempo de espera (`time.sleep`) garante que a interface do WhatsApp Web tenha tempo de carregar antes de interações automatizadas.
- Certifique-se de que os números da lista de contatos estejam no formato **internacional** (ex: `+5511999999999`).

---

## ✉️ Exemplo da Mensagem

```
Olá! 👋

Temos uma ótima notícia para você! ✨

Aproveite 10% de desconto em todos os produtos do nosso site! 🤩 É a sua chance de garantir peças de excelente qualidade com um preço especial.

Para aproveitar, basta acessar nosso site: https://bgmultipecas.com.br/ e utilizar o cupom de desconto 10%OFF no carrinho de compras! 😉

Essa oferta é por tempo limitado, então não perca essa oportunidade! Corra para o nosso site e aproveite! 🏃‍♀️💨

Qualquer dúvida, estamos à disposição! 😊

Atenciosamente,  
BG Multipeças
```

---

## ✅ Boas práticas

- Faça testes com poucos contatos antes de campanhas grandes.
- Respeite as políticas de privacidade e spam.
- Nunca envie mensagens sem consentimento do destinatário.
