def contar_caracteres(s:str):
    """Função que conta os caracteres de uma string

    Ex:
    >>> contar_caracteres('IASI')
    {'A': 1, 'A': 1, 'I': 2, 'S': 1}

    >>> contar_caracteres('BANANA')
    {'A': 3, 'B': 1, 'N': 2}

    :param s: string a ser contada
    :return:
    """

    resultado = {}
    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) +1

    return resultado


if __name__ == '__main__':
    print(contar_caracteres('IASI'))
    print()
    print(contar_caracteres('BANANA'))