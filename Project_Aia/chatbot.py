import discord
import json

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = discord.Client(intents=intents)

# Carregar dados de aprendizado
def load_learning_data():
    try:
        with open('learning_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

learning_data = load_learning_data()

@client.event
async def on_ready():
    print(f'Aia está online como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Comando para ensinar
    if message.content.startswith('!ensinar'):
        content = message.content[len('!ensinar'):].strip()  # Remove o comando
        parts = content.split('?', 1)  # Divide a mensagem em pergunta e resposta
        
        if len(parts) == 2:  # Verifica se temos uma pergunta e uma resposta
            question = parts[0].strip() + '?'  # Adiciona o '?' de volta na pergunta
            answer = parts[1].strip()  # Captura a resposta
            
            # Armazena a pergunta e resposta
            learning_data[question] = answer  
            await message.channel.send(f'Aia aprendeu: "{question}" -> "{answer}"')
            
            # Salva as mudanças no arquivo JSON
            with open('learning_data.json', 'w') as f:
                json.dump(learning_data, f)
        else:
            await message.channel.send("Por favor, use o formato: !ensinar pergunta? resposta.")

    else:
        # Caso não seja um comando de ensino, você pode registrar ou ignorar
        await message.channel.send(f'Aia registrou: "{message.content}" mas não é uma pergunta de ensino.')
        # Se quiser, pode implementar uma lógica aqui para aprender com mensagens comuns

client.run('YOUR_BOT_TOKEN')  # Substitua 'YOUR_BOT_TOKEN' pelo seu token real
