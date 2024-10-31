# funcoes.py

from nltk.corpus import wordnet
import random

# Função para encontrar sinônimos
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word, lang='por'):  # Português
        for lemma in syn.lemmas('por'):
            synonyms.add(lemma.name())
    return synonyms

# Função de memória simples
memory = {}

def remember(user, key, value):
    """Armazena preferências ou informações para lembrança futura."""
    if user not in memory:
        memory[user] = {}
    memory[user][key] = value

def recall(user, key):
    """Recupera informações armazenadas."""
    return memory.get(user, {}).get(key, None)

# Função para registrar interações
def log_interaction(user_input, bot_response):
    """Registra a interação entre o usuário e o bot."""
    with open('interactions_log.txt', 'a', encoding='utf-8') as log_file:
        log_file.write(f"Você: {user_input}\nAia: {bot_response}\n\n")