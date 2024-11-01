import datetime

# Função para logar interações
def log_interaction(user_input, response):
    with open("chat_log.txt", "a", encoding='utf-8') as log_file:
        log_file.write(f"{datetime.datetime.now()}\n")
        log_file.write(f"User: {user_input}\nAia: {response}\n\n")
