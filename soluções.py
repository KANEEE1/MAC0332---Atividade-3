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
    
def valida_cpf(cpf_string):
    # TODO:
    pass
