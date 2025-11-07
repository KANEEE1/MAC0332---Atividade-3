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

def encontrar_maior_palavra(frase):
    x = frase.split(" ")
    y = ""
    for i in x:
        if len(i) > len(y):
            y = i
    return y
    
