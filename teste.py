import traceback

def exemplo():
    resultado = 10 / 0

try:
    exemplo()
except Exception as e:
    # Obtém a mensagem de erro
    mensagem_erro = str(e)

    # Obtém detalhes do traceback
    traceback_info = traceback.format_exc()

    # Obtém o nome do erro
    nome_erro = type(e).__name__

    # Obtém a linha específica que causou o erro
    linha_quebrada = traceback_info.split("\n")[-2]
    linha_erro = linha_quebrada.strip()

    print(f"Nome do erro: {nome_erro}")
    print(f"Linha do erro: {linha_erro}")
    print(f"Mensagem de erro: {mensagem_erro}")
