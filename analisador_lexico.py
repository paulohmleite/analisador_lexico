"""
Analisador léxico

Implementado por:
Paulo Henrique M. Leite 
RGA: 201719050287

"""

# bibliotecas utilizadas
import nltk
import re


nltk.download("punkt")

file = open("programa_simples.c", "r")
process = file.read()

# funções
def limpar_comentarios(process):
    # remover comentarios do tipo //
    comentarios_uma_linha = re.sub("//.*", "", process)

    # remover comentarios do tipo /* */
    comentarios_multiplas_linhas = re.sub(
        "/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", comentarios_uma_linha
    )
    print(comentarios_multiplas_linhas)

    # retornando codigo sem comentarios
    return comentarios_multiplas_linhas


if __name__ == "__main__":
    codigo_sem_comentarios = limpar_comentarios(process)
