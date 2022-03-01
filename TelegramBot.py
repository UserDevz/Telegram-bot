import telebot

api_key = "SUA CHAVE DA API"               # API KEY do bot

bot = telebot.TeleBot(api_key)

@bot.message_handler('/start')             # Define o comando que o bot ira responder;
def comando(mensagem):                     # Criando uma funcao para a resposta;
    bot.reply_to(mensagem, "Testando")     # Envio da resposta do bot;
