import random
import time  

perguntas_respostas = [
    {
        "pergunta": "O que é Python?",
        "opcoes": ["Uma cobra venenosa", "Uma linguagem de programação", "Um sistema operacional", "Um animal de estimação"],
        "resposta": "Uma linguagem de programação"
    },
    {
        "pergunta": "Qual é o símbolo de atribuição em Python?",
        "opcoes": ["=", "=>", "<-", "=="],
        "resposta": "="
    },
    {
        "pergunta": "Qual é a estrutura de controle usada para repetir um bloco de código em Python?",
        "opcoes": ["if-else", "for", "switch-case", "try-except"],
        "resposta": "for"
    },
    {
        "pergunta": "Em Python, como você imprime algo na tela?",
        "opcoes": ["print()", "console.log()", "System.out.println()", "Console.WriteLine()"],
        "resposta": "print()"
    },
    {
        "pergunta": "Qual é o resultado da expressão '3 + 2 * 5' em Python?",
        "opcoes": ["25", "15", "13", "7"],
        "resposta": "13"
    },
    {
        "pergunta": "O que é um loop infinito em programação?",
        "opcoes": ["Um loop que nunca é executado", "Um loop que repete um número finito de vezes", "Um loop que nunca termina", "Um loop que só executa uma vez"],
        "resposta": "Um loop que nunca termina"
    },
    {
        "pergunta": "Qual é a função do 'if' em Python?",
        "opcoes": ["Repetir um bloco de código", "Executar um bloco de código se uma condição for verdadeira", "Executar um bloco de código se uma condição for falsa", "Executar um bloco de código sempre"],
        "resposta": "Executar um bloco de código se uma condição for verdadeira"
    },
    {
        "pergunta": "O que é um 'bug' em programação?",
        "opcoes": ["Um inseto que entra no computador", "Um recurso não documentado", "Um erro ou falha no código", "Um vírus de computador"],
        "resposta": "Um erro ou falha no código"
    },
    {
        "pergunta": "Qual é o tipo de dado usado para armazenar números inteiros em Python?",
        "opcoes": ["float", "string", "boolean", "int"],
        "resposta": "int"
    },
    {
        "pergunta": "O que é um 'loop for'?",
        "opcoes": ["Uma instrução para sair de um loop", "Um loop que executa apenas uma vez", "Um loop que repete um número fixo de vezes", "Um loop que nunca termina"],
        "resposta": "Um loop que repete um número fixo de vezes"
    },
]

frases = [
    "Bem-vindo(a) ao desafio mágico da programação!",
    "Você é um mago da programação em busca do conhecimento supremo!",
    "E alcançou a última fase de seu treinamento mágico!",
    "Prepare-se para testar seus poderes de programação!",
]

def imprimir_mensagens():
    for frase in frases:
        print(frase)
        time.sleep(3)  
        print()  


def apresentar_perguntas():
    random.shuffle(perguntas_respostas)
    pontuacao = 0

    for i, pergunta_info in enumerate(perguntas_respostas, start=1):
        pergunta = pergunta_info["pergunta"]
        opcoes = pergunta_info["opcoes"]
        resposta_correta = pergunta_info["resposta"]

        while True:  
            print(f"Pergunta {i}: {pergunta}")

            for j, opcao in enumerate(opcoes, start=1):
                print(f"{j}. {opcao}")

            resposta_usuario = input("Sua resposta (Digite o número da opção): ")

            if resposta_usuario.isdigit() and 1 <= int(resposta_usuario) <= len(opcoes):
                resposta_usuario = opcoes[int(resposta_usuario) - 1]
                break  
            else:
                print("Opção inválida. Tente novamente.")
                continue

        if resposta_usuario == resposta_correta:
            print("Resposta correta!\n")
            pontuacao += 1
        else:
            print(f"Resposta incorreta. A resposta correta era: {resposta_correta}\n")

    return pontuacao

def jogo():
    nome_jogador = input("Qual é o seu nome, meu caro mago? ").strip().capitalize()

    imprimir_mensagens()

    pontuacao = apresentar_perguntas()

    print(f"{nome_jogador}, sua pontuação final é: {pontuacao}/10")

    if pontuacao >= 7:
        print(f"Parabéns, {nome_jogador}! Você passou na fase de programação! Você é um mago estudioso!")
    else:
        print(f"{nome_jogador}, você não passou na fase de programação :(. Estude mais um pouco e tente novamente!")

jogo()
