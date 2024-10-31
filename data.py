# data.py

# Perguntas e suas categorias (intents)
training_data = [
    # Saudações (greeting)
    ("Olá", "greeting"),
    ("Oi", "greeting"),
    ("Como vai?", "greeting"),
    ("Bom dia", "greeting"),
    ("Boa tarde", "greeting"),

    # Identidade (identity)
    ("Quem é você?", "identity"),
    ("Qual é o seu nome?", "identity"),
    ("O que você é?", "identity"),
    ("Você é uma IA?", "identity"),
    ("De onde você veio?", "identity"),

    # Funcionalidade (functionality)
    ("O que você faz?", "functionality"),
    ("Como você funciona?", "functionality"),
    ("Você pode me ajudar?", "functionality"),
    ("Quais são suas habilidades?", "functionality"),
    ("O que você sabe fazer?", "functionality"),

    # Despedidas (farewell)
    ("Tchau", "farewell"),
    ("Adeus", "farewell"),
    ("Até logo", "farewell"),
    ("Volte logo", "farewell"),
    ("Até mais!", "farewell"),

    # Conhecimento Geral (general_knowledge)
    ("Qual é a capital do Brasil?", "general_knowledge"),
    ("Quem foi o primeiro presidente do Brasil?", "general_knowledge"),
    ("Qual é a língua oficial do Brasil?", "general_knowledge"),
    ("Qual é o maior país do mundo?", "general_knowledge"),
    ("Onde fica a Estátua da Liberdade?", "general_knowledge"),

    # Filosofia (philosophy)
    ("Qual é o sentido da vida?", "philosophy"),
    ("O que é a felicidade?", "philosophy"),
    ("O que é a verdade?", "philosophy"),
    ("Existe vida após a morte?", "philosophy"),
    ("O que é a liberdade?", "philosophy"),

    # Piadas (joke)
    ("Me conte uma piada!", "joke"),
    ("Você sabe contar piadas?", "joke"),
    ("Qual é a melhor piada que você conhece?", "joke"),
    ("Você conhece alguma piada de tio?", "joke"),
    ("Que tipo de música as plantas gostam?", "joke"),  # Resposta: "FOLK!"

    # Curiosidades (curiosity)
    ("Me fale uma curiosidade.", "curiosity"),
    ("Qual é a coisa mais estranha que você sabe?", "curiosity"),
    ("Você sabe alguma curiosidade sobre animais?", "curiosity"),
    ("O que é mais curioso que você conhece?", "curiosity"),
    ("Você tem uma curiosidade interessante para me contar?", "curiosity"),

    # Jogos (games)
    ("Qual é o seu jogo favorito?", "games"),
    ("Você gosta de jogos de estratégia?", "games"),
    ("Quais jogos você recomenda?", "games"),
    ("Você já jogou Valorant?", "games"),
    ("Qual jogo você mais gosta de jogar?", "games"),
    # Animes (anime)
    ("Você gosta de animes?", "anime"),
    ("Qual é o seu anime favorito?", "anime"),
    ("Quais animes você recomenda?", "anime"),
    ("Qual foi o último anime que você assistiu?", "anime"),
    ("Você conhece o anime High School DXD?", "anime")
]

# Respostas com emoções
emotional_responses = {
    "happy": "Que ótimo! 😊",
    "annoyed": "Perguntando isso de novo? Vira o disco... 🙄",
    "playful": "Oh, essa é Boa em! Vamos ver...",
}

recurring_jokes = [
    "Ah, essa é complicada em eu sou uma IA não o Google. 😂",
    "Bem, eu sou só um código, mas entendo o que você quer dizer... ou não. 😆",
    "Quer dizer que sou só um chatbot por enquanto, mas vou te ajudar com tudo que eu puder! 😉",
]

# Respostas
responses = {
    "greeting": "Oi! Como posso te ajudar?",
    "identity": "Eu sou a Aia! Eu sou um chatbot criado pelo Junin!",
    "functionality": [
        "Eu sou um chatbot que responde perguntas usando Python e Machine Learning!",
        "Basicamente, eu aprendo com as perguntas que me fazem e tento ajudar da melhor forma possível!",
        "Posso responder perguntas e compartilhar curiosidades!",
    ],
    "farewell": "Tchau! Volte sempre!",
    "general_knowledge": {
        "capital_brazil": "A capital do Brasil é Brasília! 🏛️",
        "first_president_brazil": "O primeiro presidente do Brasil foi Marechal Deodoro da Fonseca!",
    },
    "philosophy": "O sentido da vida é viver. Mas se eu tivesse que escolher algo mais específico, diria que é sempre sorrir e fazer os outros sorrirem também! 😊",
    "joke": "Por que o livro de matemática se suicidou? Porque tinha muitos problemas! 😂",
    "curiosity": "Sabia que as lhamas podem fazer amigos para a vida toda? Elas são super leais! 🦙",
    "games": "Meus jogos favoritos incluem Hollow Knight, Valorant e Inside the Backrooms! 🎮",
    "anime": "Eu adoro animes! Alguns dos meus favoritos são High School DXD, Dragon Ball e Toaru Majutsu no Index! 🍥",
}
