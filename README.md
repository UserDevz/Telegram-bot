<H1 text align='center'>Telegram-bot</h1>

<img src='https://img.shields.io/badge/Python-3.10-green'> <img src='https://img.shields.io/badge/biblioteca-pytelegrambotapi-green'> <img src='https://img.shields.io/badge/criador-UserDevz-green'>


<b>Pequena demonstração de um bot para telegram em Python</b>
</br>

<h2>Código explicação:</h2></br>

<strong>Para pegar sua chave api, entre em contato com @FatherBot no telegram</strong>

<p>Instalando a biblioteca:</p>

    pip install pytelegrambotapi

<p>Importando a biblioteca Telebot:</p>

    import telebot

<p>Código: </p>

    api_key = 'chave api'

    bot = telebot.TeleBot(api_key)             # Passa a chave do Telegram para a biblioteca

    @bot.message_handler('/start')             # Define o comando que o bot ira responder;
    def comando(mensagem):                     # Criando uma funcao para a resposta;
        bot.reply_to(mensagem, "Testando")     # Envio da resposta do bot;

<p>Após fazer tudo isso:</p>

    python bot.py
