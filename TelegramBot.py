import telebot
import BotCredentials

bot = telebot.TeleBot(botCredentials.api_key)

@bot.message_handler('/start')             # Define o comando que o bot ira responder;
def comando(mensagem):                     # Criando uma funcao para a resposta;
    bot.reply_to(mensagem, "Testando")     # Envio da resposta do bot;
