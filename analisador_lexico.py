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

file = open("exemplos/programa_simples.c", "r")
process = file.read()


# definições
operadores = "(=) | (-) | (+) | (\*) | (\++) | (--) | (<=) | (>=)"
identificadores = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
keywords = ""

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


if __name__ == "__main__":

    # limpar comentarios
    codigo_sem_comentarios = limpar_comentarios(process)
    codigo_sem_comentarios_split = codigo_sem_comentarios.split("\n")

    # limpar espaços
    codigo_limpo_espacos = limpar_espacos(codigo_sem_comentarios_split)
    print("codigo sem comentarios sem espaços")
    print(codigo_limpo_espacos)

    codigo_limpo_espacos_join = "\n".join([str(elem) for elem in codigo_limpo_espacos])
    print("*" * 30)
    print('adiciona um \\n antes de cada linha de código')
    print(codigo_limpo_espacos_join)

    codigo_limpo_espacos_join_split = codigo_limpo_espacos_join.split('\n')
    print("*" * 30)
    print('oioi')
    print(codigo_limpo_espacos)

    
    print(codigo_limpo_espacos_join_split == codigo_limpo_espacos)



    codigo = []

    for line in codigo_sem_comentarios:
        codigo.append(line)

    print(codigo)
