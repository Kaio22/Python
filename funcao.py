

def imprime_frutas():
    frutas = ["Melão","Abacaxi","Manga"]
    for fruta in frutas:
        print("Agora é a fruta: {}".format (fruta))

imprime_frutas()


def nome():
    name = str(input('Entre com o seu nome: '))
    if set('aeiou').intersection(name.lower()):
        print("Seu nome tem uma vogal")
    else:
        print("Seu nome não tem vogal")
nome()



