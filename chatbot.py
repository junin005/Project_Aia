# chatbot.py

from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from funcoes import get_synonyms, log_interaction, remember, recall
from data import training_data, responses, emotional_responses, recurring_jokes
import nltk
import random

# Certifique-se de que os recursos do NLTK estejam baixados
nltk.download('wordnet')
nltk.download('omw-1.4')

# Separar dados em perguntas e categorias
questions, categories = zip(*training_data)

# Criar o pipeline do modelo
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Treinar o modelo com perguntas e categorias
model.fit(questions, categories)

# Carregar o GPT-Neo (Assumindo que foi instalado e está acessível localmente)
gpt_neo = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

# Função para resposta de personalidade usando o GPT-Neo
def generate_gpt_response_with_personality(prompt):
    personality_prompt = (
        "You are Aia, a witty and slightly sarcastic AI created by Junin. "
        "You enjoy anime, games, and always answer with a playful tone. "
        "Respond to this: " + prompt
    )
    response = gpt_neo(personality_prompt, max_length=100, num_return_sequences=1, temperature=0.8)
    return response[0]["generated_text"]

# Função principal do chatbot
def chatbot_answer(user_input, user="default_user"):
    # Checa memória para preferências
    if "meu jogo favorito" in user_input.lower():
        remember(user, "favorite_game", user_input)
        return "Ok! Vou lembrar que esse é seu jogo favorito!"

    # Respostas diretas a perguntas específicas
    if "sentido da vida" in user_input.lower():
        return responses["philosophy"]

    # Respostas emocionais com base em "estado"
    if "piada" in user_input.lower():
        return random.choice(recurring_jokes)

    # Verifica por sinônimos ou frases comuns
    for question, answer in training_data:
        question_words = question.lower().split()
        user_input_words = user_input.lower().split()
        if any(word in get_synonyms(q) for q in question_words for word in user_input_words):
            return responses.get(answer, "Desculpa, ainda não sei responder isso. 😅")

    # Usa o modelo de machine learning para previsão
    category = model.predict([user_input])[0]
    if category in responses:
        return responses[category]

    # Gera uma resposta com o GPT-Neo e personalidade
    return generate_gpt_response_with_personality(user_input)

# Loop principal do chatbot
print("Bem-vindo ao chatbot Aia! Digite 'sair' para encerrar.")

while True:
    user_input = input("Você: ")
    if user_input.lower() == "sair":
        print("Aia: Até mais! 😎")
        break

    response = chatbot_answer(user_input)
    print(f"Aia: {response}")

    # Registrar interação
    log_interaction(user_input, response)