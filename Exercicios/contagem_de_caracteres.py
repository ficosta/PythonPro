def contar_caracteres(s:str):
    """Função que conta os caracteres de uma string

    Ex:
    >>> contar_caracteres('IASI')
    A: 1
    A: 1
    I: 2
    S: 1

    >>> contar_caracteres('BANANA')
    A: 3
    B: 1
    N: 2

    :param s: string a ser contada
    :return:
    """
    caracteres_ordenados = sorted(s)

    caracteres_anterior = caracteres_ordenados[0]
    contagem = 1
    for caracter in caracteres_ordenados[1:]:
        if caracter==caracteres_anterior:
            contagem +=1
        else:
            print(f'{caracteres_anterior}: {contagem}')
            caracteres_anterior=caracter
            contagem=1
    print(f'{caracteres_anterior}: {contagem}')

if __name__ == '__main__':
    contar_caracteres('IASI')
    print()
    contar_caracteres('BANANA')