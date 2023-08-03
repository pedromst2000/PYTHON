# implementar um programa que leia um texto e imprime as diversas palavras do texto por ordem inversa

# exemplo :

# texto : Este é um teste de AED
# resultado : AED de teste um é Este

print()
texto = input("Insira um texto: ")


try:
    # check if the input is a string
    if type(texto) is not str or len(texto) == 0:
        raise ValueError
except ValueError:
    print("O texto inserido não é válido.")
    exit()


def reverse_text(text):
    # split the text into words
    words = text.split()
    # reverse the list
    words.reverse()
    # join the list into a string
    text = " ".join(words)
    return text


print()
print(f'Resultado: {reverse_text(texto)}')
print()