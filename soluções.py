def sao_anagramas(string1, string2):
    # TODO:
    pass


def cifra_de_cesar(texto, deslocamento):
    nova_string = ""
    for i in texto:
        if i.islower():
            nova_string += chr((ord(i) - ord('a') + deslocamento) % 26 + ord('a'))
        elif i.isupper():
            nova_string += chr((ord(i) - ord('A') + deslocamento) % 26 + ord('A'))
        else:
            nova_string += i
    return nova_string
    pass

def encontrar_maior_palavra(frase):
    palavras = frase.split(" ")
    maior_palavra = ""
    for palavra in palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
    return maior_palavra