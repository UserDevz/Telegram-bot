<H1 text align='center'>Telegram-bot</h1>

<img src='https://img.shields.io/badge/Python-3.10-green'> <img src='https://img.shields.io/badge/biblioteca-pytelegrambotapi-green'> <img src='https://img.shields.io/badge/criador-UserDevz-green'>
<img src='https://img.shields.io/badge/Licensa-MIT License-green'> <img src='https://img.shields.io/badge/open%20source-%E2%99%A5%EF%B8%8F-green'>

<b>Pequena demonstração de um bot para telegram em Python</b>
</br>

<h2>Código explicação:</h2></br>

<strong>Para pegar sua chave api, entre em contato com @FatherBot no telegram</strong>

<p>Instalando a biblioteca:</p>

    pip install pytelegrambotapi

<p>Importando a biblioteca Telebot:</p>

    import telebot
    import botCredentials

<p>Evitando exportar sua chave API por engano pro repositório Git: </p>

    mv _gitignore .gitignore

<p>Código: </p>

  (em botCredentials.py):

    api_key = 'chave api'

  (em TelegramBot.py):

    bot = telebot.TeleBot(botCredentials.api_key) # Passa a chave do Telegram para a biblioteca

    @bot.message_handler('/start')                # Define o comando que o bot ira responder;
    def comando(mensagem):                        # Criando uma funcao para a resposta;
        bot.reply_to(mensagem, "Testando")        # Envio da resposta do bot;
    bot.polling()                                 # Comando para iniciar o bot e ativar a API;

<p>Após fazer tudo isso:</p>

    python TelegramBot.py
