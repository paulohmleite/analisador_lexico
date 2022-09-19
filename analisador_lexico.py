"""
Analisador léxico

Implementado por:
Paulo Henrique M. Leite 
RGA: 201719050287
------------------------

------------------------

------------------------

------------------------

------------------------


"""

# bibliotecas utilizadas
import nltk
import re


nltk.download("punkt")

file = open("exemplos/programa_simples.txt", "r")
process = file.read()


# definições gramática
operadores = "(/)|(%)|(--)|(<=)|(>=)|(\++)|(-)|(=)|(\*)"
identificadores = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
keywords = ""
numerais = "^(\d+)$"

# funções

# função que limpa comentários do código
def limpar_comentarios(codigo):
    # remover comentarios do tipo //
    comentarios_uma_linha = re.sub("//.*", "", codigo)

    # remover comentarios do tipo /* */
    comentarios_multiplas_linhas = re.sub(
        "/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", comentarios_uma_linha
    )
    # TODO saída: código sem comentarios
    print(comentarios_multiplas_linhas)
    print("*" * 30)

    # retornando codigo sem comentarios
    return comentarios_multiplas_linhas


# função que limpa espaços
def limpar_espacos(codigo):
    codigo_apos_scanner = []

    for linha in codigo:
        if linha.strip() != "":
            codigo_apos_scanner.append(linha.strip())

    return codigo_apos_scanner


# função main
if __name__ == "__main__":

    # variaveis de saída do stacktrace de tokens
    # podemos associar a linha do token por aqui, usando um dict
    '''
    exemplo_dict = [
        ['token1', 'line_token'],
        ['token2', 'line_token'],
    ]
    '''

    keywods_stacktrace = []
    operadores_stacktrace = []
    identificadores_stacktrace = []
    numerais_stacktrace = []

    contador = 0

    # limpar comentarios
    codigo_sem_comentarios = limpar_comentarios(process)
    print("*" * 30)
    print('codigo_sem_comentarios')
    print(codigo_sem_comentarios)
    codigo_sem_comentarios_split = codigo_sem_comentarios.split("\n")
    print("*" * 30)
    print('codigo_sem_comentarios_split')
    print(codigo_sem_comentarios_split)

    # limpar espaços
    codigo_limpo_espacos = limpar_espacos(codigo_sem_comentarios_split)
    print("*" * 30)
    print("codigo_limpo_espacos")
    print(codigo_limpo_espacos)

    codigo_limpo_espacos_join = "\n".join([str(elem) for elem in codigo_limpo_espacos])
    print("*" * 30)
    print('codigo_limpo_espacos_join \\n')
    print(codigo_limpo_espacos_join)

    codigo_limpo_espacos_join_split = codigo_limpo_espacos_join.split('\n')
    print("*" * 30)
    print('codigo_limpo_espacos_join_split')
    print(codigo_limpo_espacos_join_split)


    print(codigo_limpo_espacos_join_split == codigo_limpo_espacos)



    codigo = []

    for line in codigo_sem_comentarios:
        codigo.append(line)

    print('codigo_sem_comentarios antes de tokenize')
    print(codigo_limpo_espacos_join_split)

    # display_contador = 0
    line_code = 0

    print('codigo_sem_comentarios')
    print(codigo_limpo_espacos_join_split)
    for line in codigo_limpo_espacos_join_split:
        # print('line')
        # print(line)
        contador = contador + 1
        # para caso a linguagem seja C
        if(line.startswith("#include")):
            tokens = nltk.word_tokenize(line)
        else:
            tokens = nltk.wordpunct_tokenize(line)
        for token in tokens:
            if (re.findall(operadores, token)):
                operadores_stacktrace.append(token)
            elif(re.findall(numerais,token)):
                numerais_stacktrace.append(token)
            elif (re.findall(identificadores, token)):
                identificadores_stacktrace.append(token)

    print("Existem ",len(identificadores_stacktrace),"Identificadores: ", identificadores_stacktrace)
    print("Existem ",len(numerais_stacktrace),"Numerais: ", numerais_stacktrace)
    print("\n")



    tokens = nltk.word_tokenize('int a, b, c;')
    print('esses são os tokens!!!')
    print(tokens)


    # retornar stacktrace de cada token com dados (linha)



